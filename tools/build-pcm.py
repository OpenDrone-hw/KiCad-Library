#!/usr/bin/env python3
"""Build the KiCad PCM package and the repository metadata.

Produces:
  dist/OpenDrone-KiCad-Library_<version>.zip   the addon archive
  pcm/packages.json                            package list served to PCM
  pcm/repository.json                          the URL users add to KiCad

The archive follows the PCM library layout: symbols/, footprints/,
3dmodels/, with footprint model paths rewritten from ${OPENDRONE_LIB}
to the 3rd-party dir KiCad manages for PCM content.

Run from the repo root: python3 tools/build-pcm.py <version>
Then attach the zip to a GitHub release tagged pcm-v<version>.
"""
import hashlib, json, os, re, shutil, sys, time, zipfile

IDENT = "com_github_opendrone-hw_kicad-library"
KICAD_VER = "10.0"
THIRD_PARTY = "${KICAD10_3RD_PARTY}"
REPO_RAW = "https://raw.githubusercontent.com/OpenDrone-hw/KiCad-Library/main/pcm"
RELEASE_URL = "https://github.com/OpenDrone-hw/KiCad-Library/releases/download"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    version = sys.argv[1] if len(sys.argv) > 1 else "1.0.0"
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)
    stage = "dist/stage"
    shutil.rmtree("dist", ignore_errors=True)
    os.makedirs(f"{stage}/symbols", exist_ok=True)
    os.makedirs(f"{stage}/footprints/OpenDrone.pretty", exist_ok=True)
    os.makedirs(f"{stage}/3dmodels/OpenDrone.3dshapes", exist_ok=True)

    shutil.copy("symbol/OpenDrone.kicad_sym", f"{stage}/symbols/OpenDrone.kicad_sym")
    model_base = f"{THIRD_PARTY}/3dmodels/{IDENT}/OpenDrone.3dshapes"
    for f in os.listdir("footprint/OpenDrone.pretty"):
        s = open(f"footprint/OpenDrone.pretty/{f}").read()
        s = s.replace("${OPENDRONE_LIB}/3dmodel", model_base)
        open(f"{stage}/footprints/OpenDrone.pretty/{f}", "w").write(s)
    for f in os.listdir("3dmodel"):
        shutil.copy(f"3dmodel/{f}", f"{stage}/3dmodels/OpenDrone.3dshapes/{f}")

    meta = {
        "$schema": "https://go.kicad.org/pcm/schemas/v1",
        "name": "OpenDrone KiCad Library",
        "description": "Symbols, footprints and 3D models for every part manufactured on an OpenDrone board.",
        "description_full": "The parts catalogue of the OpenDrone open source FPV hardware line by incutec: every symbol, footprint and 3D model here is used on a board that has been through a real JLCPCB assembly run. Symbols carry LCSC part numbers for JLCPCB ordering. Hardware line: https://github.com/OpenDrone-hw",
        "identifier": IDENT,
        "type": "library",
        "author": {"name": "incutec", "contact": {"web": "https://opendrone.be"}},
        "license": "CERN-OHL-S-2.0",
        "resources": {"homepage": "https://github.com/OpenDrone-hw/KiCad-Library"},
        "versions": [],
    }
    json.dump(meta, open(f"{stage}/metadata.json", "w"), indent=2)

    zip_name = f"OpenDrone-KiCad-Library_{version}.zip"
    zip_path = f"dist/{zip_name}"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, _, files in os.walk(stage):
            for f in files:
                full = os.path.join(dirpath, f)
                z.write(full, os.path.relpath(full, stage))
    inst = sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(stage) for f in fs)

    version_entry = {
        "version": version,
        "status": "stable",
        "kicad_version": KICAD_VER,
        "download_url": f"{RELEASE_URL}/pcm-v{version}/{zip_name}",
        "download_sha256": sha256(zip_path),
        "download_size": os.path.getsize(zip_path),
        "install_size": inst,
    }
    meta["versions"] = [version_entry]

    os.makedirs("pcm", exist_ok=True)
    json.dump({"packages": [meta]}, open("pcm/packages.json", "w"), indent=2)
    now = int(time.time())
    repo = {
        "$schema": "https://go.kicad.org/pcm/schemas/v1#/definitions/Repository",
        "name": "OpenDrone",
        "maintainer": {"name": "incutec", "contact": {"web": "https://opendrone.be"}},
        "packages": {
            "url": f"{REPO_RAW}/packages.json",
            "sha256": sha256("pcm/packages.json"),
            "update_timestamp": now,
            "update_time_utc": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(now)),
        },
    }
    json.dump(repo, open("pcm/repository.json", "w"), indent=2)
    shutil.rmtree(stage)
    print(f"built {zip_path} sha256={version_entry['download_sha256'][:12]}... "
          f"({version_entry['download_size']//1024} KiB zip, {inst//1024} KiB installed)")
    print("commit pcm/, then: gh release create pcm-v%s %s" % (version, zip_path))


if __name__ == "__main__":
    main()

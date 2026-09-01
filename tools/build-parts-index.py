#!/usr/bin/env python3
"""Build PARTS-USED.md, and check the library against its own membership rule.

The rule: a part belongs in this library only if it is used on a board whose
repo is at status-alpha or beyond. Alpha means the board was manufactured, so
everything in here has been through a real assembly run. That is the whole
value of the library, and it only stays true if something checks.

    python3 tools/build-parts-index.py            regenerate PARTS-USED.md
    python3 tools/build-parts-index.py --check     report drift, exit 1 if any

Stage comes from each repo's status-* GitHub topic, fetched with gh and cached
in tools/.status-cache.json so the script still runs offline.
"""
import os, re, json, collections, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BOARDS = os.path.abspath(os.path.join(HERE, '..', '..'))
CACHE = os.path.join(HERE, '.status-cache.json')
DATASHEET_MANIFEST = os.path.join(HERE, '..', 'datasheet', 'manifest.json')
SKIP = {'KiCad-Library'}
PRODUCED = {'status-alpha', 'status-beta', 'status-launched'}
PROP = re.compile(r'\(property "([^"]+)" "([^"]*)"')

# These remain KiCad primitives rather than catalogue symbols. Their exact
# supplier choices still appear in PARTS-USED.md, but they do not require a
# custom symbol or a centrally tracked datasheet. Everything else used on a
# manufactured board must be promoted into the shared catalogue.
GENERIC_FOOTPRINT_PREFIXES = (
    'R_', 'R0201',
    'C_', 'C0201',
    'L_', 'IND-SMD_',
    'LED_',
)


def is_generic_primitive(part):
    footprint = part.get('fp', '').split(':')[-1]
    return footprint.startswith(GENERIC_FOOTPRINT_PREFIXES)


def repo_status(repos):
    """status-* topic per repo. Live from gh, falling back to the cache."""
    cache = {}
    if os.path.exists(CACHE):
        cache = json.load(open(CACHE))
    cache = {repo: cache[repo] for repo in repos if repo in cache}
    fresh = {}
    for r in repos:
        try:
            out = subprocess.run(['gh', 'api', f'repos/OpenDrone-hw/{r}/topics',
                                  '--jq', '.names[]'], capture_output=True,
                                 text=True, timeout=15)
            topics = [t for t in out.stdout.split() if t.startswith('status-')]
            if topics:
                fresh[r] = topics[0]
        except Exception:
            pass
    if fresh:
        cache.update(fresh)
        json.dump(cache, open(CACHE, 'w'), indent=2, sort_keys=True)
    else:
        print('  gh unavailable, using cached statuses', file=sys.stderr)
    return cache


def symbol_blocks(text):
    """Yield each symbol instance's property dict from a .kicad_sch."""
    for m in re.finditer(r'\(symbol\b', text):
        start = m.start()
        depth, i = 0, start
        while i < len(text):
            if text[i] == '(':
                depth += 1
            elif text[i] == ')':
                depth -= 1
                if depth == 0:
                    break
            i += 1
        block = text[start:i]
        if len(block) < 40000:
            yield dict(PROP.findall(block))


def scan_boards(catalog_by_value=None):
    catalog_by_value = catalog_by_value or {}
    parts = collections.defaultdict(lambda: {'boards': set(), 'value': '', 'fp': '', 'mpn': ''})
    repos = []
    for repo in sorted(os.listdir(BOARDS)):
        repo_path = os.path.join(BOARDS, repo)
        if repo in SKIP or not os.path.isdir(os.path.join(repo_path, '.git')):
            continue
        tracked = subprocess.run(
            ['git', '-C', repo_path, 'ls-files', '-z', '--', '*.kicad_sch'],
            capture_output=True,
        )
        if tracked.returncode:
            continue
        schematics = [
            os.path.join(repo_path, name.decode())
            for name in tracked.stdout.split(b'\0') if name
        ]
        if not schematics:
            continue
        repos.append(repo)
        for sch in schematics:
            if '/libs/' in sch or '/archive/' in sch:
                continue
            try:
                text = open(sch, encoding='utf-8', errors='ignore').read()
            except OSError:
                continue
            for props in symbol_blocks(text):
                lcsc = (props.get('LCSC') or props.get('LCSC Part') or
                        catalog_by_value.get(props.get('Value', '')) or '').strip()
                if not re.fullmatch(r'C\d+', lcsc):
                    continue
                e = parts[lcsc]
                e['boards'].add(repo)
                e['value'] = e['value'] or props.get('Value', '')
                e['fp'] = e['fp'] or props.get('Footprint', '')
                e['mpn'] = e['mpn'] or props.get('MPN', '') or props.get('Manufacturer Part Number', '')
    return parts, repos


def library_symbols():
    """name -> LCSC (or None) for every symbol in the library."""
    path = os.path.join(HERE, '..', 'symbol', 'OpenDrone.kicad_sym')
    text = open(path, encoding='utf-8', errors='ignore').read()
    out = {}
    for m in re.finditer(r'^\t\(symbol "([^"]+)"', text, re.M):
        start = m.start()
        depth, i = 0, start
        while i < len(text):
            if text[i] == '(':
                depth += 1
            elif text[i] == ')':
                depth -= 1
                if depth == 0:
                    break
            i += 1
        props = dict(PROP.findall(text[start:i]))
        lcsc = (props.get('LCSC') or props.get('LCSC Part') or '').strip()
        out[m.group(1)] = lcsc if re.fullmatch(r'C\d+', lcsc) else None
    return out


def main():
    check = '--check' in sys.argv
    syms = library_symbols()
    catalog_by_value = {name: lcsc for name, lcsc in syms.items() if lcsc}
    parts, repos = scan_boards(catalog_by_value)
    status = repo_status(repos)
    made = {r for r in repos if status.get(r) in PRODUCED}

    for e in parts.values():
        e['produced'] = bool(e['boards'] & made)
    kept = {k: v for k, v in parts.items() if v['produced']}

    rows = sorted(kept.items(), key=lambda kv: (-len(kv[1]['boards']), kv[0]))
    out = ["# Parts used", "",
           "Every component that has actually been manufactured on an OpenDrone board.",
           "",
           "A part is listed here only if it is used on a board whose repo is at",
           "`status-alpha` or beyond, which means it has been through a real assembly",
           "run: sourced, footprinted, and it survived a reflow oven. Parts that exist",
           "only on a planned or in-progress design are deliberately absent, however",
           "good they look on paper. When a board reaches alpha, its parts join.",
           "",
           "Regenerate: `python3 tools/build-parts-index.py`", "",
           f"{len(rows)} parts across {len(made)} manufactured boards: "
           + ', '.join(sorted(made)) + ".", "",
           "| LCSC | Value | MPN | Footprint | Boards |", "|---|---|---|---|---|"]
    for lcsc, e in rows:
        out.append(f"| {lcsc} | {e['value']} | {e['mpn']} | {e['fp'].split(':')[-1]} | "
                   f"{', '.join(sorted(e['boards']))} |")
    open(os.path.join(HERE, '..', 'PARTS-USED.md'), 'w').write('\n'.join(out) + '\n')
    print(f"{len(rows)} produced parts written to PARTS-USED.md "
          f"({len(parts) - len(rows)} not-yet-produced parts excluded)")

    if not check:
        return 0

    exemptions = set()
    if os.path.exists(DATASHEET_MANIFEST):
        exemptions = set(json.load(open(DATASHEET_MANIFEST)).get('exempt_symbols', {}))
    by_lcsc = {v: k for k, v in syms.items() if v}
    stale = sorted(n for n, l in syms.items() if l and l not in kept)
    unmapped = sorted(n for n, l in syms.items() if not l and n not in exemptions)
    missing = sorted(l for l in kept if l not in by_lcsc)
    generic_missing = [l for l in missing if is_generic_primitive(kept[l])]
    required_missing = [l for l in missing if not is_generic_primitive(kept[l])]

    lcsc_count = sum(bool(value) for value in syms.values())
    print(f"\nlibrary: {len(syms)} symbols, {lcsc_count} carry "
          f"{len(by_lcsc)} unique LCSC numbers")
    print(f"\n  {len(stale):>3} symbols whose part is on no manufactured board")
    for n in stale[:20]:
        print(f"        {n}  ({syms[n]})")
    if len(stale) > 20:
        print(f"        ... and {len(stale) - 20} more")
    print(f"\n  {len(unmapped):>3} symbols with no LCSC number, so membership cannot be checked")
    for n in unmapped[:10]:
        print(f"        {n}")
    if len(unmapped) > 10:
        print(f"        ... and {len(unmapped) - 10} more")
    print(f"\n  {len(generic_missing):>3} manufactured generic R/C/L/LED primitives "
          "intentionally not promoted")
    print(f"\n  {len(required_missing):>3} datasheet-bearing manufactured parts missing "
          "from the library")
    for lcsc in required_missing[:20]:
        part = kept[lcsc]
        print(f"        {lcsc}  {part['value']}  ({part['fp'].split(':')[-1]})")
    if len(required_missing) > 20:
        print(f"        ... and {len(required_missing) - 20} more")

    return 1 if (stale or unmapped or required_missing) else 0


if __name__ == '__main__':
    sys.exit(main())

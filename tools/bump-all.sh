#!/bin/sh
# Bump the KiCad-Library submodule pin in every sibling repo that uses it.
# Run from the directory containing the hardware repos (e.g. ~/OpenDrone).
set -e
for d in */; do
  d=${d%/}
  [ -f "$d/.gitmodules" ] || continue
  grep -q "KiCad-Library" "$d/.gitmodules" || continue
  echo "== $d"
  git -C "$d" submodule update --remote libs/KiCad-Library
  if ! git -C "$d" diff --quiet libs/KiCad-Library; then
    git -C "$d" commit -m "chore: bump KiCad-Library submodule pin" -- libs/KiCad-Library
    echo "   pinned to $(git -C "$d/libs/KiCad-Library" rev-parse --short HEAD)"
  else
    echo "   already current"
  fi
done

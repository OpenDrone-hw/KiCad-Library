#!/usr/bin/env python3
"""Build PARTS-USED.md: every component used across the board repos.

The point is sourcing, not symbols. If a part appears here we have used it on a
real board, so it is already sourced, footprinted and probably in stock. Check
here before drawing a new part. Nothing needs a library symbol to be listed.

Run from the KiCad-Library checkout:  python3 tools/build-parts-index.py
"""
import os, re, glob, collections, subprocess

BOARDS = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SKIP = {'KiCad-Library'}
PROP = re.compile(r'\(property "([^"]+)" "([^"]*)"')


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


def main():
    parts = collections.defaultdict(lambda: {'boards': set(), 'value': '', 'fp': '', 'mpn': ''})
    for repo in sorted(os.listdir(BOARDS)):
        if repo in SKIP or not os.path.isdir(os.path.join(BOARDS, repo, '.git')):
            continue
        for sch in glob.glob(os.path.join(BOARDS, repo, '**', '*.kicad_sch'), recursive=True):
            if '/libs/' in sch or '/archive/' in sch:
                continue
            try:
                text = open(sch, encoding='utf-8', errors='ignore').read()
            except OSError:
                continue
            for props in symbol_blocks(text):
                lcsc = (props.get('LCSC') or '').strip()
                if not re.fullmatch(r'C\d+', lcsc):
                    continue
                e = parts[lcsc]
                e['boards'].add(repo)
                e['value'] = e['value'] or props.get('Value', '')
                e['fp'] = e['fp'] or props.get('Footprint', '')
                e['mpn'] = e['mpn'] or props.get('MPN', '') or props.get('Manufacturer Part Number', '')

    rows = sorted(parts.items(), key=lambda kv: (-len(kv[1]['boards']), kv[0]))
    out = ["# Parts used", "",
           "Every component with an LCSC code used on an OpenDrone board, generated",
           "from the board schematics. A part listed here is already sourced and",
           "footprinted, so reuse is cheaper than drawing something new.",
           "",
           "Regenerate: `python3 tools/build-parts-index.py`", "",
           f"{len(rows)} distinct parts across {len({b for _, v in rows for b in v['boards']})} boards.", "",
           "| LCSC | Value | MPN | Footprint | Boards |", "|---|---|---|---|---|"]
    for lcsc, e in rows:
        fp = e['fp'].split(':')[-1]
        out.append(f"| {lcsc} | {e['value']} | {e['mpn']} | {fp} | {', '.join(sorted(e['boards']))} |")
    open(os.path.join(os.path.dirname(__file__), '..', 'PARTS-USED.md'), 'w').write('\n'.join(out) + '\n')
    print(f"{len(rows)} parts written to PARTS-USED.md")


if __name__ == '__main__':
    main()

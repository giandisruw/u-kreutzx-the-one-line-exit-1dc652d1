#!/usr/bin/env python3
""" The One-Line Exit — make.fun entry.

Writes one line (the funniest one-line resignation letter) to /output/entry.txt.
Stdlib only, no network, no API key.

The line was chosen by pairwise judging (Caffeine router, kit's judge
brief) over 6 drafted candidates: it won all 3 of its pairings.
"""

import os

LINE = 'Dear boss: I quit. The printer broke again, and unlike the printer, I can be fixed by leaving.'

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

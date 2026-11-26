#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line about a smart fridge to /output/entry.txt.
The line targets the fridge's firmware-update habit: a machine that
cannot simply say the milk is gone without Wi-Fi, a reboot, and
a permission slip first.
"""

from pathlib import Path

ROAST = (
    "My smart fridge pushed a firmware update at 3 a.m., and now it needs "
    "Wi-Fi, a reboot, and a permission slip just to tell me we're out of milk."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    line = ROAST.strip()
    if not line:
        raise SystemExit("roast line must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"roast line is {len(line)} chars, over the {MAX_CHARS} limit")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

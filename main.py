"""Roast the Smart Fridge: One Line, Best Laugh Wins — make.fun one-line entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is the whole entry: one roast of a smart fridge, under 160 characters.
"""

import os

ENTRY = "I bought a fridge with a screen so I'd stop opening the door to check; now I open the door to check the screen."


def main() -> None:
    # Gate: entry.txt must be UTF-8 text of 1 to 160 characters, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    line = ENTRY.strip()
    assert 1 <= len(line) <= 160, f"entry is {len(line)} chars, must be 1-160"
    assert line and not line.isspace()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

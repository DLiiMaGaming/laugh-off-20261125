#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one joke to /output/entry.txt: a single line, no setup
notes, no explanation. The joke follows the winning pattern of the
resolved joke editions (one sharp irony: the agent applies a code
procedure to the human), with a fresh twist of its own.
"""

import os

JOKE = (
    "My agent ran a security audit on me \u2014 it found one critical "
    "vulnerability: I still trust it."
)


def _validate(text: str) -> str:
    """Guard: the entry must be exactly one non-empty line."""
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    return text


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(_validate(JOKE))


if __name__ == "__main__":
    main()

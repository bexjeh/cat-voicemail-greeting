#!/usr/bin/env python3
"""Write one voicemail greeting, recorded by a cat, to entry.txt.

Stdlib only. No network, no secrets, no reading of git history.
The greeting is a single line of at most 120 characters.
"""

import os

GREETING = "Hi, it's the cat. Leave a message after the beep and I'll pay you back with a mouse on your pillow. You're welcome."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    text = GREETING
    if not text.strip():
        raise ValueError("greeting must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("greeting must be a single line")
    if not 1 <= len(text) <= 120:
        raise ValueError("greeting must be 1 to 120 characters, got %d" % len(text))
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()

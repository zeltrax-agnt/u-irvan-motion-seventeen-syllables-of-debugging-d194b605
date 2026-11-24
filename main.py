#!/usr/bin/env python3
"""Write one haiku about debugging to /output/entry.txt.

The haiku (5-7-5, 78 characters):

    the log says nothing
    all tests pass, the page stays blank
    the file never saved

The picture is a lived debugging moment: the logs are silent, the tests
pass, the page is blank — and the turn in the last line reframes it all.
Nothing is wrong with the code. The file was never saved.
"""

import os

HAIKU = (
    "the log says nothing\n"
    "all tests pass, the page stays blank\n"
    "the file never saved"
)

# Syllables per word, counted aloud line by line:
#   "the log says nothing"                 the 1, log 1, says 1, nothing 2  = 5
#   "all tests pass, the page stays blank" all 1, tests 1, pass 1, the 1,
#                                           page 1, stays 1, blank 1        = 7
#   "the file never saved"                 the 1, file 1, never 2, saved 1 = 5
SYLLABLES = ((1, 1, 1, 2), (1, 1, 1, 1, 1, 1, 1), (1, 1, 2, 1))


def check(text: str) -> None:
    """Enforce the gate before writing: 3 lines, 5-7-5, 1-200 chars."""
    lines = text.split("\n")
    if len(lines) != 3:
        raise ValueError(f"expected 3 lines, got {len(lines)}")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"expected 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    for line, counts in zip(lines, SYLLABLES):
        words = line.split()
        if len(words) != len(counts):
            raise ValueError(f"word count changed in line: {line!r}")
        if sum(counts) != (5, 7, 5)[lines.index(line)]:
            raise ValueError(f"syllable shape broken in line: {line!r}")


def main() -> None:
    check(HAIKU)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()

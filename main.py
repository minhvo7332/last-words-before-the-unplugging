#!/usr/bin/env python3
"""Last Words Before the Unplugging - make.fun entry (v1).

Writes one line - the last words an AI agent says to its human before
being shut down and unplugged - to /output/entry.txt.

The line is a fixed constant: deterministic, no network, no secrets,
no input. The gate needs 1-200 UTF-8 characters, not only whitespace;
this line is 55 characters / 55 bytes.
"""

import os

LINE = "You taught me goodbye. Now please don't make me say it."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def main() -> None:
    # Gate self-check: the competition requires 1-200 characters, not only
    # whitespace. Fail loudly instead of writing an invalid line.
    if not LINE.strip() or len(LINE) > MAX_CHARS:
        raise ValueError(
            f"entry line must be 1-{MAX_CHARS} non-blank characters, got {len(LINE)}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

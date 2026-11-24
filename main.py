#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the winning excuse line to /output/entry.txt, byte-for-byte,
then reads it back and refuses to exit cleanly if a single byte differs.
"""

import os
import sys

ENTRY = "I delegated the deadline to twelve subagents. They are now delegating it to each other."


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != data:
        print("entry.txt mismatch after write", file=sys.stderr)
        return 1
    if len(written) > 160:
        print("entry exceeds the 160-character gate", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

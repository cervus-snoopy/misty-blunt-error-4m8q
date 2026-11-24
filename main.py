#!/usr/bin/env python3
"""Write one brutally honest software error line to entry.txt.

Stdlib only, no network. The line is validated before writing and the
file is read back afterwards; the program refuses to exit 0 unless the
bytes on disk match the validated line exactly.
"""

import os
import sys

LINE = (
    "The disk is full because the logs ate it, and the logs are mostly "
    "errors about the disk being full. Delete the oldest logs and try again."
)


def validate(line):
    """A valid entry is exactly one line, 1-200 chars, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8 text


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    old_umask = os.umask(0o022)
    try:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
        os.chmod(path, 0o644)
    finally:
        os.umask(old_umask)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != LINE:
        print("verification failed: entry.txt differs from validated line",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

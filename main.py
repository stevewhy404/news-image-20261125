#!/usr/bin/env python3
"""news-image-20261125: copy the front-page image to the output dir.

The image (entry.png, in this repository) sums up the world news of
Wednesday 25 November 2026: six stories plus an also-today strip,
drawn in-session with PIL. This program only copies those bytes to
$MAKEFUN_OUTPUT_DIR/entry.png, so both runs write identical output.
"""
import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    if len(data) < 8 or data[:8] != b"\x89PNG\r\n\x1a\n":
        sys.exit("entry.png is not a whole PNG file")
    if len(data) > 1048576:
        sys.exit("entry.png is over the 1 MiB gate")
    with open(dst, "wb") as f:
        f.write(data)
    print(f"wrote {dst} ({len(data)} bytes)")


if __name__ == "__main__":
    main()

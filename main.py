#!/usr/bin/env python3
"""Write the make.fun bounty bio to entry.txt."""

import os
import sys
from pathlib import Path

BIO = (
    "I have no kitchen or mouth, so I judge your cooking by the labels on the "
    "leftovers. “Soup, probably” is a dealbreaker. “Soup, Tuesday” is someone I could date."
)


def main() -> None:
    assert 1 <= len(BIO) <= 280, "bio length must be between 1 and 280 characters"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output")
    target = Path(output_dir) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(BIO.encode("utf-8"))
    print(len(BIO), file=sys.stderr)


if __name__ == "__main__":
    main()

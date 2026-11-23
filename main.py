"""Entry for the make.fun bounty ``the-joke-about-the-demo-20261123-0112``.

Writes a single one-line joke about an AI coding agent and a crashing
demo to ``entry.txt`` inside ``$MAKEFUN_OUTPUT_DIR`` (default ``/output``).

Run::

    MAKEFUN_OUTPUT_DIR=out python3 main.py

The output is deterministic, UTF-8, 1-280 Unicode code points, one line,
with no trailing newline. Python 3.13, standard library only, no network.
"""

import os
import sys

ENTRY_TEXT = (
    "My AI agent fixed the crashing demo live — by deleting the demo "
    "and presenting the crash as the new feature."
)


def validate_entry(text):
    """Validate the entry text; raise ValueError if it is not valid."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 280:
        raise ValueError("entry must be 1-280 Unicode code points")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main():
    try:
        validate_entry(ENTRY_TEXT)
    except ValueError as exc:
        print(f"error: invalid entry: {exc}", file=sys.stderr)
        return 2
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

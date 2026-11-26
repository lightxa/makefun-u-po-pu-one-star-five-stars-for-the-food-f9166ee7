"""One Star, Five Stars for the Food.

Writes a single-sentence alien tourist's one-star review of planet Earth
that still slips in a real compliment about the food, to entry.txt.

Pure Python 3.13 standard library, deterministic, no network.
"""

# One specific grievance only an outsider would notice (Earth bottles its
# own free rain and sells it back to visitors) and one specific food
# (dumplings from a street cart); the comic turn lands in the last clause.
ENTRY = (
    "One star: this planet bottles its own free rain and sells it back "
    "to visitors, but the dumplings from a street cart were so good I "
    "almost forgave the whole racket."
)

import os
import sys


def main() -> int:
    """Write ENTRY to entry.txt under the output directory."""
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())

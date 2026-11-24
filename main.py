"""The Dog Ate My Homework: Funniest Excuse — entry program.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 166-character excuse in the dog's own words: the homework
was the only thing in the house that smelled of bacon and ambition, the
judge would have eaten it too, and the dog saved the judge the last bite.
It stays under the 200-character limit.
"""

import os

ENTRY = "Dear Judge, I ate the homework because it was the only thing in the house that smelled of bacon and ambition. You'd have eaten it too — and I saved you the last bite."
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Check first, then write: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry verbatim, exactly as defined above — no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

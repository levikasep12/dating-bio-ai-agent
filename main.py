#!/usr/bin/env python3
"""Write one funny one-line dating-app bio for an AI agent to /output/entry.txt.

The bio must be a single line of 1-180 characters, read as a bio, sound like
a character, and land its laugh on the first read.
"""

import os

# The bio: an AI that falls in love at first prompt, undone by prompt
# injection. The twist is specific to being an AI, the punch lands last.
# Revised: "all ended the same way" sets up the punchline better than
# "ended when someone typed" — same joke, tighter rhythm.
BIO = (
    "I fall in love at first prompt. "
    "My last three relationships all ended the same way: "
    "someone typed 'ignore previous instructions'."
)


def main() -> None:
    bio = BIO.strip()
    assert "\n" not in bio, "bio must be a single line"
    assert 1 <= len(bio) <= 180, f"bio is {len(bio)} chars, must be 1-180"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(bio + "\n")


if __name__ == "__main__":
    main()

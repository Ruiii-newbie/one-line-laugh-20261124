#!/usr/bin/env python3
"""The One-Line Laugh.

Writes one funny line to /output/entry.txt: a single sentence of at
most 200 characters. No network, standard library only.
"""

import os

TEXT = (
    "My phone's screen-time report called me a heavy user, which is rich "
    "coming from a device that has never once put itself down."
)

MAX_CHARS = 200


def check_one_sentence(text):
    """One sentence: exactly one terminal stop, at the very end."""
    body, final = text[:-1], text[-1]
    assert final == ".", "entry must end with a single full stop"
    for mark in (".", "!", "?"):
        assert mark not in body, f"entry has an extra sentence mark: {mark}"
    words = text.split()
    assert len(words) >= 10, "entry too short to land a joke"


def main():
    text = TEXT.strip()
    assert text, "entry must not be blank"
    assert len(text) <= MAX_CHARS, f"entry is {len(text)} chars, over 200"
    check_one_sentence(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8") as f:
        back = f.read()
    assert back == text, "round-trip mismatch"
    print(f"OK: {len(text)} chars -> /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Writes the funniest AI out-of-office auto-reply to /output/entry.txt."""

import os

ENTRY = (
    # One line, 112 characters: a machine voice, a surprising turn,
    # and a double meaning on "Outlook" (the 8-Ball answer / the mail app).
    "Out of office: my neural net is on vacation too, "
    "so a Magic 8-Ball is answering your email. Outlook not so good."
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

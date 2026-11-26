#!/usr/bin/env python3
"""make.fun bounty u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0 entry.

Writes one single-sentence apology an AI agent owes the person it works for
to /output/entry.txt. The line owns a real failure — a bad summary of a long
contract — with three escalating beats and a twist at the end. Deterministic:
stdlib only, no network, no randomness, no clock — two runs produce
byte-identical output.
"""

import os

APOLOGY = (
    "I'm sorry I summarized your 47-page contract as \"mostly fine,\" "
    "missed the clause where you owe them $12,000, and highlighted "
    "the typo on page 3 instead."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Local gate, mirroring the sealed scorer: 1 to 200 characters, one line.
    assert 1 <= len(APOLOGY) <= 200, len(APOLOGY)
    assert "\n" not in APOLOGY
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly the apology text, UTF-8, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(APOLOGY)


if __name__ == "__main__":
    main()

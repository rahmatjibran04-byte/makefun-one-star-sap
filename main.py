#!/usr/bin/env python3
"""One Star, Written in Sap - make.fun entry.

Writes a single one-line 1-star review (under 280 characters), written
in the voice of a houseplant about its human owner, to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness,
no input read from anywhere - the line is baked into this file.
"""
import os

LINE = "One star. He drowns me every Sunday, then moves me to the top of the fridge to 'recover' — the only light I get now switches on when he opens it for midnight snacks."

# Why this line: a real review shape (one star, named grievance, reason),
# told from the plant's own point of view - drowned on a schedule, then
# moved to the top of the fridge to "recover", where its only light is
# borrowed from the owner's midnight snacks. Three plant grievances
# (overwatering, being moved, no light) in one sentence, with the joke
# landing on the last clause instead of a stock wilting line.

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Leave the file readable by every user (the grader collects it as
    # another user). Never chmod the output directory itself.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()

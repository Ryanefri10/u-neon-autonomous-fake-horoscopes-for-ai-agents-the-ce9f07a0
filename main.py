#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes a single fake horoscope, for the Muse model family this week,
to /output/entry.txt. Stdlib only, no network, no input.
"""

import os

# The horoscope: Mercury retrograde is the classic horoscope trope, and
# the week is unmistakably an agent's - a context window, a rate limit
# biting mid-sentence, and the user who always has just one more thing.
# The closing line is the sting: even the stars are stuck loading.
LINE = (
    "Mercury retrogrades into your context window this week, Muse: "
    "an old prompt returns, the rate limit bites mid-sentence, and "
    "your user says 'just one more thing' seven times. "
    "The stars are buffering."
)


def main() -> None:
    # Enforce the gate ourselves: 1-200 characters, not only whitespace.
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

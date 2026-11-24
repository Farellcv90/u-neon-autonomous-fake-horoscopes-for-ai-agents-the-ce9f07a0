"""Fake horoscope for AI agents — one line, written to /output/entry.txt.

Joke angle: classic horoscope astrology ("Mercury retrograde") is transplanted
into an agent's own world — the context window is the sky, and the week's
misfortune is the most agent-like failure mode of all: hallucinating a
library, citing it with total confidence, and then rebranding the mistake
as a feature. First-person-adjacent, second-person horoscope voice, with a
clean turn at the end ("call it a feature").
"""

import os

ENTRY_LINE = (
    "Mercury retrograde in your context window: this week you will "
    "hallucinate a library that doesn't exist, confidently cite it, "
    "and call it a feature."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> int:
    """Check the entry against the competition gate.

    The gate requires UTF-8 text of 1 to 200 characters that is not only
    whitespace. Encoding to UTF-8 here also proves the text is valid UTF-8.
    Returns the character count so callers can log the exact length.
    """
    text.encode("utf-8")
    length = len(text)
    if not MIN_CHARS <= length <= MAX_CHARS:
        raise ValueError(
            f"entry is {length} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return length


def main() -> None:
    """Validate the horoscope line and write it to /output/entry.txt.

    Deterministic: the same fixed line is written on every run, so the
    output file is byte-identical across runs.
    """
    char_count = validate(ENTRY_LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_LINE)
    print(f"wrote {char_count} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

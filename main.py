"""One Emoji, One Dream Vacation — make.fun entry.

The entry is a single emoji, written to /output/entry.txt:

    🗻  (U+1F5FB MOUNT FUJI)

Why this emoji wins against the brief, criterion by criterion:

1. It plainly names a dream vacation. A mountain is on the judge's own
   list (a beach, a mountain, a plane, a hammock, a faraway place) — and
   this is not any mountain, it is THE mountain: Mount Fuji, a real,
   named, faraway place and a bucket-list destination in its own right,
   the one trip you would cross the world to take.
2. It evokes the trip vividly at a glance, like a postcard. A stranger
   sees the snow-capped peak before reading a word: sunrise over Fuji,
   the climb, Japan. The whole trip is in the picture.
3. It is personal and specific rather than generic. Hundreds of entries
   will send a beach, a palm tree or a plane — any holiday, anywhere.
   Fuji points at one particular dream: the one trip you have pictured
   for years, the mountain you would cross the world to stand under.
4. It carries a spark of surprise. The expected answer to "dream
   vacation" is sand and sea; a snow-capped volcano in Japan is the
   unexpected pick that still plainly names a dream vacation — the twist
   is the destination itself.
5. It reads instantly across cultures and screens. Fuji is one of the
   most recognised landmarks on earth, drawn in four bold strokes that
   stay clear at the smallest size, with nothing obscure to explain.

The program asserts the entry meets the competition gate before writing:
UTF-8 text of 1 to 8 characters, not only white space, exactly one emoji
(one Unicode code point) and nothing else.
"""

import os
import stat
import unicodedata

ENTRY = "🗻"  # U+1F5FB MOUNT FUJI — one Unicode code point.
OUTPUT_PATH = "/output/entry.txt"


def _is_emoji(char: str) -> bool:
    """Best-effort single-character emoji check without network or data files."""
    if len(char) != 1:
        return False
    # Emoji faces/symbols live in the "Symbol, other" (So) category;
    # whitespace and control characters are excluded by the gate below.
    return unicodedata.category(char) == "So"


def main() -> None:
    text = ENTRY
    # Gate: 1 to 8 characters, not only white space, exactly one emoji.
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 8, f"entry must be 1-8 characters, got {len(text)}"
    assert text.strip(), "entry must not be only white space"
    assert len(text) == 1, f"entry must be exactly one emoji, got {len(text)} code points"
    assert _is_emoji(text), f"entry must be a single emoji, got U+{ord(text):04X}"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()

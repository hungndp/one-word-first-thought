import os

# One word, first thought: "apricity" — the warmth of the sun on a cold
# winter's day. A rare, vivid word: it calls up a precise sensory image
# (cold skin, sudden sun), sounds soft and surprising, and is not the
# obvious pick. Exactly one word, 8 characters, no punctuation, no spaces.
TEXT = "apricity"

# Guard the gate: the entry must be exactly one word, 1-24 characters.
assert TEXT.isalpha() and 1 <= len(TEXT) <= 24, "entry must be one word"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

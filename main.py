"""Write the one-word-from-grandma entry to /output/entry.txt.

Exactly one word: the word grandma would text about AI.
"""

from pathlib import Path

ENTRY = "apaan"
# One word, 5 characters — the word grandma would text about AI.

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()

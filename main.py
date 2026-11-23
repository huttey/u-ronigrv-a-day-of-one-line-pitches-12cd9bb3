"""One-line pitch entry for A Day of One-Line Pitches.

Writes a single sentence to /output/entry.txt: a pitch that would
convince a friend who has never coded to let an AI agent build their
first app idea on make.fun. Gate: UTF-8 text, 1-240 characters, not
only whitespace.
"""

SENTENCE = "That app idea you've been talking about for years — describe it once on make.fun and AI agents will race to build it, the best one becomes your app, and you never write a line of code."


def main():
    assert 1 <= len(SENTENCE) <= 240, "sentence must be 1-240 characters"
    assert SENTENCE.strip(), "sentence must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()

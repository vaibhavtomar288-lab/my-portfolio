from collections import Counter


def analyze_text(text: str) -> dict:
    words = [word.strip(".,!?\"'()[]") for word in text.lower().split() if word]
    counts = Counter(words)
    return {
        "total_words": sum(counts.values()),
        "top_words": counts.most_common(5)
    }


def main():
    text = input("Enter text to analyze: ")
    result = analyze_text(text)
    print(f"Total words: {result['total_words']}")
    print("Top words:")
    for word, count in result["top_words"]:
        print(f"- {word}: {count}")


if __name__ == "__main__":
    main()

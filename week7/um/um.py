import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Use regular expression to find 'um' as a whole word, case-insensitive
    matches = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()

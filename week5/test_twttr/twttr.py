def main():
    s = input("Input: ")
    new_word = shorten(s)
    print("Output:", new_word)


def shorten(word):
    vowels = "aeiouAEIOU"
    return ''.join(c for c in word if c not in vowels)


if __name__ == "__main__":
    main()

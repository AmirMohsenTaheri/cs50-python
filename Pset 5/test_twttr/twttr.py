def main():
    name = input("Input: ")
    new_name = shorten(name)
    print(f"Output: {new_name}")


def shorten(word):
    new_word = ""
    for ch in word:
        if ch in [
        "a", "e", "u", "i", "o",
        "A", "E", "U", "I", "O",
        ]:
            continue
        else:
            new_word += ch
    return new_word

if __name__ == "__main__":
    main()

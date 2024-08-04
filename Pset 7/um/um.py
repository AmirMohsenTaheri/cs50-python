import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    text = "(^|\W)um($|\W)"
    match = re.findall(text, s, re.IGNORECASE)
    if match:
        return len(match)


...


if __name__ == "__main__":
    main()

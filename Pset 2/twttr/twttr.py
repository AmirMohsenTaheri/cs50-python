name = input("Input: ")
new_name = ""
for ch in name:
    if ch in [
        "a", "e", "u", "i", "o",
        "A", "E", "U", "I", "O",
        ]:
        continue
    else:
        new_name += ch
print(f"Output: {new_name}")

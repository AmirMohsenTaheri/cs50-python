def main():
    name = input("Please Enter? ")
    print(chenger(name))


def chenger(n):
    if ":)" or ":(" in n:
        n = n.replace(":)", "🙂")
        n = n.replace(":(", "🙁")
    return n


main()

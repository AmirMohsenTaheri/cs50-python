def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum():
        if 2 <= len(s) <= 6 :
            if s[0:2].isalpha():
                if last_digit(s):
                    if is_zero(s):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def last_digit(n):
    j = -1
    for i in range(len(n) -1):
        if n[j].isalpha():
            j -= 1
            if n[j].isdigit():
                return False
        else:
            j -= 1
    return True


def is_zero(z):

    for j in z:
        if j.isdigit():
            if j == "0":
                return False
            else:
                return True
    return True
main()

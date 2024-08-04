def main():
    x = get_fuel()

    if x <= 1:
        print("E")
    elif x >= 99:
        print("F")
    else:
        print(f"{int(x)}%")


def get_fuel():
    while True:
        try:
            fuel = input("Fraction: ")
            x, y = fuel.split("/")
            out = round((int(x) / int(y)) * 100)
            if out <= 100:
                return out
            else:
                pass
        except (ValueError, ZeroDivisionError):
            pass
main()

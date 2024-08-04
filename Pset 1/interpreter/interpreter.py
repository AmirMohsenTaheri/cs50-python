def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)
    print(computing(x,y,z))


def computing(x,y,z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "/":
        return x / z
    elif y == "*":
        return x * z

main()

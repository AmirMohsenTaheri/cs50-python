import inflect

p = inflect.engine()

my_name = []

while True:
    try:
        name = input("Input: ")
        my_name.append(name)
    except EOFError:
        break

print("Adieu, adieu, to", p.join(my_name))

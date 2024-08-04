import sys
import os

PATH = sys.argv[1]

# validation of PATH
def validation():

    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".txt"):
            if not os.path.exists(PATH):
                with open(PATH, 'w+') as file:
                    file.write("")
        else:
            sys.exit("Invalid argument")

    elif len(sys.argv) < 2 :
        sys.exit("Too few command-line arguments")

    else:
        sys.exit("Too many command-line arguments")

# add
def add(n, num):

    validation()

    new_phone = n + ":" + num + "\n"
    with open(PATH, 'a+') as file:
        file.write(new_phone)

# search
def search(name):

    validation()

    with open(PATH) as file:
        for line in file:
            if name == line.split(":")[0]:
                return line
            else:
                return "Not fund"

#  delete contact
def delete(name):
    validation()

    new_data = ""

    with open(PATH) as file:
        for line in file:
            if not name == line.split(":")[0]:
                new_data += line
    return new_data


def show():
    validation()
    with open(PATH, 'r') as file:
        print(file.read())


# ### start with menu
def main():
    while True:
        try:
            menu ="Menu:\n 1-Add contacts\n 2-Search contacts\n 3-Delete contacts \n 4-Show all contacts \n 0-Exit"
            print(menu)
            ch = int(input("please choose: "))
            os.system('clear')

            if ch == 1:
                name = input("Enter Name:  ")
                number = input("Enter Number: ")
                add(name, number)

            elif ch == 2:
                name = input("Enter Name:  ")
                print(search(name))


            elif ch == 3:
                name = input("Enter Name:  ")
                new_data = delete(name)
                with open(PATH, "w") as file:
                    file.write(new_data)

            elif ch == 4:
                show()

            elif ch == 0:
                sys.exit("Good by")

            else:
                pass

        except (TypeError, ValueError):
            os.system('clear')
            pass

if __name__ == "__main__":
    main()

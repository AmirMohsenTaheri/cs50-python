import sys

if len(sys.argv) == 2:

    if sys.argv[1].endswith(".py"):

        try:

            line_cunt = 0

            with open(sys.argv[1], "r") as file:
                lines = file.readlines()

                for line in lines:

                    line = line.lstrip()
                    
                    if line.startswith("#"):
                        continue

                    elif line == "":
                        continue

                    else:
                        line_cunt += 1
            print(line_cunt)

        except (FileNotFoundError):
            sys.exit("File does not exist")

    else:
        sys.exit("Not a Python file")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments ")

elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

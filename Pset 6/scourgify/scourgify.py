import sys
import csv

if len(sys.argv) == 3:
    try:
        list_dic = []
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                list_dic.append({"first" : first, "last": last, "house" : row["house"]})

        with open(sys.argv[2], "w") as new_file:
            writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for i in range(len(list_dic)):
                writer.writerow({"first": list_dic[i]["first"], "last": list_dic[i]["last"], "house": list_dic[i]["house"]})


    except(FileNotFoundError):
        sys.exit(f"Could not read {sys.argv[1]}")

elif len(sys.argv) <= 3:
    sys.exit("Too few command-line arguments ")

elif len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments")

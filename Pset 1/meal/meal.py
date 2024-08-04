def main():
    time = input("What time is it? ")
    mealTime = convert(time)
    if 7 <= mealTime <= 8 :
        print("breakfast time")
    elif 12 <= mealTime <= 13:
        print("lunch time")
    elif 18 <= mealTime <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)
    hours = float(hours)
    if minutes == 0:
        return hours + 0
    elif 0 < minutes <= 15:
        return hours + 0.25
    elif 15 < minutes <= 30:
        return hours + 0.5
    elif 30 < minutes <= 45:
        return hours + 0.75
    elif 45 < minutes < 60 :
        return hours + 0.99


if __name__ == "__main__":
    main()

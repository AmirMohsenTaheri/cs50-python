import random


def main():
    eqn = 0
    score = 0
    level = get_level()
    while eqn < 10:
        x, y = generate_integer(level)
        answer = x + y
        j = 0
        while j < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == answer:
                    eqn +=1
                    score += 1
                    break
                else:
                    raise ValueError
            except (ValueError, NameError):
                print("EEE")
                j += 1
                pass
            if j == 3:
                eqn += 1
                print((f"{x} + {y} = {answer}"))
                break
    print(f"Score: {score}")







def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass



def generate_integer(level):
    match level:
        case 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        case 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        case 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        case _:
            raise ValueError
    return x, y


if __name__ == "__main__":
    main()

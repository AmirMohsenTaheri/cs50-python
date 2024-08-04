import random
import sys
while True:
    try:
        level = int(input("level: "))
        if level > 0:
            n = random.randint(1, level)
            while True:
                try:
                    guess = int(input("guess: "))
                    if guess > n:
                        print("Too large!")
                    elif guess < n :
                        print("Too small!")
                    else:
                        print("Just right!")
                        sys.exit()
                except (ValueError):
                    pass
        else:
            pass
    except(ValueError):
        pass
    
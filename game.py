import random


def main():

    while True:
        s_level = input("Level: ")

        try:
            level = int(s_level)

            if level > 1:
                g_number = random.randint(0, level)
                break
        except:
            pass

    while True:

        guess = input("Guessing: ")

        try:
            if int(guess) < g_number:
                print("Too small!")
            elif int(guess) > g_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except:
            pass


if __name__ == "__main__":
    main()

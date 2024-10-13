import random


def main():
    # Variables
    count = 9
    score = 0
    level = get_level()

    # Loop for 10 questions
    while count >= 0:
        # Generate random numbers with the function
        numbers = generate_integer(level)

        # Assign random numbers to check_answer function
        u_answer = check_anwser(numbers[0], numbers[1])
        count -= 1

        # Check for True value of the check_answer function to count the score
        if u_answer == True:
            score += 1
        else:
            None

    print(f"Score: {score}")


def get_level():

    while True:
        try:
            l = int(input("Level: "))
            if l >= 1 and l <= 3:
                break

        except ValueError:
            pass

    return l


def generate_integer(level):

    if level == 1:
        x = random.randint(0, 10)
        y = random.randint(0, 10)

    elif level == 2:
        x = random.randint(10, 100)
        y = random.randint(10, 100)

    elif level == 3:
        x = random.randint(100, 1000)
        y = random.randint(100, 1000)

    else:
        raise ValuError

    return x, y


# Fuction dedicated to check the user answer inside a while loop
def check_anwser(x, y):

    attempts = 3
    question = f"{x} + {y} = "
    t_answer = x + y

    while True:

        # First check for the number of attempts left
        if attempts == 0:
            print(f"{question} {t_answer}")
            break

        try:
            user_answer = int(input(f"{question}"))

            # If the answer is correct
            if user_answer == t_answer and attempts >= 1:
                return True

            # If the answer is incorrect and still there is attemps left
            elif user_answer != t_answer and attempts >= 1:
                print("EEE")
                attempts -= 1

        # if the user inputs other value than a positive integer
        except:
            print("EEE")
            attempts -= 1
            pass


if __name__ == "__main__":
    main()

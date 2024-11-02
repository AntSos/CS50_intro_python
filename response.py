import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(email):

    response = validators.email(email)

    if response == True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()

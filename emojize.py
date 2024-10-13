import emoji


def main():
    enter = input("Input: ")

    print(f"Output: {emoji.emojize(enter, language="alias")}")


if __name__ == "__main__":
    main()

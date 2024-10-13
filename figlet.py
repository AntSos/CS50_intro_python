import sys
import random
from pyfiglet import Figlet


def main():

    # Create a list with the fonts
    fonts = Figlet().getFonts()

    # Create a comand line arguments list
    comand_line = ["-f", "--font"]

    # First 3 conditions
    if len(sys.argv) == 3 and sys.argv[1] in comand_line and sys.argv[2] in fonts:
        new_text = Figlet(font=sys.argv[2])

    # Second single condition
    elif len(sys.argv) == 1:
        new_text = Figlet(font=fonts[random.randint(0, len(fonts))])

    # Exit sistem
    else:
        sys.exit("Invalid usage")

    # Ask for text and print it
    text = input("Input: ")
    print(new_text.renderText(text))


if __name__ == "__main__":
    main()

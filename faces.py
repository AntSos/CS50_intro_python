def main():
    enter = input("Writesome text:  and add an emoticon: ")
    print(emoji(enter))

def emoji(text):
    return text.replace(":)", "\U0001F642").replace(":(", "\U0001F641")


if __name__=="__main__":
    main()

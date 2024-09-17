def main():
    enter = input("Writesome text: ")
    print(slow_them(enter))

def slow_them(text):
    return text.replace(" ", "...")


if __name__=="__main__":
    main()
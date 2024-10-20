def main():

    greeting = input("Greeting: ")

    cash = value(greeting)

    print(f"${cash}")

def value(greeting):

    greeting = greeting.lower().replace(" ", "")

    if "hello" in greeting:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100



if __name__=="__main__":
    main()


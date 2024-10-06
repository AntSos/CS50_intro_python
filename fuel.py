def main():

    while True:

        fraction_str = input("Fraction: ")
        fraction_list = fraction_str.split("/")

        try:
            x = int(fraction_list[0])
            y = int(fraction_list[1])

            result = x / y

            if result <= 1:
                break

        except ValueError:
            pass

        except ZeroDivisionError:
            pass

    percent = round((result) * 100)

    if percent <= 1:
        print("E")

    elif percent >= 99:
        print("F")

    else:
        print(f"{percent}%")

if __name__=="__main__":
    main()

def main():

    fraction_str = input("Fraction: ")
    percent = convert(fraction_str)
    result = gauge(percent)
    print(result)

def convert(fraction_str):

    while True:

        fraction_list = fraction_str.split("/")

        try:
            x = int(fraction_list[0])
            y = int(fraction_list[1])

            result = x / y

            if result <= 1:
                percent = round((result) * 100)
                return percent

            else:
                fraction_str = input("Fraction: ")
                pass

        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):

    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage}%"

if __name__=="__main__":
    main()


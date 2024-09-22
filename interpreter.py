def main():

    expression = input("Expression: ").lower().split()

    x = float(expression[0])
    y = expression[1]
    z = float(expression[2])


    if y == "+":
        result = (x + z)

    elif y == "-":
        result = (x - z)

    elif y == "*":
        result = (x * z)

    elif y == "/":
        result = (x / z)


    print(round(result, 1))


if __name__=="__main__":
    main()

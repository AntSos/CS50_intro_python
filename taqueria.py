def main():

    menu = {"Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
            }

    total_order = 0.0

    try:
        while True:
            item = input("Item: ").title()
            if item in menu:
                total_order += menu[item]

                print("Total: $", end = "")
                print(f"{total_order:.2f}")

    except EOFError:
        print()

if __name__=="__main__":
    main()

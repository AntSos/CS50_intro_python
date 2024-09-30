def main():

    total_amount = 50

    while total_amount > 0:
        print(f"Amount Due: {total_amount}")
        inserted = int(input("Insert Coin: "))
        if inserted == 25 or inserted == 10 or inserted == 5:
            total_amount -= inserted
        else:
            continue
    print(f"Change Owed: {total_amount * -1}")


if __name__=="__main__":
    main()

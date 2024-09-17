def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = float(d[1:])
    return dollars

def percent_to_float(p):
    percent = float(p[0:2]) / 100
    return percent

if __name__=="__main__":
    main()
def main():
    mass = input("Enter a mass in Kilograms: ")
    result = calculate_E(mass)
    print(f"E = {result}")

def calculate_E(mass):
    return int(mass) * (300000000)**2


if __name__=="__main__":
    main()

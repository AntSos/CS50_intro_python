def main():

    day_time = input("What time is it? ")

    new_hour = convert(day_time)

    if new_hour >= 7 and new_hour <= 8:
        print("breakfast time")

    elif new_hour >= 12 and new_hour <= 13:
        print("lunch time")

    elif new_hour >= 18 and new_hour <= 19:
        print("dinner time")

    else:
        print("")

def convert(time):
    # Split string by : character
    new_time = time.split(":")
    # Time to float format
    new_hour = ((float(new_time[0]) * 60) + float(new_time[1])) / 60

    return new_hour

if __name__=="__main__":
    main()

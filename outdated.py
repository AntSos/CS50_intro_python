def main():

    months = [  "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
              ]

    while True:
        try:
            user_date = input("Date: ").strip()

            if "/" in user_date:
                month, day, year = user_date.split("/")
                if int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
                    break

            elif "," in user_date:
                month, day, year = user_date.split()
                if month in months:
                    month = months.index(month) + 1
                    day = int(day.replace(",", ""))
                    year = int(year)

                    if int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
                        break

        # Catch exception
        except:
            pass

    # Format one digit with 2
    print(f"{year}-{int(month):02}-{int(day):02}")

if __name__=="__main__":
    main()
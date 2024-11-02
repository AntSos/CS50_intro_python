import re


def main():
    print(convert(input("Hours: ")))


def convert(s):

    # Pattern to get the dessired hour with tags for each elemnt
    h_pattern = r"(?P<s_hour>0?[1-9]|1[0-2])(?P<s_c_hour>:[0-5]\d)?\s(?P<s_M_hour>[AP]M)\s+to\s+(?P<f_hour>0?[1-9]|1[0-2])(?P<f_c_hour>:[0-5]\d)?\s(?P<f_M_hour>[AP]M)"

    # If there is a match, assign it to the variable and assign all the other variables according to the tag
    if hour_match := re.search(h_pattern, s, re.IGNORECASE):

        s_hour = int(hour_match.group("s_hour"))
        s_c_hour = hour_match.group("s_c_hour")
        s_M_hour = hour_match.group("s_M_hour")
        f_hour = int(hour_match.group("f_hour"))
        f_c_hour = hour_match.group("f_c_hour")
        f_M_hour = hour_match.group("f_M_hour")

        # Adjust bouth hours values if they are 12
        if s_hour == 12:
            s_hour = 0

        if f_hour == 12:
            f_hour = 0

    else:
        raise ValueError

    # Hour order: AM to PM increse final hour
    if s_M_hour == "AM" and f_M_hour == "PM":
        f_hour += 12
    # Hour order: AM to PM increse starting hour
    elif s_M_hour == "PM" and f_M_hour == "AM":
        s_hour += 12

    # Case 1: bouth minutes are None and first hour is in AM
    if s_c_hour == None and f_c_hour == None:
        return f"{s_hour:02d}:00 to {f_hour:02d}:00"

    # Case 2: first hour minutes is None
    elif s_c_hour == None and f_c_hour != None:
        # Check for minutes less than 60
        if int(f_c_hour[1:]) >= 60:
            return ValueError
        else:
            return f"{s_hour:02d}:00 to {f_hour:02d}{f_c_hour}"

    # Case 3: second hour minutes is None
    elif s_c_hour != None and f_c_hour == None:
        # Check for minutes less than 60
        if int(s_c_hour[1:]) >= 60:
            return ValueError
        else:
            return f"{s_hour:02d}{s_c_hour} to {f_hour:02d}:00"

    # Case 4: minutes are present in bouth given hours
    else:
        # Check bouth minutes less than 60 in bouth hours
        if int(s_c_hour[1:]) >= 60 or int(f_c_hour[1:]) >= 60:
            return ValueError

        else:
            return f"{s_hour:02d}{s_c_hour} to {f_hour:02d}{f_c_hour}"


if __name__ == "__main__":
    main()

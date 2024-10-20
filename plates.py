def main():

    plate = input("Plate: ")

    is_valid(plate)

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Condition for logitud greater than 2 and less or equal to 6
    if len(s) >= 2 and len(s) <= 6:
        # If every character is letter,return true
        if s.isalpha():
            return True
        # Else if first two characters are lettersan the others numbers
        elif s[:2].isalpha() and s.isalnum():
            # Loop trhough every character of the string string
            for char in s:
                # If it is a digit
                if char.isdigit():
                    # Its number index position will be saved in position variable
                    position = s.index(char)
                    # If from this position its a number and diferent from 0
                    if s[position:].isdigit() and int(char) != 0:
                        return True
                    else:
                        return False

        else:
             return False

    else:
        return False

if __name__=="__main__":
    main()

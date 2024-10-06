def main():

    grocery_list = {}

    try:
        while True:
            item = input("").upper()

            # If the item is in the dictionary
            if item in grocery_list:
                # Update the value of that item adding 1
                grocery_list[item] = grocery_list[item] + 1

            # Else, add the item to the dictionary and assign 1 as value
            else:
                grocery_list[item] = 1

    # Catch exception when control + d is pressed
    except EOFError:
        print()

    # Sort elements in grocery_list dictionary: # sorted(grocery_list.keys()) also could be used
    # Create a list of the keys in grocery_list dictionary
    grocery_list_keys = list(grocery_list.keys())
    # Sort that list using .sort()
    grocery_list_keys.sort()
    # Create anew dictionary usig grocery_list dictionary and the previous sorted list
    sorted_grocery_list = {i: grocery_list[i] for i in grocery_list_keys}

    # Print every element in the sorted dictionary
    for element in sorted_grocery_list:
        print(sorted_grocery_list[element], element)

if __name__=="__main__":
    main()
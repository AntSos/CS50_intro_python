def main():
    variable_name = input("camelCase: ")
    new_variable_name = ""

    # Loop throght variable name
    for letter in variable_name:
        # Condition for uppercase letters 0 index
        if letter.isupper():
            new_variable_name += "_" + letter.lower()
        else:
            new_variable_name += letter

    print(f"snake_case: {new_variable_name}")
if __name__=="__main__":
    main()

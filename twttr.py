def main():

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    word = input("Input: ")
    new_word = ""

    # Loop throght the word
    for letter in word:
        # Condition for vowels in the list
        if letter in vowels:
            new_word += ""
        else:
            new_word += letter

    print(f"Output: {new_word}")

if __name__=="__main__":
    main()

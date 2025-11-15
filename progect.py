def get_ascii_value():
    """
    Prompts the user to enter a character and prints its ASCII/Unicode value.
    """
    while True:
        char_input = input("Enter a single character: ")

        if len(char_input) == 1:
            ascii_value = ord(char_input)
            print(f"The ASCII/Unicode value of '{char_input}' is: {ascii_value}")
            break
        else:
            print("Invalid input. Please enter only a single character.")
get_ascii_value()
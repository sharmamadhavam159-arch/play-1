def check_age():
    """
    Prompts the user for their age, validates the input, and checks if it's even or odd.
    """
    while True:
        age_input = input("Please enter your age: ")

        try:
            # Attempt to convert the input into an integer
            age = int(age_input)

            # Check if the age is a reasonable, non-negative number
            if age < 0 or age > 120:
                print(f"Error: Age '{age_input}' seems invalid or unreasonable (must be between 0 and 120). Please try again.")
                continue # Loop again for new input
            
            # If conversion and range check pass, the input is correct
            print(f"Success: The age entered is correctly recorded as {age}.")

            # Check if the age is even or odd using the modulo operator (%)
            if age % 2 == 0:
                print(f"The age {age} is an even number.")
            else:
                print(f"The age {age} is an odd number.")
            
            break # Exit the while loop since valid input was received

        except ValueError:
            # This block runs if int(age_input) fails (e.g., user enters "ten" or "abc")
            print(f"Error: Invalid input '{age_input}'. Please enter a whole number (digits only).")
            # Loop again for new input

if __name__ == "_main_":
    check_age()
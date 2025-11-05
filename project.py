def classify_temperature():
    """
    Prompts the user for a temperature and classifies it into categories
    using conditional statements.
    """
    try:
        temperature_str = input("Enter the temperature in Celsius: ")
        temperature = float(temperature_str)

        if temperature < 0:
            print(f"The temperature {temperature}°C is Freezing.")
        elif 0 <= temperature < 10:
            print(f"The temperature {temperature}°C is Very Cold.")
        elif 10 <= temperature < 20:
            print(f"The temperature {temperature}°C is Cold.")
        elif 20 <= temperature < 30:
            print(f"The temperature {temperature}°C is Moderate.")
        elif 30 <= temperature < 40:
            print(f"The temperature {temperature}°C is Hot.")
        else:  # temperature >= 40
            print(f"The temperature {temperature}°C is Very Hot.")

    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")

# Call the function to run the program
classify_temperature()
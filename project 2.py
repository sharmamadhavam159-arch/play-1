
character = input("Enter a character: ")
if len(character) != 1:
    print("Please enter only a single character.")
else:
 if character.isalpha():
        print(f"'{character}' is an alphabet.")
 else:
       print(f"'{character}' is not an alphabet.")
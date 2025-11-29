num_str = input("Enter a number: ")
try:
    num = int(num_str)
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()
count = 0 
if num == 0:
    count = 1
else:
    if num < 0:
        num = -num
    while num > 0:
        num //= 10 
        count += 1
print(f"The number of digits in {num_str} is: {count}")
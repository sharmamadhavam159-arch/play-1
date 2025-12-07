def decimal_to_binary(decimal_num):
    """
    Converts a decimal number (integer) to its binary representation.
    """
    if decimal_num == 0:
        return "0"
    binary_representation = ""
    temp_num = abs(decimal_num)
    while temp_num > 0:
        remainder = temp_num % 2
        binary_representation = str(remainder) + binary_representation
        temp_num = temp_num // 2 
    if decimal_num < 0:
        return "-" + binary_representation
    else:
        return binary_representation
num1 = 45
num2 = 0
num3 = -10
print(f"The binary representation of {num1} is: {decimal_to_binary(num1)}")
print(f"The binary representation of {num2} is: {decimal_to_binary(num2)}")
print(f"The binary representation of {num3} is: {decimal_to_binary(num3)}")

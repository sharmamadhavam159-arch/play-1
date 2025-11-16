medical_cause = input("medical cause Y or N")
if medical_cause == 'Y':
    print("allowed")
atten = int(input("attendnce "))
if atten >= 75:
    print("allowed")
else:
    print("not allowed")
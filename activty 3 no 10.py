print("Enter marks  obtain in 3 exam ")
n1 = int(input("physics"))
n2 = int(input("chemistry"))
n3 = int(input("maths"))
total = n1 + n2 + n3 
avg = (total / 3)
if avg >= 40 : 
    print("you are pass")
else : 
    print("you re fail")
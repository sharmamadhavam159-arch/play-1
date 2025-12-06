row = int(input("Enter your number:")) 
number = 1
print("flyod triangle")
for i in range(1 , row +   1) :
    for j in range (1 , i + 1 ) :
        print( number , end = "")
        number = number + 1
    print()
valid = False
while not valid : #uing nested while loop
    try:
       n=int(input("Enter a number:"))
       while n%2 == 0:
        print("bye")
       valid = True
    except ValueError :
        print("invlid")
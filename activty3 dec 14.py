def add(p,Q):
    return(p+Q)
def sub(p,Q):
    return(p-Q)
def multyply(p,Q):
    return(p*Q)
def divde(p,Q):
    return(p/Q)
print("please select option")
print("a . add")
print("b . subtract")
print("c . multyply")
print("d . divide")
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
choice = input("enter a,b,c,d")
if choice == "a":
    result=add(num1,num2)
    print("add is",result)
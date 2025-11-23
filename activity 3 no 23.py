num = int(input("Enter a number:"))
sum = 0
tem = num
while tem > 0:
    digit = tem % 10
    sum+=digit**3
    tem//= 10 
if sum== num:
    print("it is amstrong number")
else:
    print("it is not amstrong number")
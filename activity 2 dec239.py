try:
    num1, num2 = eval(input("Enter two number, seperated by a comma :"))
    result = num1 / num2 
    print("result is", result)
#using multiple except  block for different type of error
except ZeroDivisionError:
    print("division by zero is error||")
except SyntaxError:
    print("coma is missing . Enter numbers seperated by comma like this 1,2")
except:
    print("wrong input")
else:
    print("No exceptions")
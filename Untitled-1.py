rows = int(input("Please Enter the Total Number of Rows: "))
ch = input("Please Enter any Character: ")
print("Mirrored Right Triangle Star Pattern")
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if(j <= rows - i):
            print(' ', end = '') 
        else:
            print('%c' %ch, end = '')
    print() 

print("half pyramid partern of (*)")
n = int(input("enter number of row:" ))
for i in range(n): 
  for j in range(i+1):
    print("* ",end="")
  print()
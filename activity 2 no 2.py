amount = int(input("Please enter the amount"))
count100 = amount//100
print("100 ruppe notes", count100)
remaing = amount % 100
print("remaing after 100 ",remaing )
count50 = remaing//50
print("50 ruppe notes",count50)
remaing = remaing % 50
print("remaing after 50", remaing)
count20 = remaing//20
print("20 ruppe notes", count20)
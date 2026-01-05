L = (4,5,1,2,9,7,8,10)
print("oringnal list:",L)
count = 0 
for i in L:
    count += i 
avg = count/len(L)
print("sum =",count)
print("average =",avg)
L.sort()
print("Smallest element is:",L[0])
print("largest elementi is:",L(-1))
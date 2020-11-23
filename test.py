a = [1,2,3,4,5]

b = [0]*len(a)

for i in range(len(a)):
    b[i-3] = a[i]

print(b)
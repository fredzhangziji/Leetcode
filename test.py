import bisect

a = [1,2,3,4,5,7]

i = bisect.bisect(a,6)
a.insert(i, 6)
print(a, i)
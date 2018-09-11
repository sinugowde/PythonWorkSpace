numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(numList)
listLen = len(numList)
listIter = iter(numList)
for item in range(listLen):
    print(next(listIter))

print("-"*20)

o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)
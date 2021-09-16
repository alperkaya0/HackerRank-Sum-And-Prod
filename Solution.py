import numpy

inp = input()
inp = inp.split(" ")
n = int(inp[0])
m = int(inp[1])


array = []

for x in range(n):
    arr = input()
    arr = arr.split(" ")

    for x in range(len(arr)):
        arr[x] = float(arr[x])
    
    array.append(arr)

print(int(numpy.prod(numpy.sum(array, axis = 0))))


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
x = arr.copy()
arr[0] = 42 

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5, 6])
x = arr.view()
arr[0] = 42 

print(arr)
print(x)

a = arr.copy()
b = arr.view()

print(a.base)
print(b.base)

3
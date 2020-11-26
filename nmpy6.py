 #shape of an array

import numpy as np

arr = np.array([[1, 2, 3, 4,], [5, 6, 7, 8,]])
print(arr.shape)

arr = np.array([1, 2, 3, 4, 5], ndmin=5)

print(arr)
print('Shape of array: ',arr.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 4, 3, 2, 1, 4, 4])
newarr = arr.reshape(4, 3) #from 1-D to 2-D
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 4, 3, 2, 1, 4, 4])
newarr = arr.reshape(2, 3, 2)
print(newarr)

arr = np.array([1, 2, 3, 5, 4, 5, 6, 7, 8])
newarr = arr.reshape(3, 3)
print(newarr)

arr = np.array([1, 2, 3, 5, 4, 5, 6, 7])
print(arr.reshape(2, 4).base)

arr = np.array([1, 2, 3, 5, 4, 5, 6, 7])
newarr = arr.reshape(2, 2, -1)
print(newarr)

arr = np.array([[1, 2, 3, 5],[ 4, 5, 6, 7]])
newarr = arr.reshape(-1)
print(newarr)
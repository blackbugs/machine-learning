import numpy as np

mylist = [1, 2, 4, 5, 3, 6, 6, 9, 8, 10]

arr = np.array(mylist)

print(arr)
print(type(arr)) # to check the type
arr0 = np.array(42) # 0-D arrays
print(arr)

arr1 = np.array([1, 2, 3, 4, 5, 6, 7]) #1-D arrays
print(arr)

arr2 = np.array([[1,2,3,4,5,6], [6,5,4,3,2,1]]) #2-D arrays
print(arr)

arr3 = np.array([[[1,2,3,4,5,6],[1,2,3,4,5,6]], [[1,2,3,4,5,6],[6,5,4,3,2,1]]]) #3-D arrays
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
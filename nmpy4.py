import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.dtype) #to know the type use "dtype" function.

arr = np.array(['apple', 'banana', 'mango', 'cherry'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4,], dtype='S')
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4,], dtype='i4')
print(arr)
print(arr.dtype)

arr = np.array([1.2, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

arr = np.array([1.2, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)

arr2 = np.arange(20,41)
print(arr2)

fives = np.ones(10)*5
print(fives)

arr3 = np.random.randint(1, 50, 24).reshape(3, 4, 2)
print(arr3)

arr4 = np.random.rand(4,5)
print(arr4)

np.random.seed(123)
arr5 = np.random.randint(1, 50, 20)
print(arr5%2 == 0)

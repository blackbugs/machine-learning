import numpy as np

arr = np.array([1, 2, 3, 5, 6, 7])
print([2]) #access the element by index value

print(arr[0] + arr[3]) #add two element by its index value

arr = np.array([[1, 2, 3, 5, 6, 7],[1, 2, 3, 5, 6, 7]])
print('2nd element on 1st element: ', arr[0, 1]) #Access the 2nd element on 1st dim in 2D arrays

arr = np.array([[1, 2, 3, 5, 6, 7],[1, 2, 3, 5, 6, 7]])
print('5th element on 2nd dim:', arr[1, 4])

#Access 3D arrays

arr = np.array([[[1, 2, 3, 5, 6, 7],[1, 2, 3, 5, 6, 7]],[[1, 2, 3, 5, 6, 7],[1, 2, 3, 5, 6, 7]]])
print('Access the third element of the second array of the first array: ',arr[0, 1, 2]) #Access the third element of the second array of the first array

#negative indexing

arr = np.array([[1, 2, 3, 5, 6, 7],[1, 2, 3, 5, 6, 7]])
print('Last element from 2nd dim: ', arr[1, -1])

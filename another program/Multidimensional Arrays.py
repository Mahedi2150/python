from numpy import *

array1 = array([
    [1,2,3,4,6,8],
    [4,4,3,6,2,1]
])

"""print(array1)
print(array1.dtype)
print(array1.ndim)
print(array1.shape)
print(array1.size)"""

array2 = array1.flatten()
print("1D :",array2)

array3 = array2.reshape(3,4)
print(array3)

array4 = array2.reshape(2,2,3)
print(array4)

print(array4.ndim)
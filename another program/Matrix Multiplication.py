import numpy as np


m1 = ([1,2,3],
      [4,5,6],
      [7,3,5]
)

m2 = ([3,4,2],
      [7,8,9],
      [3,5,9]
)
result = np.add(m1,m2)
print("ADD :\n",result)

result = np.subtract(m1,m2)
print("SUB :\n",result)

result = np.dot(m1,m2)
print("Matrix Multiplication :\n",result)

result = np.multiply(m1,m2)
print("General Multiplication :\n",result)

result = np.divide(m1,m2)
print("General Division :\n",result)

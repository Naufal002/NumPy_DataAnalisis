import os 
os.system('cls')

# Import Module Numpy
import numpy as np

a = np.matrix([[1,1],
                [1,1]])

b = np.matrix([[2,2],
                [2,2]])

total = np.dot(a,b)
print(total)
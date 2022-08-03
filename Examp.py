import os
os.system('cls')

# IMPORT PACKAGE NUMPY
import numpy as np

a = np.matrix([[1,1],
                [1,1]])

b = np.matrix([[2,2],
                [2,2]])

total = np.dot(a,b)
print(total)


'''
a = np.arange(1,6,3)

# DISPLAY
hasil_akhir = len(a)
print(f"{a} | Panjang: {hasil_akhir}")
'''

# [1 1]  [2 2]
# [1 1]  [2 2]

# [1.2 + 1.2]
# [1.2 + 1.2]

# = [4 4]
#     [4 4]
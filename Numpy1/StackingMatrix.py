import numpy as np

a = np.array(([1,2,3]))

b = np.array(([4,5,6]))

Matrix_a = np.zeros((2,3))
Matrix_b = np.ones((2,3))

# Stacking Matrix
c = np.hstack((a,b))
d = np.vstack((a,b))

Stacking_Matrix = np.vstack((Matrix_a,Matrix_b))
print(Stacking_Matrix)

print(d)
 
print(c)
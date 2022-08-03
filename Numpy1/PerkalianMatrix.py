import numpy as np

a = np.array((
    [1,2],
    [3,4]
))

b = np.ones((2,2))

print("matrix A")
print(a)

print("matrix B")
print(b)


# Perkalian matrix
c = np.dot(a,b)

print("Matirix C")
print(c)
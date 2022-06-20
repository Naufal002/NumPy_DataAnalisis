
import numpy as np

    # Data

    # Kolom: 3
    # Baris: 2
a = np.array((
    [1,2,3],
    [4,5,6]
))

print("matrix dengan ukuran: ",a.shape)
print(a)

    # Transpose
print("Transpose Matrix dari a: ")
print(np.transpose(a))


    # Flatten
print("Flatten Matrix a:")
print(np.ravel(a))

    #Reshape Matrix
print("Reshape Matrix dari a:")
print(a.reshape(1,6)) 
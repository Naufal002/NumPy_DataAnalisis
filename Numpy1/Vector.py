
import numpy as np

# Membuat Vector
a = np.array([1,2,3,4,5])
b = np.array([1.5, 2.5, 5, 6, 7])

# Membuat Vector dengan range
c = np.arange(1,10,2)

# Membuat Linscape
d = np.linspace(1,10,4)

# array multidimensi/Matrix
e = np.array([(1,2,3), (4,5,6)])

# matrix dengan zeros
f = np.zeros((5,5))

# matrix dengan nilai satu
g = np.ones((5,5))

# matrix identitas
h1 = np.identity(5)
h2 = np.eye(5)

    # Display
print(h2)
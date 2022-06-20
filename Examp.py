import numpy as np

a = np.array((
    [1,2],
    [3,4]
))

b = np.ones((2,2))


# Count 
c = np.dot(a,b)
print(c)
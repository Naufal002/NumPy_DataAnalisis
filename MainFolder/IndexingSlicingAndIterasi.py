import numpy as np
import 

a = np.arange(10)**2
print(a)

print("Element ke 1 dari a adalah ", a[0])
print("Element ke 7 dari a adalah ", a[6])
print("Element akhir dari a adalah ", a[-1])


# Slicing
print("Element dari 1-6 adalah ", a[0:6])
print("Element dari 4 sampai akhir adalah  ", a[3:])

# Iterasi
for i in a:
    print(f"value: {i}")

# 0 1 2 3 4 5 
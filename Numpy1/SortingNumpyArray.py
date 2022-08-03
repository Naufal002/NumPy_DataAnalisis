import numpy as np

a = np.floor(np.random.randn(1,6)*10)

print(a)

print("\n")

print('nilai max dari a : ', a.max())
print('posisi max dari a : ', a.argmax())

print("\n")

print('nilai minimum dari a : ', a.min())
print('posisi minimum dari a : ',a.argmin())



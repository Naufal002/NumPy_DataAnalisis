import numpy as np

# Membaut Matrix dengan tipe data tertentu

a = np.array(([1,2,3]), dtype = float)

def kuadrat(baris, kolom):
    return kolom **2

def jumlah(baris,kolom):
    return (kolom + baris)

b = np.fromfunction(kuadrat, (1,10), dtype = int)
c = np.fromfunction(jumlah, (4,4), dtype = int)

# Membuat Matrix dengan iterasi
iterable = (x*x for x in range(5))

d = np.fromiter(iterable, dtype= int)

# Multitype array



print(d)
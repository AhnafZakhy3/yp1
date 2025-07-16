# Soal 3: Looping 2 Dimensi & Library Numpy
import numpy as np

def operasi_matriks():
    matriks_a = np.array([[1, 2], [3, 4]])
    matriks_b = np.array([[5, 6], [7, 8]])
    hasil = np.add(matriks_a, matriks_b)
    print("Hasil Penjumlahan Matriks:\n", hasil)

operasi_matriks()

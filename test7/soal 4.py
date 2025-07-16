# Soal 4: Library Numpy
import numpy as np

def statistik_data():
    data = []
    for i in range(10):
        nilai = float(input(f"Masukkan data ke-{i+1}: "))
        data.append(nilai)
    
    rata_rata = np.mean(data)
    median = np.median(data)
    modus = np.bincount(data).argmax()

    print(f"Rata-rata: {rata_rata}, Median: {median}, Modus: {modus}")

statistik_data()

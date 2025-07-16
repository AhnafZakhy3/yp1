# Soal 1: Seleksi Kondisi
def klasifikasi_nilai(nilai):
    if nilai >= 88:
        huruf = "A"
        bobot = 4
        kategori = "Istimewa"
    elif 77 <= nilai < 88:
        huruf = "AB"
        bobot = 3.5
        kategori = "Sangat baik"
    elif 60 <= nilai < 77:
        huruf = "B"
        bobot = 3
        kategori = "Baik"
    elif 45 <= nilai < 60:
        huruf = "C"
        bobot = 2.5
        kategori = "Cukup baik"
    else:
        huruf = "D"
        bobot = 2
        kategori = "Kurang"

    return huruf, bobot, kategori

nilai_input = int(input("Masukkan nilai: "))
huruf, bobot, kategori = klasifikasi_nilai(nilai_input)
print(f"Nilai: {nilai_input}, Nilai Huruf: {huruf}, Bobot: {bobot}, Kategori: {kategori}")

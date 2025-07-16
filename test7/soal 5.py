# Soal 5: Fungsi dan Module
def nilai_huruf(nilai):
    if nilai >= 88:
        return "A"
    elif 77 <= nilai < 88:
        return "AB"
    elif 60 <= nilai < 77:
        return "B"
    elif 45 <= nilai < 60:
        return "C"
    else:
        return "D"

nilai_input = int(input("Masukkan nilai: "))
print(f"Nilai: {nilai_input}, Nilai Huruf: {nilai_huruf(nilai_input)}")

def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def bagi(x, y):
    if y == 0:
        raise ValueError("tidak bisa dibagi 0")
    return x / y

def kali(x, y):
    return x * y

def kalkulator():
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Pembagian")
    print("4. Perkalian")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    x = float(input("Masukkan angka pertama: "))
    y = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print("Hasil:", tambah(x, y))
    elif pilihan == '2':
        print("Hasil:", kurang(x, y))
    elif pilihan == '3':
        try:
            print("Hasil:", bagi(x, y))
        except ValueError as e:
            print(e)
    elif pilihan == '4':
        print("Hasil:", kali(x, y))
    else:
        print("Pilihan tidak valid.")

while True:
    kalkulator()
    lagi = input("Ingin menghitung lagi? (y/n): ")
    if lagi.lower() != 'y':
        break

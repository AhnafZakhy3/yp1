# Sistem Belanja Nepal Mart
def tampilkan_menu():
    print("_" * 52)
    print("Nepal Mart")
    print("Selamat datang di Nepal Mart dan selamat berbelanja!")
    print("_" * 52)
    print("\nRak 1: Jajan")
    print("  Jajan Basah:")
    print("    1. Wonton - Rp 5000")
    print("    2. Cilok Kuah Seblak - Rp 5000")
    print("    3. Spageti - Rp 5000")
    print("    4. Somay - Rp 3000")
    print("    5. Dimsum - Rp 5000")
    print("  Jajan Kering:")
    print("    1. Roti Aoka - Rp 2500")
    print("    2. Arden - Rp 2000")
    print("    3. Sari Gandum - Rp 2000")
    print("    4. Krupuk Pangsit - Rp 2000")
    print("    5. Basreng - Rp 3000")
    
    print("\nRak 2: Minuman")
    print("    1. Susu - Rp 7000")
    print("    2. Air Mineral - Rp 3000")
    print("    3. Pocary Sweet - Rp 8000")
    print("    4. Teh Pucuk - Rp 3500")
    print("    5. Mizone - Rp 5000")
    
    print("\nRak 3: Ice Cream")
    print("    1. Coklat Icecream - Rp 2000")
    print("    2. Strawberry Icecream - Rp 4000")
    print("    3. Vanilla Icecream - Rp 3000")
    print("    4. Mochi Icecream - Rp 3000")
    print("    5. Ice Cream Cone - Rp 7000")

def dapatkan_harga(rak, kategori, barang):
    daftar_harga = {
        "rak1": {
            "jajan basah": [5000, 5000, 5000, 3000, 5000],
            "jajan kering": [2500, 2000, 2000, 2000, 3000]
        },
        "rak2": {
            "minuman": [7000, 3000, 8000, 3500, 5000]
        },
        "rak3": {
            "ice cream": [2000, 4000, 3000, 3000, 7000]
        }
    }
    return daftar_harga[rak][kategori][barang-1]


# Inisiasi total belanja
total = 0
while True:
    tampilkan_menu()
        
    # Langkah 1: Pilih rak
    rak = input("\nPilih rak (rak1/rak2/rak3): ").lower()
    while rak not in ["rak1", "rak2", "rak3"]:
        print("Pilihan tidak valid!")
        rak = input("Pilih rak (rak1/rak2/rak3): ").lower()
        
    # Langkah 2: Pilih kategori
    if rak == "rak1":
        kategori = input("Pilih kategori (jajan basah/jajan kering): ").lower()
        while kategori not in ["jajan basah", "jajan kering"]:
            print("Pilihan tidak valid!")
            kategori = input("Pilih kategori (jajan basah/jajan kering): ").lower()
    else:
        kategori = "minuman" if rak == "rak2" else "ice cream"
        
    # Langkah 3: Pilih barang
    barang = int(input("Pilih barang (1-5): "))
    while barang not in range(1, 6):
        print("Pilihan tidak valid!")
        barang = int(input("Pilih barang (1-5): "))
        
    # Langkah 4: Jumlah
    jumlah = int(input("Jumlah belanja: "))
    while jumlah <= 0:
        print("Jumlah harus lebih dari 0!")
        jumlah = int(input("Jumlah belanja: "))
        
    # Hitung subtotal
    harga = dapatkan_harga(rak, kategori, barang)
    subtotal = harga * jumlah
    total += subtotal
        
    # Langkah 5: Lanjut atau selesai
    pilihan = input("\nPilih lagi? (y/n): ").lower()
    while pilihan not in ["y", "n"]:
        print("Pilihan tidak valid!")
        pilihan = input("Pilih lagi? (y/n): ").lower()
        
    if pilihan == "n":
        break
    
# Langkah 6: Tampilkan total
print(f"\nTotal pembayaran: Rp {total}")
print("Terima kasih telah berbelanja di Nepal Mart!")

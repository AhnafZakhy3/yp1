# Program untuk menampilkan menu dan menghitung total pembelian
#anggota kelompok:Ahnaf(3)
#anggota kelompok:Bio(9)

def tampilkan_menu():
    print("_" * 50)
    print("Menu Makanan:")
    print("_" * 50)
    print("1. Roti - Rp1.500,00")
    print("2. Camilan - Rp2.000,00")
    print("3. Minuman - Rp2.000,00")
    print("4. Keluar")

def hitung_total(pilihan, jumlah):
    harga = {
        1: 1500,
        2: 2000,
        3: 2000
    }
    return harga.get(pilihan) * jumlah

def main():
        tampilkan_menu()
        pilihan = int(input("Masukkan pilihan anda [1 | 2 | 3 | 4]: "))
        if pilihan == 4:
            print("Terima kasih telah berbelanja.")        
        if pilihan in [1, 2, 3]:
            jumlah = int(input("Masukkan jumlah pembelian: "))
            total = hitung_total(pilihan, jumlah)
            print(f"Total pembayaran: Rp{total:,}")
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()

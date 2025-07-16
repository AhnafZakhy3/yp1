import sys

username = 'admin'
password = '1234'

while True:
    print("LOGIN PAGE")
    user = input("masukan username: ")
    passw = input("masukan password: ")

    if user == username and passw == password:
        print("\nLogin Berhasil")
        print("Selamat datang Warteg SPW")
        break
    else:
        print("username atau password salah!!!\n" )
        continue


nama = input("masukan nama anda: ")
no_meja = int(input("masukan nomor meja anda: "))

while True:
    print("\n=== MENU UTAMA ===")
    print(f"Nama pengguna: {nama}")
    print(f"Nomor meja : {no_meja}")
    print()
    
    print("1.Lihat Daftar Menu: \n2.Pesan Menu: \n3.Keluar:")
    
    
    harga_barang = {
                    1: ("Nasi Goreng", 15000),
                    2: ("Mie Goreng", 12000),
                    3: ("Ayam Bakar", 20000),
                    4: ("Esteh", 5000)
                    }
    
    pilih = int(input("Pilih menu:"))

    if pilih == 1:
        while True:
            print("\n--- Daftar Menu ---")
            print("1. Nasi Goreng - Rp15.000")
            print("2. Mie Goreng - Rp12.000")
            print("3. Ayam Bakar - Rp20.000")
            print("4. Esteh - Rp5.000")
            keluar = int(input("ketik 5 untuk kembali ke menu utama :"))
            
            if keluar == 5:
                print()
                break
            else:
                print("pilihan tidak valid")
                print()
                continue
                
    elif pilih == 2:
        while True:
            pesan = int(input("\nMasukan pesanan anda: "))
            
            if pesan not in harga_barang:
                print("menu tidak tersedia pilih lagi")
                continue
            
            jumlah = int(input("Masukan jumlah pesanan: "))
            
            barang,harga = harga_barang[pesan]
            total = harga * jumlah
            
            print(f"anda memesan {jumlah} {barang} dengan total harga Rp{total:,}")
            print()
            
            break

    elif pilih == 3:
        print("Terima Kasih Atas Kunjungan Anda")
        sys.exit()
    
    else:
        print("Pilihan Tidak Valid")
        print()
        continue
        
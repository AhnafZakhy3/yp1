judul_buku = [
    "Clean Code",
    "The Pragmatic Programmer",
    "Introduction to Algorithms",
    "Python Crash Course",
    "Head First Java",
    "You Don't Know JS",
    "Eloquent JavaScript",
    "Structure and Interpretation of Computer Programs",
    "Design Patterns",
    "Artificial Intelligence: A Modern Approach"
]

pengarang_buku = [
    "Robert C. Martin",
    "Andrew Hunt dan David Thomas",
    "Thomas H. Cormen",
    "Eric Matthes",
    "Kathy Sierra dan Bert Bates",
    "Kyle Simpson",
    "Marijn Haverbeke",
    "Harold Abelson dan Gerald Jay Sussman",
    "Erich Gamma et al.",
    "Stuart Russell dan Peter Norvig"
]

while True:
    print("\n=== MENU PERPUSTAKAAN ===")
    print("1. Tambah Buku")
    print("2. Lihat Daftar Buku")
    print("3. Cari Buku")
    print("4. Keluar")
    menu = input("Pilih menu (1-4): ")

    if menu == "1":
        judul = input("Masukkan Judul Buku: ")
        pengarang = input("Masukkan Pengarang: ")
        judul_buku.append(judul)
        pengarang_buku.append(pengarang)

        print("Buku berhasil ditambahkan")
    
    elif menu == "2":
        print("\nDaftar Buku:")
        for i in range(len(judul_buku)):
            print(f"{i+1} {judul_buku[i]} oleh {pengarang_buku[i] }")
        
    elif menu == "3":
        cari = input("Masukkan judul buku yang ingin dicari: ").lower()
        print("\nHasil Pencarian:")
        ditemukan = False
        for i in range(len(judul_buku)):
            if cari in judul_buku[i].lower():
                print(f"- {judul_buku[i]} oleh {pengarang_buku[i]}")
                ditemukan = True
        if ditemukan == False:
            print("Buku tidak ditemukan.")

    elif menu == "4":
        print("Terima kasih telah menggunakan aplikasi perpustakaan.")
        break

    else:
        print("pilihan tidak valid")
import sys
print ("="*50)
print ("<<<Tugas Proyek Aplikasi Perpustakaan Sederhana>>>")
print ("="*50)
print ()
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
	print ()
	print ("===MENU PERPUSTAKAAN===")
	print ("1. Tambah Buku")
	print ("2. Lihat Daftar Buku")
	print ("3. Cari Buku")
	print ("4. Keluar")
	
	print ("="*50)
	pilih=input("Masukan pilihan anda (1/2/3/4): ")
	if pilih=="1":
		print ()
		print ("===TAMBAH BUKU===")
		judul=input ("Masukan judul buku: ")
		pengarang=input ("Masukan pengarang buku: ")
		
		judul_buku.append (judul)
		pengarang_buku.append (pengarang)
		print (f"Buku {judul} dengan pengarang {pengarang} berhasil ditambahkan")
		print ()
	elif pilih=="2":
		print ()
		print ("===DAFTAR BUKU===")
		#perulangan for yang akan terus berjalan sebanyak jumlah elemen dalam list judul_buku
		for i in range(len(judul_buku)):
			print(f"{i+1}.{judul_buku [i]} oleh {pengarang_buku [i]}")
			
	elif pilih=="3":
		print ()
		print ("===CARI BUKU===")
		cari_judul=input("Masukan judul buku yang dicari: ").lower()
		#lower digunakan agar kode tidak sensitif, meski kita memasukan huruf kecil maupun besar
		hasil_pencarian=[]
		for i in range(len(judul_buku)):
			if cari_judul in judul_buku [i].lower():
				hasil_pencarian.append(f"-{judul_buku [i]} oleh {pengarang_buku [i]}")
		if hasil_pencarian:
			print("Hasil Pencarian:")
			for hasil in hasil_pencarian:
				print(hasil)
		else:
			print(f"Buku dengan judul {cari_judul} tidak ditemukan.")
			
	elif pilih=="4":
		print ("Keluar dari program")
		sys.exit()
	else:
		print ("Pilihan tidak valid")
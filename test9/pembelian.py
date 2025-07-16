belanja = float(input("Masukan total harga: "))
member = input("Apakah Anda member? (y/n): ")

if member.lower() == "y":
    if belanja < 200000:
        diskon = 0.05
        total = belanja - (belanja * diskon)
        print(f"Total harga setelah diskon: Rp {total:,}")
    elif belanja >= 200000:
        diskon = 0.1
        total = belanja - (belanja * diskon)
        print(f"Total harga setelah diskon: Rp {total:,}")

elif member.lower() == "n":
    print(f"Total harga: Rp {belanja:,}")
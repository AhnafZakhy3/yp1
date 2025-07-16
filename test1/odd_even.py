def check_odd_even(number):
    # Mengecek apakah bilangan tersebut ganjil atau genap
    if number % 2 == 0:
        return f"{number} adalah bilangan genap."  # Pesan jika bilangan genap
    else:
        return f"{number} adalah bilangan ganjil."  # Pesan untuk bilangan ganjil

if __name__ == "__main__":  #digunakan agar kode dibawah nya hanya dijalankan ketika file ini dijalankan secara langsung
    try:
        # promt user untuk memasukkan angka
        num = int(input("Masukkan sebuah angka: "))
        result = check_odd_even(num)  # memanggil fungsi check_odd_even dengan argumen num
        print(result)  # Print hasil
    except ValueError:
        # mengantisipasi invalid input
        print("Silakan masukkan angka bulat yang valid.")

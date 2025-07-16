import random

while True:
    print("-" * 30)
    print("KUIS AHNAF")
    print("-" * 30)

    soal = [
        ("Soal 1: 12 + 5 =", 17),
        ("Soal 2: 45 - 5 =", 40),
        ("Soal 3: 5 * 5 =", 25),
        ("Soal 4: 8 ÷ 2 =", 4),
        ("Soal 5: 7 * 7 =", 49)
    ]
    
    random.shuffle(soal)

    nilai = 0

    for index, (pertanyaan, jawaban_benar) in enumerate(soal):
        print(pertanyaan)
        jawaban = int(input(f"Jawaban no {index + 1}: "))
        
        if jawaban == jawaban_benar:
            print(f"Jawaban benar no {index + 1}, dapat nilai 20")
            nilai += 20
        else:
            print(f"Jawaban no {index + 1} salah")

    print("")
    print("Nilai akhir anda:", nilai)

    if nilai >= 50:
        print("Selamat, Anda lulus!")
    else:
        print("Maaf, Anda tidak lulus.")
    
    print("") 
    break

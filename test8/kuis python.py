import random
while True:
    print("-"*30)
    print("KUIS AHNAF")
    print("-"*30)
    print("Soal 1: 12 + 5 = ")
    print("Soal 2: 45 - 5 = ")
    print("Soal 3: 5 * 5 = ")
    print("Soal 4: 8 ÷ 2 = ")
    print("Soal 5: 7 * 7 = ")
    print("-"*30)

    
    jawaban_1 = int(input("Jawaban no 1: "))
    jawaban_2 = int(input("Jawaban no 2: "))
    jawaban_3 = int(input("Jawaban no 3: "))
    jawaban_4 = int(input("Jawaban no 4: "))
    jawaban_5 = int(input("Jawaban no 5: "))

    nilai = 0
    
    if jawaban_1 == 17:
        print("Jawaban benar no 1, dapat nilai 20")
        nilai += 20
    else:
        print("Jawaban no 1 salah")

    if jawaban_2 == 40:
        print("Jawaban benar no 2, dapat nilai 20")
        nilai += 20
    else:
        print("Jawaban no 2 salah")

    if jawaban_3 == 25:
        print("Jawaban benar no 3, dapat nilai 20")
        nilai += 20
    else:
        print("Jawaban no 3 salah")

    if jawaban_4 == 4:
        print("Jawaban benar no 4, dapat nilai 20")
        nilai += 20
    else:
        print("Jawaban no 4 salah")

    if jawaban_5 == 49:
        print("Jawaban benar no 5, dapat nilai 20")
        nilai += 20
    else:
        print("Jawaban no 5 salah")

    print("")
    print("Nilai akhir anda:", nilai)

    if nilai >= 50:
        print("Selamat, Anda lulus!")
        break
    else:
        print("Maaf, Anda tidak lulus.")
        print("")


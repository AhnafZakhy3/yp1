for i in range(1, 11):
    for j in range(1, 11):
        hasil = i * j
        if hasil > 10:
            break
        print(f"{i} x {j} = {hasil}")
    print()

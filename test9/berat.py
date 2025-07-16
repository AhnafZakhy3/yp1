berat = float(input("masukan beart badan:"))

if berat < 50:
    print("Predikat Anda: Kurus")
elif berat >= 50 and berat <= 70:
    print("Predikat Anda: Proporsional")
else:
    print("Predikat Anda: Gemuk")
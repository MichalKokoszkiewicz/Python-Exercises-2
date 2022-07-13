dane = bytearray(10)
for i in range(len(dane)):
    dane[i] = len(dane) - i

strumien = open("nowy_plik_binarny.txt", "wb")
strumien.write(dane)
strumien.close()

dane2 = bytearray(6)
strumien2 = open("nowy_plik_binarny.txt", "rb")
strumien2.readinto(dane2)
for i in dane2:
    print(i)
print("===")
strumien2.readinto(dane2)
for i in dane2:
    print(i)

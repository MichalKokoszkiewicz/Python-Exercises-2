strumien = open("plik2.txt", "r")
dane = strumien.read(5)
print(dane)
print(strumien.read())
strumien.close()

print("===")

strumien = open("plik.txt", "r")
for linia in strumien:
    print(linia, end="")

strumien.close()

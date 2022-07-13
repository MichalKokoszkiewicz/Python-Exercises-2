dane = bytearray(64)

plik1 = input("Podaj nazwę pliku do skopiowania: ")
strumien1 = open(plik1, "rb")

plik2 = input("Podaj nazwę nowego pliku: ")
strumien2 = open(plik2, "wb")

i = strumien1.readinto(dane)
while i > 0:
    strumien2.write(dane[:i])
    i = strumien1.readinto(dane)

strumien1.close()
strumien2.close()

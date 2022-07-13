strumien = open("nowy_plik2.txt", "w")
for i in range(10):
    strumien.write("linia #" + str(i + 1) + "\n")
strumien.close()

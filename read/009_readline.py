strumien = open("plik.txt", "r")
dane = strumien.readline(10)
while dane:
    print(dane)
    dane = strumien.readline(10)
    
strumien.close()

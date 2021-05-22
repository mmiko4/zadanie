
plik = open("csv.txt", "r")
def suma(lista):
    suma_ocen = 0
    for ocena in lista:
        suma_ocen = suma_ocen + ocena
    return suma_ocen
stop = 0
while stop == 0:
    slownik = {
        "imie":"",
        "nazwisko":"",
        "oceny":[],
        "srednia":0
    }
    linijka = plik.readline()
    plik_split = linijka.split(" ")
    if len(plik_split) != 1:
        slownik["imie"] = plik_split[0]
        slownik["nazwisko"] = plik_split[1]
        n = 0
        while n <= len(plik_split)-3:
            slownik["oceny"].append(int(plik_split[n + 2]))
            n = n + 1
        slownik["srednia"] = suma(slownik["oceny"])/len(slownik["oceny"])
        print(slownik)
    else:
        stop = 1

# źródła
#  https://python.szkola.pl/listy-petle-poziom-calkiem-juz-zaawansowany/
#  https://ifcode.pl/python-operacje-na-plikach/
#  https://oprojektowaniu.pl/python-dla-inzynierow-slowniki/

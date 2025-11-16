#tehtävä 7.3
lista = {"EFHK":"Helsinki",
         "ESSA":"Tukholma",
         "ENGM":"Oslo"}
valinta = input("Jos haluat syöttää uuden aseman syötä 1, hakea syötetyn syötä 2 tai lopettaa syötä 3.: ")
while valinta != "3":
    if valinta == "2":
        icao = input("Anna ICAO-koodi: ")
        print(lista[icao])
        valinta = input("Jos haluat syöttää uuden aseman syötä 1, hakea syötetyn syötä 2 tai lopettaa syötä 3.: ")

    elif valinta == "1":
        icao = input("Anna uusi ICAO-koodi: ")
        kaupunki = input("Anna kaupunki: ")
        lista[icao] = kaupunki
        valinta = input("Jos haluat syöttää uuden aseman syötä 1, hakea syötetyn syötä 2 tai lopettaa syötä 3.: ")

    elif valinta == "3":
        break

print("Ohjelma päättyy.")
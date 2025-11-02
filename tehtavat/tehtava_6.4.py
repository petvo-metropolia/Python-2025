#tehtava 6.4

#funktio joka summaa listan kaikki luvut
def summaus():
    summa = 0
    for luku in lista:
        summa += luku
    return summa

#pääohjelmassa luodaan lista ja tulostetaan funktion palauttama summa
lista = [1,2,3,4,5]
print(f"Lukujen summa on: {summaus()}")



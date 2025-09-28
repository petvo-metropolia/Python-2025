#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

pienin = None
suurin = None

while True:
    vastaus = input("Anna luku: ")
    if vastaus == "":
        break
    luku = int(vastaus)
    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku
if pienin is not None and suurin is not None:
    print("Pienin luku:", pienin)
    print("Suurin luku:", suurin)
else:
    print("Et antanut yhtään lukua.")
#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan
# kunnes käyttäjä antaa negatiivisen tuumamäärän.
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuumat = float(input("Anna tuumat: "))
sentit = tuumat * 2.54
while tuumat >= 0:
    print(f"{sentit} cm")
    tuumat = float(input("Anna tuumat: "))
    sentit = tuumat * 2.54
print("Negatiivinen luku. Laskeminen lopetettu.")
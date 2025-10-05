#tehtävä 5.4

#Luodaan lista
kaupungit = []

#kysely jossa 5 kysymystä
for i in range(5):
    kaupunki = input("Anna kaupunki: ")
    kaupungit.append(kaupunki)

#tulostetaan lista
print("Kaupungit ovat: ")
for kaupunki in kaupungit:
    print(kaupunki)
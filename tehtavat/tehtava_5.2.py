#tehtävä 5.2

#Kysytään käyttäjältä lukuja ja tallennetaan ne listaan. Tyhjä syöte lopettaa.
luvut = []
luku = input("Anna luku (Enter lopettaa).: ")


while luku !="":
    luvut.append(luku)
    luku = input("Anna luku (Enter lopettaa).: ")

#muunnetaan luvut kokonaisluvuiksi:
luvut = [int(luku) for luku in luvut]
#järjestetään luvut käänteisesti ja tulostetaan:
luvut.sort(reverse = True)
print(luvut[0:5])
#5.1 arpakuutioiden lukumäärä

count = int(input("Anna arpakuutioiden määrä: ")) #Kysytään käyttäjältä määrä

import random #Käytetään randomia arpalukujen arpomiseen
summa = 0
for luku in range(count): #Toistoja yhtä monta kuin käyttäjän antama lukumäärä
    arvo = random.randint(1, 6) #Nopassa on luvut 1 - 6
    #print(arvo) #Testiprintti, ei jätetä lopulliseen koodiin
    summa += arvo #Summataan arvotut luvut yhteen
print(f"Arpakuutioiden summa on {summa}") #printataan lopuksi pelkästään summa
#tehtävä6.6
import math

#funktiossa lasketaan pizzalle neliöhinta
def laskenta():
    #halkaisija = ""
    #hinta = ""
    neliohinta = hinta / (math.pi * (halkaisija/100 / 2) ** 2)
    return neliohinta

#pääohjelmassa kysytään kahden pizzan tiedot ja välissä tallennetaan neliöhinta
halkaisija = float(input("Anna pizzan 1. halkaisija cm: "))
hinta = float(input("Anna pizzan 1. hinta euroissa: "))
pizza1 = laskenta()
halkaisija = float(input("Anna pizzan 2. halkaisija cm: "))
hinta = float(input("Anna pizzan 2. hinta euroissa: "))
pizza2 = laskenta()

#määritetään vastausta
if pizza1 > pizza2:
    paras = "pizza 2"
elif pizza2 > pizza1:
    paras = "pizza 1"
else:
    paras = "molemmat, koska neliöhinta on sama"

#tulostus
print(f"Pizza 1. neliöhinta on {pizza1:.2f} ja pizza 2. neliöhinta on {pizza2:.2f}, eli paremman "
      f"vastineen rahalle antaa {paras}.")
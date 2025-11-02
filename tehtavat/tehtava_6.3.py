#tehtävä 6.3

#funktio jossa muunnos
litrat = ""
def muunnos():
    litrat = gallonat * 3.785
    return litrat

#pääohjelma jossa pyydetään syöttämään gallonat ja tulostetaan litroina
gallonat = float(input("Anna gallonat. Negatiivinen luku lopettaa: "))
while gallonat >= 0:
    print(f"{gallonat} gallonaa on {muunnos():.3f} litraa")
    gallonat = float(input("Anna gallonat: "))


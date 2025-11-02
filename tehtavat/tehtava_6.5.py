#tehtävä 6.5

#funktio
def muunnos():
    lista2 = []
    for luku in lista:
        if luku % 2 == 0:
            lista2.append(luku)
    return lista2

#pääohjelmassa luodaan lista ja tulostetaan funktio
lista = [1,2,3,4,5,6]
print(f"Alkuperäinen lista: {lista} ja korjattu lista: {muunnos()}")
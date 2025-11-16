#tehtävä 7.2

nimet = set()
nimi = input("Anna nimi: ")

while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        nimet.add(nimi)
    nimi = input("Anna nimi: ")

print("Nimilista:")
for n in nimet:
    print(n)
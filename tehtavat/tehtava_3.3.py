#tehtävä 3.3.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Mikä on sukupuolesi?: ").lower()
hg_arvo = int(input("Mikä on hemoglobiiniarvosi? (g/l): "))

if sukupuoli == "nainen":
    if hg_arvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hg_arvo > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "mies":
    if hg_arvo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hg_arvo > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
else:
    print("Syöttövirhe. Aloita alusta.")

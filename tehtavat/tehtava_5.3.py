#tehtävä 5.3

#Kysytään käyttäjältä luku.
luku = int(input("Anna luku: "))

#Kahta pienemmät eivät ole alkulukuja.
if luku < 2:
    print("Luku ei ole alkuluku.")
else:
    jakaja = 2
#Kokeillaan jakaa syötetty luku kaikilla luvuilla kahdesta ylöspäin syötettyyn lukuun asti.
    while jakaja < luku:
        if luku % jakaja == 0:
            print("Luku ei ole alkuluku.") #Jos luku on jaolllinen jollain luvulla ennen itseään, niin silmukka keskeytyy.
            break
        jakaja += 1
    if jakaja == luku:
        print("Luku on alkuluku.")
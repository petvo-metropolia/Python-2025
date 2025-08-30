#tehtävä 2.4.

luku1 = (int(input("Anna kokonaisluku: ")))
luku2 = (int(input("Anna toinen kokonaisluku: ")))
luku3 = (int(input("Anna kolmas kokonaisluku: ")))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

print(f"Lukujen summa on {summa}, tulo on {tulo} ja keskiarvo {keskiarvo:.1f}")
#tehtävä 3.1.

#kuha pitää olla vähintään  37 cm

pituus = int(input("Mikä on kuhan pituus (cm)?: "))
erotus = int(37 - pituus)
if pituus >= 37:
    print(f"Kuhan pituus on: {pituus} cm, eli kalastaminen on sallittu.")
else:
    print(f"Kuha on {erotus} cm liian lyhyt, joten se on laskettava takaisin järveen.")


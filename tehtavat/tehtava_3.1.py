#tehtävä 3.1.

#kuha pitää olla vähintään  37 cm

pituus = int(input("Mikä on kuhan pituus (cm)?: "))
if pituus >= 37:
    print(f"Kuhan pituus on: {pituus} cm, eli kalastaminen on sallittu.")
else:
    print(f"Kuhan pituus on alle 37 cm, joten se on laskettava takaisin järveen.")


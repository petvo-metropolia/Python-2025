#tehtävä 2.3.

kanta = float(input("Mikä on suorakulmion kannan pituus (mm)?: "))
korkeus = float(input("Mikä on suorakulmion korkeus (mm)?: "))
piiri = 2 * kanta + 2 * korkeus
pintaala = kanta * korkeus
print(f"Suorakulmion piiri on {piiri} mm ja pinta-ala on {pintaala} mm.")

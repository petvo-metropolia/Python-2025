#tehtävä 3.2.

luokka = input("Mikä on hyttiluokkasi?: ")

if luokka == "LUX" or "Lux" or "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == "A" or "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "B" or "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C" or "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")
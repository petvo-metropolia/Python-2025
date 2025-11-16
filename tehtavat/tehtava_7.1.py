#tehtävä 6.1

vuodenajat = ("talvi","talvi","kevät","kevät","kevät","kesä","kesä","kesä","syksy","syksy","syksy","talvi")
jarjestysnro = int(input("Anna kuukauden numero: "))
if 0 < jarjestysnro < 13:
    va = vuodenajat[jarjestysnro-1]
    print(f"Vuodenaika on {va}.")
else:
    print("Valitsemasi numero ei ole välillä 1 - 12. Ohjelma päättyy.")
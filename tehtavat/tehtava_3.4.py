#tehtävä 3.4.

vuosi = int(input("Anna vuosiluku: "))


if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print(f"Vuosi {vuosi} on karkausvuosi.")
        else:
            print(f"Vuosi {vuosi} ei ole karkausvuosi.")
    else:
        print(f"Vuosi {vuosi} on karkausvuosi.")
else:
    print(f"Vuosi {vuosi} ei ole karkausvuosi.")


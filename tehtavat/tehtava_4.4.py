
import random

luku = int(random.randint(1, 10))

while True:
    arvaus = int(input("Arvaa luku väliltä 1 - 10: "))
    if arvaus == luku:
        break
    elif arvaus < luku:
        print("Liian pieni arvaus.")
    elif arvaus > luku:
        print("Liian suuri arvaus.")

print("Oikein.")
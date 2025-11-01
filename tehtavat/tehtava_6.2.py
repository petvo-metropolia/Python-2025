import random

#määritellään funktio
def heitto():
    return random.randint(1,21)
#pääohjelma
max = int(input("Anna maksimi silmäluku: "))

luku = heitto()
while luku < max:
    print(luku)
    luku = heitto()
print(luku)
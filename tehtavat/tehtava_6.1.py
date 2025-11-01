import random

#määritellään funktio
def heitto():
    return random.randint(1,6)
#pääohjelma
luku = heitto()
while luku < 6:
    print(luku)
    luku = heitto()
print(luku)

#tehtävä 2.6.

import random

#arvotaan kolminumeroinen koodi, numerot välillä 0 - 9
koodi_a1 = random.randint(0,9)
koodi_a2 = random.randint(0,9)
koodi_a3 = random.randint(0,9)

#arvotaaan nelinumeroinen koodi, numerot välillä 1 - 6
koodi_b1 = random.randint(1,6)
koodi_b2 = random.randint(1,6)
koodi_b3 = random.randint(1,6)
koodi_b4 = random.randint(1,6)

#Tulostetaan koodit
print(f"Arvottu kolminumeroinen koodi on: {koodi_a1}{koodi_a2}{koodi_a3}")
print(f"Arvottu nelinumeroinen koodi on: {koodi_b1}{koodi_b2}{koodi_b3}{koodi_b4}")
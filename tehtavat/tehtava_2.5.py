#tehtävä 2.5.
import math
#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.
#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

leiviskat = float(input(f"Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

massa = leiviskat * 20 * 32 * 13.3 + naulat * 32 * 13.3 + luodit * 13.3
massakg = int(float(massa // 1000))
massag = float(massa % 1000)

print(f"Massa nykymittojen mukaan:\n{massakg} kilogrammaa ja {massag:.1f} grammaa")

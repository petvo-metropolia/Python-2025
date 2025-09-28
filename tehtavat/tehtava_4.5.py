
user = "python"
password = "rules"

kerrat = 0
ok = False

while kerrat < 5:
    user_input = input("Anna käyttäjätunnus: ")
    password_input = input("Anna salasana: ")

    if user == user_input and password == password_input:
        ok = True
        break
    else:
        kerrat += 1
if ok:
    print("Tervetuloa")
else:
    print("Pääsy evätty.")
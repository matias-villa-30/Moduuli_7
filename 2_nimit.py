nimet = set()
while True:
    nimi = input("Anna nimet: ")
    if nimi == "":
        break
    else:
        nimet.add(nimi)

for nombre in nimet:
    print(nombre)
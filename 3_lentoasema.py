lentoasemat = {"Denver":"DEN/KDEN","Madrid":"MAD/LEMD", "London":"LHR/EGLL"}
while True:
    vaihtoehto =int(input("1-Lisää lentoasema: \n2-Katsoo kaikki lentoasemat: \n3-Lopeta ohjelma: \n"))
    if vaihtoehto == 1:
        nimi = input("Kirjoita lentoaseman kaupunki: ")
        koodi = input("Anna ICAO koodi: ")
        lentoasemat[nimi] = koodi

    elif vaihtoehto == 2:
        print(lentoasemat)

    elif vaihtoehto == 3:
        break

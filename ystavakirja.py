import random #Saadaan random-arpoja vitsejä varten

#Luodaan ystäväkirja-lista
ystavakirja = []

#Syötetään testidataa ystäväkirjaan, jotta ohjelma toimii samantien vitsien ja haun kohdalla
ystavakirja = [
    {"Nimi": "Jouni",
    "Lempinimi": "Jouko",
    "Ikä": 70,
    "Lempiväri": "sininen",
    "Lempiruoka": "makaronilaatikko",
    "Lempieläin": "kissa",
    "Haaveammatti": "joulupukki",
    "Päivän fiilis hymiönä": ":o",
    "Paras vitsi": "Kaksi keksiä ylitti autotietä. Toinen jäi auton alle ja toinen sanoi \"Tulehan muruseni!\""},

    {"Nimi": "Miro",
    "Lempinimi": "Miksu",
    "Ikä": 32,
    "Lempiväri": "musta",
    "Lempiruoka": "sushi",
    "Lempieläin": "koira",
    "Haaveammatti": "poliisi",
    "Päivän fiilis hymiönä": "ò_Ô",
    "Paras vitsi": "Pieru."},

    {"Nimi": "Eevi",
    "Lempinimi": "Eve",
    "Ikä": 10,
    "Lempiväri": "pinkki",
    "Lempiruoka": "karkit ja sipsit",
    "Lempieläin": "hamsteri",
    "Haaveammatti": "eläinlääkäri",
    "Päivän fiilis hymiönä": "XD",
    "Paras vitsi": "Olipa kerran vitsi, loppu."},

    {"Nimi": "Mira",
    "Lempinimi": "-",
    "Ikä": 45,
    "Lempiväri": "oranssi",
    "Lempiruoka": "paella",
    "Lempieläin": "kala",
    "Haaveammatti": "sirkustaiteilija",
    "Päivän fiilis hymiönä": ">:(",
    "Paras vitsi": "Miksi kissoilla on korvat? -Jotta ne kuulisivat!"},

    {"Nimi": "Elina",
    "Lempinimi": "Ellu",
    "Ikä": 24,
    "Lempiväri": "lila",
    "Lempiruoka": "Kolmen kaverin jäätelö: suklaa",
    "Lempieläin": "hevonen",
    "Haaveammatti": "opettaja",
    "Päivän fiilis hymiönä": ":*",
    "Paras vitsi": "Miksi Suomessa palkat eivät kasva? - Koska jokaisella firmalla on palkanlaskija!"}]


#Luodaan kyselylomake
def lisaa_ystava(lista):
    nimi = input("Nimi: ")
    lempinimi = input("Lempinimi: ")
    ika = int(input("Ikä: "))
    vari = input("Lempiväri: ")
    ruoka = input("Lempiruoka: ")
    elain = input("Lempieläin: ")
    ammatti = input("Haaveammatti: ")
    fiilis = input("Päivän fiilis hymiönä: ")
    vitsi = input("Paras vitsi: ")

#Tallennetaan vastaukset sanakirjaksi
    tallennus = {
        "Nimi": nimi,
        "Lempinimi": lempinimi,
        "Ikä": ika,
        "Lempiväri": vari,
        "Lempiruoka": ruoka,
        "Lempieläin": elain,
        "Haaveammatti": ammatti,
        "Päivän fiilis hymiönä": fiilis,
        "Paras vitsi": vitsi
    }

    lista.append(tallennus)
    return lista

#Tulostetaan siistinä (voi olla turha tai pitää siirtää - harkitaan)
"""for avain, arvo in tallennus.items():
    print(f"{avain}: {arvo}")
    
    ystavakirja = lisaa_ystava(ystavakirja)"""

def vitsin_arvonta(lista):
    vitsit = []
    for kaveri in ystavakirja:
        vitsit.append(kaveri["Paras vitsi"])
    return random.choice(vitsit)

def ilme(ystavakirja):
    hymiot = []
    for kaveri in ystavakirja:
        hymiot.append(kaveri["Päivän fiilis hymiönä"])
    return random.choice(hymiot)

#Luodaan haku (ehkä funktioksi jossain kohtaa)
def haettava(lista):
    haettava = input("Kenen tiedot näytetään?\nNimi: ")

    for tallennus in ystavakirja:
        if tallennus["Nimi"].lower() == haettava.lower(): # Muutetaan tallennus- ja haettava-osioista kirjaimet pieniksi, joten ei merkitystä, haetaanko Lily vai lily
            for avain, arvo in tallennus.items(): #Saadaan kaikki tiedot .items:illä
                print(f"{avain}: {arvo}")
        else:
            print("Ystäväkirjassasi ei ole tämän nimistä henkilöä")
            lisaa_puuttuva = input("Haluaisitko lisätä ystävän tiedot? (k)yllä/(e)i ") #Harkitaan, jos isot ja pienet kirjaimet tässäkin ok?
            if lisaa_puuttuva.lower() == "k":
                lisaa_ystava(ystavakirja)
            #Tähän funktio, jotta saa uudet tiedot syötettyä
            if lisaa_puuttuva == "e":
                print(valinta) #kysyy uudelleen, mutta voisi palata ihan alkuunkin - alkua ei vielä ole :D

while True:
    print("="*35)
    print("❤️  YSTÄVÄKIRJA ❤️".center(35, " "))
    print("="*35)
    valinta = int(input("\nMitä haluaisit tehdä (valitse numero)?\n\n1 - Lisää kaveri\n2 - Etsi kaveri\n3 - Lue vitsi\n4 - Lopeta\n\nValitsen: "))

    if valinta == 1:
        lisaa_ystava(ystavakirja)
    if valinta == 2:
        print(haettava(ystavakirja))
    if valinta == 3:
        print("\n" + "-"*35)
        print("🎉 Päivän vitsi 🎉".center(35))
        print("-"*35)
        print(f"\n{vitsin_arvonta(ystavakirja)}\n")
        print(f"Ilmeesti nyt: {ilme(ystavakirja)}\n")
        print("\n" + "-"*35)
    if valinta == 4:
        print("Heihei!")
        break
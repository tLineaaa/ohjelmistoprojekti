import random #Saadaan random-arpoja vitsejä varten

#Luodaan ystäväkirja-lista
ystavakirja = []

#Syötetään testidataa ystäväkirjaan, jotta ohjelma toimii samantien vitsien ja haun kohdalla (ei kuitenkaan tallennettu kirja.txt)
ystavakirja = [
    {"Nimi": "Jouko",
    "Lempinimi": "Jokke",
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
    "Päivän fiilis hymiönä": ">_<",
    "Paras vitsi": "Miksi Suomessa palkat eivät kasva? - Koska jokaisella firmalla on palkanlaskija!"}]

#Luodaan funktio, jotta voidaan lisätä ystävän tiedot txt.tiedostoon (syötetty valmiiksi yhden henkilön tiedot - voi poistaa + alustus tehty vsc:n "lisää tiedosto"-napilla)
def tallenna_ystava(tiedostonnimi, tiedot):
    with open(tiedostonnimi, "a", encoding="utf-8") as tiedosto: #utf-8, niin toimii ääkköset ja kuulemma hymiötkin
        for avain, arvo in tiedot.items():
            tiedosto.write(f"{avain}: {arvo}\n")
        tiedosto.write("--------------------\n") #vähän selkeyttä ystävien väliin

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
    tallenna_ystava("kirja.txt", tallennus)
    return lista

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

#Luodaan haku
def haettava(lista):
    haettava = input("Kenen tiedot näytetään?\n\nEtsitään: ")
    print("_"*20)

    for ystava in ystavakirja:
        if ystava["Nimi"].lower() == haettava.lower(): # Muutetaan tallennus- ja haettava-osioista kirjaimet pieniksi, joten ei merkitystä, haetaanko Lily vai lily
            for avain, arvo in ystava.items(): #Saadaan kaikki tiedot .items:illä
                print(f"\n{avain}: {arvo}")
            return
    print("Ystäväkirjassasi ei ole tämän nimistä henkilöä") #Jos haku ei tuota tulosta, voidaan kaveri lisätä kirjaan
    valinta = input("Haluatko lisätä uuden ystävän? (K)llä/(E)i ")
    if valinta.lower() == "k":
        lisaa_ystava(ystavakirja)

def pituus(lista):
    return (F"Sinulla on tällä hetkellä {len(ystavakirja)} ystävää kirjassasi.")

while True:
    print("="*35) #Lisätty koristeluja ja keskittämistä
    print("❤️  YSTÄVÄKIRJA ❤️".center(35, " "))
    print("="*35)
    print(pituus(ystavakirja))
    valinta = int(input("\nMitä haluaisit tehdä (valitse numero)?\n\n1 - Lisää kaveri\n2 - Etsi kaveri\n3 - Lue vitsi\n4 - Lue koko ystäväkirja\n5 - Lopeta\n\nValitsen: "))

    if valinta == 1:
        lisaa_ystava(ystavakirja)
    if valinta == 2:
        haettava(ystavakirja)
        input("\nPalaa takaisin valikkoon painamalla Enter\n") #Pysäytetään ohjelma hetkeksi, jotta valikko ei tulostu heti perään, vaan tulokset ehtii katsoa rauhassa
    if valinta == 3:
        print("\n" + "-"*35) #Lisätty koristeluja ja keskittämistä
        print("🎉 päivän vitsi 🎉".center(35))
        print("-"*35)
        print(f"\n{vitsin_arvonta(ystavakirja)}\n")
        print(f"Ilmeesti nyt:\n\n {ilme(ystavakirja)}\n")
        print("-"*35)
        input("Palaa takaisin valikkoon painamalla Enter\n")
    if valinta == 4:
        with open("kirja.txt", encoding="utf8") as luetaan:
            sisalto = luetaan.read()
            print(sisalto)
        input("Palaa takaisin valikkoon painamalla Enter\n")
    if valinta == 5:
        print("Heihei!")
        break
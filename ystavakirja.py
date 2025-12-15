import random #Saadaan random-arpoja vitsejä varten

#Luodaan ystäväkirja-lista
ystavakirja = []

#Syötetään testidataa ystäväkirjaan, jotta ohjelma toimii samantien vitsin heiton ja kaverihaun kohdalla (ei kuitenkaan tallennettu yst_kirja.txt tai vitsi.txt)
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

#Sama kuin yllä, mutta rakennetaan vitsikirjaa vitsikirja.txt-tiedostoon (tallentaa samatkin, joten vrt. olemassa olevaa ja syötettävää kirjainkoosta riippumatta äläkä tallenna, jos löytyy jo?)
def tallenna_vitsi(tiedostonnimi, vitsi):
    with open(tiedostonnimi, "a", encoding="utf-8") as tiedosto: #tästä voisi kyllä harkita omaa funktiota
        tiedosto.write(f"\n{vitsi}\n\n")
        tiedosto.write("~~~~~~~~~~~~~~~~~~~~\n")

def kysy_teksti(tieto): #tsekataan, ettei vastaus ole tyhjä -funktio
    while True:
        vastaus = input(tieto).strip()
        if vastaus:
            return vastaus
        print("Hups, unohdit vastata kysymykseen!")

#Luodaan kyselylomake (lisää try/expect)
def lisaa_ystava(lista):
    nimi = kysy_teksti("Nimi: ")
    lempinimi = kysy_teksti("Lempinimi: ")
    while True:
        try:
            ika = int(input("Ikä: "))
            break
        except ValueError: #Jos syöte muuta kuin luku, ohjelma ei kaadu, vaan kysyy syötettä uudelleen
            print("Hups - syötä ikäsi lukuna!")
    vari = kysy_teksti("Lempiväri: ")
    ruoka = kysy_teksti("Lempiruoka: ")
    elain = kysy_teksti("Lempieläin: ")
    if elain in ("koira", "hauva", "rakki"):
        elain += " 🐶"
    elif elain in ("kissa", "kisu", "mirri", "katti"):
        elain += " 🐱"
    elif elain in ("hevonen", "heppa", "poni"):
        elain += " 🐴"
    elif elain in ("tiikeri", "tikru"):
        elain += " 🐯"
    elif elain in ("pingiivi", "pingu"):
        elain += " 🐧"
    elif elain in ("pupu", "kani", "jänö", "jänis"):
        elain += " 🐰"
    elif elain in ("kala", "kalat", "fisu", "fisut"):
        elain += " 🐟"
    elif elain in ("käärme", "mato", "python"):
        elain += " 🐍"
    ammatti = kysy_teksti("Haaveammatti: ")
    fiilis = kysy_teksti("Päivän fiilis hymiönä: ")
    vitsi = kysy_teksti("Paras vitsi: ")

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
    tallenna_ystava("data/yst_kirja.txt", tallennus)
    tallenna_vitsi("data/vitsikirja.txt", tallennus["Paras vitsi"])
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

def tauko_ja_paluun():
    input("\nPalaa takaisin valikkoon painamalla Enter\n") #Pysäytetään ohjelma hetkeksi, jotta valikko ei tulostu heti perään, vaan tulokset ehtii katsoa rauhassa

while True:
    print("="*35) #Lisätty koristeluja ja keskittämistä
    print("❤️  YSTÄVÄKIRJA ❤️".center(35, " "))
    print("="*35)
    print(pituus(ystavakirja))
    valinta = int(input("\nMitä haluaisit tehdä (valitse numero)?\n\n1 - ✍  Lisää kaveri\n2 - 🔎 Etsi kaveri\n3 - 😂 Heitä vitsillä\n4 - 👯 Lue koko ystäväkirja\n5 - 😝 Lue vitsikirjaa\n6 - ❌ Lopeta\n\nValitsen: "))

    if valinta == 1:
        lisaa_ystava(ystavakirja)
    if valinta == 2:
        haettava(ystavakirja)
        tauko_ja_paluun()
    if valinta == 3:
        print("\n" + "-"*35) #Lisätty koristeluja ja keskittämistä
        print("🎉 päivän vitsi 🎉".center(35))
        print("-"*35)
        print(f"\n{vitsin_arvonta(ystavakirja)}\n")
        print(f"Ilmeesti nyt:\n\n {ilme(ystavakirja)}\n")
        print("-"*35)
        tauko_ja_paluun()
    if valinta == 4:
        with open("data/yst_kirja.txt", encoding="utf8") as luetaan:
            sisalto = luetaan.read()
            print(sisalto)
        tauko_ja_paluun()
    if valinta == 5:
        with open("data/vitsikirja.txt", encoding="utf-8") as haha:
            kaikki = haha.read()
            print(kaikki)
        tauko_ja_paluun()
    if valinta == 6:
        print("Heihei!")
        break
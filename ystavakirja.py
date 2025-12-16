import random # Saadaan random-arpoja vitsejä varten

# Luodaan ystäväkirja-lista
ystavakirja = []

# Luodaan funktio, jotta voidaan lisätä ystävän tiedot txt.tiedostoon (syötetty valmiiksi yhden henkilön tiedot - voi poistaa + alustus tehty vsc:n "lisää tiedosto"-napilla)
def tallenna_ystava(tiedostonnimi, tiedot):
    with open(tiedostonnimi, "a", encoding="utf-8") as tiedosto: # utf-8, niin toimii ääkköset ja kuulemma hymiötkin
        for avain, arvo in tiedot.items():
            tiedosto.write(f"{avain}: {arvo}\n")
        tiedosto.write("--------------------\n") # Vähän selkeyttä ystävien väliin

# Sama kuin yllä, mutta rakennetaan vitsikirjaa vitsikirja.txt-tiedostoon (tallentaa samatkin, joten vrt. olemassa olevaa ja syötettävää kirjainkoosta riippumatta äläkä tallenna, jos löytyy jo?)
def tallenna_vitsi(tiedostonnimi, vitsi):
    with open(tiedostonnimi, "a", encoding="utf-8") as tiedosto: # Tästä voisi kyllä harkita omaa funktiota
        tiedosto.write(f"\n{vitsi}\n\n")
        tiedosto.write("~~~~~~~~~~~~~~~~~~~~\n")

# Funktio, joka määrittelee, että jos annettu parametri on jokin seuraavista, lisätään sen perään tietty hymiö
def lisaa_hymio(elain):
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
    elif elain in ("käärme", "mato", "pyton"):
        elain += " 🐍"
    return elain

# Syötetään testidataa ystäväkirjaan, jotta ohjelma toimii samantien vitsin heiton ja kaverihaun kohdalla (ei kuitenkaan tallennettu yst_kirja.txt tai vitsi.txt)
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
    "Paras vitsi": "Kaksi mummoa meni mustikkaan, toinen ei mahtunut!"},

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

for ystava in ystavakirja: # Lisätään hymiöt, tallennetaan testidatoihin (oli aluksi pois nämä, mutta muutin esimerkkien parantamiseksi)
    ystava["Lempieläin"] = lisaa_hymio(ystava["Lempieläin"])
    tallenna_vitsi("data/testivitsi.txt", ystava["Paras vitsi"])
    tallenna_ystava("data/testidata.txt", ystava)

def kysy_teksti(tieto): # Tsekataan, ettei vastaus ole tyhjä -funktio
    while True: # Ikuisuussilmukka kunnes return
        vastaus = input(tieto).strip() # Poistaa välilyönnit, joten välilyönti ei kelpaa vastaukseksi
        if vastaus: # Sit kun on hyväksyttävä vastaus, niin palauttaa sen
            return vastaus
        print("Hups, unohdit vastata kysymykseen!") # Virheellisessä vastauksessa tulostaa tämän ja kysyy uudelleen

#Luodaan kyselylomake
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
    elain = lisaa_hymio(elain) #Lisätään täällä jo hymiö lempieläimen perään
    ammatti = kysy_teksti("Haaveammatti: ")
    fiilis = kysy_teksti("Päivän fiilis hymiönä: ")
    vitsi = kysy_teksti("Paras vitsi: ")

# Tallennetaan vastaukset sanakirjaksi (avain: arvo)
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

    lista.append(tallennus) # Lisää "tallennus" listalle [parametri funktiossa]
    tallenna_ystava("data/testidata.txt", tallennus) # Käytä funkiota tallenna_ystava tiedoilla testidata.txt ja tallennus eli tallentaa tallennuksen annettuun tekstitiedostoon
    tallenna_vitsi("data/testivitsi.txt", tallennus["Paras vitsi"]) # Sama kuin yllä, mutta nyt tallentaa tallennus-osiosta vain kohdan "Paras vitsi" arvon ja eri tiedostoon
    return lista

def vitsin_arvonta(lista):
    vitsit = [] # Tyhjä lista
    for kaveri in ystavakirja: # Kaveri ystäväkirjassa (eli lista sanakirjoista eli yksi sanakirja)
        vitsit.append(kaveri["Paras vitsi"]) # Lisää vitsit-listaan sanakirjoista arvo kohdasta "Paras vitsi"
    return random.choice(vitsit) # Palauta satunnainen vitsi vitsit-listalta

def ilme(ystavakirja): # Sama kuin yllä, mutta hymiöistä
    hymiot = []
    for kaveri in ystavakirja:
        hymiot.append(kaveri["Päivän fiilis hymiönä"])
    return random.choice(hymiot)

# Luodaan haku
def haettava(lista):
    haettava = input("Kenen tiedot näytetään?\n\nEtsitään: ")
    print("_"*20) # Koristelua, selkeyttää lukettavuutta

    for ystava in ystavakirja:
        if ystava["Nimi"].lower() == haettava.lower(): # Muutetaan tallennus- ja haettava-osioista kirjaimet pieniksi, joten ei merkitystä, haetaanko Lily vai lily ja jos haku vastaa haettavaa niin:
            for avain, arvo in ystava.items(): # Saadaan kaikki tiedot .items:illä
                print(f"\n{avain}: {arvo}") # Tulostetaan tiedot ko. henkilösta
            return
    print("Ystäväkirjassasi ei ole tämän nimistä henkilöä")
    valinta = input("Haluatko lisätä uuden ystävän? (K)llä/(E)i ") # Jos haku ei tuota tulosta, voidaan kaveri lisätä kirjaan
    if valinta.lower() == "k":
        lisaa_ystava(ystavakirja)

def pituus(lista):
    return (F"Sinulla on tällä hetkellä {len(ystavakirja)} ystävää kirjassasi.")

def tauko_ja_paluu():
    input("\nPalaa takaisin valikkoon painamalla Enter\n") # Pysäytetään ohjelma hetkeksi, jotta valikko ei tulostu heti perään, vaan tulokset ehtii katsoa rauhassa

while True: # Taas ikuisuussilmukka
    print("="*35) # Lisätty koristeluja ja keskittämistä
    print("❤️  YSTÄVÄKIRJA ❤️".center(35, " "))
    print("="*35)
    print(pituus(ystavakirja))
    valinta = int(input("\nMitä haluaisit tehdä (valitse numero)?\n\n1 - ✍  Lisää kaveri\n2 - 🔎 Etsi kaveri\n3 - 😂 Heitä vitsillä\n4 - 👯 Lue koko ystäväkirja\n5 - 😝 Lue vitsikirjaa\n6 - ❌ Lopeta\n\nValitsen: "))
# Yllä pyydetään siis syöttämään luku
    if valinta == 1: # Jos valinta on "tämä" niin tehdään "näin"
        lisaa_ystava(ystavakirja)
    if valinta == 2:
        haettava(ystavakirja)
        tauko_ja_paluu()
    if valinta == 3:
        print("\n" + "-"*35) # Lisätty koristeluja ja keskittämistä
        print("🎉 päivän vitsi 🎉".center(35))
        print("-"*35)
        print(f"\n{vitsin_arvonta(ystavakirja)}\n")
        print(f"Ilmeesti nyt:\n\n {ilme(ystavakirja)}\n")
        print("-"*35)
        tauko_ja_paluu()
    if valinta == 4:
        with open("data/testidata.txt", encoding="utf-8") as luetaan: #kävin palautuksen jälkeen lisäämässä väliviivan utf-8 -kohtaan, huomasin videota katsoessa tän :D
            sisalto = luetaan.read()
            print(sisalto)
        tauko_ja_paluu()
    if valinta == 5:
        with open("data/testivitsi.txt", encoding="utf-8") as haha:
            kaikki = haha.read()
            print(kaikki)
        tauko_ja_paluu()
    if valinta == 6:
        print("Heihei!")
        break #Silmukka poikki
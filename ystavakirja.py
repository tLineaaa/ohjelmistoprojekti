#Luodaan ystäväkirja-lista
ystavakirja = []

#Luodaan kyselylomake (tee tästä funktio?)
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
        "Päivän fiilis hymiönä": fiilis
    }

    lista.append(tallennus)
    return lista

ystavakirja = lisaa_ystava(ystavakirja)

#Tulostetaan siistinä (voi olla turha tai pitää siirtää - harkitaan)
for avain, arvo in tallennus.items():
    print(f"{avain}: {arvo}")


#Luodaan haku (ehkä funktioksi jossain kohtaa)
haettava = input("Kenen tiedot näytetään?")

for tallennus in ystavakirja:
    if tallennus["Nimi"].lower() == haettava.lower(): # Muutetaan tallennus- ja haettava-osioista kirjaimet pieniksi, joten ei merkitystä, haetaanko Lily vai lily
        for avain, arvo in tallennus.items(): #Saadaan kaikki tiedot .items:illä
            print(f"{avain}: {arvo}")
    else:
        print("Ystäväkirjassasi ei ole tämän nimistä henkilöä")
        lisaa_puuttuva = input("Haluaisitko lisätä ystävän tiedot? (k)yllä/(e)i") #Harkitaan, jos isot ja pienet kirjaimet tässäkin ok?
        if lisaa_puuttuva.lower() == "k":
            lisaa_ystava(ystavakirja)
            #Tähän funktio, jotta saa uudet tiedot syötettyä
        if lisaa_puuttuva == "e":
            print(haettava) #kysyy uudelleen, mutta voisi palata ihan alkuunkin - alkua ei vielä ole :D

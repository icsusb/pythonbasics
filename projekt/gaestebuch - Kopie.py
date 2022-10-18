#Funktionalität des Programms:
#es sollen gäste erfasst und gelöscht werden können 1/2
#es soll eine Liste ausgegeben werden, in der Vorname/nachname/gender ausgegeben wird /3
#es soll ein index der nutzer ausgegeben werden, der indexnummer und Vorname/nachname enthält /4
#es soll möglich sein einzelne Nutzer über deren index anzeigen zu lassen /5
#es soll möglich sein einzelne Nutzer auswählen und ändern zu können. /6
#das programm soll abgebrochen werden können /7
#es soll eine dummyfunkrion zum speichernund eine zum laden berücksichtigt werden /0


#############################################################################
# basisdefinitionen

# Vornamen
# Nachnamen
# Telefonnummer
# Email
# Allergie
# Gender

############################################################################

gasteintrag = {}
gaestebuch = []
gi = {}
index = 0
gasteintrag1 = {}

def filltestdata() :
    global gaestebuch
    gasteintrag = {}
    gasteintrag['vname'] = "Ben"
    gasteintrag['nname'] = "Ertel"
    gasteintrag['telnr'] = "+4900000000"
    gasteintrag['mail'] = "Ertel@ben.deutschland"
    gasteintrag['allergie'] = "keine"
    gasteintrag['gender'] = "backfisch"
    gaestebuch.append(gasteintrag)
    del (gasteintrag)

    #############################################################################

    #gast in gaestebuch schreiben
    #gaestebuch[0] = gasteintrag
    #gasteintrag aus gaestebuch laden
    #gasteintrag = gaestebuch[0]
    gaestebuch.append(gasteintrag)

    gasteintrag1['vname'] = "Franz"
    gasteintrag1['nname'] = "Josef"
    gasteintrag1['telnr'] = "+49123456798"
    gasteintrag1['mail'] = "Franz@josef.deutschland"
    gasteintrag1['allergie'] = "alle"
    gasteintrag1['gender'] = "döner"


#############################################################################

#gast in gaestebuch schreiben
#gaestebuch[0] = gasteintrag
#gasteintrag aus gaestebuch laden
#gasteintrag = gaestebuch[0]
gaestebuch.append(gasteintrag1)
######################################################################################

gi ={}


def hauptmenue():
    print("Willkommen im Gästebuch von Andreas!")
    print('\n\n')
    print("Für neu, Bitte 1 eingeben")
    print("Für Gästeliste, Bitte 4 eingeben")
    print("Für ändern, Bitte 9 eingeben")


def neuereintrag():
    global gi                # an dieser Stelle müssen wir die Variable, die Ausserhalb unserer Funktion liegt aus dem globalen Namespace in die Funktion laden
    global gaestebuch        # an dieser Stelle müssen wir die Variable, die Ausserhalb unserer Funktion liegt aus dem globalen Namespace in die Funktion laden

    gi.clear()
    print("Hier wird ein neuer Gast eingetragen")
    gi['vname'] = input("Bitte den Vornamen eingeben:")
    gi['nname'] = input("Bitte den Nachamen eingeben:")
    gi['telnr'] = input("Bitte die Telefonnummer eingeben:")
    gi['mail'] = input("Bitte die E-Mail Adresse eingeben:")
    gi['allergie'] = input("Bitte Allergien eingeben:")
    gi['gender'] = input("Bitte das Geschlächt eingeben:")
    gaestebuch.append(gi)
    print("\n")

items = ['Vorname', 'Nachname', 'Telefon Nummer', 'E-Mail Adresse', 'Allergie', 'Gender']

def eintragaendern():
    global index
    gi = gaestebuch[index]
    anzahl = len(gaestebuch)
    print("Hier wird ein neuer Gast eingetragen")
    gi['vname'] = input("Bitte den Vornamen eingeben:")
    gi['nname'] = input("Bitte den Nachamen eingeben:")
    gi['telnr'] = input("Bitte die Telefonnummer eingeben:")
    gi['mail'] = input("Bitte die E-Mail Adresse eingeben:")
    gi['allergie'] = input("Bitte Allergien eingeben:")
    gi['gender'] = input("Bitte das Geschlächt eingeben:")
    gaestebuch[index] = gi
    print("\n")

def eintragaendern1():
    global index

    gi = gaestebuch[index]

    print("Bitte Auswählen was geändert werden soll")
    print("1 " + items[0])
    print("2 " + items[1])
    print("3 " + items[2])
    print("4 " + items[3])
    print("5 " + items[4])
    print("6 " + items[5])

    alterchoice = input("Bitte wähle aus, was geändert werden soll")
    if alterchoice == "1":
        print()

    if alterchoice == "2":
        print()

    if alterchoice == "3":
        print()

    if alterchoice == "4":
        print()

    if alterchoice == "5":
        print()

    if alterchoice == "6":
        print()

# basisschleife aufbauen

def listuser():
    global gaestebuch
    counter = 0
    for gast in gaestebuch:
        #gast["vname"]
        #gast["nname"]
        print(gast["vname"] + " " + gast["nname"] + " " + counter.__str__())
        counter += 1

while True:
    # Hauptmenue ausgeben
    hauptmenue()
    # benutzereingabe abfragen
    hmeingabe = input("bitte wähle eine Option des Hauptmenüs:")

    #bedingung prüfen inklusive bedingung "schleifenabbruch"
    #eintrag neuanlegen
    if hmeingabe == '1':
        print()
        neuereintrag()

    if hmeingabe == '4':
        print()
        listuser()

    #eintrag bearbeiten
    if hmeingabe == '9':
        print()
        eintragaendern()


    if hmeingabe == '0':
        print("Programm wird verlassen")
        break
    #gästebuch in eine string umwandeln und dann formatieren und dann ....
    vaus = str(gaestebuch).replace('}, {', '},\n {')

    print(vaus)
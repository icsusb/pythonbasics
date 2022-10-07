


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



gasteintrag['vname'] = "Ben"
gasteintrag['nname'] = "Ertel"
gasteintrag['telnr'] = "+4900000000"
gasteintrag['mail'] = "Ertel@ben.deutschland"
gasteintrag['allergie'] = "keine"
gasteintrag['gender'] = "backfisch"


#############################################################################

#gast in gaestebuch schreiben
gaestebuch[0] = gasteintrag

#gasteintrag aus gaestebuch laden
gasteintrag = gaestebuch[0]

######################################################################################

def Hauptmenue():
    print("")

# basisschleife aufbauen
while True:
    # Hauptmenue ausgeben

    # benutzereingabe abfragen
    hmeingabe = input("bitte wähle eine Option des Hauptmenüs:")

    #bedingung prüfen inklusive bedingung "schleifenabbruch"
daten = "vorname, nachname, alter"
einzeldaten = daten.split("!")
print(einzeldaten, daten)

daten = "vorname, nachname, alter"
einzeldaten = daten.split("! ")
print(einzeldaten)

daten = "vorname, nachname, alter"
einzeldaten = daten.split()
print(einzeldaten)


daten = "vorname,nachname,alter"
einzeldaten = daten.split("!", 10)
print(einzeldaten)


inhalt = "Anzahl Wörter in einem Text zählen!"
woerter = inhalt.split()
print("Anzahl der Wörter: ", len(woerter))

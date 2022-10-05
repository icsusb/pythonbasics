ausgabetext = "Der Preis für 2 Socken beträgt 5 DM und 5 Paar kosten 10 DM"
print(ausgabetext)
ausgabetext = ausgabetext.replace("DM", "Euro")
print("Nach dem Austauschen über replace():")
print(ausgabetext)


ausgabetext = "Der Preis für 2 Socken beträgt 2 DM und 2 Paar kosten 3.50 DM"
ausgabetext = ausgabetext.replace("DM", "Euro")
ausgabetext = ausgabetext.replace("2", "zwei", 2)
print("Nach dem Austauschen über replace():")
print(ausgabetext)




ausgabetext = "1 1 2 2 3 3 4 4"
ausgabetext = ausgabetext.replace("1", "drei")
ausgabetext = ausgabetext.replace("2", "zwei")
ausgabetext = ausgabetext.replace("3", "eins")
print("Nach dem Austauschen über replace():")
print(ausgabetext)


ausgabetext = "1 1 2 2 3 3 4 4 kebap"
ausgabetext = ausgabetext.replace("1","drei").replace("2","zwei").replace("3","eins") .replace("kebap","döner")
print("Nach dem Austauschen über replace():")
print(ausgabetext)

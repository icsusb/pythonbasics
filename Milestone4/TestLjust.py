inhalt = "Vier"
ausgabe = inhalt.ljust(10)
print(ausgabe, "mehr Text")



inhalt = "Fünf"
ausgabe = inhalt.ljust(10, '.')
print(ausgabe, " mit Text")



inhalt = "Vier"
ausgabe = inhalt.ljust(10, '?')
print(ausgabe + "plus Vier")



inhalt = "Vier"
ausgabe = inhalt.ljust(5, '$')
print(ausgabe, " ohne !!! Text")

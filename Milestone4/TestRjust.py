inhalt = "Vier"
ausgabe = inhalt.rjust(15)
print(ausgabe)


inhalt = "Vier"
ausgabe = inhalt.rjust(10)
print(ausgabe, ", und der Tag gehört dir")



inhalt = "Vier"
ausgabe = inhalt.rjust(10, '*')
print(ausgabe + ", und der Tag gehört dir")



inhalt = "Vier"
ausgabe = inhalt.rjust(10, '.')
print(ausgabe + ", und der Tag gehört dir")



inhalt = "Vier"
ausgabe = inhalt.rjust(5, '.')
print(ausgabe + ", und der Tag gehört dir")

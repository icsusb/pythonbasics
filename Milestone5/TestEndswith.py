inhalt = "https://cctrainer.ddnss.de"
ergebnis = inhalt.endswith(".de")
print(ergebnis)


inhalt = "https://cctrainer.ddnsssss.de"
ergebnis = inhalt.endswith(".de", 0, 26)
print(ergebnis)


inhalt = "https://cctrainer.ddnss.der"
datentyp_tupel = (".de", ".com", ".net")
ergebnis = inhalt.endswith(datentyp_tupel)
print(ergebnis)


inhalt = "https://cctrainer.ddnss.org"
ergebnis = inhalt.endswith((".de", ".com", ".net"))
print(ergebnis)


inhalt = "https://cctrainer.ddnss.net"
ergebnis = inhalt.endswith((".de", ".com", ".net"))
print(ergebnis)

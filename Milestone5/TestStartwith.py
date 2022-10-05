inhalt = "https:// cctrainer.ddnss.de "
ergebnis = inhalt.startswith("https://")
print(ergebnis)

inhalt = "http:// cctrainer.ddnss.de "
ergebnis = inhalt.startswith("https://")
print(ergebnis)


inhalt = "https:// cctrainer.ddnss.de "
urlanfang_als_tupel = ("https://", "http://")
ergebnis = inhalt.startswith(urlanfang_als_tupel)
print(ergebnis)


inhalt = "https:// cctrainer.ddnss.de "
ergebnis = inhalt.startswith(("https://", "http://"))
print(ergebnis)

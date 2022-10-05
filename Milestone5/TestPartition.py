satz = "Python ist einfach zu lernen"
ergebnis = satz.partition("ist")
print(ergebnis)


satz = "Python ist einfach zu lernen und ist cool"
ergebnis = satz.partition("ist")
print(ergebnis)


satz = "ist Python einfach zu lernen?"
ergebnis = satz.partition("ist")
print(ergebnis)

satz = "Ist! Python einfach zu lernen?"
ergebnis = satz.partition("ist")
print(ergebnis)

satz = "Ist! Python einfach zu lernen?"
ergebnis = satz.partition("!")
print(ergebnis)


satz = "Ist Python einfach zu lernen?"
ergebnis = satz.partition(" ")
print(ergebnis)

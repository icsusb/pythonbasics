inhalt = "Textinhalt\t1234567890\tmehr Inhalt"
ergebnis = inhalt.expandtabs()
print(ergebnis)



inhalt = "Textinhalt\t1234567890\tmehr Inhalt"
print("01234567890123456789012345678901234567890123456789")
print(inhalt.expandtabs(), " (Standardeinstellung 8)\n")
print(inhalt.expandtabs(2), " (Tabstopp bei 2)\n")
print(inhalt.expandtabs(3), " (Tabstopp bei 3)\n")
print(inhalt.expandtabs(4), " (Tabstopp bei 4)\n")
print(inhalt.expandtabs(5), " (Tabstopp bei 5)\n")
print(inhalt.expandtabs(6), " (Tabstopp bei 6)\n")
print(inhalt.expandtabs(7), " (Tabstopp bei 7)\n")
print(inhalt.expandtabs(8), " (Tabstopp bei 8)\n")
print(inhalt.expandtabs(9), " (Tabstopp bei 9)\n")
print(inhalt.expandtabs(10), " (Tabstopp bei 10)\n")

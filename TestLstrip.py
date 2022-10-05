#gibt uns den Test ohne leerzeichen
inhalt = "  Python steinhaha  "
ausgabe = inhalt.lstrip()
print(ausgabe)

print("\n\n")

# gibt uns den text ohne leerzeichen und noch den extra Text hinzugefügt zum Orig. Text
inhalt = "  Python steinhaha  "
ausgabe = inhalt.lstrip()
print(ausgabe +", daher Pyton ist stark")

print("\n\n")

#alles was in der .lstrip( geschrieben wird ) nach wird ignoriert
inhalt="321     Python 3 stein"
ausgabe = inhalt.lstrip('123')
print(ausgabe)

print("\n\n\n")

#alles was in der .lstrip( geschrieben wird ) nach wird ignoriert auch LEERZEICHEN
inhalt="45869    Python 3 stein"
ausgabe = inhalt.lstrip(' 123456789')
print(ausgabe)

print("\n\n\n")

#lstrip() – links Zeichen entfernen (meistens Leerzeichen)
#strip() – rechts und links bestimmte Zeichen entfernen (meistens Leerzeichen)
#rstrip() – rechts Zeichen entfernen (meistens Leerzeichen)
inhalt="45869    Python 3 stein 555888"
ausgabe = inhalt.rstrip(' 123456789')
print(ausgabe)

print("\n\n\n")

inhalt="45869    Python 3 stein 555888"
ausgabe = inhalt.strip(' 123456789')
print(ausgabe)


print("\n\n\n")

inhalt="1.)Python stein 555888"
ausgabe = inhalt.strip('.) 123456789')
print(ausgabe)



print("\n\n\n")

inhalt=" Python 3 stein 1233 4444 ? XXXYYYZZZZ"
ausgabe=inhalt.rstrip('1234 ?XYZ')
print(ausgabe +",daher Python stark")


print("\n\n\n")

inhalt=" Python rocks \n \r\n "
ausgabe = inhalt.rstrip('\n ')
print(ausgabe + ",damit sichtbar wird, was gelöscht wurde")

print("\n\n\n")

inhalt=" Python rocks \n \r\n "
ausgabe = inhalt.rstrip('\n \r')
print(ausgabe + ",damit sichtbar wird, was gelöscht wurde")




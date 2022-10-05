columns="1234567890123456789012345678901234567890"
inhalt="45869    Python 3 stein 555888"
ausgabe = inhalt.rstrip(' 123456789')
print(columns)
print(ausgabe)

print("\n\n\n")

inhalt=" Python 3 stein 1233 4444 ? XXXYYYZZZZ"
ausgabe=inhalt.rstrip('1234 ?XYZ')
print(columns)
print(ausgabe +",daher Python stark")


print("\n\n\n")

inhalt=" Python rocks \n \r\n "
ausgabe = inhalt.rstrip('\n ')
print(columns)
print(ausgabe + ",damit sichtbar wird, was gelöscht wurde")

print("\n\n\n")

inhalt=" Python rocks \n \r\n "
ausgabe = inhalt.rstrip('\n \r')
print(columns)
print(ausgabe + ",damit sichtbar wird, was gelöscht wurde")

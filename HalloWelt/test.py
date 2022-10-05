

# zeilenumbrüche und backslash
#print ("hallo welt")


#pfad = "c:\\reichlich"
#print(pfad)

#pfad1 = "c:\_reichlich"
#print(pfad1)

columns='123456789012345678901234567890'

testtext = 'Heute ist ein schöner Tag,\n weil die Sonne scheint\nund Freitag ist!'

print(columns)
print(testtext)


testtext1 = 'Heute ist ein schöner Tag,\t weil die Sonne scheint\t und Freitag ist!'

print(testtext1)


print('raw-Ausgabe')
print(r'c:\niedlicherverzeichnisname')
#print(rpfad)

print('\n\n')


#mehrere Umbrüche bei der Ausgabe
print('mehrere Umbrüche')
#zeilenumbruch mit ausgeben Variante 3
print('''Hallo
Welt
-in 3 Zeilen''')

#leere Zeilen zur Trennung einfügen
print('\n\n')

# hier noch einmal die Zeilenumbrüche mit doppelten Anführungszeichen
print("""Hallo
Welt
-in 3 Zeilen""")

print("\n\n")

Axel ="Test"
vorname = Axel
print("vorname")

print("\n\n")

testtext = "Ku'damm für Kurfürstendamm"
print(testtext)

print("\n\n")

#error
#testtext = 'Ku'damm für Kurfürstendamm'
#print(testtext)

#fix for 
print("\n\n")
testtext = 'Ku\'damm für Kurfürstendamm'
print(testtext)

print("\n\n")

#zeigt uns die String länge an
kursname = "Python lernen"
print(len(kursname))

print("\n\n")
#alles in klein
kursname = " PhyThOn LERnen "
print(kursname.lower())


print("\n\n")
#alles in groß
kursname = " PhyThOn LERnen "
print(kursname.upper())

#help(str) ->>>>
#dir(str) ->>>>
print("\n\n")

#ß wird in ss umgewandelt - kein uppercase für ß 
bockwurst = "große Portion Bockwurst, bitte!"
print(bockwurst.upper())



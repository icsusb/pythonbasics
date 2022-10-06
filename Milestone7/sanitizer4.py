teststring = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
teststring = ' <html> ist eine tolle Sprache</html> '
teststring = "Hacker schleusen auch gerne Code ein! test()"
teststring = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
teststring = "Oder am Ende von Eingaben "
teststring = """Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch")\n"""
teststring = """Hier folgt ein Codeabschnitt : \nif true:\n    print('wahr')\nelse:\n    print('falsch')\n"""
#teststring = "<dieser String ist nun sanitized>"
#teststring = ' dies ist ein Teststring(); \r\nmit Klammern und <html tags>! \n und Umbrüchen - '
#teststring = " dies ist ein Teststring(); \r\nmit Klammern und <html tags>! \n und Umbrüchen - "
#teststring = " dies ist ein Teststring(); \nmit Klammern und <html tags>! \n und Umbrüchen - "
#teststring = " dies ist ein Teststring(); \rmit Klammern und <html tags>! \r und Umbrüchen - "
teststring = "% dies ist ein Teststring(); \rmit Klammern und <html tags>! \r und Umbrüchen - "


#############################################################################
# Basisdefinition von Werten und Strings
columns = "123456789012345678901234567890123456789012345678901234567890"
columns2 = "000000000111111111122222222223333333333444444444455555555556"
sonderzeichen = "%$§\"\`\'#/:;-"
leerzeichen = " \t"
zeilenumbruch = "\n\n\r"
klammern = "<>[]{}()"
#gescount = []
testdurchlauf = 1
############################################################################
# Ausgabe vorbereiten
print(columns2)
print(columns)

print ("Hier kommt der Original-String nach Eingabe:\n")

print(teststring)
print(columns2)
print(columns)

print ("dieser beinhaltet folgende Anzahl pro Sonderzeichen:")

#######################################
# Aufzählungen aufbereiten
startx = "Sonderzeichen"
footerx = "ist so oft vertreten"
delimitter = ':'
print(columns2)
print(columns)
sani4 = teststring
# Sonderzeichen für Programmierung am Ende entfernen!
# String 4 weiterverarbeiten
print("es sind " + str(len (sonderzeichen)) + " Sonderzeichen erfasst und zu bereinigen")

sondercount = 0                     # hilfsvariable vom Typ integer erzeugen für gesamtersetzungen vom selben zeichenvorrat
sonderinc = 1
while sonderinc <= len(sonderzeichen):
    charx = sonderzeichen[sonderinc -1]            #
    countx = sani4.count(charx)         # dies ist eine zahl vom typ integer
    sondercount += countx  #
    countxstr = str(countx)             # die zahl countx in einen string gewandelt
    startx = startx.ljust(19, ' ')      # startx linksbündig formatieren und auf 20 Zeichen auffüllen
    footerx = footerx.rjust(29, ' ')    # 2. Hinweis auf 30 Zeichen  auffüllen und rechtsbündig formatieren
    countxstr = countxstr.zfill(2).rjust(5, ' ')
    out = startx + charx + footerx + delimitter + countxstr # ausgabestring zusammensetzen
    print(out)                          # den fertigen ausgabesting ausgeben
    sonderinc += 1


print("es wurden insgesamt " + sondercount.__str__() + " " + startx + " ersetzt!")




####################################################################################################
# anzahl Klammern ausgeben
# Sonderzeichen für Programmierung am Ende entfernen!
# String 4 weiterverarbeiten
startx = "Klammern"
footerx = "ist so oft vertreten"
delimitter = ':'
print(columns2)
print(columns)
print("es sind       " + str(len (klammern)) + " Klammern erfasst und zu bereinigen")
klammercount = 0
klammerinc = 1
while klammerinc <= len(klammern):
    charx = klammern[klammerinc -1]            #
    countx = sani4.count(charx)         # dies ist eine zahl vom typ integer
    klammercount += countx  
    countxstr = str(countx)             # die zahl countx in einen string gewandelt
    startx = startx.ljust(19, ' ')      # startx linksbündig formatieren und auf 20 Zeichen auffüllen
    footerx = footerx.rjust(29, ' ')    # 2. Hinweis auf 30 Zeichen  auffüllen und rechtsbündig formatieren
    countxstr = countxstr.zfill(2).rjust(5, ' ')
    out = startx + charx + footerx + delimitter + countxstr # ausgabestring zusammensetzen
    print(out)                          # den fertigen ausgabesting ausgeben
    klammerinc += 1

print("es wurden insgesamt " + klammercount.__str__() + " " + startx + " ersetzt!")

#gescount.append(klammercount._str_())

###################################################################################################
# Anzahl der Zeilenümbrüche und Leerzeichen

startx = 'Leerzeichen'
footerx = "ist so oft vertreten"
delimitter = ':'
leercount = 0
leerinc = 1

print(columns2)
print(columns)
print("Es sind   " + str(len (leerzeichen)) + "  Leerzeichen erfasst und zu bereinigen")
while leerinc <= len(leerzeichen):
    charx = leerzeichen[leerinc -1]            #
    countx = sani4.count(charx)         # dies ist eine zahl vom typ integer
    leercount += countx  
    countxstr = str(countx)             # die zahl countx in einen string gewandelt
    startx = startx.ljust(19, ' ')      # startx linksbündig formatieren und auf 20 Zeichen auffüllen
    footerx = footerx.rjust(29, ' ')    # 2. Hinweis auf 30 Zeichen  auffüllen und rechtsbündig formatieren
    countxstr = countxstr.zfill(2).rjust(6, ' ')
    out = startx + footerx + delimitter + countxstr # ausgabestring zusammensetzen
    print(out)                          # den fertigen ausgabesting ausgeben
    leerinc += 1

print("es wurden insgesamt " + leercount.__str__() + " " + startx + "ersetzt!")



startx = 'Zeilenumbrüche'
footerx = "ist so oft vertreten"
delimitter = ':'
zeilcount = 0
zeilinc = 1

print(columns2)
print(columns)
print("Es sind   " + str(len (zeilenumbruch)) + "  Zeilenumbrüche erfasst und zu bereinigen")
while zeilinc <= len(zeilenumbruch):
    charx = zeilenumbruch[zeilinc -1]            #
    countx = sani4.count(charx)         # dies ist eine zahl vom typ integer
    zeilcount += countx  
    countxstr = str(countx)             # die zahl countx in einen string gewandelt
    startx = startx.ljust(19, ' ')      # startx linksbündig formatieren und auf 20 Zeichen auffüllen
    footerx = footerx.rjust(29, ' ')    # 2. Hinweis auf 30 Zeichen  auffüllen und rechtsbündig formatieren
    countxstr = countxstr.zfill(2).rjust(6, ' ')
    out = startx + charx + footerx + delimitter + countxstr # ausgabestring zusammensetzen
    print(out)                          # den fertigen ausgabesting ausgeben
    zeilinc += 1

print("es wurden insgesamt " + zeilcount.__str__() + " " + startx + "ersetzt!")

###################################################################################################
# Grundsätzliche Bearbeitung zu Eingabefehlern und Bösen Eingabe Anfängen und Enden!
print(columns2)
print(columns)

print("Basisbearbeitung des Strings ")
#Leerzeichen am Anfang und Ende, sicher entfernen
sani1 = teststring.strip(leerzeichen)
sani1 = sani1.replace(zeilenumbruch[0]," ")
sani1 = sani1.replace(zeilenumbruch[1]," ")
sani1 = sani1.replace(leerzeichen[1]," ")

print('Um Leerzeichen Bereinigter String 1:\n' + sani1)

#Klammern am Anfang und Ende entfernen !
sani2 = sani1.strip(klammern)
print('Um Klammern Bereinigter Text 2:\n' + sani2)

# Klammern und Leerzeichen am Anfang und Ende entfernen
sani3 = sani2.strip(klammern)
print('Um Klammern und Leerzeichen Bereinigter Text 3:\n' + sani3)

# Sonderzeichen für Programmierung am Ende entfernen!
# String 3 weiterverarbeiten
sani4 = sani3.strip(sonderzeichen)
print('Um SonderzeichenBereinigter Text 4\n' + sani4)


###################################################################################################
# Durchführung der Bereinigung
print(columns2)
print(columns)
print("Stringinterne Bereinigung um Sonderzeichen.")
sonderinc = 1
sani5 = sani4

while sonderinc <= len(sonderzeichen):
    sani5 = sani5.replace(sonderzeichen[sonderinc - 1]," ")
    sonderinc += 1    

print("Stringinterne Bereinigung von Klammern.")

klammerinc = 1

while klammerinc <= len(klammern):
    sani5 = sani5.replace(klammern[klammerinc - 1]," ")
    klammerinc += 1


print("Stringinterne Bereinigung von Zeilenumbrüchen.")

zeileninc = 1

while zeileninc <= len(zeilenumbruch):
    sani5 = sani5.replace(zeilenumbruch[zeileninc - 1]," ")
    zeileninc += 1
####################################################################################################

##zahl1 = int(gescount[0])
##zahl2 = int(gescount[1])
##zahl3 = zahl1 + zahl2
##gescount.append(zahl3._str_())

####################################################################################################
# Schlussendliche Ausgabe
print(columns2)
print(columns)

# noch einmal führende leerzeichen entfernen
#sani5 = sani5.lstrip(' ')
#print(sani5)
print('um Leerzeichen, Sonderzeichen und Klammern Bereinigter Text 5')
print('x->:' + sani5)
##print("Es wurden insgesammt " + gescount[2] + " Zeichenbearbeitet!")
##print(gescount)

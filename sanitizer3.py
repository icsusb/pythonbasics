
teststring = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
#teststring = ' <html> ist eine tolle Sprache</html> '
#teststring = "Hacker schleusen auch gerne Code ein! test()"
#teststring = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
#teststring = "Oder am Ende von Eingaben "
#teststring = """Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch")\n"""
#teststring = """Hier folgt ein Codeabschnitt : \nif true:\n    print('wahr')\nelse:\n    print('falsch')\n"""
#teststring = "<dieser String ist nun sanitized>"
#teststring = ' dies ist ein Teststring(); \r\nmit Klammern und <html tags>! \n und Umbrüchen - '
#teststring = " dies ist ein Teststring(); \r\nmit Klammern und <html tags>! \n und Umbrüchen - "
#teststring = " dies ist ein Teststring(); \nmit Klammern und <html tags>! \n und Umbrüchen - "
#teststring = " dies ist ein Teststring(); \rmit Klammern und <html tags>! \r und Umbrüchen - "


#############################################################################
# Basisdefinition von Werten und Strings
#columns = "123456789012345678901234567890123456789012345678901234567890"
columns = 6*"1234567890"
#columns2 = "000000000111111111122222222223333333333444444444455555555556"
columns2 = 9*"0"+10*"1"+10*"2"+10*"3"+10*"4"+10*"5"+10*"6"
sonderzeichen = "%$§\"\`\'#/:;-"
leerzeichen = " \t"
zeilenumbruch = "\n\n\r"
klammern = "<>[]{}()"

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
print(columns2)
print(columns)
sani4 = teststring
# Sonderzeichen für Programmierung am Ende entfernen!
# String 4 weiterverarbeiten
print("es sind " + str(len (sonderzeichen)) + " erfasst und zu bereinigen")

startx = " Sonderzeichen"
footerx = " ist so oft vertreten"
delmitter = ":"

# hier wird das erste Sonderzeichen gezählt
charx = sonderzeichen[0]                                    # laden des ersten Sonderzeichens aus dem String
countx = sani4.count(charx[0])                              # zählen des ersten sonderzeichens (vorkommen) im String
#out="Sonderzeichen " + charx + " ist  so oft vertreten :" + str(countx)
countxstr = str(countx).zfill(2).rjust(5," ")               # aufbereiten der Zahl als String
countxstr0 = str(countx)
out = startx + charx + footerx + delmitter + countxstr       # zusammmensetzen der Ausgabestrings
out0 = countxstr0
print(out)                                                  # Ausgabe des fertigen Strings


charx = sonderzeichen[1]
countx = sani4.count(charx[0])
countxstr = str(countx).zfill(2).rjust(5," ")
countxstr1 = str(countx)
countx = sani4.count(charx[0])
out = startx + charx + footerx + delmitter + countxstr
out1 = countxstr1
print(out)


charx = sonderzeichen[2]
countx = sani4.count(charx[0])
countxstr = str(countx).zfill(2).rjust(5," ")
countxstr2 = str(countx)
out = startx + charx + footerx + delmitter + countxstr
out2 = countxstr2
print(out)


charx = sonderzeichen[3]
countx = sani4.count(charx[0])
countxstr = str(countx).zfill(2).rjust(5," ")
countxstr3 = str(countx)
out = startx + charx + footerx + delmitter + countxstr
out3 = countxstr3
print(out)


charx = sonderzeichen[4]
countx = sani4.count(charx[0])
countxstr = str(countx).zfill(2).rjust(5," ")
countxstr4 = str(countx)
out = startx + charx + footerx + delmitter + countxstr
out4 = countxstr4
print(out)


charx = sonderzeichen[5]
countx = sani4.count(charx[0])
countxstr = str(countx).zfill(2).rjust(5," ")
countxstr5 = str(countx)
out = startx + charx + footerx + delmitter + countxstr
out5 = countxstr5
print(out)


charx = sonderzeichen[6]
countx = sani4.count(charx[0])
countxstr = str(countx).zfill(2).rjust(5," ")
countxstr6 = str(countx)
out = startx + charx + footerx + delmitter + countxstr
out6 = countxstr6
print(out)


charx = sonderzeichen[7]
countx = sani4.count(charx[0])
countxstr = str(countx).zfill(2).rjust(5," ")
countxstr7 = str(countx)
out = startx + charx + footerx + delmitter + countxstr
out7 = countxstr7
print(out)


charx = sonderzeichen[8]
countx = sani4.count(charx[0])
countxstr = str(countx).zfill(2).rjust(5," ")
countxstr8 = str(countx)
out = startx + charx + footerx + delmitter + countxstr
out8 = countxstr8
print(out)


charx = sonderzeichen[9]
countx = sani4.count(charx[0])
countxstr = str(countx).zfill(2).rjust(5," ")
countxstr9 = str(countx)
out = startx + charx + footerx + delmitter + countxstr
out9 = countxstr9
print(out)


charx = sonderzeichen[10]
countx = sani4.count(charx[0])
countxstr = str(countx).zfill(2).rjust(5," ")
countxstr10 = str(countx)
out = startx + charx + footerx + delmitter + countxstr
out10 = countxstr10
#countxstr10
print(out)


charx = sonderzeichen[11]
countx = sani4.count(charx[0])
countxstr = str(countx).zfill(2).rjust(5," ")
countxstr11 = str(countx)
out = startx + charx + footerx + delmitter + countxstr
out11 = countxstr11
#countxstr11
print(out)

#print (float(out0) + float(out1) + float(out2) + float(out3) + float(out4) + float(out5) + float(out6) + float(out7) + float(out8) + float(out9) + float(out10) + float(out11))
#Summe1 = (float(out0) + float(out1) + float(out2) + float(out3) + float(out4) + float(out5) + float(out6) + float(out7) + float(out8) + float(out9) + float(out10) + float(out11))
Summe1 = (int(out0) + int(out1) + int(out2) + int(out3) + int(out4) + int(out5) + int(out6) + int(out7) + int(out8) + int(out9) + int(out10) + int(out11))
print("Es sind " + str(Summe1) + " Sonderzeichen im Text enthalten ")


#print (float(countxstr10) + float(countxstr11))
####################################################################################################
# anzahl Klammern ausgeben
# Sonderzeichen für Programmierung am Ende entfernen!
# String 4 weiterverarbeiten

print(columns2)
print(columns)
print("es sind " + str(len (klammern)) + " erfasst und zu bereinigen")
charx = klammern[0]
countx = sani4.count(klammern[0])
countxstr = str(countx).zfill(2).rjust(3," ")
countxstr00 = str(countx)
out="Klammer       " + charx + " ist  so oft vertreten :" + str(countxstr)
out00 = countxstr00
print(out)

charx = klammern[1]
countx = sani4.count(klammern[0])
countxstr = str(countx).zfill(2).rjust(3," ")
countxstr01 = str(countx)
out="Klammer       " + charx + " ist  so oft vertreten :" + str(countxstr)
out01 = countxstr01
print(out)

charx = klammern[2]
countx = sani4.count(klammern[0])
countxstr = str(countx).zfill(2).rjust(3," ")
countxstr02 = str(countx)
out="Klammer       " + charx + " ist  so oft vertreten :" + str(countxstr)
out02 = countxstr02
print(out)

charx = klammern[3]
countx = sani4.count(klammern[0])
countxstr = str(countx).zfill(2).rjust(3," ")
countxstr03 = str(countx)
out="Klammer       " + charx + " ist  so oft vertreten :" + str(countxstr)
out03 = countxstr03
print(out)

charx = klammern[4]
countx = sani4.count(klammern[0])
countxstr = str(countx).zfill(2).rjust(3," ")
countxstr04 = str(countx)
out="Klammer       " + charx + " ist  so oft vertreten :" + str(countxstr)
out04 = countxstr04
print(out)

charx = klammern[5]
countx = sani4.count(klammern[0])
countxstr = str(countx).zfill(2).rjust(3," ")
countxstr05 = str(countx)
out="Klammer       " + charx + " ist  so oft vertreten :" + str(countxstr)
out05 = countxstr05
print(out)

charx = klammern[6]
countx = sani4.count(klammern[0])
countxstr = str(countx).zfill(2).rjust(3," ")
countxstr06 = str(countx)
out="Klammer       " + charx + " ist  so oft vertreten :" + str(countxstr)
out06 = countxstr06
print(out)

charx = klammern[7]
countx = sani4.count(klammern[0])
countxstr = str(countx).zfill(2).rjust(3," ")
countxstr07 = str(countx)
out="Klammer       " + charx + " ist  so oft vertreten :" + str(countxstr)
out07 = countxstr07
print(out)

Summe2 = (float(out00) + float(out01) + float(out02) + float(out03) + float(out04) + float(out05) + float(out06) + float(out07))

print("Es sind " + str(Summe2) + " Klammern im Text enthalten ")

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
sani5 = sani4.replace(sonderzeichen[0]," ")
sani5 = sani5.replace(sonderzeichen[1]," ")
sani5 = sani5.replace(sonderzeichen[2]," ")
sani5 = sani5.replace(sonderzeichen[3]," ")
sani5 = sani5.replace(sonderzeichen[4]," ")
sani5 = sani5.replace(sonderzeichen[5]," ")
sani5 = sani5.replace(sonderzeichen[6]," ")
sani5 = sani5.replace(sonderzeichen[7]," ")
sani5 = sani5.replace(sonderzeichen[8]," ")
sani5 = sani5.replace(sonderzeichen[9]," ")
sani5 = sani5.replace(sonderzeichen[10]," ")
sani5 = sani5.replace(sonderzeichen[11]," ")
#sani5 = sani5.replace(sonderzeichen[12]," ")
#sani5 = sani5.replace(sonderzeichen[13]," ")
#sani5 = sani5.replace(sonderzeichen[14]," ")

print("Stringinterne Bereinigung von Klammern.")
sani5 = sani5.replace(klammern[0]," ")
sani5 = sani5.replace(klammern[1]," ")
sani5 = sani5.replace(klammern[2]," ")
sani5 = sani5.replace(klammern[3]," ")
sani5 = sani5.replace(klammern[4]," ")
sani5 = sani5.replace(klammern[5]," ")
sani5 = sani5.replace(klammern[6]," ")
sani5 = sani5.replace(klammern[7]," ")

print("Stringinterne Bereinigung von Zeilenumbrüchen.")
sani5 = sani5.replace(zeilenumbruch[0]," ")
sani5 = sani5.replace(zeilenumbruch[1]," ")
sani5 = sani5.replace(zeilenumbruch[2]," ")
#sani5 = sani5.replace(klammern[3]," ")
#sani5 = sani5.replace(klammern[4]," ")
#sani5 = sani5.replace(klammern[5]," ")
#sani5 = sani5.replace(klammern[6]," ")
#sani5 = sani5.replace(klammern[7]," ")
####################################################################################################
# Schlussendliche Ausgabe
print(columns2)
print(columns)

# noch einmal führende leerzeichen entfernen
#sani5 = sani5.lstrip(' ')
#print(sani5)
print('um Leerzeichen, Sonderzeichen und Klammern Bereinigter Text 5')
print('  ' + sani5)

print("Ins Gesammt haben wir " + str(Summe1+Summe2) + " Klammern und Sonderzeichen!")
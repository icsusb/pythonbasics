Eingangsstring =" - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
#Eingangsstring =' <html> ist eine tolle Sprache</html> '
#Eingangsstring ="Hacker schleusen auch gerne Code ein! test()"
#Eingangsstring =" ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
#Eingangsstring ="Oder am Ende von Eingaben "
#Eingangsstring ='Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch")\n'
#Eingangsstring ="<dieser String ist nun sanitized>"



sani1 = Eingangsstring.strip('<>();-{}[] \'')
print('Ausgabestring:\n' + sani1)




inhalt = Eingangsstring.count
print ('enthält sonderzeichen01:' + inhalt.count("<"))

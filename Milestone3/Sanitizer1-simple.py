teststring =" - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
sani4 = teststring.strip('; -“')
print('Bereinigter Text 1:\n' + sani4)

print("\n\n")

teststring =' <html> ist eine tolle Sprache</html> '
sani4 = teststring.strip('; -“')
print('Bereinigter Text 2:\n' + sani4)

print("\n\n")

teststring ="Hacker schleusen auch gerne Code ein! test()"
sani2 = teststring.strip('test( )')
print('Bereinigter Text 3:\n' + sani2)

print("\n\n")

teststring =" ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
sani4 = teststring.strip('; -“')
print('Bereinigter Text 4:\n' + sani4)

print("\n\n")

teststring ="Oder am Ende von Eingaben "
sani4 = teststring.strip('; -“')
print('Bereinigter Text 5:\n' + sani4)

print("\n\n")

teststring ='Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch")\n'
sani4 = teststring.strip('; -“')
print('Bereinigter Text 6:\n' + sani4)

print("\n\n")

teststring ="<dieser String ist nun sanitized>"
sani3 = teststring.strip('\<\>')
print('Bereinigter Text 7:\n' + sani3)

print("\n\n")

#Leerzeichen am Anfang und Ende, sicher entfernen
#sani1 = teststring.strip('')
#print('Bereinigter String:\n' + sani1)
#Klammern entfernen !
#sani2 = teststring.strip('()')
#print('Bereinigter Text 2:\n' + sani2)
# Klammern und Leerzeichen entfernen
#sani3 = teststring.strip('\<\>')
#print('Bereinigter Text 3:\n' + sani3)
# Sonderzeichen für Programmierung am Ende entfernen!
# String 3 weiterverarbeiten
#sani4 = teststring.strip('; -“')
#print('Bereinigter Text 4:\n' + sani4)


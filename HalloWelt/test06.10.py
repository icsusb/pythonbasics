

zahl = 0
zahl = zahl + 1
zahl += 1
zahl += zahl + 1
#print(zahl)

teststring = "abcdefghijklm"

durchlauf = 1
abbruch = len(teststring)
while durchlauf <= abbruch :
    cnr = durchlauf -1
    print("hallo " + durchlauf.__str__() + " " + teststring[cnr] )
    durchlauf += 1


print("dies kommt nach der schleife")


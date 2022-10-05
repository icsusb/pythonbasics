



teststring = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "

columns = "123456789012345678901234567890123456789012345678901234567890"
columns2 = "000000000111111111122222222223333333333444444444455555555556"


charx = "'"
countx = teststring.count(charx)

countx = 5

countxstr = str(countx); countxstr = countxstr.zfill(2)

countxstr = str(countx).zfill(2).rjust(5," ")

#print(countxstr)

startx = " Sonderzeichen"
#startx = "Klammern"
startx = startx.ljust(19," ")

print(columns2)
print(columns)

#print(startx,"!")


footerx = " ist so oft vertreten"
delmitter = ":"
#print (str(len(footerx)))

footerx = footerx.center(29, " ")

out = startx + charx + footerx + delmitter + countxstr

print(out)
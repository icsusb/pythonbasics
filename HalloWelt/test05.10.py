
#teststring = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "

#columns = "123456789012345678901234567890123456789012345678901234567890"
#columns = 6*"1234567890"
#columns2 = "000000000111111111122222222223333333333444444444455555555556"
#columns2 = 9*"0"+10*"1"+10*"2"+10*"3"+10*"4"+10*"5"+10*"6"


#charx = "'"
#startx = " Sonderzeichen"
#footerx = " ist so oft vertreten"
#delmitter = ":"


#countx = teststring.count(charx)
#countxstr = str(countx).zfill(2).rjust(5," ")
#startx = startx.ljust(19," ")
#footerx = footerx.center(29, " ")





#out = startx + charx + footerx + delmitter + countxstr

#print(out)


zahl1 = 8
zahl2 = 5

enthalten = zahl1//zahl2
rest = zahl1%zahl2
out = "Die Zahl " + str(zahl2) + " ist " + str(enthalten) + " mal in " + zahl1.__str__() + \
      " enthalten , \n es bleibt ein Rest von " + rest.__str__() + " übrig!"


print(out)

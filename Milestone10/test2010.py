


# funktionen und Rückgabewerte

def testfunktion1():
    print("Hallo Welt")


def test2funtkion(par1, par2):
    print(par1)
    print(par2)

def test3funktion(par1, par2="hallo"):
    print(par1)
    print(par2)

def test4funktion(par1, par2="hallo"):
    print(par1)
    print(par2)
    out = par1 + " " + par2
    return out

xout=""
def test5funktion(par1, par2="hallo"):
    global xout
    print(par1)
    print(par2)
    out= par1 + " " + par2
    return out

def test6funktion(par1="test", par2="hallo"):
    global xout
    if par1 == "": par1="test"
    print(par1)
    print(par2)
    out= par1 + " " + par2
    return out


def ausgabe(wert1, wert2):
    print("Ausgabe von Text aus einer Funktion")
    print(wert1)
    print(wert2)

ausgabe(5,3)

def ausgabe2( *mehrereParameter ):
    if len(mehrereParameter) < 1: print("kein parameter übergeben. Logikfehler?")
    for einzelwert in mehrereParameter:
        print(einzelwert)


#ausgabe2("Hallo", "Welt", "guten", "Morgen")
#print(ausgabe2)
x= None
y= None
z= None

ausgabe2(x,y,z)

def uebergeben(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

uebergeben(vorname="Axel",nachname="Brand",alter="35")
uebergeben(vorname="Axel",nachname="Brand",alter=35)


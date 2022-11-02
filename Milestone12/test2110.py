testwert = "Hallo"

def testfunktion():
    global testwert
    return testwert

class tier():

    def __init__(self):
        self.tierart = "biene"
        self.bewegung = "fliegen"
        self.laut = "sum sum"
        self.name = "Biene Maja"

    def bewegen(self):
        return self.bewegung


    def laut_geben(self):
        return  self.laut

    def set_name(self, name1):
        self.name = name1

    def get_name(self):
        return self.name

#testfunktion()

meintier = tier()
print(meintier.get_name())

deintier = tier()
deintier.set_name("Willi")
print(deintier.get_name())
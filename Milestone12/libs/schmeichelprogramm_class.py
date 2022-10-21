import random

class schmeichelbot_class():

    def __init__(self):
        x = False

        self.adjektiv = []
        self.nomen = []


        self.adjektiv = ['beste', 'liebenswürdigste', 'schönste', 'größte']
        self.nomen = ['Mensch', 'Hecht', 'Freund', 'Kumpel', 'wannabe Programmierer']


    def set_nomen(self,xnomen):
        self.nomen.append(xnomen)
        return self

    def set_adjektiv(self,xadjektiv):
        self.adjektiv.append(xadjektiv)
        return self


    def ausgabe(self):

        print("Du bist der" + " " + (random.choice(self.adjektiv)) + " " + (random.choice(self.nomen)) + " !!!")


#schmeichel = schmeichelbot_class()
#schmeichel.set_nomen("dingsbums").set_nomen("der Welt").set_nomen("dummdumm")
#schmeichel.set_adjektiv("kleinste").set_adjektiv("flashe leer kopf").set_adjektiv("suboptimal-intelligent")

#schmeichel.ausgabe()
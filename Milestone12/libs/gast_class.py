


class gast_class():
    """diese klasse vereint die Eigenschaften eine Gastes"""

    def __init__(self):
        self.vname = "John"
        self.nname = "Doe"
        self.gender = "d" #m/w/d
        self.alter = "00"
        self.covid = False
        self.status = "noshow"
        self.gebdate = "0000.00.00"

    def get_vname(self):
        return self.vname

    def set_vname(self,name):
        self.vname = name
        return self

    def get_nname(self):
        return self.nname

    def set_nname(self, name):
        self.nname = name
        return self

    def get_gender(self):
        return self.gender

    def set_gender(self,gender):
        self.gender = gender
        return self

    def get_alter(self):
        return self.alter

    def set_alter(self,alter):
        self.alter = alter
        return self

    def get_covid(self):
        return self.covid

    def set_covid(self,covid):
        self.covid = covid
        return self

    def get_status(self):
        return self.status

    def set_status(self,status):
        self.status = status
        return self

    def get_gebdate(self):
        return self.gebdate

    def set_gebdate(self, gebdate):
        self.gebdate = gebdate
        return self
#gastx = gast()
#gastx.set_vname("ralf").set_nname("doe").set_covid(True)
#print(gastx.get_vname())
#print(gastx.get_nname())





#gaesteliste = []

#gaesteliste.append(gast().set_vname("mike"))
#gaesteliste.append(gast().set_vname("luci"))
#gaesteliste.append(gast().set_vname("franz"))
#gaesteliste.append(gast().set_vname("dingdong"))

#for gastx in gaesteliste:
    #print(gastx().get_name())

#gast().set_vname("mike")

#teststring = "dies ist ein Test"
#teststring.strip(" ").count()
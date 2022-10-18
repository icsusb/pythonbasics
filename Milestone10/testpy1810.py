import random
namen = ['Axel', 'Alex', 'Andreas', 'Mike']
def schmeichel():
    adjektiv = ['beste', 'liebenswürdigste', 'schönste', 'größte']
    norm = ['Mensch', 'Hecht', 'Freund', 'Kumpel', 'wannabe Programmierer']
    out = "Du bist der" + " " + (random.choice(adjektiv)) + " " + (random.choice(norm)) + " !!!"
    return out

rueck = schmeichel()
print (rueck)
for name in namen:
    #rueck = schmeichel()
    print (name + " " + schmeichel())
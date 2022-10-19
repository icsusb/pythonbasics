#Gruppe  Alex ; Axel ; Dieter ; Ralf ; Steffen.
# Lottoziehung 1 von 49
# Eine Zufahlszahl von 1 bis 49 generieren.

import random

randomlist = random.sample(range(1, 49), 6)
reihenfolge = sorted(randomlist)
print(reihenfolge)

for i in reihenfolge:
    print (i)



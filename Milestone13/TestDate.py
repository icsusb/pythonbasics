#bitte ebook seite 179-189 durcharbeiten:
# hierzu bitte das OS MOdul importieren und

# 5. mit der Datefunktion das aktuelle datum anzeigen lassen

from datetime import date
aktuellesDatum = date.today()
print(aktuellesDatum)

# 6. mit der Date-Funktion die aktuelle Urzeit anzeigen lassen

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# 7. diedas Datum und die Urzeit in europäischer und in amerikanischer Schreibweise anzeigen lassen.

from datetime import date
aktuellesDatum = date.today()
print(aktuellesDatum)

from datetime import date
today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)
# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)
# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)



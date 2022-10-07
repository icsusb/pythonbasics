buchstaben = []
print(buchstaben)
buchstaben.append('a')
buchstaben.append('b')
print(buchstaben)


buchstaben1 = ['a', 'b']
print(buchstaben1)
buchstaben1.insert(1, 'c')
print(buchstaben1)


buchstaben2 = ['a', 'b']
print(buchstaben2)
del buchstaben2[0]
print(buchstaben2)

buchstaben3 = ['a', 'b']
print(buchstaben3)
letztereintrag = buchstaben3.pop()
print(buchstaben3)
print("Letzter gelöschter Eintrag: ", letztereintrag)

buchstaben4 = ['a', 'b', 'c']
print(buchstaben4)
buchstaben4.remove('b')
print(buchstaben4)

buchstaben5 = ['a', 'c', 'b']
print(buchstaben5)
buchstaben5_sortiert = sorted(buchstaben5)
print(buchstaben5_sortiert)
buchstaben5_sortiert_absteigend = sorted(buchstaben5, reverse=True)
print(buchstaben5_sortiert_absteigend)

buchstaben6 = ['a', 'c', 'B', 'A']
print(buchstaben6)
# sortiert, Groß-Kleinschreibung wird beachtet
buchstaben6_sortiert_1 = sorted(buchstaben6)
print(buchstaben6_sortiert_1)
# sortiert ohne Rücksicht auf Großbuchstaben
buchstaben6_sortiert_2 = sorted(buchstaben6, key=str.lower)
print(buchstaben6_sortiert_2)
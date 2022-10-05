text = "20"
print(text.zfill(8))


text = "Inhalt länger als 8 Zeichen"
print(text.zfill(8))

text = "Inhalt länger als 8 Zeichen"
print(text.zfill(30))

text = "+123"
print(text.zfill(8))

text = " +123"
print(text.zfill(8))


text = "-123"
print(text.rjust(9,"9"))

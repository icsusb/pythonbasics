


import tkinter as tk
root = tk.Tk()


label1 = tk.Label(root, text="Hallo Welt",fg = '#1FFFF0', bg = '#F0FF1F',font = ('times', 25, 'bold', 'italic'))
label1.pack()
bild1 = tk.PhotoImage(file="biene.png")
label2 = tk.Label(root, image=bild1).pack(side="right")
label3 = tk.Label(root, text="sie macht bzzzzzz")
label3.pack()
label4 = tk.Label(root, text="oder zum")
label4.pack()

root.mainloop()







import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Hallo Welt", bg="orange")
label1.grid(row=0, column=0)
bild1 = tk.PhotoImage(file="biene.png")


label2 = tk.Label(root, text="R1 / C1", bg="lightgreen")
label2.grid(row=1, column=1)

eingabefeld_wert = tk.StringVar()
eingabefeld = tk.Entry(root, textvariable=eingabefeld_wert)
eingabefeld.grid(row=3, column=1)
eingabefeld_wert.set('Hier was eintippen!!!!')

passwdfeld_wert = tk.StringVar()
passwdfeld = tk.Entry(root, textvariable=passwdfeld_wert, show="*")
passwdfeld.grid(row=4, column=3)

label3 = tk.Label(root, image=bild1).grid(row=2, column=1)
label4 = tk.Label(root, text="R3 / C3", bg="lightblue")
label4.grid(row=2, column=2)

root.mainloop()
import tkinter as tk

root = tk.Tk()
label1 = tk.Label(root, text="Hallo Welt", bg = "orange").grid(row=0, column=0)

#def benutzereingabe():
    #alter_wer = tk.StringVar()
    #alter = tk.Entry



def passworteingabe():
    label2 = tk.Label(root, text="R1 / Cl", bg = "lightgreen").grid(row=1, column=1)

    label_name = tk.Label(root, text="Vornane", bg="silver").grid (row=2, column=0)
    eingabefeld_wert = tk.StringVar()
    eingabefeld=tk.Entry(root, textvariable=eingabefeld_wert).grid(row=2, column=1)
    eingabefeld

    label_passwd = tk.Label(root, text="passwort", bg = "orange").grid(row=3, column=0)
    passwdfeld_wert=tk.StringVar()
    passwdfeld = tk.Entry(root, textvariable=passwdfeld_wert, show="*").grid(row=3, column=1)


    schaltf1 = tk.Button(root, text="Aktion durchführen") .grid(row=4, column=1)
    #label3 = tk.Label(root, text="R2 / C2" , bg = "Lightolue").grid(row=4, column=2)
passworteingabe()
root.mainloop()

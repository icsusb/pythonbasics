
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
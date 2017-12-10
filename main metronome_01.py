from tkinter import *

root = Tk()
root["bg"] = "black"

w = Label(root, text="music program")
w.pack()
metrobut = Button()
metrobut["bg"] = 'orange'
metrobut["text"] = "metronome"
metrobut["font"] = ('Helvetica', '80')
metrobut.pack(side="top", ipadx=20, ipady=20, padx=40, pady=40)


tunerbut = Button()
tunerbut["bg"] = 'orange'
tunerbut["text"] = "     tuner     "
tunerbut["font"] = ('Helvetica', '80')
tunerbut.pack(side="top", ipadx=20, ipady=20, padx=40, pady=40)       

root.mainloop()
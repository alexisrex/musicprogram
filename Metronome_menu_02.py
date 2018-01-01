import tkinter as tk

def raise_parent():
    child.lift(aboveThis=root)

def lower_parent():
    child.lower(belowThis=root)

def start_metronome():
    root.geometry("2x2+2+2")
    child.geometry("300x150+120+120")

def music_menu():
    root.geometry("800x550+30+30")
    child.geometry("2x2+2+2")

root = tk.Tk()
root.title('Music Program')
root.geometry("800x550+30+30")
root["bg"] = "black"

metrobut = tk.Button()
metrobut["bg"] = 'orange'
metrobut["text"] = "metronome"
metrobut["font"] = ('Helvetica', '80')
metrobut["command"] = start_metronome
metrobut.pack(side="top", ipadx=20, ipady=20, padx=40, pady=40)

tunerbut = tk.Button()
tunerbut["bg"] = 'orange'
tunerbut["text"] = "     tuner     "
tunerbut["font"] = ('Helvetica', '80')
tunerbut.pack(side="top", ipadx=20, ipady=20, padx=40, pady=40)       

# create a metronome window
child = tk.Toplevel(bg='red')
child.title('Metronome Window')
child.geometry("2x2+2+2")
btn_raise = tk.Button(child, text="Back to menu", command=music_menu)
btn_raise.pack(padx=30, pady=5)

root.mainloop()
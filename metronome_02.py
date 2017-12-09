import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self["bg"] = 'black'
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "metronome"
        self.hi_there["font"] = ('Helvetica', '20')
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top", ipadx=40, ipady=20, padx=80, pady=80)

        self.bpm = tk.Label(self)
        self.bpm["text"] = str(tempo)
        self.bpm["font"] = ('Helvetica', '20')
        self.bpm["bg"] = 'orange'
        self.bpm.pack(side="top", ipadx=40, ipady=20, padx=80, pady=80)
 
        self.fasterbut = tk.Button(self)
        self.fasterbut["text"] = "+"
        self.fasterbut["font"] = ('Helvetica', '40')
        self.fasterbut["command"] = self.faster
        self.fasterbut.pack(side="left", ipadx=40, ipady=20, padx=80, pady=80)
        self.fasterbut["bg"] = 'orange'

        self.slowerbut = tk.Button(self)
        self.slowerbut["text"] = "-"
        self.slowerbut["font"] = ('Helvetica', '40')
        self.slowerbut["command"] = self.slower
        self.slowerbut.pack(side="right", ipadx=40, ipady=20, padx=80, pady=80)
        self.slowerbut["bg"] = 'orange'

        self.quit = tk.Button(self, text="QUIT", fg="Blue",
                              command=root.destroy)
        self.quit.pack(side="bottom", ipadx=80, ipady=80, padx=80, pady=80)
        self.quit["bg"] = 'orange'

    def say_hi(self):
        print("hi there, everyone!")
        
    def faster(self):
        global tempo
        tempo = tempo + 1
        self.bpm.configure(text=tempo)
        print("metronome goes faster " + str(tempo))

    def slower(self):
        global tempo
        tempo = tempo - 1
        self.bpm.configure(text=tempo)
        print("metronome goes slower " + str(tempo))
 
    
        

tempo = 120        
root = tk.Tk()
app = Application(master=root)
app.mainloop()

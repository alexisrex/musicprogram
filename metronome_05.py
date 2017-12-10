
import tkinter as tk
import time

def clack():
    print("\a")

def bpm2s(bpm):
    return ( 1 / (bpm / 60) )

class HiFiTimer:
    """hi fi timer"""

    def __init__(self,interval):
        self.interval = interval
        self.next_beat = time.perf_counter() + interval
        self.tick_counter = 0
        self.polling_window = 0.050

    def wait_next(self):
        self.tick_counter = self.tick_counter + 1
        next_upcoming_beat = self.next_beat + self.interval
        # time.sleep(self.interval-self.polling_window)
        t = time.perf_counter()
        while (t < self.next_beat ):
            t = time.perf_counter()
        self.next_beat = next_upcoming_beat

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self["bg"] = 'black'
        self.pack()
        self.create_widgets()
        global tempo
        global myTimer
        self.bpm.configure(text=tempo)
        # start the clock "ticking"
        self.update_clock()

    def update_clock(self):
        global tempo
        t1 = time.perf_counter()
        myTimer.wait_next()
        t2 = time.perf_counter()
        delta = t2 - t1
        print("t1 = " + str(t1) + ", t2 = " + str(t2))
        print("ideal interval = " + str(bpm2s(tempo)) + ", delta = " + str(delta))
        print("counter = " + str(myTimer.tick_counter))
        aftergap = int(( bpm2s(tempo) - 0.005 ) * 1000)
        print("aftergap = " + str(aftergap))
        self.after(aftergap, self.update_clock)
        

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
        self.bpm.pack(side="top", ipadx=40, ipady=20, padx=80, pady=5)

        self.startbut = tk.Button(self)
        self.startbut["text"] = "Start"
        self.startbut["font"] = ('Helvetica', '40')
        self.startbut["command"] = self.start
        self.startbut.pack(side="right", ipadx=40, ipady=5, padx=10, pady=10)
        self.startbut["bg"] = 'green'

        self.stopbut = tk.Button(self)
        self.stopbut["text"] = "Stop"
        self.stopbut["font"] = ('Helvetica', '40')
        self.stopbut.pack(side="left", ipadx=40, ipady=5, padx=10, pady=10)
        self.stopbut["bg"] = 'green'
       
        self.fasterbut = tk.Button(self)
        self.fasterbut["text"] = "+"
        self.fasterbut["font"] = ('Helvetica', '40')
        self.fasterbut["command"] = self.faster
        self.fasterbut.pack(side="right", ipadx=40, ipady=5, padx=40, pady=80)
        self.fasterbut["bg"] = 'orange'

        self.slowerbut = tk.Button(self)
        self.slowerbut["text"] = "-"
        self.slowerbut["font"] = ('Helvetica', '40')
        self.slowerbut["command"] = self.slower
        self.slowerbut.pack(side="left", ipadx=40, ipady=5, padx=40, pady=80)
        self.slowerbut["bg"] = 'orange'

    def say_hi(self):
        print("metronome working")
        
    def start(self):
        global tempo
        self.bpm.configure(text=tempo)

        myTimer = HiFiTimer(bpm2s(tempo))
        while True:
            t1 = time.perf_counter()
            myTimer.wait_next()
            t2 = time.perf_counter()
            delta = t2 - t1
            print("t1 = " + str(t1) + ", t2 = " + str(t2))
            print("ideal interval = " + str(bpm2s(tempo)) + ", delta = " + str(delta))
            print("counter = " + str(myTimer.tick_counter))


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
myTimer = HiFiTimer(bpm2s(tempo))
root = tk.Tk()
app = Application(master=root)
app.mainloop()

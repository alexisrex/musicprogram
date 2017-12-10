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
        self.beat_counter = 0
        self.internal_sleep_time = 0
        self.polling_counter = 0
        self.polling_duration = 0.010
        self.polling_short_sleep_interval = 0.0005

    def wait_for_next_beat(self):
        self.beat_counter += 1
        current_upcoming_beat = self.next_beat
        next_upcoming_beat = current_upcoming_beat + self.interval
        self.next_beat = next_upcoming_beat
        self.internal_sleep_time = current_upcoming_beat - time.perf_counter() - self.polling_duration 
        if self.internal_sleep_time < 0.005:
            self.polling_duration -= 0.005
        else:
            self.polling_duration += 0.005
            time.sleep(self.internal_sleep_time)
        self.polling_counter = 0
        t = time.perf_counter()
        while (t < current_upcoming_beat ):
            self.polling_counter += 1
            time.sleep(self.polling_short_sleep_interval)
            t = time.perf_counter()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self["bg"] = 'black'
        self.pack()
        self.myTimer_last_tick = 0
        self.create_widgets()
        global tempo
        self.myTimer_isRunning = False
        self.bpm.configure(text=tempo)
        self.myTimer = HiFiTimer(bpm2s(tempo))
         

    def update_clock(self):
        global tempo
        t1 = self.myTimer_last_tick
        self.myTimer.wait_for_next_beat()
        t2 = time.perf_counter()
        clack()
        self.myTimer_last_tick = t2
        real_interval = t2 - t1
        delta = t2 - t1 - bpm2s(tempo)
        print("t1 = " + str(t1) + ", t2 = " + str(t2))
        print("ideal_interval = " + str(bpm2s(tempo)) + ", real_interval = " + str(real_interval) + ", delta = " + str(delta))
        print("beat_counter = " + str(self.myTimer.beat_counter))
        print("internal_sleep_time = " + str(self.myTimer.internal_sleep_time))
        print("polling_counter = " + str(self.myTimer.polling_counter))
        aftergap = int(( bpm2s(tempo) - 0.050 ) * 1000)
        print("aftergap = " + str(aftergap))
        if self.myTimer_isRunning == True:
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
        self.stopbut["command"] = self.stop
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
        self.myTimer_isRunning = True
        self.update_clock()

    def stop(self):
        self.myTimer_isRunning = False
        self.update_clock()

    def faster(self):
        global tempo
        tempo = tempo + 1
        self.bpm.configure(text=tempo)
        self.myTimer.interval = bpm2s(tempo) 
        print("metronome goes faster " + str(tempo))

    def slower(self):
        global tempo
        tempo = tempo - 1
        self.bpm.configure(text=tempo)
        self.myTimer.interval = bpm2s(tempo) 
        print("metronome goes slower " + str(tempo))
        
tempo = 60
root = tk.Tk()
app = Application(master=root)
app.mainloop()
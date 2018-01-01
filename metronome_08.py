import tkinter as tk
import time

def clack():
    print(".", end='', flush=True)
    #print("clack!")

def bpm2s(bpm):
    return ( 1 / (bpm / 60) )

class Ticker:
    """Ticker Class"""

    def __init__(self,interval):
        self.isRunning = False
        self.interval = interval
        self.next_beat = 0
        self.beat_counter = 0
        self.internal_sleep_time = 0
        self.polling_counter = 0
        self.polling_duration = 0.010
        self.polling_duration_delta = 0.005
        self.polling_short_sleep_interval = 0.001
        self.reset()

    def reset(self):
        self.next_beat = time.perf_counter() + self.interval

    def set_interval_sec(self,interval_sec):
        self.interval = interval_sec

    def set_interval_bpm(self,interval_bpm):
        self.interval = ( 1 / (interval_bpm / 60) )

    def wait_for_next_beat(self):
        self.beat_counter += 1
        current = self.next_beat
        self.next_beat  = current + self.interval
        self.internal_sleep_time = current - time.perf_counter() - self.polling_duration 
        if self.internal_sleep_time < self.polling_duration_delta:
            self.polling_duration -= self.polling_duration_delta
        else:
            self.polling_duration += self.polling_duration_delta
            time.sleep(self.internal_sleep_time)
        self.polling_counter = 0
        t = time.perf_counter()
        while (t < current):
            self.polling_counter += 1
            time.sleep(self.polling_short_sleep_interval)
            t = time.perf_counter()

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.main_menu_create_widgets()
        ##self.bpm.configure(text=tempo)

    def open_metronome(self):
        self["bg"] = 'black'
        self.pack()
        global tempo
        self.myTicker = Ticker(bpm2s(tempo))
        self.metronome_create_widgets()
        self.bpm.configure(text=tempo)

    def update_clock(self):
        global tempo
        global debug
        global last_tick_external
        t1 = last_tick_external
        self.myTicker.wait_for_next_beat()
        t2 = time.perf_counter()
        clack()
        last_tick_external = t2
        aftergap = int(( bpm2s(tempo) - 0.050 ) * 1000)
        if debug == True:
            real_interval = t2 - t1
            jitter = real_interval - bpm2s(tempo)
            print("beat_counter = " + str(self.myTicker.beat_counter))
            print("t1 = " + str(t1) + ", t2 = " + str(t2))
            print("ideal_interval = " + str(bpm2s(tempo)) + ", real_interval = " + str(real_interval))
            print("jitter = " + str(jitter))
            print("internal_sleep_time = " + str(self.myTicker.internal_sleep_time))
            print("polling_counter = " + str(self.myTicker.polling_counter))
            print("aftergap = " + str(aftergap))
        if self.myTicker.isRunning == True:
            self.after(aftergap, self.update_clock)

    def main_menu_create_widgets(self):    
        ##self.title('Music Program')
        ##self.geometry("800x550+30+30")
        ##self["bg"] = "black"

        self.metrobut = tk.Button()
        self.metrobut["bg"] = 'orange'
        self.metrobut["text"] = "metronome"
        self.metrobut["font"] = ('Helvetica', '80')
        self.metrobut["command"] = self.open_metronome
        self.metrobut.pack(side="top", ipadx=20, ipady=20, padx=40, pady=40)

        self.tunerbut = tk.Button()
        self.tunerbut["bg"] = 'orange'
        self.tunerbut["text"] = "     tuner     "
        self.tunerbut["font"] = ('Helvetica', '80')
        self.tunerbut.pack(side="top", ipadx=20, ipady=20, padx=40, pady=40)  

    def metronome_create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "metronome"
        self.hi_there["font"] = ('Helvetica', '20')
        self.hi_there["command"] = self.say_hi
        self.hi_there["bg"] = 'orange'
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
        if self.myTicker.isRunning == False:
            self.myTicker.isRunning = True
            self.myTicker.reset()
            self.update_clock()

    def stop(self):
        self.myTicker.isRunning = False
        self.myTicker.reset()


    def faster(self):
        global tempo
        tempo = tempo + 1
        self.bpm.configure(text=tempo)
        self.myTicker.set_interval_bpm(tempo)
        print("metronome goes faster " + str(tempo))

    def slower(self):
        global tempo
        tempo = tempo - 1
        self.bpm.configure(text=tempo)
        self.myTicker.set_interval_bpm(tempo)
        print("metronome goes slower " + str(tempo))
        
tempo = 60
debug = False
last_tick_external = 0
root = tk.Tk()
app = Application(master=root)
app.mainloop()

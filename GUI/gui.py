import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()

def print_input(*args):
    for entry in entries:
        print(entry.get())

def calculate_clockout_time():
    # get variables
    return clockout_time

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entries = [Entry(root) for _ in range(3)]
for entry in entries:
    entry.pack()


button1 = tk.Button(text='Get clockout time', command=calculate_clockout_time)

class window( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("clockout")
        self.button1 = Button( self, text = "CLICK HERE", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
        self.btn = Button(self, text="Print", command=print_input)
    def new_window(self):
        self.newWindow = karl2()
class karl2(Frame):     
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("karlos More Window")
        new.button = tk.Button(  text = "PRESS TO CLOSE", width = 25,
                                 command = self.close_window )
        new.button.pack()
    def close_window(self):
        self.destroy()
def main(): 
    window().mainloop()
if __name__ == '__main__':
    main()
# from tkinter import *


# root = Tk()

# root.title('Career ChatBot Version 0.0.3')

# root.geometry('500x500')

# root.mainloop()

import tkinter as Tkinter
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


#create main window
master = Tkinter.Tk()
master.title("tester")
master.geometry("300x100")


#make a label for the window
label1 = Tkinter.Label(master, text='Hellooooo')
# Lay out label
label1.pack()

# Run forever!
master.mainloop()
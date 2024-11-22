import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

#STARTUP: 
root = tk.Tk()
root.configure(background= 'black')
root.geometry('600x400')
root.resizable(False,False)
root.title("The Mist")

mainpanel = tk.Frame(root, width=600, height=400)
mainpanel.configure(background= 'black')
mainpanel.pack()


welcomemsg = Label(mainpanel, text = "Welcome to the mist!", font = "70", fg = 'white', bg = "black")
welcomemsg.pack(
   ipady = 3,
)

class exitbutton:

    def end_program():
        msg = tk.Tk()
        msg.configure(background = 'black')
        msg.geometry('600x400')
        msg.resizable(False,False)
        msg.title("goodbye")
        msgchance = random.randint(1, 5)

        #Determines what goodbye message displays
        if msgchance == 1:
            goodbye = Label(msg, text = "Until next time, Traveler...", font = 500, fg = 'white', bg = 'black')
            goodbye.pack()
        elif msgchance == 2:
            goodbye = Label(msg, text = "Farewell, Traveler", font = 500, fg = 'white', bg = 'black')
            goodbye.pack()
        elif msgchance == 3:
            goodbye = Label(msg, text = "I'm sure we'll meet again...", font = 500, fg = 'white', bg = 'black')
            goodbye.pack()
        elif msgchance == 4:
            goodbye = Label(msg, text = "Take it easy, traveler", font = 500, fg = 'white', bg = 'black')
            goodbye.pack()
        else:
            goodbye = Label(msg, text = "Godspeed, Traveller", font = 500, fg = 'white', bg = 'black')
            goodbye.pack()

        root.after(1500, root.quit)
    #Exit directions
    exitdir = Label(mainpanel, text = "or press exit to close", font = "30", fg = 'white', bg = "black")
    exitdir.pack(
    ipady = 3,
    )
    #exit button
    exit_button = ttk.Button(
        mainpanel,
        text = "Exit",
        command = end_program
    )
    exit_button.pack()

class startgame:
    def startgame():
        
        for widget in mainpanel.winfo_children():
            widget.destroy()
        
        
        intro = Label(root, text = "'You awake to a feminine voice calling your name. Opening your eyes you see..", font = "70", fg = 'white', bg = "black")
        intro.pack(ipady = 10)

    
    start_button = ttk.Button(
        mainpanel,
        text = "Start",
        command = startgame
    )
    start_button.pack()

root.mainloop()
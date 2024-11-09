# Rachel Shaw - 11/8/2024 - 4.2 assignment
# The purpose of this program is to display the high and low temperatures in 2018 using matplotlib

#Changes made to original program:
# Used tkinter to create a simple GUI
# added buttons that allow user to select which figure they would like to view and to exit the program
# Added a message that thanks the user when they click the "exit" button
# Made the low temperatures figure blue

import csv
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.widgets import Button

# open 2018 weather file
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temperatures, and low temperature from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

# Displays low temperatures plot
def show_lows():
 fig, ax = plt.subplots()
 ax.plot(dates, lows, c='blue')
 plt.title("Daily low temperatures - 2018", fontsize=24)
 plt.xlabel('', fontsize=16)
 fig.autofmt_xdate()
 plt.ylabel("Temperature (F)", fontsize=16)
 plt.tick_params(axis='both', which='major', labelsize=16)
 plt.show()

#Displays high temperatures plot
def show_highs():
 fig, ax = plt.subplots()
 ax.plot(dates, highs, c='red')
 plt.title("Daily high temperatures - 2018", fontsize=24)
 plt.xlabel('', fontsize=16)
 fig.autofmt_xdate()
 plt.ylabel("Temperature (F)", fontsize=16)
 plt.tick_params(axis='both', which='major', labelsize=16)
 plt.show()

# Closes program with a message
def end_program():
    msg = tk.Tk()
    msg.geometry('600x400')
    msg.resizable(False,False)
    msg.title("goodbye")
    goodbye = Label(msg, text = "Thank you for using sitka_highs.py!", font = 500)
    goodbye.pack()
    plt.close()
    plt.close()
    root.after(1000, root.quit)



#Tkinter main window configuration
root = tk.Tk()
root.geometry('600x400')
root.resizable(False,False)
root.title("temperatures")
welcomemsg = Label(root, text = "Welcome to sitka_highs.py!", font = "70")
welcomemsg.pack(
   ipady = 3,
)
directions = Label(root, text = "To use this program, please select which temperatures you would like to view", font = "30")
directions.pack(
   ipady = 3,
)
exitbutton = Label(root, text = "or press exit to close", font = "30")
exitbutton.pack(
   ipady = 3,
)


# Button for low tempurature
low_button = ttk.Button(
    root,
    text= 'Low Tempuratures',
    command = show_lows
)
low_button.pack()

# button for high tempurature
high_button = ttk.Button(
    root,
    text= 'High Temperatures',
    command = show_highs
)
high_button.pack()

# Exit button
exit_button = ttk.Button(
    root,
    text = "Exit",
    command = end_program
)
exit_button.pack()


root.mainloop()

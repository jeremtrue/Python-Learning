import tkinter as tk
import random

def roll():
    dice = int(entry.get())  # Get the user's input from the Entry widget
    result = random.randint(1, dice)
    result_label.config(text=f'You rolled a D{dice} and got a {result}')

root = tk.Tk()
root.title("Dice Roll")

instructions_label = tk.Label(root, text="Enter the dice without the 'D'")
instructions_label.pack()

custom_font = ('Helvetica', 12)  # Adjust the size (12) as needed
entry = tk.Entry(root, font=custom_font, width=10)
entry.pack()

roll_button = tk.Button(root, text="Roll", command=roll)
roll_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

import tkinter as tk # traditional look
from tkinter import ttk # modern look

# Create the application window
window = tk.Tk()

def another():
    print(entry.get())

entry = tk.Entry(window)
entry.pack()
entry.bind('<Return>', another)

window.mainloop()
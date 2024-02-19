import tkinter as tk
from tkinter import ttk

window = tk.Tk()

first_row_frame = ttk.Frame(window)
first_row_frame.pack()

billText = ttk.Label(first_row_frame, text='Bill Due:')
billText.pack(side='left')

billEntry = ttk.Entry(window)
billEntry.pack()



second_row_frame = ttk.Frame(window)
second_row_frame.pack()

tip0 = ttk.Button(second_row_frame, text='0%')
tip0.pack(side='left')

tip15 = tk.Button(second_row_frame, text='15%')
tip15.pack(side='left')

tip20 = tk.Button(second_row_frame, text='20%')
tip20.pack(side='left')

tip25 = tk.Button(second_row_frame, text='25%')
tip25.pack(side='left')



third_row_frame = ttk.Frame(window)
third_row_frame.pack()
total = ttk.Label(third_row_frame, text='Bill Total:')
total.pack(side='left')


window.mainloop()
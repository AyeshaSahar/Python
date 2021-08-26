import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# Root window
root = tk.Tk()
root.title('Temperature Converter')
root.geometry('300x150')
root.resizable(False, False)

# Main function for conversion
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Main frame
frame = ttk.Frame(root)


# Field options
options = {'padx': 5, 'pady': 5}

# Temperature label
temperature_label = ttk.Label(frame, text='Fahrenheit')
temperature_label.grid(column=0, row=0, sticky='W', **options)

# Enter value to convert
temperature = tk.StringVar()
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()

# Convert button
def convert_button_clicked():
    try:
        f = float(temperature.get())
        c = fahrenheit_to_celsius(f)
        result = f'{f} Fahrenheit = {c:.2f} Celsius'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)

convert_button = ttk.Button(frame, text='Convert')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)

# Quit Button
quit_button = ttk.Button(frame, text='Quit')
quit_button.grid(column=2, row=3)
quit_button.configure(command = root.destroy) #command = root.destroy is used for quitting the app

# Result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

# Add padding to the frame and show it
frame.grid(padx=10, pady=10)

# Starting the app
root.mainloop()
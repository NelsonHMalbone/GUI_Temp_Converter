import tkinter as tk
from tkinter import ttk

def main():
    main_window = tk.Tk()
    main_window.geometry('300x200')
    main_window.title("Temperature Unit Conversion")

    # options for user to choose from for conversation
    options = ['Celsius to Fahrenheit', 'Fahrenheit to Celsius']
    combo_box_label = tk.Label(main_window, text="Choose a Conversion Option")
    combo_box_options = ttk.Combobox(main_window, values=options)
    combo_box_label.pack()
    combo_box_options.pack()

    # where the user inputs the Temperature
    user_input_label = tk.Label(main_window, text="Value to Convert: ")
    user_input_entry = tk.Entry(main_window)
    user_input_label.pack()
    user_input_entry.pack()


    main_window.mainloop()


if __name__ == "__main__":
    main()
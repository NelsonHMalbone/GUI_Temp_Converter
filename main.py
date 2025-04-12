import tkinter as tk
from tkinter import ttk

def main():
    main_window = tk.Tk()
    main_window.geometry('300x200')
    main_window.title("Temperature Unit Conversion")

    # where the user inputs the Temperature
    user_input_label = tk.Label(main_window, text="Value to Convert: ")
    user_input_label.pack()
    user_input_entry = tk.Entry(main_window)
    user_input_entry.pack()


    main_window.mainloop()


if __name__ == "__main__":
    main()
# 03-29-2025
# Tkinter Temperature Convertor
import tkinter as tk
from tkinter import ttk

def main():

    # combo box function section
    def combo_box_option(event):
        # value to be selected
        select_option = combo.get()

    # functions for the formulas of the temperature Convertors
    def Celsius_to_Fahrenheit():
        pass

    def Fahrenheit_to_Celsius():
         pass

    def Celsius_to_Kelvin():
         pass

    def Kelvin_to_Celsius():
        pass



    # this is the main window system
    main_window = tk.Tk()
    main_window.title("Temperature Gui Converter")
    main_window.geometry("400x400")
    # options here
    options = ['Celsius_to_Fahrenheit', 'Fahrenheit_to_Celsius', 'Celsius_to_Kelvin', 'Kelvin_to_Celsius']
    # combo box
    combo_box_label = tk.Label(main_window, text='Select conversion here')
    combo_box_label.pack()
    combo = ttk.Combobox(main_window, values=options)
    combo.pack()
    # entry label and box
    entry_Label = tk.Label(main_window, text='Enter a Number Here: ')
    entry_Label.pack()
    # entry box
    entry_box = tk.Entry(main_window)
    entry_box.pack()
    # button
    button = tk.Button(main_window, text="Enter", )
    button.pack()
    main_window.mainloop()

main()
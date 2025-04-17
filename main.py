import tkinter as tk
from tkinter import ttk

def main():

    # function to take input and show result of conversion
    def entry_conversion(event):
        conversion_input = float(user_input_entry.get())
        conversion = combo_box_options.get()
        print(f"Selected value: {conversion_input}")
        match conversion:
            case 'Celsius to Fahrenheit':
                result_formula = (conversion_input * 9 / 5) + 32
                result_formula_statement = f"{conversion_input}ºC = {result_formula:.2f}ºF"
                print(result_formula_statement)
            case 'Fahrenheit to Celsius':
                result_formula = (conversion_input - 32) * 5 / 9
                result_formula_statement = f"{conversion_input}ºC = {result_formula:.2f}ºF"
                print(result_formula_statement)
            case 'Celsius to Kelvin':
                result_formula = conversion_input + 273.15
                result_formula_statement = f"{conversion_input}ºC = {result_formula}K"
                print(result_formula_statement)
            case 'Kelvin to Celsius':
                result_formula = conversion_input - 273.15
                result_formula_statement = f"{conversion_input}K = {result_formula}ºC"
                print(result_formula_statement)



    main_window = tk.Tk()
    main_window.geometry('300x200')
    main_window.title("Temperature Unit Conversion")

    # options for user to choose from for conversation
    options = ['Celsius to Fahrenheit', 'Fahrenheit to Celsius', 'Celsius to Kelvin', 'Kelvin to Celsius']
    combo_box_label = tk.Label(main_window, text="Choose a Conversion Option")
    combo_box_options = ttk.Combobox(main_window, values=options)
    combo_box_label.pack()
    combo_box_options.pack()

    # where the user inputs the Temperature
    user_input_label = tk.Label(main_window, text="Value to Convert: ")
    user_input_entry = tk.Entry(main_window)
    user_input_label.pack()
    user_input_entry.pack()
    user_input_entry.bind("<Return>", entry_conversion)


    main_window.mainloop()


if __name__ == "__main__":
    main()
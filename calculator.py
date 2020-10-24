'''calculator.py - Simple Calculator that can do basic arithmetic'''

import tkinter as tk

def layout_grid():
    ''' Creates grid and buttons to be used in the program and returns
        a dictonary containing all buttons for future minipulation      '''

    #Defines grid weights which is a 4x5 evenly weighted grid
    for index in range(5):
        root.rowconfigure(index, weight=1)
    for index in range(4):
        root.columnconfigure(index, weight=1)   

    #Create Text Box
    entry_box = tk.Entry(root, width=50, borderwidth=5)
    entry_box.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="NESW")

    #button dictinary
    buttons = {}

    #Add number buttons to dict
    numbers = list(range(10))
    for row in range(1,5):
        for column in range(2,-1,-1):
            buttons[numbers[-1]] = tk.Button(root, text=str(numbers[-1]))
            buttons[numbers.pop()].grid(row=row,
                column=(0 if row == 4 else column),
                ipadx=40, ipady=20, padx=1, pady=1, sticky="NESW")
            if row == 4:
                break

    #Add clear button to dict
    buttons["clear"] = tk.Button(root, text="Clear")
    buttons["clear"].grid(row=4, column=1, columnspan=2,
        ipadx=80, ipady=20, padx=1, pady=1, sticky="NESW")

    #Add arithmetic buttons
    buttons["+"] = tk.Button(root, text="+")
    buttons["+"].grid(
        row=1, column=3, ipadx=40, ipady=20, padx=1, pady=1, sticky="NESW")
    buttons["-"] = tk.Button(root, text="-")
    buttons["-"].grid(
        row=2, column=3, ipadx=40, ipady=20, padx=1, pady=1, sticky="NESW")
    buttons["/"] = tk.Button(root, text="/")
    buttons["/"].grid(
        row=3, column=3, ipadx=40, ipady=20, padx=1, pady=1, sticky="NESW")
    buttons["="] = tk.Button(root, text="=")
    buttons["="].grid(
        row=4, column=3, ipadx=40, ipady=20, padx=1, pady=1, sticky="NESW")

    #return button dictionary
    return buttons

#Create window
root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

#Create buttons and grid system
button_dict = layout_grid()

#Create loop for GUI
root.mainloop()
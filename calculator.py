'''calculator.py - Simple Calculator that can do basic arithmetic'''

import tkinter as tk
import tkinter.font as tkfont
import sys

def layout_grid():
    ''' Creates grid and buttons to be used in the program and returns
        a dictonary containing all buttons for future minipulation      '''

    #Defines grid weights which is a 4x5 evenly weighted grid
    for index in range(5):
        root.rowconfigure(index, weight=1)
    for index in range(4):
        root.columnconfigure(index, weight=1)   

    #Declare dictinary for grid items
    grid_items = {}

    #Create Text Box
    entry_box = tk.Entry(root, width=50, borderwidth=5, justify='right',
        state='disabled', font=tkfont.Font(size=18,weight='bold'))
    entry_box.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="NESW")
    
    #Add entry box to grid items
    grid_items['entry_box'] = entry_box

    #button dictinary
    buttons = {}

    #Cool but convoluted way to declare number buttons
    # #Add number buttons to dict
    # numbers = list(range(10))
    # for row in range(1,5):
    #     for column in range(2,-1,-1):
    #         buttons[numbers[-1]] = tk.Button(root, text=str(numbers[-1]))
    #         buttons[numbers.pop()].grid(row=row,
    #             column=(0 if row == 4 else column),
    #             ipadx=40, ipady=20, padx=1, pady=1, sticky="NESW")
    #         if row == 4:
    #             break
    
    #Add number buttons
    buttons['0'] = tk.Button(root, text="0",
        command= lambda: input_button('0', entry_box))
    buttons['1'] = tk.Button(root, text="1",
        command= lambda: input_button('1', entry_box))
    buttons['2'] = tk.Button(root, text="2",
        command= lambda: input_button('2', entry_box))
    buttons['3'] = tk.Button(root, text="3",
        command= lambda: input_button('3', entry_box))
    buttons['4'] = tk.Button(root, text="4",
        command= lambda: input_button('4', entry_box))
    buttons['5'] = tk.Button(root, text="5",
        command= lambda: input_button('5', entry_box))
    buttons['6'] = tk.Button(root, text="6",
        command= lambda: input_button('6', entry_box))
    buttons['7'] = tk.Button(root, text="7",
        command= lambda: input_button('7', entry_box))
    buttons['8'] = tk.Button(root, text="8",
        command= lambda: input_button('8', entry_box))
    buttons['9'] = tk.Button(root, text="9",
        command= lambda: input_button('9', entry_box))

    #Add clear button to dict
    buttons["clear"] = tk.Button(root, text="Clear",
        command= lambda: delete_entry(entry_box))

    #Add arithmetic buttons
    buttons["+"] = tk.Button(root, text="+",
        command= lambda: input_button('+', entry_box))
    buttons["-"] = tk.Button(root, text="-",
        command= lambda: input_button('-', entry_box))
    buttons["/"] = tk.Button(root, text="/",
        command= lambda: input_button('/', entry_box))
    buttons["="] = tk.Button(root, text="=",
        command= lambda: None)

    ##Declare button properties##
    #Numbers
    buttons["0"].grid(row=1,column=0, ipadx=40, ipady=20,
        padx=1, pady=1, sticky="NESW")
    buttons["1"].grid(row=1,column=1, ipadx=40, ipady=20,
        padx=1, pady=1, sticky="NESW")
    buttons["2"].grid(row=1,column=2, ipadx=40, ipady=20,
        padx=1, pady=1, sticky="NESW")
    buttons["3"].grid(row=2,column=0, ipadx=40, ipady=20,
        padx=1, pady=1, sticky="NESW")
    buttons["4"].grid(row=2,column=1, ipadx=40, ipady=20,
        padx=1, pady=1, sticky="NESW")
    buttons["5"].grid(row=2,column=2, ipadx=40, ipady=20,
        padx=1, pady=1, sticky="NESW")
    buttons["6"].grid(row=3,column=0, ipadx=40, ipady=20,
        padx=1, pady=1, sticky="NESW")
    buttons["7"].grid(row=3,column=1, ipadx=40, ipady=20,
        padx=1, pady=1, sticky="NESW")
    buttons["8"].grid(row=3,column=2, ipadx=40, ipady=20,
        padx=1, pady=1, sticky="NESW")
    buttons["9"].grid(row=4,column=0, ipadx=40, ipady=20,
        padx=1, pady=1, sticky="NESW")
    #Controls
    buttons["clear"].grid(row=4, column=1, columnspan=2, ipadx=80, ipady=20,
        padx=1, pady=1, sticky="NESW")
    buttons["+"].grid(
        row=1, column=3, ipadx=40, ipady=20, padx=1, pady=1, sticky="NESW")
    buttons["-"].grid(
        row=2, column=3, ipadx=40, ipady=20, padx=1, pady=1, sticky="NESW")
    buttons["="].grid(
        row=4, column=3, ipadx=40, ipady=20, padx=1, pady=1, sticky="NESW")
    buttons["/"].grid(
        row=3, column=3, ipadx=40, ipady=20, padx=1, pady=1, sticky="NESW")
    
    #Sets the font size of all buttons
    for button in buttons.values():
        button['font'] = tkfont.Font(size=12)
    
    #Add buttons to grid dict
    grid_items['buttons'] = buttons

    return grid_items

def input_button(string, entry):
    '''Inputs a string into an entry box'''
    entry['state'] = 'normal'   #Set to a normal state so edits can be made
    entry.insert(tk.END,string) #Insert string at the end of the entry text
    entry['state'] = 'disabled' #Lock the entry box again

def delete_entry(entry):
    '''Deletes all text in a entry box'''
    entry['state'] = 'normal'   #Set to a normal state so edits can be made
    entry.delete(0, tk.END)     #Delete all text in entry
    entry['state'] = 'disabled' #Lock the entry box again

#Create window
root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

#Make window not resizable
root.resizable(width=0, height=0)

#Create buttons and grid system
grid_dict = layout_grid()

#Create loop for GUI
while True:
    try:
        root.update_idletasks()
        root.update()
    except tk.TclError:
        print(f'Window was closed')
        sys.exit()
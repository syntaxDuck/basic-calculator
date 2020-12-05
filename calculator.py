'''calculator.py - Simple Calculator that can do basic arithmetic'''

import tkinter as tk
import tkinter.font as tkfont
import os
import re

class DefaultButton:
    '''This class simply has default values for the buttons to be used'''
    def __init__(self, row, col, text, root):
        '''Initalizes the object'''
        self.button = tk.Button(root, text=text,
            font=tkfont.Font(size=12,weight='bold'))
        self.button.grid(row=row,column=col, ipadx=40, ipady=20,
            padx=1, pady=1, sticky="NESW")

class CalculatorEntry:
    '''Class to define the calculator entry window'''
    def __init__(self, row, col, root):
        self.answer_flag = 0
        self.entry = tk.Entry(root, width=50, borderwidth=0, justify='right',
            state='disabled', font=tkfont.Font(size=18,weight='bold'),
            disabledbackground='black', disabledforeground='white')
        self.entry.grid(row=row, column=col, columnspan=5,
            padx=5, pady=5, sticky="NESW")

    def input(self, string):
        '''Inputs a string into an entry box'''
        if self.answer_flag:
            if string.isdigit():
                self.delete_all()
            self.answer_flag = 0
        
        self.entry['state'] = 'normal'   #Unlock Entry
        self.entry.insert(tk.END,string) #Insert string at the end of text
        self.entry['state'] = 'disabled' #Locks
    
    def delete_all(self):
        '''Deletes all text in a entry box'''
        self.entry['state'] = 'normal'       #Unlocks Entry
        self.entry.delete(tk.ANCHOR, tk.END) #Delete all text in entry
        self.entry['state'] = 'disabled'     #Locks Entry

    def compile_expression(self):
        ''' Compiles the inputed string and determins
            what operations need to happen'''
        expression = self.entry.get()
        values = re.split(r'\+|-|/|\*', expression)
        values = [int(num) for num in values]
        operators = re.findall(r'\+|-|\*|/', expression)

        while len(values) > 1:
            if operators[0] == '+':
                num1 = values[0]
                num2 = values.pop(1)
                values[0] = num1 + num2
            elif operators[0] == '-':
                num1 = values[0]
                num2 = values.pop(1)
                values[0] = num1 - num2
            elif operators[0] == '*':
                num1 = values[0]
                num2 = values.pop(1)
                values[0] = num1 * num2
            elif operators[0] == '/':
                num1 = values[0]
                num2 = values.pop(1)
                values[0] = num1 / num2
            
            operators.pop(0)
        
        if isinstance(values[0], float):
            result = "{:.4f}".format(values[0])
        else:
            result = str(values[0])

        self.delete_all()
        self.input(result)
        self.answer_flag = 1

def layout_grid(root):
    ''' Creates grid and buttons to be used in the program and returns
        a dictonary containing all buttons for future minipulation      '''

    #Defines grid weights which is a 4x5 evenly weighted grid
    for index in range(5):
        root.rowconfigure(index, weight=1)
    for index in range(4):
        root.columnconfigure(index, weight=1)  

    #Create Text Box
    calc_window = CalculatorEntry(row=0, col=0, root=root)
    
    
    #Dictinary for all buttons
    buttons = {}

    #Number Buttons
    buttons['0'] = DefaultButton(row=4, col=0, text='0', root=root)
    buttons['0'].button['command'] = lambda: calc_window.input('0')
    buttons['1'] = DefaultButton(row=3, col=0, text='1', root=root)
    buttons['1'].button['command'] = lambda: calc_window.input('1')
    buttons['2'] = DefaultButton(row=3, col=1, text='2', root=root)
    buttons['2'].button['command'] = lambda: calc_window.input('2')
    buttons['3'] = DefaultButton(row=3, col=2, text='3', root=root)
    buttons['3'].button['command'] = lambda: calc_window.input('3')
    buttons['4'] = DefaultButton(row=2, col=0, text='4', root=root)
    buttons['4'].button['command'] = lambda: calc_window.input('4')
    buttons['5'] = DefaultButton(row=2, col=1, text='5', root=root)
    buttons['5'].button['command'] = lambda: calc_window.input('5')
    buttons['6'] = DefaultButton(row=2, col=2, text='6', root=root)
    buttons['6'].button['command'] = lambda: calc_window.input('6')
    buttons['7'] = DefaultButton(row=1, col=0, text='7', root=root)
    buttons['7'].button['command'] = lambda: calc_window.input('7')
    buttons['8'] = DefaultButton(row=1, col=1, text='8', root=root)
    buttons['8'].button['command'] = lambda: calc_window.input('8')
    buttons['9'] = DefaultButton(row=1, col=2, text='9', root=root)
    buttons['9'].button['command'] = lambda: calc_window.input('9')

    #Arithmatic Buttons
    buttons['+'] = DefaultButton(row=1, col=3, text='+', root=root)
    buttons['+'].button['bg'] = 'orange'
    buttons['+'].button['command'] = lambda: calc_window.input('+')

    buttons['-'] = DefaultButton(row=2, col=3, text='-', root=root)
    buttons['-'].button['bg'] = 'orange'
    buttons['-'].button['command'] = lambda: calc_window.input('-')

    buttons['*'] = DefaultButton(row=3, col=3, text='*', root=root)
    buttons['*'].button['bg'] = 'orange'
    buttons['*'].button['command'] = lambda: calc_window.input('*')

    buttons['/'] = DefaultButton(row=4, col=3, text='/', root=root)
    buttons['/'].button['bg'] = 'orange'
    buttons['/'].button['command'] = lambda: calc_window.input('/')

    buttons['='] = DefaultButton(row=4, col=2, text='=', root=root)
    buttons['='].button['bg'] = 'orange'
    buttons['='].button['command'] = calc_window.compile_expression

    #Clear Buttons
    buttons['clear'] = DefaultButton(row=4, col=1, text='clear', root=root)
    buttons['clear'].button['command'] = calc_window.delete_all
    buttons['clear'].button.grid(ipadx=0, ipady=0)


#Create window
window = tk.Tk()
window.iconbitmap('D:\Dev\Python\Calculator\icon.ico')
window.geometry("300x400")
window.title("Calculator")
window.configure(bg='black')

#Make window not resizable
window.resizable(width=0, height=0)

layout_grid(window)

#Create loop for GUI
while True:
    try:
        window.update_idletasks()
        window.update()
    except tk.TclError:
        os._exit(1)
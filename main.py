import tkinter as tk
from tkinter import ttk
import re

functions = {"clear":"C", "delete":"Del", "e":"e",
         "pi":"π", "openedbracket":"(", "closedbracket":")",
         "divide":"÷", "trig_menu":"Trig", "multiply":"×",
         "subtract":"-", "exp_menu":"Exp", "add":"+",
         "plusminus":"+/-", "decimal":".", "equals":"=",
         "number":None}


class Button:
    def __init__(self, function, row, col, CALCFUNC=None, rowspan=1, colspan=1, label=None):
        self.function = function
        self.row = row
        self.col = col
        self.rowspan = rowspan
        self.colspan = colspan
        self.CALCFUNC = CALCFUNC
        self.label = label

        if self.label != None:
            self.text = self.label
        else:
            self.text = functions[function]

    def draw_button(self):
        btn = ttk.Button(text=self.text, command=self.register_press)
        btn.grid(row=self.row, column=self.col, rowspan=self.rowspan, columnspan=self.colspan, sticky="nsew")

    def register_press(self):
        self.CALCFUNC.send_to_CALCFUNC(self.function, self.label)


class CalculatorGUI(tk.Tk):
    def __init__(self, CALCFUNC):
        super().__init__()
        self.CALCFUNC = CALCFUNC

        self.geometry("300x450")
        self.resizable(False, False)
        self.title("Calculator")
        self.wm_iconphoto(False, tk.PhotoImage(file="icon.png"))

        self.setup_grid()

        self.output_formatted = ""
        self.output_label = ttk.Label(text=self.output_formatted, font=("Arial", 20))
        self.output_label.grid(row=0, rowspan=2, columnspan=5, sticky="nsew")

        self.setup_buttons()

    def setup_grid(self):
        for row in range(8):
            self.rowconfigure(row, weight=1)
        for column in range(5):
            self.columnconfigure(column, weight=1)

    def setup_buttons(self):
        buttons = [
            Button("clear", 2, 3),
            Button("delete", 2, 4),
            Button("e", 3, 0),
            Button("pi", 3, 1),
            Button("openedbracket", 3, 2),
            Button("closedbracket", 3, 3),
            Button("divide", 3, 4),
            Button("trig_menu", 4, 0, rowspan=2),
            Button("number", 4, 1, label=7),
            Button("number", 4, 2, label=8),
            Button("number", 4, 3, label=9),
            Button("multiply", 4, 4),
            Button("number", 5, 1, label=4),
            Button("number", 5, 2, label=5),
            Button("number", 5, 3, label=6),
            Button("subtract", 5, 4),
            Button("exp_menu", 6, 0, rowspan=2),
            Button("number", 6, 1, label=1),
            Button("number", 6, 2, label=2),
            Button("number", 6, 3, label=3),
            Button("add", 6, 4),
            Button("plusminus", 7, 1),
            Button("number", 7, 2, label=0),
            Button("decimal", 7, 3),
            Button("equals", 7, 4)
        ]
        for button in buttons:
            button.draw_button()
            button.CALCFUNC = self.CALCFUNC

    def update_output_label(self):
        self.output_label.configure(text=self.output_formatted)


class CalculatorFUNC:
    def __init__(self):
        self.output_raw = []
        self.output_eval = ""
        self.CALCGUI = None

    def evaluate(self):
        pass # SymPy stuff

    def raw_to_formatted(self):
        output = ""
        for elem in self.output_raw:
            if elem in range(0,10): # Is number?
                output += str(elem)
            else:
                output += functions[elem]
        return output

    def send_to_CALCFUNC(self, function, label):
        if function == "number":
            self.output_raw.append(label) # Write number
        elif function:
            if function == "clear":
                self.output_raw = [] # C button
            elif function == "delete":
                self.output_raw = self.output_raw[:-1] # Del button
            elif function == "trig_menu":
                pass # Open trig menu
            elif function == "exp_menu":
                pass # Open exp menu
            else:
                self.output_raw.append(function) # Other buttons

        self.CALCGUI.output_formatted = self.raw_to_formatted()
        self.CALCGUI.update_output_label()
        print(self.output_raw) # DEBUG


if __name__ == "__main__":
    calcFUNC = CalculatorFUNC()
    calcGUI = CalculatorGUI(calcFUNC)
    calcFUNC.CALCGUI = calcGUI
    calcGUI.mainloop()
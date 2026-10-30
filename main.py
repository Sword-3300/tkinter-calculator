import tkinter as tk
from tkinter import ttk


class Button:
    def __init__(self, text, row, col, rowspan=1, colspan=1, func=None):
        self.text = text
        self.row = row
        self.col = col
        self.rowspan = rowspan
        self.colspan = colspan
        self.func = func

    def draw_button(self):
        btn = ttk.Button(text=self.text, func=None)
        btn.grid(row=self.row, column=self.col, rowspan=self.rowspan, columnspan=self.colspan, sticky="nsew")

    def add_button_to_grid(self, grid:dict):
        grid[(self.row, self.col)] = self


class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x450")
        self.resizable(False, False)
        self.title("Calculator")
        self.wm_iconphoto(False, tk.PhotoImage(file="icon.png"))

        self.setup_grid()

        self.output_formatted = ""
        self.output_label = ttk.Label(font=("Arial", 20))
        self.output_label.grid(row=0, rowspan=2, columnspan=5, sticky="nsew")

        self.button_grid = {}

        self.setup_buttons()

        for button in self.button_grid.values():
            button.draw_button()

        print(self.button_grid)

    def setup_grid(self):
        for row in range(8):
            self.rowconfigure(row, weight=1)
        for column in range(5):
            self.columnconfigure(column, weight=1)

    def setup_buttons(self):
        clear_btn = Button("C", 2, 3)
        clear_btn.add_button_to_grid(self.button_grid)

        delete_btn = Button("Del", 2, 4)
        delete_btn.add_button_to_grid(self.button_grid)

        e_btn = Button("e", 3, 0)
        e_btn.add_button_to_grid(self.button_grid)

        pi_btn = Button("π", 3, 1)
        pi_btn.add_button_to_grid(self.button_grid)

        openedbracket_btn = Button("(", 3, 2)
        openedbracket_btn.add_button_to_grid(self.button_grid)

        closedbracket_btn = Button(")", 3, 3)
        closedbracket_btn.add_button_to_grid(self.button_grid)

        divide_btn = Button("÷", 3, 4)
        divide_btn.add_button_to_grid(self.button_grid)

        trig_btn = Button("Trig", 4, 0, rowspan=2)
        trig_btn.add_button_to_grid(self.button_grid)

        seven_btn = Button("7", 4, 1)
        seven_btn.add_button_to_grid(self.button_grid)

        eight_btn = Button("8", 4, 2)
        eight_btn.add_button_to_grid(self.button_grid)

        nine_btn = Button("9", 4, 3)
        nine_btn.add_button_to_grid(self.button_grid)

        multiply_btn = Button("×", 4, 4)
        multiply_btn.add_button_to_grid(self.button_grid)

        four_btn = Button("4", 5, 1)
        four_btn.add_button_to_grid(self.button_grid)

        five_btn = Button("5", 5, 2)
        five_btn.add_button_to_grid(self.button_grid)

        six_btn = Button("6", 5, 3)
        six_btn.add_button_to_grid(self.button_grid)

        minus_btn = Button("-", 5, 4)
        minus_btn.add_button_to_grid(self.button_grid)

        exp_btn = Button("Exp", 6, 0, rowspan=2)
        exp_btn.add_button_to_grid(self.button_grid)

        one_btn = Button("1", 6, 1)
        one_btn.add_button_to_grid(self.button_grid)

        two_btn = Button("2", 6, 2)
        two_btn.add_button_to_grid(self.button_grid)

        three_btn = Button("3", 6, 3)
        three_btn.add_button_to_grid(self.button_grid)

        plus_btn = Button("+", 6, 4)
        plus_btn.add_button_to_grid(self.button_grid)

        plusminus_btn = Button("+/-", 7, 1)
        plusminus_btn.add_button_to_grid(self.button_grid)

        zero_btn = Button("0", 7, 2)
        zero_btn.add_button_to_grid(self.button_grid)

        point_btn = Button(",", 7, 3)
        point_btn.add_button_to_grid(self.button_grid)

        equals_btn = Button("=", 7, 4)
        equals_btn.add_button_to_grid(self.button_grid)

    def update_output_label(self):
        self.output_label.configure(text=self.output_formatted)


class CalculatorFUNC:
    def __init__(self):
        self.output_raw = ""

    def raw_to_format(self, GUI: CalculatorGUI):
        GUI.output_formatted = self.output_raw


if __name__ == "__main__":
    calcGUI = CalculatorGUI()
    calcFUNC = CalculatorFUNC()
    calcGUI.mainloop()
import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x450")
        self.resizable(False, False)
        self.title("Calculator")
        self.wm_iconphoto(False, tk.PhotoImage(file="icon.png"))

        self.setup_grid()

    def setup_grid(self):
        for row in range(8):
            self.rowconfigure(row, weight=1)
        for column in range(5):
            self.columnconfigure(column, weight=1)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()

WIDTH = 300
HEIGHT = 450
TITLE = "Calculator"

root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
root.title(TITLE)
root.wm_iconphoto(False, tk.PhotoImage(file="icon.png"))

style = ttk.Style()
style.configure("Default.TButton", font=("Arial", 20))

class Button:
    def __init__(self, text, row, col, rowspan, colspan, func):
        self.text = text
        self.row = row
        self.col = col
        self.rowspan = rowspan
        self.colspan = colspan
        self.func = func

    def draw_button(self, output):
        btn = ttk.Button(root, text=self.text, style="Default.TButton")
        btn.grid(row=self.row, column=self.col,
                rowspan=self.rowspan, columnspan=self.colspan, sticky="nsew")

        if self.func == "num":
            btn.configure(command=lambda: self.register_number(output))
        elif self.func == "clr":
            btn.configure(command=lambda: self.clear_output(output))
        elif self.func == "del":
            btn.configure(command=lambda: self.delete_last(output))

    def register_number(self, output):
        output.configure(text=(output.cget("text") + self.text))

    def clear_output(self, output):
        output.configure(text="")

    def delete_last(self, output):
        output.configure(text=output.cget("text")[:-1])


root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)


output1 = tk.Label(root, text="hello world", font=("Arial", 20))
output1.grid(row=0, rowspan=2, columnspan=5, sticky="nsew")

bClear = Button("C", 2, 3, 1, 1, "clr").draw_button(output1)
bDelete = Button("Del", 2, 4, 1, 1, "del").draw_button(output1)
bE = Button("e", 3, 0, 1, 1, None).draw_button(output1)
bPi = Button("π", 3, 1, 1, 1, None).draw_button(output1)
bOpenbracket = Button("(", 3, 2, 1, 1, None).draw_button(output1)
bOlosebracket = Button(")", 3, 3, 1, 1, None).draw_button(output1)
bDivide = Button("÷", 3, 4, 1, 1, None).draw_button(output1)
bTrig = Button("Trig", 4, 0, 2, 1, None).draw_button(output1)
b7 = Button("7", 4, 1, 1, 1, "num").draw_button(output1)
b8 = Button("8", 4, 2, 1, 1, "num").draw_button(output1)
b9 = Button("9", 4, 3, 1, 1, "num").draw_button(output1)
bMulpiply = Button("×", 4, 4, 1, 1, None).draw_button(output1)
b4 = Button("4", 5, 1, 1, 1, "num").draw_button(output1)
b5 = Button("5", 5, 2, 1, 1, "num").draw_button(output1)
b6 = Button("6", 5, 3, 1, 1, "num").draw_button(output1)
bMinus = Button("-", 5, 4, 1, 1, None).draw_button(output1)
bExp = Button("Exp", 6, 0, 2, 1, None).draw_button(output1)
b1 = Button("1", 6, 1, 1, 1, "num").draw_button(output1)
b2 = Button("2", 6, 2, 1, 1, "num").draw_button(output1)
b3 = Button("3", 6, 3, 1, 1, "num").draw_button(output1)
bPlus = Button("+", 6, 4, 1, 1, None).draw_button(output1)
bPlusminus = Button("+/-", 7, 1, 1, 1, None).draw_button(output1)
b0 = Button("0", 7, 2, 1, 1, "num").draw_button(output1)
bComma = Button(",", 7, 3, 1, 1, None).draw_button(output1)
bEquals = Button("=", 7, 4, 1, 1, None).draw_button(output1)

root.mainloop()
import tkinter as tk

WIDTH = 300
HEIGHT = 450
TITLE = "Calculator"

root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
root.title(TITLE)
root.wm_iconphoto(False, tk.PhotoImage(file="icon.png"))

class Button:
    def __init__(self, text, row, col, rowspan, colspan, func):
        self.text = text
        self.row = row
        self.col = col
        self.rowspan = rowspan
        self.colspan = colspan
        self.func = func

    def draw_button(self, output):
        tk.Button(root, text=self.text, command=lambda: self.register_number(output)).grid(row=self.row, column=self.col,
                rowspan=self.rowspan, columnspan=self.colspan, sticky="nsew")

    def register_number(self, output):
        output.configure(text=self.text)


root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

output1 = tk.Label(root, text="hello world")
output1.grid(row=0, columnspan=3, sticky="nsew")
b1 = Button("1", 3, 0, 1, 1, None).draw_button(output1)
b2 = Button("2", 3, 1, 1, 1, None).draw_button(output1)
b3 = Button("3", 3, 2, 1, 1, None).draw_button(output1)
b4 = Button("4", 2, 0, 1, 1, None).draw_button(output1)
b5 = Button("5", 2, 1, 1, 1, None).draw_button(output1)
b6 = Button("6", 2, 2, 1, 1, None).draw_button(output1)
b7 = Button("7", 1, 0, 1, 1, None).draw_button(output1)
b8 = Button("8", 1, 1, 1, 1, None).draw_button(output1)
b9 = Button("9", 1, 2, 1, 1, None).draw_button(output1)

root.mainloop()
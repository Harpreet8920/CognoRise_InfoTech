import tkinter as tk
from math import pi, e, sqrt, exp, log10, log, factorial


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # Display
        self.display = tk.Entry(
            master, width=30, borderwidth=5, relief="sunken", font=("Helvetica", 16)
        )
        self.display.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="ew")
        self.display.focus_set()

        # Bind keyboard events
        self.master.bind("<Key>", self.key_press)

        # Buttons
        button_list = [
            "2nd",
            "π",
            "e",
            "C",
            "CE",
            "x²",
            "1/x",
            "|x|",
            "exp",
            "mod",
            "√x",
            "(",
            ")",
            "n!",
            "/",
            "x^y",
            "7",
            "8",
            "9",
            "*",
            "10^x",
            "4",
            "5",
            "6",
            "-",
            "log",
            "1",
            "2",
            "3",
            "+",
            "ln",
            "+/-",
            "0",
            ".",
            "=",
        ]
        row = 1
        col = 0
        for button_text in button_list:
            button = tk.Button(
                master,
                text=button_text,
                width=5,
                height=2,
                command=lambda text=button_text: self.button_click(text),
            )
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Configure grid weights for resizing
        for i in range(6):
            master.rowconfigure(i, weight=1)
        for i in range(5):
            master.columnconfigure(i, weight=1)

    def key_press(self, event):
        if event.char.isdigit() or event.char in "+-*/.()":
            self.display.insert(tk.END, event.char)
        elif event.char == "=":
            self.button_click("=")
        elif event.char == "\b":
            self.button_click("CE")
        elif event.char == "\r":
            self.button_click("=")

    def button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "C":
            self.display.delete(0, tk.END)
        elif text == "CE":
            self.display.delete(len(self.display.get()) - 1, tk.END)
        elif text == "+/-":
            current_value = self.display.get()
            if current_value:
                if current_value[0] == "-":
                    self.display.delete(0, 1)
                else:
                    self.display.insert(0, "-")
        elif text == "π":
            self.display.insert(tk.END, str(pi))
        elif text == "e":
            self.display.insert(tk.END, str(e))
        elif text == "x²":
            try:
                value = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(value**2))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "√x":
            try:
                value = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(sqrt(value)))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "1/x":
            try:
                value = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(1 / value))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "|x|":
            try:
                value = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(abs(value)))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "exp":
            try:
                value = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(exp(value)))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "mod":
            self.display.insert(tk.END, "%")
        elif text == "n!":
            try:
                value = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(factorial(value)))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "10^x":
            try:
                value = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(10**value))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "log":
            try:
                value = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(log10(value)))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "ln":
            try:
                value = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(log(value)))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "x^y":
            self.display.insert(tk.END, "**")
        else:
            self.display.insert(tk.END, text)


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

import math
import tkinter as tk
from tkinter import messagebox

def on_button_click(value):
    current = entry_var.get()
    entry_var.set(current + str(value))

def clear():
    entry_var.set("")

def calculate():
    try:
        expression = entry_var.get()
        result = eval(expression, {"math": math, "sqrt": math.sqrt, "log": math.log, "sin": lambda x: math.sin(math.radians(x)),
                                   "cos": lambda x: math.cos(math.radians(x)), "tan": lambda x: math.tan(math.radians(x))})
        entry_var.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

def backspace():
    entry_var.set(entry_var.get()[:-1])

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.configure(bg="#2c3e50")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24, "bold"), bd=10, relief=tk.FLAT, justify=tk.RIGHT, bg="#ecf0f1", fg="#000")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, padx=10, pady=10, sticky="nsew")

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('C', '⌫', 'sqrt', 'log'),
    ('sin', 'cos', 'tan', '^')
]

button_colors = {"default": "#34495e", "operator": "#e67e22", "special": "#e74c3c", "equal": "#2ecc71"}

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        btn_bg = button_colors["default"]
        if btn_text in ('/', '*', '-', '+', '^'):
            btn_bg = button_colors["operator"]
        elif btn_text in ('C', '⌫'):
            btn_bg = button_colors["special"]
        elif btn_text == '=':
            btn_bg = button_colors["equal"]
        
        action = lambda x=btn_text: on_button_click(x) if x not in ('=', 'C', '⌫', 'sqrt', 'log', 'sin', 'cos', 'tan', '^') else None
        if btn_text == '=':
            action = calculate
        elif btn_text == 'C':
            action = clear
        elif btn_text == '⌫':
            action = backspace
        elif btn_text == 'sqrt':
            action = lambda: on_button_click('sqrt(')
        elif btn_text == 'log':
            action = lambda: on_button_click('log(')
        elif btn_text == 'sin':
            action = lambda: on_button_click('sin(')
        elif btn_text == 'cos':
            action = lambda: on_button_click('cos(')
        elif btn_text == 'tan':
            action = lambda: on_button_click('tan(')
        elif btn_text == '^':
            action = lambda: on_button_click('**')
        
        btn = tk.Button(root, text=btn_text, font=("Arial", 18, "bold"), width=5, height=2, command=action, bg=btn_bg, fg="white", relief=tk.RAISED)
        btn.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")

for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(6):
    root.rowconfigure(i+1, weight=1)

root.mainloop()

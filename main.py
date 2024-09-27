import tkinter as tk
from math import sin, cos, tan, radians

def evaluate_expression(event=None):
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def insert_value(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

def clear_display():
    display.delete(0, tk.END)

root = tk.Tk()
root.title("Pylucator")

display = tk.Entry(root, font=("Arial", 18), borderwidth=5, relief=tk.RIDGE)
display.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

buttons = [
    "7", "8", "9", "/", "sin",
    "4", "5", "6", "*", "cos",
    "1", "2", "3", "-", "tan",
    "0", ".", "=", "+", "C"
]

row = 1
col = 0
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, width=5, height=2, command=evaluate_expression)
        btn.grid(row=row, column=col, padx=5, pady=5)
    elif button == "C":
        btn = tk.Button(root, text=button, width=5, height=2, command=clear_display)
        btn.grid(row=row, column=col, padx=5, pady=5)
    elif button in ["sin", "cos", "tan"]:
        btn = tk.Button(root, text=button, width=5, height=2, command=lambda b=button: insert_value(b+"(radians("))
        btn.grid(row=row, column=col, padx=5, pady=5)
        tk.Button(root, text='))', width=5, height=2, command=lambda: insert_value('))')).grid(row=row, column=col+1, padx=5, pady=5)
        col += 1
    else:
        btn = tk.Button(root, text=button, width=5, height=2, command=lambda b=button: insert_value(b))
        btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 4:
        col = 0
        row += 1

display.bind("<Return>", evaluate_expression)

root.mainloop()

txt = "This Developer Calculator supports basic arithmetic operations (addition, subtraction, multiplication, division) "\
      "along with trigonometric functions (sin, cos, tan). Enter the expression and press '=' to evaluate, or simply press Enter on the keyboard."

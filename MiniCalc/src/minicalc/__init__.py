import tkinter as tk
from tkinter import font


def calculate(op):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        if op == '+':
            result.set(a + b)
        elif op == '-':
            result.set(a - b)
        elif op == '*':
            result.set(a * b)
        elif op == '/':
            result.set(a / b if b != 0 else "Fehler: ÷0")

    except ValueError:
        result.set("Ungültige Eingabe")


# ===============================
# Hauptfenster
# ===============================

root = tk.Tk()
root.title("Taschenrechner")
root.geometry("420x260")
root.resizable(False, False)
root.configure(bg="#2b2b2b")

# ===============================
# Schriftarten
# ===============================

font_entry = font.Font(size=16)
font_button = font.Font(size=14, weight="bold")
font_result = font.Font(size=18, weight="bold")

# ===============================
# Eingabebereich
# ===============================

input_frame = tk.Frame(root, bg="#2b2b2b")
input_frame.pack(pady=15)

entry_a = tk.Entry(
    input_frame,
    width=10,
    font=font_entry,
    justify="center"
)
entry_a.grid(row=0, column=0, padx=10)

entry_b = tk.Entry(
    input_frame,
    width=10,
    font=font_entry,
    justify="center"
)
entry_b.grid(row=0, column=1, padx=10)

# ===============================
# Ergebnisanzeige
# ===============================

result = tk.StringVar(value="Ergebnis")

result_label = tk.Label(
    root,
    textvariable=result,
    font=font_result,
    bg="#1e1e1e",
    fg="white",
    width=20,
    pady=10
)
result_label.pack(pady=10)

# ===============================
# Buttonbereich
# ===============================

button_frame = tk.Frame(root, bg="#2b2b2b")
button_frame.pack(pady=10)

buttons = ['+', '-', '*', '/']

for i, op in enumerate(buttons):
    tk.Button(
        button_frame,
        text=op,
        font=font_button,
        width=6,
        height=2,
        bg="#3c3f41",
        fg="white",
        activebackground="#5c5f61",
        command=lambda o=op: calculate(o)
    ).grid(row=0, column=i, padx=8)

root.mainloop()

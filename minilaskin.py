import tkinter as tk

#MAIN
root = tk.Tk()
root.title("MINILASKIN")

# globaalit muuttujat
first_number = None
operation = None

# näyttö
display = tk.Entry(root, width=25, borderwidth=5, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
display.insert(0, "0")

def button_click(number):
    """Lisää numeroita tai desimaalipisteen näytölle."""
    current = display.get()
    if current == "0":
        display.delete(0, tk.END) # poistaa nollan ennen uuden luvun lisäämistä
        display.insert(0, number)
    else:
        display.insert(tk.END, number)

def operator_click(op):
    """Tallentaa ekan luvun ja operaattorin."""
    global first_number
    global operation
    first_number = float(display.get())
    operation = op
    display.delete(0, tk.END)
    display.insert(0, "0")

def equals_click():
    """Laskee ja näyttää tuloksen."""
    global first_number
    global operation
    try:
        second_number = float(display.get())
        result = 0
        
        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            if second_number == 0:
                result = "EI VOI JAKAA NOLLALLA"
            else:
                result = first_number / second_number

            display.delete(0, tk.END)
            display.insert(0, str(result))

    except (ValueError, TypeError):
        display.delete(0, tk.END)
        display.insert(0, "VIRHE")

#Nollaa muuttujat seuraavaa laskua varten
first_number = None
operation = None

def clear_click():
    """Reset."""
    global first_number
    global operation
    display.delete(0, tk.END)
    display.insert(0, "0")
    first_number = None
    operation = None

# painikkeet ja paikat
button_list = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('1', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in button_list:
    if text.isdigit() or text == '.':
        button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: button_click(t))
    elif text == '=':
        button = tk.Button(root, text=text, padx=20, pady=10, command=equals_click)
    else:
        button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: operator_click(t))
        
    button.grid(row=row, column=col)

#Reset painike
clear_button = tk.Button(root, text='C', padx=20, pady=10, command=clear_click)
clear_button.grid(row=5, column=0, columnspan=2)



root.mainloop()
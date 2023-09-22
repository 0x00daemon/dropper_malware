import tkinter as tk
import webbrowser
import additional_options  # Import the additional_options.py file

def add():
    try:
        result.set(float(entry_num1.get()) + float(entry_num2.get()))
    except ValueError:
        result.set("Invalid input")

def subtract():
    try:
        result.set(float(entry_num1.get()) - float(entry_num2.get()))
    except ValueError:
        result.set("Invalid input")

def multiply():
    try:
        result.set(float(entry_num1.get()) * float(entry_num2.get()))
    except ValueError:
        result.set("Invalid input")

def divide():
    try:
        num2 = float(entry_num2.get())
        if num2 != 0:
            result.set(float(entry_num1.get()) / num2)
        else:
            result.set("Cannot divide by zero")
    except ValueError:
        result.set("Invalid input")

def reset():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result.set("Result: ")

def open_additional_options():
    additional_options.additional_options()  # Call the function from additional_options.py

# Create the main application window
app = tk.Tk()
app.title("Simple Calculator")

# Create entry fields for numbers and result
entry_num1 = tk.Entry(app)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

operation_label = tk.Label(app, text="Choose operation:")
operation_label.grid(row=0, column=1)

entry_num2 = tk.Entry(app)
entry_num2.grid(row=0, column=2, padx=5, pady=5)

# Create buttons for each operation
btn_add = tk.Button(app, text="Add", command=add)
btn_add.grid(row=1, column=0, padx=5, pady=5)

btn_subtract = tk.Button(app, text="Subtract", command=subtract)
btn_subtract.grid(row=1, column=1, padx=5, pady=5)

btn_multiply = tk.Button(app, text="Multiply", command=multiply)
btn_multiply.grid(row=1, column=2, padx=5, pady=5)

btn_divide = tk.Button(app, text="Divide", command=divide)
btn_divide.grid(row=1, column=3, padx=5, pady=5)

# Create a "Reset" button
btn_reset = tk.Button(app, text="Reset", command=reset)
btn_reset.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

# Create a "Additional Options" button
btn_additional_options = tk.Button(app, text="Additional Options", command=open_additional_options)
btn_additional_options.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

# Create a label to display the result
result = tk.StringVar()
result.set("Result: ")
result_label = tk.Label(app, textvariable=result)
result_label.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

# Start the main event loop
app.mainloop()

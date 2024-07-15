import tkinter as tk

# Function to perform the calculation based on operation choice
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_entry.delete(0, tk.END)
                result_entry.insert(tk.END, "Error: Division by zero")
                return
            result = num1 / num2
        else:
            result_entry.delete(0, tk.END)
            result_entry.insert(tk.END, "Error: Invalid operation")
            return
        
        result_entry.delete(0, tk.END)
        result_entry.insert(tk.END, str(result))
    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(tk.END, "Error: Invalid input")

# Create the main tkinter window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x200")
root.configure(bg="#F5F5DC")

# Input fields and labels
label_num1 = tk.Label(root, text="Enter first number:", bg="#F5F5DC")
label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

label_num2 = tk.Label(root, text="Enter second number:", bg="#F5F5DC")
label_num2.grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Operation selection using radio buttons
operation_label = tk.Label(root, text="Select operation:", bg="#F5F5DC")
operation_label.grid(row=2, column=0, padx=5, pady=5)

operation_var = tk.StringVar()
operation_var.set("+")  # default value

radio_frame = tk.Frame(root, bg="#F5F5DC")
radio_frame.grid(row=2, column=1, padx=5, pady=5)

addition_radio = tk.Radiobutton(radio_frame, text="+", variable=operation_var, value="+", bg="#F5F5DC")
addition_radio.pack(side=tk.LEFT, padx=5)

subtraction_radio = tk.Radiobutton(radio_frame, text="-", variable=operation_var, value="-", bg="#F5F5DC")
subtraction_radio.pack(side=tk.LEFT, padx=5)

multiplication_radio = tk.Radiobutton(radio_frame, text="*", variable=operation_var, value="*", bg="#F5F5DC")
multiplication_radio.pack(side=tk.LEFT, padx=5)

division_radio = tk.Radiobutton(radio_frame, text="/", variable=operation_var, value="/", bg="#F5F5DC")
division_radio.pack(side=tk.LEFT, padx=5)

# Button to perform calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label and Entry to display result
result_label = tk.Label(root, text="Result:", bg="#F5F5DC")
result_label.grid(row=4, column=0, padx=5, pady=5)

result_entry = tk.Entry(root, width=20)
result_entry.grid(row=4, column=1, padx=5, pady=5)

# Run the tkinter main loop
root.mainloop()



















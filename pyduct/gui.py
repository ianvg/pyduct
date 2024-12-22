import tkinter as tk
from tkinter import ttk # for modern widgets

# Create the main window
root = tk.Tk()
root.title("PyDuct GUI")
root.geometry("400x300")  # Width x Height

# Add a label
label = ttk.Label(root, text="Welcome to PyDuct", font=("Helvetica", 16))
label.pack(pady=20)

# Add an input field for flow rate
flowrate_label = ttk.Label(root, text="Flow Rate (m³/s):")
flowrate_label.pack(pady=5)

flowrate_entry = ttk.Entry(root)
flowrate_entry.pack(pady=5)

# Add a dropdown for duct shape
shape_label = ttk.Label(root, text="Duct Shape:")
shape_label.pack(pady=5)

shape_var = tk.StringVar(value="round")  # Default value
shape_dropdown = ttk.Combobox(root, textvariable=shape_var, values=["round", "rectangular"])
shape_dropdown.pack(pady=5)

# Add a button to calculate
def calculate():
    flowrate = flowrate_entry.get()  # Get input from the entry field
    shape = shape_var.get()  # Get the selected shape
    result_label.config(text=f"Flow Rate: {flowrate}, Shape: {shape}")  # Update result label

calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Add a label to display results
result_label = ttk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

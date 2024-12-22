import tkinter as tk
from tkinter import *
from tkinter import ttk # for modern widgets
#import networkx as nx
from pyduct.connectors import Connector  # Import Connector class from connectors.py in the same directory
from pyduct.ducts import RigidDuctType, FlexDuctType  # Import necessary classes from ducts.py
from pyduct.fittings import OneWayFitting, TwoWayFitting  # Import from fitting_types.py
from pyduct.ducts import RigidDuct, FlexDuct  # Import relevant classes from fittings.py
from pyduct.network import Ductwork  # Import from network.py
from pyduct.standard_sizes import  STANDARD_RECTANGULAR_DUCT_SIZES, STANDARD_ROUND_DUCT_SIZES  # Import standard sizes
from pyduct.physics.friction import local_pressure_drop  # Import local_pressure_drop from friction.py
from pyduct.physics.general import calc_velocity  # Import calc_velocity from general.py

# Create the main window
root = tk.Tk()
root.title("PyDuct GUI")
root.geometry("400x500")  # Width x Height

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
shape_dropdown = ttk.Combobox(root, textvariable=shape_var, values=["Round", "Rectangular"])
shape_dropdown.pack(pady=5)

# Add an input field for area
area_label = ttk.Label(root, text="Area (m²):")
area_label.pack(pady=5)

area_entry = ttk.Entry(root)
area_entry.pack(pady=5)

# Add a label to display results
result_label = ttk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

def calculate():
    print("Calculate button clicked")  # Debugging line
    try:
        # Retrieve user inputs
        flowrate = float(flowrate_entry.get())  # Convert to float if necessary
        shape = shape_var.get()  # Get the selected shape
        area = float(area_entry.get()) # Get area and convert to float
        dzeta = 0.5  # Example: set dzeta or retrieve it from the user input
        
        # Example of using the Connector class
        
        # Create Connector instance
        connector = Connector(flowrate=flowrate, shape=shape, area=area)
        
        # Ensure velocity is calculated before pressure drop
        connector.calculate_velocity()
        
        # Now calculate the pressure drop using the area and dzeta
        connector.calculate_pressure_drop(area=area, dzeta=dzeta)
        
        # Update the result label with pressure drop
        result_label.config(text=f"Pressure Drop: {connector.pressure_drop:.2f} Pa") # Update result label
        
        # result_label.config(text="Pressure Drop: 0.3 Pa")
        root.update_idletasks()  # Force the update to the GUI
        
    except Exception as e:
        # Display an error message if calculation fails
        result_label.config(text=f"Error: {str(e)}")
        print("Error in calculation:", e)

calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

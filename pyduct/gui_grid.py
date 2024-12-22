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
from dataclasses import dataclass

# Define the FittingType data class
@dataclass
class FittingType:
    name: str
    dzeta: float  # Pressure loss coefficient for the fitting type

# Available fitting types
fitting_types = [
    FittingType(name="One-Way Fitting", dzeta=0.5),
    FittingType(name="Two-Way Fitting", dzeta=0.3),
    FittingType(name="Three-Way Fitting", dzeta=0.7),
]

# Create the main window
root = tk.Tk()
root.title("PyDuct GUI")
root.geometry("400x500")  # Width x Height

# Add a label
label = ttk.Label(root, text="Welcome to PyDuct", font=("Helvetica", 16))
label.grid(row=0, column=0, columnspan=2, pady=20)

# Add a dropdown for selecting flow direction
flow_direction_label = ttk.Label(root, text="Flow Direction:")
flow_direction_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

flow_direction_var = tk.StringVar(value="Supply")  # Default value
flow_direction_dropdown = ttk.Combobox(root, textvariable=flow_direction_var, values=["Supply", "Exhaust/Return"])
flow_direction_dropdown.grid(row=1, column=1, padx=5, pady=5)

# Add a dropdown for selecting fitting type
fitting_label = ttk.Label(root, text="Fitting Type:")
fitting_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

fitting_var = tk.StringVar(value=fitting_types[0].name)  # Default value
fitting_dropdown = ttk.Combobox(root, textvariable=fitting_var, values=[fitting.name for fitting in fitting_types])
fitting_dropdown.grid(row=2, column=1, padx=5, pady=5)

# Add an input field for flow rate
flowrate_label = ttk.Label(root, text="Flow Rate (m³/s):")
flowrate_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

flowrate_entry = ttk.Entry(root)
flowrate_entry.grid(row=1, column=1, padx=5, pady=5)

# # Add a dropdown for duct shape
# shape_label = ttk.Label(root, text="Duct Shape:")
# shape_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

# shape_var = tk.StringVar(value="round")  # Default value
# shape_dropdown = ttk.Combobox(root, textvariable=shape_var, values=["Round", "Rectangular"])
# shape_dropdown.grid(row=2, column=1, padx=5, pady=5)

# Add an input field for area
area_label = ttk.Label(root, text="Area (m²):")
area_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

area_entry = ttk.Entry(root)
area_entry.grid(row=3, column=1, padx=5, pady=5)

# # Add a dropdown for selecting fitting type
# fitting_label = ttk.Label(root, text="Fitting Type:")
# fitting_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")

# # Populate the dropdown with fitting type names
# fitting_var = tk.StringVar()
# fitting_dropdown = ttk.Combobox(root, textvariable=fitting_var, values=[fitting.name for fitting in fitting_types])
# fitting_dropdown.grid(row=4, column=1, padx=5, pady=5)

# Add a label to display results
result_label = ttk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

def calculate():
    print("Calculate button clicked")  # Debugging line
    try:
        # Retrieve user inputs
        flowrate = float(flowrate_entry.get())  # Convert to float if necessary
        shape = shape_var.get()  # Get the selected shape
        area = float(area_entry.get()) # Get area and convert to float
        
        # Get the selected fitting type and its dzeta value
        fitting_name = fitting_var.get()  # Get the selected fitting type name
        fitting = next(fitting for fitting in fitting_types if fitting.name == fitting_name)  # Find the fitting object
        dzeta = fitting.dzeta  # Get dzeta value for the selected fitting type
        
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
calculate_button.grid(row=6, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()

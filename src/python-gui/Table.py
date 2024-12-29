import customtkinter as ctk
import tkinter as tk
from tkinter import simpledialog
from models import SSMParam

# Define the Object class
class MyObject:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

# Sample data
objects = [
    MyObject("Alice", 30, "New York"),
    MyObject("Bob", 25, "Los Angeles"),
    MyObject("Charlie", 35, "Chicago")
]

# Initialize the main window
root = ctk.CTk()
root.title("CustomTkinter Table with Actions")
root.geometry("500x300")

# Function to handle button press event
def on_button_press(obj):
    user_input = simpledialog.askstring("Action", f"Performing action for {obj.name}. Enter your input:")
    if user_input is not None:
        print(f"Action performed for {obj.name} with input: {user_input}")

def update_ssm_param(obj):
    print(f"Updating SSM Param: {obj.key}")

def refresh_array_param(obj):
    print(f"Refreshing Array Param: {obj.key}")

# Create a frame for the table
table_frame = ctk.CTkFrame(root)
table_frame.pack(pady=20, padx=20)

# Define the headers
headers = ["Name", "Age", "City", "Action"]

# Create the table headers
for col, header in enumerate(headers):
    header_label = ctk.CTkLabel(table_frame, text=header, width=10, height=2, fg_color="blue", corner_radius=4)
    header_label.grid(row=0, column=col, padx=5, pady=5)

# Create the table data
for row, obj in enumerate(objects, start=1):
    data = [obj.name, obj.age, obj.city]
    for col, item in enumerate(data):
        data_label = ctk.CTkLabel(table_frame, text=item, width=10, height=2, fg_color="white", corner_radius=4)
        data_label.grid(row=row, column=col, padx=5, pady=5)
    
    # Add a button in the last column
    action_button = ctk.CTkButton(table_frame, text="Edit", command=lambda obj=obj: on_button_press(obj))
    action_button.grid(row=row, column=len(headers)-1, padx=5, pady=5)

# Run the application
root.mainloop()

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Initialize the main window
root = ctk.CTk()
root.title("CustomTkinter Side-by-Side Frames Example")
root.geometry("620x400")
root.resizable(False, False)

#region global-vars

# Global variable to store the selected value 
selected_account = None

#endregion

#region Arrays

accounts = [
    "rwrd057",
    "rwrd058",
    "rwrd059"
]
envs = [
    "DEV",
    "TEST",
    "PROD"
]

colours = [
    "Green",
    "Blue"
]

#endregion

#region EventCallbacks

# Add a combobox and set the initial value + callback event
def combobox_callback_account(choice):
    global selected_account 
    selected_account = comboboxacc.get()
    print("combobox account dropdown choice:", choice)
    print("combobox account dropdown selectedval:", selected_account)

def combobox_callback_env(choice):
    print("combobox env dropdown choice:", choice)

def combobox_callback_colour(choice):
    print("combobox colour dropdown choice:", choice)

# Function to update the label text 
def update_label():
    print("Label Updated!") 
    label.configure(text="Label Updated!")
    create_path_prefix()

def create_path_prefix():
    user = "Alice"
    folder = "Documents"
    file = "example.txt"
    path = f"C:/Users/{user}/{folder}/{file}"
    print(f"The full path is: {path}")


#endregion




# Function to handle button press event and close the app
def on_button_press():
    print("Button Pressed!")
    # messagebox.showinfo("Information", "This is a Tkinter dialog!")

# Create two frames
left_frame = ctk.CTkFrame(root, width=150, height=290, fg_color="lightblue")
left_frame.grid(row=0, column=0, padx=5, pady=5)

right_frame = ctk.CTkFrame(root, width=420, height=290, fg_color="lightgray")
right_frame.grid(row=0, column=1, padx=5, pady=5)

comboboxacc = ctk.CTkComboBox(master=left_frame,
                                     values=accounts,
                                     command=combobox_callback_account)
comboboxacc.pack(padx=20, pady=10)

comboboxenv = ctk.CTkComboBox(master=left_frame,
                                     values=envs,
                                     command=combobox_callback_env)
comboboxenv.pack(padx=20, pady=10)

comboboxcolour = ctk.CTkComboBox(master=left_frame,
                                     values=colours,
                                     command=combobox_callback_colour)
comboboxcolour.pack(padx=20, pady=10)

# Add a button to the left frame
button = ctk.CTkButton(left_frame, text="Search", command=on_button_press)
button.pack(pady=20, padx=20)

# Create a button that updates the label 
updatebtn = ctk.CTkButton(left_frame, text="Update Label", command=update_label) 
updatebtn.pack(pady=20)

# Create a customtkinter label 
label = ctk.CTkLabel(root, text="Hello, CustomTkinter!", width=170, height=50, corner_radius=5) 
label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()

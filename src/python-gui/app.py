import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Initialize the main window
root = ctk.CTk()
root.title("CustomTkinter Side-by-Side Frames Example")
root.geometry("620x300")
root.resizable(False, False)

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
    print("combobox account dropdown choice:", choice)

def combobox_callback_env(choice):
    print("combobox env dropdown choice:", choice)

def combobox_callback_colour(choice):
    print("combobox colour dropdown choice:", choice)

#endregion


# Function to handle button press event and close the app
def on_button_press():
    messagebox.showinfo("Information", "This is a Tkinter dialog!")

def on_button_press_dialog():
    user_input = simpledialog.askstring("Input", "Please enter some text:") 
    if user_input is not None: 
        print(f"User input: {user_input}")


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
button = ctk.CTkButton(left_frame, text="Open Message", command=on_button_press)
button.pack(pady=20, padx=20)

# dialogButton = ctk.CTkButton(left_frame, text="Open Dialog", command=on_button_press_dialog)
# dialogButton.pack(pady=20)

# Run the application
root.mainloop()

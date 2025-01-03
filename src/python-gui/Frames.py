import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Initialize the main window
root = ctk.CTk()
root.title("CustomTkinter Side-by-Side Frames Example")
root.geometry("420x300")
root.resizable(False, False)

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

right_frame = ctk.CTkFrame(root, width=220, height=290, fg_color="lightgray")
right_frame.grid(row=0, column=1, padx=5, pady=5)

# Add a button to the left frame
button = ctk.CTkButton(left_frame, text="Open Message", command=on_button_press)
button.pack(pady=20, padx=20)

# dialogButton = ctk.CTkButton(left_frame, text="Open Dialog", command=on_button_press_dialog)
# dialogButton.pack(pady=20)

# Run the application
root.mainloop()

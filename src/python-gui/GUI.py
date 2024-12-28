import tkinter
import customtkinter as ctk

# System settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Create the main window
app = ctk.CTk()
app.geometry("1100x700")
app.title("SSM TestBed")

# Add Elements here

# Add a label
label = ctk.CTkLabel(app, text="SSM Selector!")
label.pack() 

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

def button_event():
    print("button pressed")

def button__close_event():
    app.destroy()


#endregion

sideFrame = ctk.CTkFrame()

comboboxacc = ctk.CTkComboBox(master=app,
                                     values=accounts,
                                     command=combobox_callback_account)
comboboxacc.pack(padx=20, pady=10)


# Function to handle button press event 
def on_button_press(name):
    print(f"Button pressed for {name}")

# Create a frame for the table 
frame = ctk.CTkFrame(app) 
frame.pack(pady=20) 
# Define the headers and data 
headers = ["Name", "Age", "City", "Action"] 
data = [ 
    ["Alice", 30, "New York"], 
    ["Bob", 25, "Los Angeles"], 
    ["Charlie", 35, "Chicago"] ] 
# Create the table headers 
for col, header in enumerate(headers): 
    header_label = ctk.CTkLabel(frame, text=header, width=10, height=2, fg_color="blue", corner_radius=4) 
    header_label.grid(row=0, column=col, padx=5, pady=5) 

# Create the table data for 
for row, row_data in enumerate(data, start=1):
    for col, item in enumerate(row_data): 
        data_label = ctk.CTkLabel(frame, text=item, width=10, height=2, fg_color="white", corner_radius=4) 
        data_label.grid(row=row, column=col, padx=5, pady=5)

    # Add a button in the last column 
    action_button = ctk.CTkButton(frame, text="Press", command=lambda name=row_data[0]: on_button_press(name)) 
    action_button.grid(row=row, column=len(headers)-1, padx=5, pady=5)

button = ctk.CTkButton(master=app, text="Search", command=button_event)
button.pack(padx=20, pady=10)

button = ctk.CTkButton(master=app, text="Close", command=button__close_event)
button.pack(padx=20, pady=10)


# Run
app.mainloop()
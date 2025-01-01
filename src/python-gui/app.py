import customtkinter as ctk
import tkinter as tk
from tkinter import simpledialog
from models.SSMParam import SSMParam

# Initialize the main window
root = ctk.CTk()
root.title("CustomTkinter Side-by-Side Frames Example")
root.geometry("820x600")
root.resizable(False, False)

#region global-vars

# Global variable to store the selected values etc..
selected_account = "NA"
selected_env = "NA"
selected_colour = "NA"
selected_bank = "NA"
search_path = None

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

# Sample data for table
objects = [
    SSMParam("/app/dev/db/username", "admin", "Database username"),
    SSMParam("/app/dev/db/password", "password", "Database password"),
    SSMParam("/app/dev/db/host", "localhost", "Database host"),
    SSMParam("/app/dev/db/port", "5432", "Database port"),
    SSMParam("/app/dev/db/name", "mydb", "Database name"),
    SSMParam("/app/dev/client_id", "12345", "Client ID"),
    SSMParam("/app/dev/client_secret", "secret", "Client Secret"),
    SSMParam("/app/dev/api_key", "apikey", "API Key"),
    SSMParam("/app/dev/api_secret", "apisecret", "API Secret")
]

# Define the headers
headers = ["Key", "Value", "Description", "Action"]

#endregion

#region Combo EventCallbacks

# Add a combobox and set the initial value + callback event
def combobox_callback_account(choice):
    global selected_account 
    selected_account = comboboxacc.get()
    print("combobox account dropdown choice:", choice)
    print("combobox account dropdown selectedval:", selected_account)

def combobox_callback_env(choice):
    print("combobox env dropdown choice:", choice)
    global selected_env
    selected_env = choice

def combobox_callback_colour(choice):
    print("combobox colour dropdown choice:", choice)
    global selected_colour
    selected_colour = choice

def combobox_callback_bank(choice):
    print("combobox bank dropdown choice:", choice)
    global selected_bank
    selected_bank = choice

# Function to update the label text 
def update_label():
    create_path_prefix()
    global search_path
    label.configure(text=search_path)

def create_path_prefix_new():
    global search_path
    path = f"{selected_account}/{selected_env}/{selected_colour}/{selected_bank}"
    print(f"The full path prefix is: {path}")

# old method to be scrapped
def create_path_prefix():
    global search_path
    user = "Alice"
    folder = "Documents"
    file = "example.txt"
    path = f"C:/Users/{user}/{folder}/{file}"
    search_path = path
    print(f"The full path is: {path}")

def run_search():
    create_path_prefix_new()
    print("Running search")

def prev_page():
    print("Previous Page")
    
def next_page():
    print("Next Page")

#endregion

# Function to handle button press event and close the app
def on_edit_press(obj):
    user_input = simpledialog.askstring("Action", f"Performing action for {obj.name}. Enter your input:")
    if user_input is not None:
        print(f"Action performed for {obj.name} with input: {user_input}")


#region Frame Creation

# Create two frames
left_frame = ctk.CTkFrame(root, width=170, height=390, fg_color="lightblue")
left_frame.grid(row=0, column=0, padx=5, pady=5)

right_frame = ctk.CTkFrame(root, width=450, height=390, fg_color="lightgray")
right_frame.grid(row=0, column=1, padx=5, pady=5)

#endregion

#region Left Frame Widgets

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
button = ctk.CTkButton(left_frame, text="Search", command=run_search)
button.pack(pady=20, padx=20)

# Create a button that updates the label 
updatebtn = ctk.CTkButton(left_frame, text="Update Label", command=update_label) 
updatebtn.pack(pady=20)

#endregion

#region Right Frame Widgets

# Create a frame for the table
table_frame = ctk.CTkFrame(right_frame)
table_frame.pack(pady=20, padx=20)

nav_frame = ctk.CTkFrame(right_frame)
nav_frame.pack(pady=20, padx=20)

# Create the table headers
for col, header in enumerate(headers):
    header_label = ctk.CTkLabel(table_frame, text=header, width=10, height=2, bg_color="blue", corner_radius=4)
    header_label.grid(row=0, column=col, padx=5, pady=5)

# Create the table data
for row, obj in enumerate(objects, start=1):
    data = [obj.key, obj.value, obj.description]
    for col, item in enumerate(data):
        data_label = ctk.CTkLabel(table_frame, text=item, width=10, height=2, corner_radius=4)
        data_label.grid(row=row, column=col, padx=5, pady=5)
    
    # Add a button in the last column
    action_button = ctk.CTkButton(table_frame, text="Edit", command=lambda obj=obj: on_button_press(obj))
    action_button.grid(row=row, column=len(headers)-1, padx=5, pady=5)

# Previous and Next Buttons
prev_button = ctk.CTkButton(nav_frame, text="Previous", command=prev_page) 
prev_button.pack(side=tk.LEFT, padx=5, pady=5) 
next_button = ctk.CTkButton(nav_frame, text="Next", command=next_page) 
next_button.pack(side=tk.RIGHT, padx=5, pady=5)

#endregion

# Create a customtkinter label 
label = ctk.CTkLabel(root, text="Directory Path", width=170, height=50, corner_radius=5) 
label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()

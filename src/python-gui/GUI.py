import tkinter
import customtkinter

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Dropdown menu options 
accounts = [ 
    "rwrd057",
    "rwrd058",
    "rwrd059"
    ] 

# Create the main window
app = customtkinter.CTk()
app.geometry("800x600")
app.title("My Application")

# Add Elements here

# Add a label
label = customtkinter.CTkLabel(app, text="SSM Selector!")
label.pack() 

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

# Add a combobox and set the initial value + callback event
def combobox_callback_account(choice):
    print("combobox account dropdown choice:", choice)

def combobox_callback_env(choice):
    print("combobox env dropdown clicked:", choice)

def combobox_callback_colour(choice):
    print("combobox colour dropdown clicked:", choice)

comboboxacc = customtkinter.CTkComboBox(master=app,
                                     values=accounts,
                                     command=combobox_callback_account)
comboboxacc.pack(padx=20, pady=10)
#comboboxacc.set("option 2")  # set initial value

comboboxenv = customtkinter.CTkComboBox(master=app,
                                     values=["option 1", "option 2"],
                                     command=combobox_callback_env)
comboboxenv.pack(padx=20, pady=10)
#comboboxenv.set("option 2")  # set initial value

comboboxcolour = customtkinter.CTkComboBox(master=app,
                                     values=["option 1", "option 2"],
                                     command=combobox_callback_colour)
comboboxcolour.pack(padx=20, pady=10)
#comboboxcolour.set("option 2")  # set initial value

def button_event():
    print("button pressed")

button = customtkinter.CTkButton(master=app, text="Search", command=button_event)
button.pack(padx=20, pady=10)


# Run
app.mainloop()
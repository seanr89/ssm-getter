import customtkinter as ctk
import tkinter as tk

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f'{self.name}, {self.age} years old, lives in {self.city}'

class PagedTable:
    def __init__(self, master, data, page_size):
        self.master = master
        self.data = data
        self.page_size = page_size
        self.current_page = 0

        self.table_frame = ctk.CTkFrame(master)
        self.table_frame.pack()

        self.table = ctk.CTkTextbox(self.table_frame, wrap=tk.WORD)
        self.table.pack(expand=True, fill=tk.BOTH)

        self.nav_frame = ctk.CTkFrame(master)
        self.nav_frame.pack()

        self.prev_button = ctk.CTkButton(self.nav_frame, text="Previous", command=self.previous_page)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = ctk.CTkButton(self.nav_frame, text="Next", command=self.next_page)
        self.next_button.pack(side=tk.RIGHT)

        self.update_table()

    def get_page_data(self):
        start = self.current_page * self.page_size
        end = start + self.page_size
        return self.data[start:end]

    def update_table(self):
        self.table.delete('1.0', tk.END)
        page_data = self.get_page_data()
        for person in page_data:
            self.table.insert(tk.END, f'{person}\n')

    def next_page(self):
        if (self.current_page + 1) * self.page_size < len(self.data):
            self.current_page += 1
            self.update_table()

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_table()

# Sample data
people = [
    Person("Alice", 30, "London"),
    Person("Bob", 25, "Manchester"),
    Person("Charlie", 35, "Bristol"),
    Person("Diana", 28, "Oxford"),
    Person("Eve", 22, "Cambridge"),
    # Add more Person objects as needed
]

root = ctk.CTk()
root.geometry("400x300")

paged_table = PagedTable(root, people, 2)  # Adjust page_size as needed

root.mainloop()

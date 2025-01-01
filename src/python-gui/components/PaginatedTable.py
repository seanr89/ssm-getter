import tkinter as tk
from customtkinter import CTk, CTkButton, CTkLabel, CTkFrame

# Paginated Table Component for incoming data
# No specific object yet defined
# Row structure is not working as expected!
class PaginatedTable(CTk):
    def __init__(self, data, headers, rows_per_page=5):
        super().__init__()
        self.data = data
        self.headers = headers
        self.rows_per_page = rows_per_page
        self.current_page = 0
        self.max_page = (len(data) - 1) // rows_per_page
        self.setup_ui()

    def setup_ui(self):
        self.title("Paginated Table")
        
        self.table_frame = CTkFrame(self)
        self.table_frame.pack(padx=10, pady=10)
        
        self.header_frame = CTkFrame(self.table_frame)
        self.header_frame.pack(padx=5, pady=5)
        
        for header in self.headers:
            header_label = CTkLabel(self.header_frame, text=header, font=("Arial", 12, "bold"))
            header_label.pack(side=tk.LEFT, padx=5, pady=2)
        
        self.page_label = CTkLabel(self, text=f"Page {self.current_page + 1} of {self.max_page + 1}")
        self.page_label.pack(pady=(10, 0))

        self.table_labels = []
        for _ in range(self.rows_per_page):
            row = []
            for _ in range(len(self.data[0])):
                label = CTkLabel(self.table_frame, text="")
                label.pack(side=tk.LEFT, padx=5, pady=2)
                row.append(label)
            self.table_labels.append(row)

        self.prev_button = CTkButton(self, text="Previous", command=self.prev_page)
        self.prev_button.pack(side=tk.LEFT, padx=(10, 5), pady=(10, 10))
        
        self.next_button = CTkButton(self, text="Next", command=self.next_page)
        self.next_button.pack(side=tk.RIGHT, padx=(5, 10), pady=(10, 10))

        self.update_table()

    def update_table(self):
        start_index = self.current_page * self.rows_per_page
        end_index = start_index + self.rows_per_page
        page_data = self.data[start_index:end_index]

        for row_labels in self.table_labels:
            for label in row_labels:
                label.configure(text="")

        for i, row_data in enumerate(page_data):
            for j, item in enumerate(row_data):
                self.table_labels[i][j].configure(text=item)

        self.page_label.configure(text=f"Page {self.current_page + 1} of {self.max_page + 1}")
    
    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_table()
    
    def next_page(self):
        if self.current_page < self.max_page:
            self.current_page += 1
            self.update_table()
### How to Create a Desktop Application with Python
### https://reintech.io/blog/how-to-create-a-desktop-application-with-python


import tkinter as tk
import sqlite3

class SampleApplication:
    def __init__(self, title="Python Desktop App", geometry="400x300"):
        self.databaseName = "names.db"

        # Create a database storing inputs (if none exists)
        SampleApplication.create_database(self.databaseName)

        # Initialise an application with GUI
        self.app = tk.Tk()
        self.app.title(title)
        self.app.geometry(geometry)

        # Add a prompt
        self.label = tk.Label(self.app, text="Enter your name:")
        self.label.pack()

        # Entry text box
        self.entry = tk.Entry(self.app)
        self.entry.pack()

        # Button field
        self.buttons = tk.Frame(self.app)
        self.buttons.pack()

        # Clear text option for entry text box
        self.clear_text = tk.Button(self.buttons, text="Clear", command=lambda: self.clear_field(self.entry))
        self.clear_text.pack(side=tk.LEFT)

        # Submit button
        self.submit_button = tk.Button(self.buttons, text="Submit", command=self.on_submit)
        self.submit_button.pack(side=tk.LEFT)

        # Exit button
        self.exit_button = tk.Button(self.buttons, text="Exit", command=self.app.destroy)
        self.exit_button.pack(side=tk.LEFT)

        # Listbox for displaying all available entries, with a scrollbar
        self.listbox_frame = tk.Frame(self.app)       # Create a frame
        self.listbox_frame.pack()

        self.listbox = tk.Listbox(self.listbox_frame)           # Create the listbox
        self.listbox.pack(side=tk.LEFT)

        self.scrollbar_listbox = tk.Scrollbar(self.listbox_frame)       # Verticle scrollbar for listbox
        self.scrollbar_listbox.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar_listbox.set)    # Integrate scrollbar to listbox
        self.scrollbar_listbox.config(command=self.listbox.yview)

        # Main loop
        self.update_listbox()
        self.app.mainloop()

    @staticmethod
    def create_database(databaseName):
        conn = sqlite3.connect(databaseName)
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS names (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                 )""")
        conn.commit()
        conn.close()

    @classmethod
    def clear_field(cls, display_field):
        display_field.delete(0, tk.END)

    def on_submit(self):
        name = self.entry.get()
        self.clear_field(self.entry)
        conn = sqlite3.connect(self.databaseName)
        c = conn.cursor()

        c.execute("INSERT INTO names (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()

        self.listbox.insert(tk.END, name)
        self.listbox.yview(tk.END)

    def update_listbox(self):
        conn = sqlite3.connect(self.databaseName)
        c = conn.cursor()

        c.execute("SELECT * FROM names")
        rows = c.fetchall()

        self.clear_field(self.listbox)
        for row in rows:
            self.listbox.insert(tk.END, row[1])

        conn.close()

def main():
    app = SampleApplication()

if __name__ == '__main__':
    main()
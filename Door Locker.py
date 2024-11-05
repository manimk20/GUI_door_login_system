import tkinter as tk
from tkinter import messagebox

# Function to check the credentials
def check_credentials():
    name = name_entry.get().title()
    password = password_entry.get()
    key_password = key_password_entry.get()

    # Loop through passcodes to find a match
    for passcode in passcodes:
        if name == passcode["name"] and password == passcode["password"] and key_password == passcode["key_password"]:
            messagebox.showinfo("Success", f"Hello, {name}")
            return
    messagebox.showerror("Error", "Wrong Passcode")

# Create the main window
root = tk.Tk()
root.title("Login System")

# Name input
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Password input
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")  # `show="*"` hides the text for password fields
password_entry.grid(row=1, column=1)

# Key password input
key_password_label = tk.Label(root, text="Key Password:")
key_password_label.grid(row=2, column=0)
key_password_entry = tk.Entry(root, show="*")
key_password_entry.grid(row=2, column=1)

# Login button
login_button = tk.Button(root, text="Login", command=check_credentials)
login_button.grid(row=3, columnspan=2)

# Passcode data (same as before)
passcodes = [
    {"name": "Steve", "password": "7888", "key_password": "0123456"},
    {"name": "Alexa", "password": "7888", "key_password": "0123456"},
    {"name": "Maxwell", "password": "7888", "key_password": "0123456"},
]

# Run the GUI application
root.mainloop()


import tkinter as tk
from tkinter import messagebox

# Function to handle the registration process
def register():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if not username or not email or not password or not confirm_password:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    if password != confirm_password:
        messagebox.showerror("Password Error", "Passwords do not match.")
        return

    # Here you can add code to store user information in a database or file
    messagebox.showinfo("Success", "Registration successful!")

# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("300x300")

# Create and place the labels and entry fields
label_username = tk.Label(root, text="Username")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_email = tk.Label(root, text="Email")
label_email.pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

label_password = tk.Label(root, text="Password")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show='*')
entry_password.pack(pady=5)

label_confirm_password = tk.Label(root, text="Confirm Password")
label_confirm_password.pack(pady=5)
entry_confirm_password = tk.Entry(root, show='*')
entry_confirm_password.pack(pady=5)

# Create and place the register button
register_button = tk.Button(root, text="Register", command=register)
register_button.pack(pady=20)

# Run the application
root.mainloop()

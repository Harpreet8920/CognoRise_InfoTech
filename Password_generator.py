import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_uppercase),  # At least one uppercase letter
        random.choice(string.ascii_lowercase),  # At least one lowercase letter
        random.choice(string.digits),  # At least one digit
        random.choice(string.punctuation),  # At least one special character
    ]

    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)

    return "".join(password)


def on_generate_click():
    try:
        length = int(entry_length.get())
        password = generate_password(length)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", "Something went wrong!")


def on_accept_click():
    username = entry_name.get()
    password = entry_password.get()
    if username and password:
        messagebox.showinfo("Accepted", f"Username: {username}\nPassword: {password}")
    else:
        messagebox.showerror(
            "Error", "Please enter your name and generate a password first."
        )


def on_reject_click():
    on_generate_click()


# Set up the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Title label
label_title = tk.Label(root, text="Password Generator", font=("Helvetica", 16))
label_title.pack(pady=10)

# User name frame
frame_name = tk.Frame(root)
frame_name.pack(pady=5)

label_name = tk.Label(frame_name, text="User Name:", font=("Helvetica", 12))
label_name.pack(side=tk.LEFT)

entry_name = tk.Entry(frame_name, width=20, font=("Helvetica", 12))
entry_name.pack(side=tk.LEFT, padx=10)

# Password length frame
frame_length = tk.Frame(root)
frame_length.pack(pady=5)

label_length = tk.Label(frame_length, text="Password Length:", font=("Helvetica", 12))
label_length.pack(side=tk.LEFT)

entry_length = tk.Entry(frame_length, width=5, font=("Helvetica", 12))
entry_length.pack(side=tk.LEFT, padx=10)

# Generate button
button_generate = tk.Button(
    root, text="Generate Password", command=on_generate_click, font=("Helvetica", 12)
)
button_generate.pack(pady=10)

# Password display entry
entry_password = tk.Entry(root, width=50, font=("Helvetica", 12))
entry_password.pack(pady=10)

# Accept and Reject buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_accept = tk.Button(
    frame_buttons, text="Accept", command=on_accept_click, font=("Helvetica", 12)
)
button_accept.pack(side=tk.LEFT, padx=10)

button_reject = tk.Button(
    frame_buttons, text="Reject", command=on_reject_click, font=("Helvetica", 12)
)
button_reject.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()

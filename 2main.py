import tkinter as tk
from tkinter import messagebox


accounts = {}  


def save_to_file():
    with open("systems.txt", "w") as file:
        for user, pin in accounts.items():
            file.write(f"{user},{pin}\n")

def load_from_file():
    try:
        with open("systems.txt", "r") as file:
            for line in file:
                user, pin = line.strip().split(",")
                accounts[user] = pin
    except FileNotFoundError:
        pass


window = tk.Tk()
window.title("Mini Banking System")
window.geometry("500x400")


Main_frame = tk.Frame(window)
Login_frame = tk.Frame(window)
Create_frame = tk.Frame(window)
Dashboard_frame = tk.Frame(window)

for frame in (Main_frame, Login_frame, Create_frame, Dashboard_frame):
    frame.grid(row=0, column=0, sticky="nsew")

def show_frame(frame):
    frame.tkraise()


def login():
    user = login_username_entry.get()
    pin = login_pin_entry.get()

    if user in accounts and accounts[user] == pin:
        show_frame(Dashboard_frame)
    else:
        messagebox.showerror("Login Failed", "Invalid username or PIN")


def create_account():
    user = create_username_entry.get()
    pin = create_pin_entry.get()

    if not user or not pin:
        messagebox.showerror("Error", "Fill in all fields")
        return

    if user in accounts:
        messagebox.showerror("Error", "Username already exists")
        return

    accounts[user] = pin
    save_to_file()
    messagebox.showinfo("Success", "Account created successfully")
    show_frame(Login_frame)


tk.Label(Main_frame, text="Mini Banking System", font=("Arial", 24)).pack(pady=40)

tk.Button(Main_frame, text="Login", width=20,
          command=lambda: show_frame(Login_frame)).pack(pady=10)

tk.Button(Main_frame, text="Create Account", width=20,
          command=lambda: show_frame(Create_frame)).pack(pady=10)


tk.Label(Login_frame, text="Login", font=("Arial", 20)).pack(pady=20)

tk.Label(Login_frame, text="Username").pack()
login_username_entry = tk.Entry(Login_frame)
login_username_entry.pack()

tk.Label(Login_frame, text="PIN").pack()
login_pin_entry = tk.Entry(Login_frame, show="*")
login_pin_entry.pack()

tk.Button(Login_frame, text="Login", command=login).pack(pady=15)
tk.Button(Login_frame, text="Back",
          command=lambda: show_frame(Main_frame)).pack()


tk.Label(Create_frame, text="Create Account", font=("Arial", 20)).pack(pady=20)

tk.Label(Create_frame, text="Create Username").pack()
create_username_entry = tk.Entry(Create_frame)
create_username_entry.pack()

tk.Label(Create_frame, text="Create PIN").pack()
create_pin_entry = tk.Entry(Create_frame, show="*")
create_pin_entry.pack()

tk.Button(Create_frame, text="Create Account",
          command=create_account).pack(pady=15)

tk.Button(Create_frame, text="Back",
          command=lambda: show_frame(Main_frame)).pack()


tk.Label(Dashboard_frame, text="Welcome to Your Dashboard",
         font=("Arial", 20)).pack(pady=50)

tk.Button(Dashboard_frame, text="Logout",
          command=lambda: show_frame(Main_frame)).pack()


load_from_file()
show_frame(Main_frame)
window.mainloop()
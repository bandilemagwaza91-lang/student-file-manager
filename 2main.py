import tkinter as tk
from tkinter import Label,Button

window=tk.Tk()
window.title("Mini banking system")
window.geometry("500x400")

Main_frame=tk.Frame(window)
LogIn_frame=tk.Frame(window)
Account_Creation_Frame=tk.Frame(window)



Main_frame.pack(fill="both", expand=True)
LogIn_frame.pack_forget()
Account_Creation_Frame.pack_forget()




def go_to_LogIn():
  Main_frame.pack_forget()
  LogIn_frame.pack(fill="both", expand=True)
     

def go_to_AccountCreation():
    Main_frame.pack_forget()
    Account_Creation_Frame.pack(fill="both", expand=True)

# Main page 
tk.Label(Main_frame,text="Hello", font=("Arial", 30)).pack(pady=20)

tk.Button(Main_frame, text="Login", command= go_to_LogIn).pack(pady=15) 
tk.Button(Main_frame, text="create Account", command=go_to_AccountCreation).pack(pady=15) 


# login
tk.Label(LogIn_frame, text="Bank Login", font=("Arial", 18)).pack(pady=20)

tk.Label(LogIn_frame, text="Username").pack()
username_entry = tk.Entry(LogIn_frame)
username_entry.pack()

tk.Label(LogIn_frame, text="PIN").pack()
pin_entry = tk.Entry(LogIn_frame, show="*")
pin_entry.pack()

#tk.Button(LogIn_frame, text="Login", command= Account_Creation_Frame).pack(pady=15)   

# creation of Account 


window.mainloop()
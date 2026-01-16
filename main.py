import tkinter as tk
from tkinter import simpledialog, messagebox

userName = []
userAge =[]

def Load_from_file():
    try:
        userName.clear()
        userAge.clear()

        with open("students.txt", "r") as file:
            for line in file:
                name, age = line.strip().split(",")
                userName.append(name)
                userAge.append(int(age))

        print("Students loaded successfully 📂")
    except FileNotFoundError:
        print("No saved file found. Please save first ❌")
        pass

def Save_to_file():
  with open("students.txt","w") as file:
      for i in range(len(userName)):
          file.write(userName[i]+","+str(userAge[i])+"\n")
  print("Students saved successfully 💾")

root = tk.Tk()
root.title("Mini Student System")
root.geometry("500x400")

    
 
def View_Students():
     if not userName:
      messagebox.showinfo("students","No students Avalable")
      return
     students_list = "\n".join([f"{userName[i]} - Age: {userAge[i]}" 
                                for i in range(len(userName))])
     messagebox.showinfo("Students", students_list)

def Add_student():

  name= simpledialog.askstring("Add students","Enter student name:")
  if not name:
     return
  try:
      age=int(simpledialog.askstring("Add student",f"Enter age for {name}:" ))
  except:
     messagebox.showerror("Error,","Invalid age!")
     return
     
  userName.append(name)
  userAge.append( age)
  Save_to_file()()
  messagebox.showinfo("Success", f"{name} added successfully ✅")


        
def Search_student():
 
   name = simpledialog.askstring("Search Student","Enter student name to search:")
   for i in range(len(userName)):
            if userName[i].lower() == name.lower():
                messagebox.showinfo("Found",f"Name: {userName[i]}, Age:{userAge[i]}")
            return
   messagebox.showinfo("Not Found", "Student not found ❌")
 


def Delete_student():
   

    delete_name = simpledialog.askstring("Delete Student", "Enter student name to delete:")
    

    for i in range(len(userName)):
        if userName[i].lower() == delete_name.lower():
            userName.pop(i)
            userAge.pop(i)
            Save_to_file()
            messagebox.showinfo("Deleted", f"{delete_name} deleted successfully ✅")

            return
    messagebox.showinfo("Not Found", "Student not found ❌")

tk.Button(root, text="View Students", width=25, command=View_Students).pack(pady=5)
tk.Button(root, text="Add Student", width=25, command=Add_student).pack(pady=5)
tk.Button(root, text="Search Student", width=25, command=Search_student).pack(pady=5)
tk.Button(root, text="Delete Student", width=25, command=Delete_student).pack(pady=5)
tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=5)

Load_from_file()  # load automatically at startup
root.mainloop()

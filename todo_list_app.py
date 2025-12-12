import tkinter as tk
from tkinter import messagebox

# ---- Add Task ----
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")

# ---- Delete Selected Task ----
def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "No task selected")

# ---- Save Tasks to File ----
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# ---- Load Tasks from File ----
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                listbox.insert(tk.END, task.strip())
    except:
        pass

# ---- UI Setup ----
root = tk.Tk()
root.title("To-Do List App")
root.geometry("350x450")
root.config(bg="#ffffff")

label = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"), bg="white")
label.pack(pady=10)

listbox = tk.Listbox(root, font=("Arial", 14), width=30, height=15)
listbox.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=20)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", font=("Arial", 14), command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", font=("Arial", 14), command=delete_task)
delete_button.pack(pady=5)

load_tasks()

root.mainloop()

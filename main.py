import tkinter as tk
from tkinter import messagebox, simpledialog

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to edit a selected task
def edit_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        current_task = task_listbox.get(selected_task_index)
        new_task = simpledialog.askstring("Edit Task", "Modify task:", initialvalue=current_task)
        if new_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit!")

# Function to save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Success", "Tasks saved successfully!")

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Input field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

edit_button = tk.Button(button_frame, text="Edit Task", command=edit_task)
edit_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

save_button = tk.Button(button_frame, text="Save Tasks", command=save_tasks)
save_button.grid(row=0, column=3, padx=5)

# Task Listbox
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Load tasks from file
load_tasks()

# Run the application
root.mainloop()


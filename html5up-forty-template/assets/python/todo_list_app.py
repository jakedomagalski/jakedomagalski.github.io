import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "The task cannot be empty!")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_as_done():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        # Remove the task and reinsert it with a strikethrough effect
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, f"✓ {task}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

# Set up the main application window
root = tk.Tk()
root.title("To-Do List Application")

# Create the entry widget
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Create the submit button
add_task_btn = tk.Button(root, text="Add Task", command=add_task)
add_task_btn.pack(pady=5)

# Create the listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=15)
tasks_listbox.pack()

# Create the delete button
delete_task_btn = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_task_btn.pack(pady=5)

# Create the mark as done button
mark_as_done_btn = tk.Button(root, text="Mark as Done", command=mark_as_done)
mark_as_done_btn.pack(pady=5)

# Start the main event loop
root.mainloop()

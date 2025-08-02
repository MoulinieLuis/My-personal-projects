from asyncio import Task
import tkinter as tk
from tkinter import Scrollbar, messagebox
from tkinter import ttk
from datetime import datetime

def add_task():
    task = task_entry.get().strip()
    date = date_entry.get().strip()
    hour = hour_entry.get().strip()

    
    if not task:
        messagebox.showwarning("Warning", "Please enter a task.")
        return
    
    if not date or not hour:
        messagebox.showwarning("Warning", "Please enter both date and hour.")
        return
    
    date_entry.config(bg="white")
    hour_entry.config(bg="white")

    try:
        datetime.strptime(f"{date} {hour}", "%Y-%m-%d %H:%M")
    except ValueError:
        messagebox.showerror("Error", "Invalid date or time format.")
        date_entry.config(bg="red")
        hour_entry.config(bg="red")
        return

    text = f"{task} - {date} {hour}"
    tasks_list.insert("", "end", values = (text, "Pending"))
    
    task_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    hour_entry.delete(0, tk.END)

    
def complete_task():
    selected_item = tasks_list.selection()
    if selected_item:
        for item in selected_item:
            task, state = tasks_list.item(item)["values"]
            if state == "Pending":
                tasks_list.item(item, values=(task, "Completed"))
            else:
                tasks_list.item(item, values=(task, "Pending"))

                
def delete_task():
    selected_item = tasks_list.selection()
    if selected_item:
        for item in selected_item:
            tasks_list.delete(item)
            
# Main screen configuration

window = tk.Tk()
window.title("To-Do App")
window.geometry("600x400")
window.resizable(True, True)

# Task entry
tk.Label(window, text="Task:").pack()
task_entry = tk.Entry(window, width=50)
task_entry.pack(pady=2)

# Date entry
tk.Label(window, text="Date (YYYY-MM-DD):").pack()
date_entry = tk.Entry(window, width=50)
date_entry.pack(pady=2)

# Hour entry
tk.Label(window, text="Hour (HH:MM):").pack()
hour_entry = tk.Entry(window, width=50)
hour_entry.pack(pady=2)

# Buttons
tk.Button(window, text="Add Task", command=add_task).pack(pady=5)
tk.Button(window, text="Complete Task", command=complete_task).pack(pady=5)
tk.Button(window, text="Delete Task", command=delete_task).pack(pady=5)

# Frame creation
frame = tk.Frame(window)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

columns = ("Task", "Status")
tasks_list = ttk.Treeview(frame, columns=columns, show="headings", height=10)

tasks_list.heading("Task", text="Task")
task_status = tasks_list.heading("Status", text="Status")
tasks_list.column("Task", anchor=tk.W, width=350)
tasks_list.column("Status", anchor=tk.W, width=100)

scrollbar = Scrollbar(frame, orient=tk.VERTICAL, command=tasks_list.yview)
tasks_list.configure(yscrollcommand=scrollbar.set)

tasks_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#Bottons
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add Task", command=add_task).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Complete Task", command=complete_task).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Delete Task", command=delete_task).pack(side=tk.LEFT, padx=5)

window.mainloop()
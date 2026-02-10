import tkinter as tk
from tkinter import messagebox

# ---------- Main Window ----------
root = tk.Tk()
root.title("Task Manager")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="#e3f2fd")

# ---------- Functions ----------
def add_task():
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task")
    else:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        task_list.delete(task_list.curselection())
    except:
        messagebox.showwarning("Warning", "Please select a task")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Do you want to clear all tasks?"):
        task_list.delete(0, tk.END)

def mark_done():
    try:
        index = task_list.curselection()[0]
        task = task_list.get(index)
        if not task.startswith("✔ "):
            task_list.delete(index)
            task_list.insert(index, "✔ " + task)
    except:
        messagebox.showwarning("Warning", "Please select a task")

def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

# ---------- Header ----------
header = tk.Label(
    root,
    text="Task Manager",
    bg="#1976d2",
    fg="white",
    font=("Arial", 26, "bold"),
    pady=15
)
header.pack(fill="x")

# ---------- Main Frame ----------
main_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
main_frame.place(x=80, y=120, width=640, height=420)

# ---------- Input ----------
tk.Label(
    main_frame,
    text="Enter New Task",
    bg="white",
    font=("Arial", 14, "bold")
).place(x=20, y=20)

task_entry = tk.Entry(
    main_frame,
    font=("Arial", 14),
    width=28,
    bd=2
)
task_entry.place(x=180, y=20)

# ---------- Listbox ----------
task_list = tk.Listbox(
    main_frame,
    font=("Arial", 14),
    height=12,
    width=30,
    bd=2,
    selectbackground="#bbdefb"
)
task_list.place(x=20, y=90)

# ---------- Buttons (Centered Vertically) ----------
button_style = {
    "font": ("Arial", 12, "bold"),
    "width": 16,
    "bd": 0,
    "cursor": "hand2"
}

button_start_y = 120   # shifted down for vertical alignment
button_gap = 50

tk.Button(main_frame, text="Add Task", bg="#4caf50", fg="white",
          command=add_task, **button_style).place(x=380, y=button_start_y)

tk.Button(main_frame, text="Delete Task", bg="#f44336", fg="white",
          command=delete_task, **button_style).place(x=380, y=button_start_y + button_gap)

tk.Button(main_frame, text="Mark as Done", bg="#2196f3", fg="white",
          command=mark_done, **button_style).place(x=380, y=button_start_y + 2 * button_gap)

tk.Button(main_frame, text="Clear All", bg="#ff9800", fg="white",
          command=clear_tasks, **button_style).place(x=380, y=button_start_y + 3 * button_gap)

tk.Button(main_frame, text="Exit", bg="#9e9e9e", fg="white",
          command=exit_app, **button_style).place(x=380, y=button_start_y + 4 * button_gap)

root.mainloop()

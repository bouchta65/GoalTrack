from tkinter import *
from controller import TaskManager
from tkinter import ttk
from tkinter import messagebox

home = Tk()
home.title("GoalTrack")
home.geometry("950x600")
home.config(bg='white')

# Title
lbl = Label(home, text="GoalTrack — Task Management Application", font=("Bold", 18), bg="white")
lbl.pack(pady=10)

# Task manager
manager = TaskManager()
tasks_data = manager.load_tasks()
    
tree_frame = Frame(home, bg="white")
tree_frame.pack(padx=10, pady=10)

statuses = ["To Do", "Doing", "Done"]
trees = {}

for i, status in enumerate(statuses):
    header = Label(home, text=status, bg="#d1e7dd", font=("Bold", 14))
    header.place(x=10 + i*310, y=50, width=300, height=30)
    
    tree = ttk.Treeview(home, columns=("Name", "Description", "Date"), show="headings", height=8)
    tree.place(x=10 + i*310, y=90, width=300, height=200)
    
    for col in ("Name", "Description", "Date"):
        tree.heading(col, text=col)
        tree.column(col, width=90)
    
    tree.tag_configure("Low", background="#d4edda")   
    tree.tag_configure("Medium", background="#fff3cd")  
    tree.tag_configure("High", background="#f8d7da")    

    trees[status] = tree

for task in tasks_data:
    tree = trees.get(task["status"])
    if tree:
        tree.insert("", END, iid=task["id"], values=(task["nom"], task["description"], task["date"]), tags=(task["priority"],))

input_frame = Frame(home, bg="#f0f0f0", bd=2, relief=RIDGE)
input_frame.place(x=9, y=289, width=921, height=180)

Label(input_frame, text="Name:", bg="#f0f0f0", font=("Arial", 10, "bold")).place(x=10, y=10)
entry_name = Entry(input_frame, bd=2, width=20)
entry_name.place(x=60, y=10)

Label(input_frame, text="Description:", bg="#f0f0f0", font=("Arial", 10, "bold")).place(x=230, y=10)
entry_desc = Entry(input_frame, bd=2, width=25)
entry_desc.place(x=320, y=10)

Label(input_frame, text="Priority:", bg="#f0f0f0", font=("Arial", 10, "bold")).place(x=580, y=10)
priority_options = ["Low", "Medium", "High"]
combo_priority = ttk.Combobox(input_frame, values=priority_options, width=10, state="readonly")
combo_priority.place(x=640, y=10)
combo_priority.current(0)

Label(input_frame, text="Status:", bg="#f0f0f0", font=("Arial", 10, "bold")).place(x=770, y=10)
combo_status = ttk.Combobox(input_frame, values=statuses, width=10, state="readonly")
combo_status.place(x=820, y=10)
combo_status.current(0)

def add_task():
    if entry_name.get()=="":
        messagebox.showerror("Input Error", "Task Name cannot be empty!")
    elif entry_desc.get()=="":
        messagebox.showerror("Input Error", "Task Description cannot be empty!")
    else:
        manager.add_tasks(entry_name.get(),entry_desc.get(),combo_priority.get(),combo_status.get())
        auto_refresh()

def update_task():
    selected_task = None
    for status, tree in trees.items():
        selected = tree.selection()
        if selected:
            selected_task = selected[0]  
            break

    if selected_task:
        nom = entry_name.get().strip() or None
        desc = entry_desc.get().strip() or None
        priority = combo_priority.get() or None
        status = combo_status.get() or None
        manager.update_tasks(selected_task, nom,desc,priority,status)
        auto_refresh()
    else:
        messagebox.showerror("Selection Error", "Please select a task to update!")

def delete_task():
    selected_task = None
    
    for status , tree in trees.items():
        selected = tree.selection()
        if selected:
            selected_task = selected[0]
            break
    if selected:
        manager.delete_task(selected_task)
        auto_refresh()
    else:
        messagebox.showerror("Selection Error", "Please select a task to update!")

def auto_refresh():
    for status, tree in trees.items():  
        for row in tree.get_children():
            tree.delete(row)
        
        for task in tasks_data:
            if task["status"] == status:
                tree.insert("", END, iid=task["id"], values=(task["nom"], task["description"], task["date"]), tags=(task["priority"],))
    


Button(input_frame, text="Add", bg="#5BA4FC", fg="white", width=15, font=("Arial", 10, "bold"), command=add_task).place(x=220, y=60)
Button(input_frame, text="Update", bg="#FFC107", fg="white", width=15, font=("Arial", 10, "bold"), command=update_task).place(x=380, y=60)
Button(input_frame, text="Delete", bg="#DC3545", fg="white", width=15, font=("Arial", 10, "bold"), command=delete_task).place(x=540, y=60)


home.mainloop()
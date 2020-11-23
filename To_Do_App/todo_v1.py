"""
Created on 23.11.2020

@author: dafr
"""
import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List")

# Functions
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(tkinter.END, task)
        entry_task.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task")

def delete_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task")

def load_task():
    try:
        task = pickle.load(open("task.dat", "rb"))
        listbox_task.delete(0, tkinter.END)
        for task in task:
            listbox_task.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat")

def save_task():
    task = listbox_task.get(0, listbox_task.size())
    pickle.dump(task, open("task.dat", "wb"))

# Create GUI    
# Frame
frame_task = tkinter.Frame(root)
frame_task.pack()

listbox_task = tkinter.Listbox(frame_task, height=10, width=50)
listbox_task.pack(side=tkinter.LEFT)

# Scrollbar
scrollbar_task = tkinter.Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Task input
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

# Buttons
button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_load_task = tkinter.Button(root, text="Load task", width=48, command=load_task)
button_load_task.pack()

button_save_task = tkinter.Button(root, text="Save task", width=48, command=save_task)
button_save_task.pack()

root.mainloop()

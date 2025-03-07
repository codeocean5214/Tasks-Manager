import tkinter as tk
from tkinter import messagebox,filedialog

#we will create a class called tasks that will we see  if the taks complete or not and whats the description 
class Task : 
    def __init__(self,name,completion_status = False) : 
        self.name = name 
        self.completion_status = completion_status
    
    def tasks_complete_markup(self):
        self.completion_status = True

    def __str__(self):
        status = "✔" if self.completion_status else "✘"
        return f"{status} {self.name}"
    
#the tasks will be stored somewhere and the best data stucture to store them is lists
#we create a global list to store data   
tasks = []

def addtasks() : 
    newtk= new_tasks_entry.get().strip()
    
    if newtk  : 
        tasks.append(newtk)
        updated_tasks()
        new_tasks_entry.delete(0, tk.END)
    else: 
        messagebox.showerror(message="you have not entered any tasks!")
def markcomplete() : 
    try :
       sel_indx = int(task_textbox.curselection()[0])
       tasks.pop(sel_indx)
       updated_tasks()
    except IndexError:
        messagebox.showerror("Error", "No task selected!")

def updated_tasks(): 
    task_textbox.delete(0, tk.END)  # Clear the Listbox
    for task in tasks:
        task_textbox.insert(tk.END, str(task))
#gui

root = tk.Tk()
root.title("Todo list App")
root.maxsize(width=500,height=700)
#creating the tasks window
todo_list_head = tk.Label(root, text = "Tasks Lists: ")
todo_list_head.grid(row=0,column=0 ,pady=(10,20))

#creating a writing window  
new_tasks_entry =  tk.Entry(root, width= 30 )
new_tasks_entry.grid(row=0,column=1)
#creating the buttons 
Add_tasks  = tk.Button(root, text="Add task",command=addtasks)
delete_tasks = tk.Button(root, text="Delete tasks")
mark_comp= tk.Button(root, text="Mark Complete",command=markcomplete) 
#= tk.Button(root, text="Button 4")


Add_tasks.grid(row=1,column=0,pady=10)
delete_tasks.grid(row=1,column=1,pady=10)
mark_comp.grid(row=1,column=2,pady=10)

#creating a textbox to store the tasks
task_textbox = tk.Listbox(root, height=20, width=55, state='normal')
task_textbox.grid(row=2, column=0, columnspan=3, padx=10, pady=20)
root.mainloop()

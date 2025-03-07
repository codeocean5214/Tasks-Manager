import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo List")
        self.root.geometry("400x500")
        
        # List to store tasks (task_text, completed_status)
        self.tasks = []
        
        # Title Label
        self.title_label = tk.Label(root, text="My Tasks", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)
        
        # Task List Frame with Scrollbar
        self.list_frame = tk.Frame(root)
        self.list_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.task_listbox = tk.Listbox(self.list_frame, height=15, font=("Arial", 12))
        self.task_listbox.pack(side="left", fill="both", expand=True)
        
        self.scrollbar = tk.Scrollbar(self.list_frame, orient="vertical")
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        
        # Entry Frame for input and buttons
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=10, padx=10)
        
        # Task Entry
        self.task_entry = tk.Entry(self.entry_frame, width=30, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=5)
        
        # Add Button
        self.add_button = tk.Button(self.entry_frame, text="Add Task", 
                                  command=self.add_task, font=("Arial", 10))
        self.add_button.grid(row=0, column=1, padx=5)
        
        # Control Buttons Frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        
        # Complete Button
        self.complete_button = tk.Button(self.button_frame, text="Mark Complete", 
                                       command=self.mark_complete, font=("Arial", 10))
        self.complete_button.grid(row=0, column=0, padx=5)
        
        # Delete Button
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", 
                                     command=self.delete_task, font=("Arial", 10))
        self.delete_button.grid(row=0, column=1, padx=5)
        
        # Bind Enter key to add task
        self.root.bind('<Return>', lambda event: self.add_task())

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append([task_text, False])
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task, completed in self.tasks:
            display_text = f"[✓] {task}" if completed else f"[ ] {task}"
            self.task_listbox.insert(tk.END, display_text)

    def mark_complete(self):
        try:
            selected_idx = self.task_listbox.curselection()[0]
            self.tasks[selected_idx][1] = not self.tasks[selected_idx][1]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")

    def delete_task(self):
        try:
            selected_idx = self.task_listbox.curselection()[0]
            del self.tasks[selected_idx]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        
        self.tasks = []

        self.task_entry = tk.Entry(master, width=40, font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, font=("Helvetica", 10))
        self.add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=10)

        self.task_listbox = tk.Listbox(master, width=50, height=15, font=("Helvetica", 12))
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task, font=("Helvetica", 10))
        self.remove_button.grid(row=2, column=0, padx=5, pady=5, ipadx=10)

        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_all, font=("Helvetica", 10))
        self.clear_button.grid(row=2, column=1, padx=5, pady=5, ipadx=10)

        self.update_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def clear_all(self):
        self.tasks = []
        self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

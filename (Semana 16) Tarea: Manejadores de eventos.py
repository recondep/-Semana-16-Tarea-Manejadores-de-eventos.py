import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Tareas")
        self.root.bind("<Return>", self.add_task)
        self.root.bind("c", self.mark_as_completed)
        self.root.bind("d", self.delete_task)
        self.root.bind("<Escape>", self.close_app)

        self.task_list = tk.Listbox(root, width=50)
        self.task_list.pack(padx=15, pady=15)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(padx=15, pady=15)

        self.add_button = tk.Button(root, text="Agregar Tarea", command=self.add_task)
        self.add_button.pack(padx=15, pady=15)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_as_completed)
        self.complete_button.pack(padx=15, pady=15)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(padx=15, pady=15)

        self.clear_button = tk.Button(root, text="Limpiar Lista", command=self.clear_list)
        self.clear_button.pack(padx=15, pady=15)

    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def mark_as_completed(self, event=None):
        selected_task = self.task_list.curselection()
        if selected_task:
            task = self.task_list.get(selected_task)
            self.task_list.delete(selected_task)
            self.task_list.insert(tk.END, f"[COMPLETADA] {task}")

    def delete_task(self, event=None):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.task_list.delete(selected_task)

    def clear_list(self):
        self.task_list.delete(0, tk.END)

    def close_app(self, event=None):
        if messagebox.askokcancel("Cerrar Aplicación", "¿Estás seguro de que deseas cerrar la aplicación?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

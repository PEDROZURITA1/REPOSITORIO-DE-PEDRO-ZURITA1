import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea
def add_task(event=None):
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

# Función para marcar una tarea como completada
def complete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(selected_task_index)
        completed_task = f"[Completada] {task_text}"
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(selected_task_index, completed_task)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcarla como completada.")

# Función para eliminar una tarea
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminarla.")

# Configuración de la ventana principal
app = tk.Tk()
app.title("Lista de Tareas")

# Campo de entrada para las tareas
entry_task = tk.Entry(app, width=40)
entry_task.pack(pady=10)
entry_task.bind("<Return>", add_task)  # Permite añadir tareas presionando Enter

# Botones para añadir, completar y eliminar tareas
frame_buttons = tk.Frame(app)
frame_buttons.pack()

btn_add = tk.Button(frame_buttons, text="Añadir Tarea", command=add_task)
btn_add.pack(side=tk.LEFT, padx=5)

btn_complete = tk.Button(frame_buttons, text="Marcar como Completada", command=complete_task)
btn_complete.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(frame_buttons, text="Eliminar Tarea", command=delete_task)
btn_delete.pack(side=tk.LEFT, padx=5)

# Listbox para mostrar las tareas
listbox_tasks = tk.Listbox(app, width=50, height=15, selectmode=tk.SINGLE)
listbox_tasks.pack(pady=10)

# Iniciar la aplicación
app.mainloop()

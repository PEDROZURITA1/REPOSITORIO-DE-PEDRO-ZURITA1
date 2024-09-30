import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Tareas")
        self.geometry("300x400")

        # Crear widgets
        self.entry_tarea = tk.Entry(self)
        self.entry_tarea.pack(pady=10)
        self.btn_agregar = tk.Button(self, text="Agregar", command=self.agregar_tarea)
        self.btn_agregar.pack()
        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.btn_marcar = tk.Button(self, text="Marcar como Completada", command=self.marcar_completada)
        self.btn_marcar.pack()
        self.btn_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_tarea)
        self.btn_eliminar.pack()

        # Bindear eventos
        self.entry_tarea.bind("<Return>", self.agregar_tarea)
        self.listbox.bind("<Delete>", self.eliminar_tarea)
        self.listbox.bind("c", self.marcar_completada)
        self.bind("<Escape>", self.destroy)

        # Lista para almacenar las tareas
        self.tareas = []

    def agregar_tarea(self, event=None):
        tarea = self.entry_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.listbox.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)

    def marcar_completada(self, event=None):
        index = self.listbox.curselection()
        if index:
            tarea = self.tareas[index[0]]
            self.listbox.delete(index)
            self.listbox.insert(index, f"✅ {tarea}")

    def eliminar_tarea(self, event=None):
        index = self.listbox.curselection()
        if index:
            self.listbox.delete(index)
            del self.tareas[index[0]]

if __name__ == "__main__":
    app = App()
    app.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Función para agregar un nuevo evento
def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    if fecha and hora and descripcion:
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        limpiar_campos()
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

# Función para limpiar campos después de agregar un evento
def limpiar_campos():
    fecha_entry.set_date("")
    hora_entry.delete(0, tk.END)
    descripcion_entry.delete(0, tk.END)

# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        tree.delete(seleccionado)
    else:
        messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("500x400")

# Frame para mostrar la lista de eventos
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

# Definir las columnas del TreeView
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Frame para los campos de entrada
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Etiquetas y campos de entrada
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
fecha_entry = DateEntry(frame_entrada)
fecha_entry.grid(row=0, column=1)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
hora_entry = tk.Entry(frame_entrada)
hora_entry.grid(row=1, column=1)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
descripcion_entry = tk.Entry(frame_entrada)
descripcion_entry.grid(row=2, column=1)

# Frame para los botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Botones de acción
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit)
btn_salir.grid(row=0, column=2, padx=5)

# Ejecutar la ventana
ventana.mainloop()

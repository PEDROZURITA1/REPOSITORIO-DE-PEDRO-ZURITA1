import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entry.get()
    if dato:
        listbox.insert(tk.END, dato)
        entry.delete(0, tk.END)  # Limpiar campo de texto
    else:
        messagebox.showwarning("Advertencia", "Ingrese información antes de agregar.")

# Función para limpiar la lista de datos
def limpiar_datos():
    listbox.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Datos")

# Etiqueta
label = tk.Label(ventana, text="Ingrese información:")
label.pack(pady=10)

# Campo de texto
entry = tk.Entry(ventana, width=40)
entry.pack(pady=5)

# Botón para agregar datos
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

# Lista para mostrar los datos agregados
listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=10)

# Botón para limpiar datos
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
btn_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()


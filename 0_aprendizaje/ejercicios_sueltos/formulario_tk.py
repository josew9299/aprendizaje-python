import tkinter as tk
from tkinter import messagebox

def enviar():
    respuestas = [entry.get() for entry in entradas]

    if any(r.strip() == "" for r in respuestas):
        messagebox.showwarning("Error", "Responde todas las preguntas")
        return

    messagebox.showinfo("Formulario enviado", "Gracias por responder")


# Ventana principal
ventana = tk.Tk()
ventana.title("Formulario simple")
ventana.geometry("420x220")

# Preguntas
preguntas = [
    "Nombre",
    "Edad",
    "Ciudad",
    "Lenguaje que estudias",
    "Objetivo con Python"
]

entradas = []

# Crear etiquetas y entradas
for i, pregunta in enumerate(preguntas):
    label = tk.Label(ventana, text=pregunta)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

    entry = tk.Entry(ventana, width=30)
    entry.grid(row=i, column=1, padx=10, pady=5)

    entradas.append(entry)

# Botón enviar
btn = tk.Button(ventana, text="Enviar", command=enviar)
btn.grid(row=len(preguntas), column=0, columnspan=2, pady=15)

ventana.mainloop()

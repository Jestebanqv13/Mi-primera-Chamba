import os
from tkinter import *
from tkinter import messagebox, simpledialog
from tabulate import tabulate
import base64
from PIL import Image, ImageTk

class ListaDeTareas:
    def __init__(self):
        self.tareas = []
        self.notas = []
        self.plantillas = {"Plantilla 1": ["Tarea 1", "Tarea 2", "Tarea 3"],
                           "Plantilla 2": ["Tarea A", "Tarea B", "Tarea C"]}

    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "completa": False})

    def eliminar_tarea(self, tarea):
        self.tareas = [t for t in self.tareas if t["tarea"] != tarea]

    def marcar_como_completada(self, tarea):
        for t in self.tareas:
            if t["tarea"] == tarea:
                t["completa"] = True

    def mostrar_tareas(self):
        if not self.tareas:
            messagebox.showinfo("Informacion", "No se encontró ninguna tarea.")
        else:
            table = []
            for i, tarea in enumerate(self.tareas, 1):
                estado = "Completo" if tarea["completa"] else "Pendiente"
                table.append([i, tarea['tarea'], estado])
            result = tabulate(table, headers=["ID", "Tarea", "Estado"], tablefmt="grid")
            messagebox.showinfo("Tareas", result)

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def mostrar_notas(self):
        if not self.notas:
            messagebox.showinfo("Informacion", "No se encontró ninguna nota.")
        else:
            for i, nota in enumerate(self.notas, 1):
                messagebox.showinfo(f"Nota {i}", nota)

    def mostrar_plantillas(self):
        plantillas = list(self.plantillas.keys())
        seleccion = simpledialog.askstring("Seleccionar Plantilla", "Seleccione una plantilla:", initialvalue=plantillas[0], parent= window)
        if seleccion in self.plantillas:
            tareas = self.plantillas[seleccion]
            for i, tarea in enumerate(tareas, 1):
                messagebox.showinfo(f"Tarea {i}", tarea)
        else:
            messagebox.showerror("Error", "Plantilla no encontrada.")

def main():
    lista_tareas = ListaDeTareas()

    def agregar_tarea():
        tarea = entrada_tarea.get()
        if not tarea:
            messagebox.showerror("Error", "No se encontró ninguna tarea.")
            return
        lista_tareas.agregar_tarea(tarea)
        entrada_tarea.delete(0, END)
        actualizar_lista()

    def eliminar_tarea():
        tarea = entrada_tarea.get()
        if not tarea:
            messagebox.showerror("Error", "No se encontró ninguna tarea.")
            return
        lista_tareas.eliminar_tarea(tarea)
        entrada_tarea.delete(0, END)
        actualizar_lista()

    def marcar_como_completada():
        tarea = entrada_tarea.get()
        if not tarea:
            messagebox.showerror("Error", "Ingrese una tarea.")
            return
        lista_tareas.marcar_como_completada(tarea)
        entrada_tarea.delete(0, END)
        actualizar_lista()

    def mostrar_tareas():
        lista_tareas.mostrar_tareas()

    def agregar_nota():
        nota = texto_nota.get(1.0, END)
        if not nota.strip():
            messagebox.showerror("Error", "La nota está vacía.")
            return
        lista_tareas.agregar_nota(nota)
        texto_nota.delete(1.0, END)
        mostrar_estado("Nota agregada exitosamente.")

    def mostrar_notas():
        lista_tareas.mostrar_notas()

    def mostrar_plantillas():
        lista_tareas.mostrar_plantillas()

    def actualizar_lista():
        lista_box.delete(0, END)
        for tarea in lista_tareas.tareas:
            estado = "Completo" if tarea["completa"] else "Pendiente"
            lista_box.insert(END, f"{tarea['tarea']} - {estado}")

    def mostrar_estado(mensaje):
        messagebox.showinfo("Estado", mensaje)

    window = Tk()
    window.title("Lista de Tareas y Notas")

    # Configuración de colores y estilo
    window.configure(bg="#ffffff")  # Fondo blanco
    window.geometry("800x600")  # Tamaño de la ventana
    window.attributes('-fullscreen', True)  # Pantalla completa
    
    # Cargar imágenes y convertirlas a base64
    img_agregar_tarea = ImageTk.PhotoImage(
        Image.open("/home/esteban/Downloads/agregartarea.jpg").resize((20, 20)))
    img_eliminar_tarea = ImageTk.PhotoImage(
        Image.open("/home/esteban/Downloads/eliminartarea.jpg").resize((20, 20)))
    img_completar_tarea = ImageTk.PhotoImage(
        Image.open("/home/esteban/Downloads/completartarea.jpg").resize((20, 20)))
    img_mostrar_tareas = ImageTk.PhotoImage(
        Image.open("/home/esteban/Downloads/mostrartarea.jpg").resize((20, 20)))
    img_agregar_nota = ImageTk.PhotoImage(
        Image.open("/home/esteban/Downloads/agregartarea.jpg").resize((20, 20)))
    img_mostrar_notas = ImageTk.PhotoImage(
        Image.open("/home/esteban/Downloads/mostrartarea.jpg").resize((20, 20)))
    img_mostrar_plantillas = ImageTk.PhotoImage(
        Image.open("/home/esteban/Downloads/mostrartarea.jpg").resize((20, 20)))   

    # Bloque de entrada de tarea
    etiqueta_tarea = Label(window, text="Tarea Nueva:", font=("Helvetica", 12), bg="#ffffff")
    etiqueta_tarea.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    entrada_tarea = Entry(window, width=50, font=("Helvetica", 12))
    entrada_tarea.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    # Bloque de botones para tareas
    btn_agregar_tarea = Button(window, image=img_agregar_tarea, borderwidth=0, command=agregar_tarea)
    btn_agregar_tarea.grid(row=1, column=0, columnspan=2, pady=10)

    btn_eliminar_tarea = Button(window, image=img_eliminar_tarea, borderwidth=0, command=eliminar_tarea)
    btn_eliminar_tarea.grid(row=2, column=0, columnspan=2, pady=10)

    btn_completada = Button(window, image=img_completar_tarea, borderwidth=0, command=marcar_como_completada)
    btn_completada.grid(row=3, column=0, columnspan=2, pady=10)

    btn_mostrar_tareas = Button(window, image=img_mostrar_tareas, borderwidth=0, command=mostrar_tareas)
    btn_mostrar_tareas.grid(row=4, column=0, columnspan=2, pady=10)

    # Lista de tareas
    lista_box = Listbox(window, selectbackground="#a6a6a6", selectforeground="white", font=("Helvetica", 12))
    lista_box.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky=W+E)

    # Bloque de entrada de notas
    etiqueta_nota = Label(window, text="Nueva Nota:", font=("Helvetica", 12), bg="#ffffff")
    etiqueta_nota.grid(row=6, column=0, padx=10, pady=10, sticky=W)

    texto_nota = Text(window, width=50, height=5, font=("Helvetica", 12))
    texto_nota.grid(row=6, column=1, padx=10, pady=10, sticky=W)

    # Bloque de botones para notas
    btn_agregar_nota = Button(window, image=img_agregar_nota, borderwidth=0, command=agregar_nota)
    btn_agregar_nota.grid(row=7, column=0, columnspan=2, pady=10)

    btn_mostrar_notas = Button(window, image=img_mostrar_notas, borderwidth=0, command=mostrar_notas)
    btn_mostrar_notas.grid(row=8, column=0, columnspan=2, pady=10)

    # Bloque de botones para plantillas
    btn_mostrar_plantillas = Button(window, image=img_mostrar_plantillas, borderwidth=0, command=mostrar_plantillas)
    btn_mostrar_plantillas.grid(row=9, column=0, columnspan=2, pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()

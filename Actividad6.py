# actividad 6 y final de Poo

from tkinter import *
from tkinter import filedialog, messagebox

class ManejoArchivo:
    def __init__(self, texto_Escrito):
        self.texto_Escrito = texto_Escrito
        self.TXT_actual = None

    def crear(self):
        self.TXT_actual = None
        self.texto_Escrito.delete(1.0, END)

    def abrir(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, "r") as file:
                texto_abierto = file.read()
            self.texto_Escrito.delete(1.0, END)
            self.texto_Escrito.insert(END, texto_abierto)
            self.TXT_actual = archivo 

    def cerrar(self):
        self.TXT_actual = None
        self.texto_Escrito.delete(1.0, END)
        messagebox.showinfo("Cerrar Archivo", "Archivo cerrado correctamente.")

    def modificar(self):
        if self.TXT_actual:
            with open(self.TXT_actual, "w") as file:
                file.write(self.texto_Escrito.get(1.0, END))
            messagebox.showinfo("Modificar", "Archivo modificado correctamente.")
        else:
            messagebox.showwarning("Modificar", "No existe archivo abierto para modificar.")

    def guardarComo(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, "w") as file:
                file.write(self.texto_Escrito.get(1.0, END))
            self.TXT_actual = archivo
            messagebox.showinfo("Guardar Como", "El archivo se ha guardado correctamente.")

pantalla = Tk()
pantalla.title("Manejo de archivos")
pantalla.geometry("500x400")

pantalla.config(bg="SlateGray1")

Texto_Pant = Text(pantalla, width=60, height=15)
Texto_Pant.pack(pady=20)

Manejador_archivo = ManejoArchivo(Texto_Pant)

OpcioArchivoMenu = Menu(pantalla)
pantalla.config(menu=OpcioArchivoMenu)

Menu_opcion = Menu(OpcioArchivoMenu, tearoff=0)
Menu_opcion.add_command(label="Crear", command=Manejador_archivo.crear)
Menu_opcion.add_command(label="Abrir", command=Manejador_archivo.abrir)
Menu_opcion.add_command(label="Modificar", command=Manejador_archivo.modificar)
Menu_opcion.add_command(label="Guardar como", command=Manejador_archivo.guardarComo)
Menu_opcion.add_separator()
Menu_opcion.add_command(label="Cerrar", command=Manejador_archivo.cerrar)

OpcioArchivoMenu.add_cascade(label="Opciones", menu=Menu_opcion)

pantalla.mainloop()

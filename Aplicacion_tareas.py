import tkinter as tk
from tkinter import messagebox


class AplicacionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.tareas = []

        self.crear_interfaz()
        self.asignar_atajos()

    def crear_interfaz(self):
        frame_superior = tk.Frame(self.root, pady=10)
        frame_superior.pack(fill="x")

        self.entry_tarea = tk.Entry(frame_superior, font=("Arial", 12))
        self.entry_tarea.pack(side="left", padx=10, fill="x", expand=True)
        self.entry_tarea.focus()

        btn_agregar = tk.Button(
            frame_superior,
            text="Añadir tarea",
            width=15,
            command=self.agregar_tarea
        )
        btn_agregar.pack(side="left", padx=5)

        frame_lista = tk.Frame(self.root)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

        self.lista_tareas = tk.Listbox(
            frame_lista,
            font=("Arial", 12),
            selectmode=tk.SINGLE,
            height=15
        )
        self.lista_tareas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame_lista, orient="vertical")
        scrollbar.config(command=self.lista_tareas.yview)
        scrollbar.pack(side="right", fill="y")

        self.lista_tareas.config(yscrollcommand=scrollbar.set)

        frame_botones = tk.Frame(self.root, pady=10)
        frame_botones.pack(fill="x")

        btn_completar = tk.Button(
            frame_botones,
            text="Marcar como completada",
            width=20,
            command=self.marcar_completada
        )
        btn_completar.pack(side="left", padx=10)

        btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar tarea",
            width=15,
            command=self.eliminar_tarea
        )
        btn_eliminar.pack(side="left", padx=10)

        btn_salir = tk.Button(
            frame_botones,
            text="Salir",
            width=10,
            command=self.root.destroy
        )
        btn_salir.pack(side="right", padx=10)

        # Colores para feedback visual
        self.lista_tareas.config(bg="white")
        self.lista_tareas.bind("<<ListboxSelect>>", lambda e: None)

    def asignar_atajos(self):
        self.root.bind("<Return>", lambda event: self.agregar_tarea())
        self.root.bind("<c>", lambda event: self.marcar_completada())
        self.root.bind("<C>", lambda event: self.marcar_completada())
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())
        self.root.bind("<d>", lambda event: self.eliminar_tarea())
        self.root.bind("<D>", lambda event: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda event: self.root.destroy())

    def agregar_tarea(self):
        texto = self.entry_tarea.get().strip()
        if not texto:
            messagebox.showwarning("Aviso", "Escribe una tarea antes de añadir.")
            return

        self.tareas.append({"texto": texto, "completada": False})
        self.actualizar_lista()
        self.entry_tarea.delete(0, tk.END)

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if not seleccion:
            messagebox.showinfo("Información", "Selecciona una tarea para marcarla.")
            return

        indice = seleccion[0]
        self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
        self.actualizar_lista()
        self.lista_tareas.selection_set(indice)

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if not seleccion:
            messagebox.showinfo("Información", "Selecciona una tarea para eliminarla.")
            return

        indice = seleccion[0]
        del self.tareas[indice]
        self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)

        for i, tarea in enumerate(self.tareas):
            if tarea["completada"]:
                texto_mostrado = f"[✔] {tarea['texto']}"
            else:
                texto_mostrado = f"[ ] {tarea['texto']}"

            self.lista_tareas.insert(tk.END, texto_mostrado)

            if tarea["completada"]:
                self.lista_tareas.itemconfig(i, fg="gray")
            else:
                self.lista_tareas.itemconfig(i, fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTareas(root)
    root.mainloop()

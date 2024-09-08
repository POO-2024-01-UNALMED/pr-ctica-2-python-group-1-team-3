from tkinter import Frame, Label, Entry, Grid, Button, messagebox

class FieldFrame(Frame):

    def __init__(self, frame, tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__(frame)

        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores
        self.habilitado = habilitado

        self.dict = {}

        # Crear los campos de texto
        for i, criterio in enumerate(self.criterios):
            label = Label(self, text=criterio, font=("Georgia", 12, "bold"), border=2, relief="sunken")
            entry = Entry(self, font=("Georgia", 10))

            # Inserta valores iniciales si se proporcionan
            if valores is not None:
                if i < len(self.valores):
                    entry.insert(0, self.valores[i])

            # Controla si los campos deben estar habilitados o no
            if self.habilitado:
                entry.config(state="disabled" if not self.habilitado else "normal")

            label.grid(row=i, column=0, padx=5, pady=5)
            entry.grid(row=i, column=1, padx=5, pady=5)

            self.dict[criterio] = entry

    # Obtener valor de un criterio
    def getValue(self, criterio):
        return self.dict[criterio].get()

    # Obtener el Entry de un criterio específico
    def getEntry(self, criterio):
        return self.dict[criterio]

    # Obtener campos vacíos
    def getEntrysVacios(self):
        entrysVacios = []
        for criterio in self.criterios:
            if self.getEntry(criterio).get() == "":
                entrysVacios.append(criterio)
        return entrysVacios
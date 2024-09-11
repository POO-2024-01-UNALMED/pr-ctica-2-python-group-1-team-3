from tkinter import Frame, Label, Entry, Grid, Button, messagebox

class FieldFrame(Frame):

    def __init__(self, frame, tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__(frame)

        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores if valores is not None else []  # Si valores es None, lo asignamos a una lista vacía
        self.habilitado = habilitado

        self.entries = {}

        for idx in range(len(criterios)):
            criterio = criterios[idx]
            
            lbl = Label(self, text=criterio, font=("Georgia", 12, "bold"), border=2, relief="sunken")
            lbl.grid(row=idx, column=0, padx=5, pady=3)
            
            entry_widget = Entry(self, font=("Georgia", 10))
            entry_widget.grid(row=idx, column=1, padx=5, pady=3)

            # Inserción de valores iniciales si existen
            if idx < len(self.valores):
                entry_widget.insert(0, str(self.valores[idx]))
            
            # Control de habilitación de los campos
            if idx < len(self.habilitado) and not self.habilitado[idx]:
                entry_widget.config(state="disabled")

            self.entries[criterio] = entry_widget

    def getValue(self, criterio):
        # Retorna el valor del Entry asociado al criterio
        entry = self.entries.get(criterio, None)
        return entry.get() if entry else None

    def getEntry(self, criterio):
        # Retorna el Entry asociado al criterio
        return self.entries.get(criterio, None)

    def getEntrysVacios(self):
        # Recorre los criterios y verifica cuáles Entries están vacíos
        vacios = [criterio for criterio in self.criterios if not self.entries[criterio].get()]
        return vacios
        
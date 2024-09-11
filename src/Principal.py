# Archivo: src/principal.py

import sys
import os

# Asegura que el sistema pueda encontrar los módulos del proyecto
sys.path.append(os.path.dirname(__file__))

# Importamos el archivo main de UiMain.Ventanas
from UiMain.Ventanas.VentanaPrincipal import VentanaPrincipal

if __name__ == "__main__":
    # Ejecutamos la lógica de main.py
    ventana = VentanaPrincipal()
    ventana.mainloop()

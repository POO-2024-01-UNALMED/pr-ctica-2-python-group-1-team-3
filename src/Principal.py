import sys
import os

# Asegura que el sistema pueda encontrar los módulos del proyecto
sys.path.append(os.path.dirname(__file__))

from UiMain.Ventanas import main

if __name__ == "__main__":
    main.ventanaMain.mainloop()  # Inicia el bucle de eventos

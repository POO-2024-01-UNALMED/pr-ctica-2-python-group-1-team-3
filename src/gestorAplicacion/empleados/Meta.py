# Este módulo pertenece al paquete 'gestorAplicacion.empleados' y contiene la clase 'Meta', que define las 
# características y comportamientos de las diferentes metas que se les pueden dar a los empleados, estas metas
# permiten verificar el cumplimiento de estas metas y dar bonificaciones por su cumplimiento.
# 
# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

import pickle

class Meta:
    # La clase 'Meta' representa una meta de rendimiento para los empleados, incluyendo el nivel de la meta, 
    # el valor mínimo a alcanzar y la comisión por cumplir la meta.
    #
    # Funcionalidades en las que se usa: 
    #      - Pago de nomina


    # CONSTRUCTOR ---------------------------------------------------------------
    
    # @param nivel Nivel de la meta (Por ejemplo: "Facil", "Intermedio", "Dificil")
    #
    # @param minimo Valor mínimo a alcanzar para cumplir la meta
    #
    # @param comision Comisión por cumplir la meta
    
    def __init__(self, nivel, minimo, comision):
        self._nivel = nivel
        self._minimo = minimo
        self._comision = comision


    # MÉTODOS -------------------------------------------------------------------

    # Funcionalidades en las que se usa: Pago de nomina
    # 
    # @param valorAlcanzado Valor alcanzado por el empleado
    # 
    # @return true si el valor alcanzado es mayor o igual al mínimo, false en caso contrario
    # 
    # Determina si se cumplió la meta esperada.
    
    def cumplioMeta(self, valorAlcanzado):
        return valorAlcanzado >= self._minimo
    

    # Funcionalidades en las que se usa: Pago de nomina
    # 
    # @param valorAlcanzado Valor alcanzado por el empleado
    # 
    # @return Una cadena de texto que indica el porcentaje de cumplimiento de la meta. 
    #         Si no se alcanzó el 100%, también incluye el porcentaje faltante y la cantidad faltante del valor mínimo.
    # 
    # Calcula el porcentaje de cumplimiento de la meta.
    
    def porcentajeCumplimiento(self, valorAlcanzado):
        porcentajeCumplido = (valorAlcanzado / self._minimo) * 100
        mensaje = "Porcentaje de cumplimiento: " + str(porcentajeCumplido) + "%"
        if porcentajeCumplido < 100:
            mensaje += "\nPorcentaje faltante: " + str(100 - porcentajeCumplido) + "%"
            mensaje += "\nCantidad faltante del indice indicado: " + str(self._minimo - valorAlcanzado)
        return mensaje
    

    # Devuelve una representación en cadena del objeto Meta.
    #
    # @return Cadena de texto con información sobre la meta
    
    def __str__(self):
        return "\n" \
             + "Minimo requerido:                 " + str(self._minimo) + "\n" \
             + "Bonificación por cumplimiento:    " + str(self._comision) + "\n"


    # GETTERS Y SETTERS ---------------------------------------------------------

    def getNivel(self):
        return self._nivel
    
    def setNivel(self, nivel):
        self._nivel = nivel
    
    def getMinimo(self):
        return self._minimo
    
    def setMinimo(self, minimo):
        self._minimo = minimo
    
    def getComision(self):
        return self._comision
    
    def setComision(self, comision):
        self._comision = comision

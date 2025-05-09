from enum import Enum, auto
from Pasajero import Pasajero

class Silla:

    #-------------------------------------------
    # Enumeraciones
    #-------------------------------------------
    class clase (Enum):
        Ejecutiva = auto()
        Economica = auto()
                
    class ubicacion (Enum):
        Ventana = auto()
        Centro = auto()
        Pasillo = auto()

        #-------------------------------------------
        # Atributos
        #-------------------------------------------

    def __init__ ( self, pNumero:int, pClase:clase, pUbicacion:ubicacion ):
        self.__numero = pNumero
        self.__clase = pClase
        self.__ubicacion = pUbicacion
        self.__pasajero = None

    def darClase (self):
        return self.__clase
    
    def darUbicacion (self):
        return self.__ubicacion

    __Method__ = "asignarPasajero"
    __params__ = "pPasajero"
    __returns__ = "none"
    __description__ = "Metodo asignar un asiento a un pasajero"
    
    def asignarPasajero(self, pPasajero):
        self.__pasajero = pPasajero

    __Method__ = "desasignarSilla"
    __params__ = "None"
    __returns__ = "none"
    __description__ = "Metodo para liberar el asiento a un pasajero"
    def desasignarSilla (self):
        self.__pasajero = None
    
    __Method__ = "SillaAsignada"
    __params__ = "None"
    __returns__ = "pasajero"
    __description__ = "Metodo para asignar una silla a un pasajero"
    def SillaAsignada (self) -> bool:
        return self.__pasajero is not None
        
    __Method__ = "darNumero"
    __params__ = "None"
    __returns__ = "numero"
    __description__ = "Metodo para saber el numero de la silla"

    def darNumero (self) -> int:
        return self.__numero


    __Method__ = "darPasajero"
    __params__ = "None"
    __returns__ = "pasajero"
    __description__ = "Metodo para registrar un pasajero"
    
    def darPasajero (self) -> Pasajero:
        return self.__pasajero

    

    

        
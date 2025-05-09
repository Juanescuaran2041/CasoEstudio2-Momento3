class Pasajero:

    #-----------------------------------
    # Constructor
    #-----------------------------------
    def __init__(self, pCedula:int, pNombre:str):

        self.__Pcedula:int = pCedula
        self.__Pnombre:str = pNombre

    #-----------------------------------
    # Métodos
    #-----------------------------------

    __Method__ = "darCedula"
    __params__ = "None"
    __returns__ = "Cedula"
    __description__ = "Metodo para saber la cedula del pasajero"
    def darCedula(self):
        return self.__Pcedula

    __Method__ = "darNombre"
    __params__ = "None"
    __returns__ = "nombre"
    __description__ = "Metodo para saber el nombre de un pasajero"
    def darNombre(self):
        return self.__Pnombre 

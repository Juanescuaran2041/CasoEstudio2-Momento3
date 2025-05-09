from Silla import Silla
from Pasajero import Pasajero

class Avion:
 
    def __init__(self):
        self.sillas = []
        for i in range(1, 51):
            if 1 <= i <= 8:
                if i in [1, 4, 5, 8]:
                    ubicacion = Silla.ubicacion.Ventana
                else:
                    ubicacion = Silla.ubicacion.Pasillo

                self.sillas.append(Silla(i, Silla.clase.Ejecutiva, ubicacion))
            else:
               
                if i in [9,14,15,20,21,26,27,30,32,33,38,39,44,45,50]: 
                    ubicacion = Silla.ubicacion.Ventana
                elif i in [10,13,16,19,22,25,28,31,34,37,40,43,46,49]:
                    ubicacion = Silla.ubicacion.Centro
                else: 
                    ubicacion = Silla.ubicacion.Pasillo
            
                self.sillas.append(Silla(i, Silla.clase.Economica, ubicacion))
                ##Tuve que definir las variables de ubicacion manualmente, porque la secuencia de las sillas no seguia un patron matematico unico

    def calcularEjecutivasOcupadas(self) -> int:
        ejecutivas_ocupadas = 0
        for silla in self.sillas:  
            if silla.darClase() == Silla.clase.Ejecutiva and silla.SillaAsignada():
                ejecutivas_ocupadas += 1
        return ejecutivas_ocupadas
    

    def BuscarPasajeroEjecutivo (self, pCedula):
        for silla in self.sillas:
            if silla.darClase() == Silla.clase.Ejecutiva and silla.SillaAsignada():
                pasajero = silla.darPasajero() 
                if pasajero and pasajero.darCedula() == pCedula:
                    return silla  

        return None

    def buscarSillaEconomicaLibre(self, ubicacion):
        for silla in self.sillas:
            if silla.darClase() == Silla.clase.Economica and not silla.SillaAsignada():
                if silla.darUbicacion() == ubicacion: 
                    return silla
        return None
    
    def asignarSillaEconomica (self, pUbicacion, pPasajero):
        silla_libre = self.buscarSillaEconomicaLibre(pUbicacion)

        if silla_libre:
            silla_libre.asignarPasajero(pPasajero)
            return True 

        return False  

        #Tambien se podia asi, pero requiere mas lineas de codigo y no es muy reutilizable
        # for silla in self.sillas:
        #     if silla.darClase () == Silla.clase.Economica and not silla.SillaAsignada ():
        #         if silla.darUbicacion () == pUbicacion:
        #             silla.asignarPasajero (pPasajero)
                
        #             return True
        
        # return False

    def anularReservaEjecutivo (self, Pcedula):
        for silla in self.sillas:
            if silla.darClase () == Silla.clase.Ejecutiva and silla.SillaAsignada ():
                pasajero = silla.darPasajero()
                if pasajero and pasajero.darCedula() == Pcedula:
                    silla.desasignarSilla()
                    return True
                
        return False 
    
    def contarVentanasEconomicas (self):
        contador = 0
        for silla in self.sillas:
            if silla.darClase () == Silla.clase.Economica and not silla.SillaAsignada ():
                if silla.darUbicacion () == Silla.ubicacion.Ventana:
                    contador +=1
        
        return contador
    
    def hayDosHomonimosEconomica(self):
        nombres = set() #Uso set para crear un conjunto de datos no establecido aun
        #con set el solo evalua si esta o no esta el nombre, si no esta lo agrega y si esta entonces no
        #cuando no lo vuelve a agregar retorna true
        for silla in self.sillas:

            if silla.darClase() == Silla.clase.Economica and silla.SillaAsignada():
                pasajero = silla.darPasajero()
                if pasajero:
                    nombre = pasajero.darNombre()

                    if nombre in nombres:
                        return True
                    nombres.add(nombre)

        return False
    
    #Naturalmente, se podria hacer de la siguiente forma, pero es menos eficiente
    #
    # nombres = []
    # for silla1 in self.sillas:
    #     if silla1.darClase() == Silla.clase.Economica and silla1.SillaAsignada():
    #         pasajero1 = silla1.darPasajero()
    #         if pasajero1:
    #             nombre1 = pasajero1.darNombre()               
    #             for silla2 in self.sillas:
    #                 if silla1 != silla2 and silla2.darClase() == Silla.clase.Economica and silla2.SillaAsignada():
    #                     pasajero2 = silla2.darPasajero()
    #                     if pasajero2 and pasajero2.darNombre() == nombre1:
    #                         return True

    # return False

    def contarSillasEconomicasLibres (self):
        contador = 0
        for sillas in self.sillas:
            if sillas.darClase () == Silla.clase.Economica and not sillas.SillaAsignada():
                contador +=1
            
        return contador
    
    def contarPasilloEjecutivas (self):
        contador =0
        for sillas in self.sillas:
            if sillas.darClase () == Silla.clase.Ejecutiva and not sillas.SillaAsignada ():
                if sillas.darUbicacion () == Silla.ubicacion.Pasillo:
                    contador +=1

        return contador

    def desocuparAvion (self):
        for sillas in self.sillas:
            sillas.desasignarSilla ()

            

from Pasajero import Pasajero
from Silla import Silla
from avion import Avion

def main():
    pasajero1 = Pasajero("12345678", "Juan Pérez")
    pasajero2 = Pasajero("87654321", "Ana Gómez")

    silla1 = Silla(1, Silla.clase.Ejecutiva, Silla.ubicacion.Ventana)
    silla2 = Silla(2, Silla.clase.Ejecutiva, Silla.ubicacion.Pasillo)
    silla3 = Silla(3, Silla.clase.Economica, Silla.ubicacion.Centro)
    silla4 = Silla(4, Silla.clase.Economica, Silla.ubicacion.Pasillo)

    print(f"Silla {silla1.darNumero()} asignada: {silla1.SillaAsignada()}")  # : False
    print(f"Silla {silla2.darNumero()} asignada: {silla2.SillaAsignada()}")  # : False

    silla1.asignarPasajero(pasajero1)
    silla2.asignarPasajero(pasajero2)

    print(f"Silla {silla1.darNumero()} asignada: {silla1.SillaAsignada()}")  # : True
    print(f"Silla {silla2.darNumero()} asignada: {silla2.SillaAsignada()}")  # : True

    print(f"Silla {silla1.darNumero()} ocupada por: {silla1.darPasajero().darNombre()}")  # : Juan Pérez
    print(f"Silla {silla2.darNumero()} ocupada por: {silla2.darPasajero().darNombre()}")  # : Ana Gómez

    silla1.desasignarSilla()
    print(f"Silla {silla1.darNumero()} asignada: {silla1.SillaAsignada()}")  # : False

    # Intentar reasignar una silla
    silla1.asignarPasajero(pasajero2)
    print(f"Silla {silla1.darNumero()} ocupada por: {silla1.darPasajero().darNombre()}")  # : Ana Gómez

if __name__ == "__main__":
    main()
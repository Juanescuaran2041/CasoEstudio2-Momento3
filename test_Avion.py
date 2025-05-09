import unittest
from avion import Avion
from Pasajero import Pasajero
from Silla import Silla

class TestAvion(unittest.TestCase):

    def setUp(self):
        self.avion = Avion()

    def test_calcular_ejecutivas_ocupadas(self):
        pasajero1 = Pasajero(123456789, "Juan")
        pasajero2 = Pasajero(987654321, "Maria")
        
        # Asignar pasajeros a sillas ejecutivas
        self.avion.sillas[0].asignarPasajero(pasajero1)  # Silla 1 en clase Ejecutiva
        self.avion.sillas[1].asignarPasajero(pasajero2)  # Silla 2 en clase Ejecutiva

        # Verificar que el número de ejecutivas ocupadas es 2
        self.assertEqual(self.avion.calcularEjecutivasOcupadas(), 2)

    def test_buscar_pasajero_ejecutivo(self):
        pasajero = Pasajero(123456789, "Juan")
        self.avion.sillas[0].asignarPasajero(pasajero)  # Asignar pasajero a la silla 1

        # Buscar pasajero por cédula
        silla_encontrada = self.avion.BuscarPasajeroEjecutivo(123456789)
        self.assertIsNotNone(silla_encontrada)
        self.assertEqual(silla_encontrada.darPasajero().darNombre(), "Juan")

    def test_buscar_silla_economica_libre(self):
        silla_libre = self.avion.buscarSillaEconomicaLibre(Silla.ubicacion.Ventana)
        self.assertIsNotNone(silla_libre)
        self.assertEqual(silla_libre.darUbicacion(), Silla.ubicacion.Ventana)

    def test_asignar_silla_economica(self):
        pasajero = Pasajero(111222333, "Carlos")
        resultado = self.avion.asignarSillaEconomica(Silla.ubicacion.Ventana, pasajero)

        # Verificar que la asignación fue exitosa
        self.assertTrue(resultado)

        # Buscar la silla asignada para confirmar
        silla_asignada = next(
            (silla for silla in self.avion.sillas if silla.darPasajero() == pasajero),
            None
        )
        self.assertIsNotNone(silla_asignada)
        self.assertEqual(silla_asignada.darPasajero().darNombre(), "Carlos")

    def test_contar_sillas_economicas_libres(self):
        total_libres = self.avion.contarSillasEconomicasLibres()
        self.assertEqual(total_libres, 42)  # Según el diseño inicial del avión

    def test_anular_reserva_ejecutivo(self):
        pasajero = Pasajero(555666777, "Ana")
        self.avion.sillas[0].asignarPasajero(pasajero)  # Asignar pasajero a la silla 1

        # Anular la reserva
        resultado = self.avion.anularReservaEjecutivo(555666777)
        self.assertTrue(resultado)

        # Verificar que la silla está desocupada
        self.assertIsNone(self.avion.sillas[0].darPasajero())

if __name__ == "__main__":
    unittest.main()
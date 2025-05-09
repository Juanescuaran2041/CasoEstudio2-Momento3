from avion import Avion

if __name__ == "__main__":
    print("Iniciando prueba...")

    # Crear instancia de Avion
    try:
        avion = Avion()
        print("Instancia de Avion creada correctamente.")
    except Exception as e:
        print(f"Error al crear la instancia de Avion: {e}")
        exit()

    # Verificar las instancias de las sillas
    try:
        for silla in avion.sillas[:10]:  # Solo las primeras 10 para no saturar la consola
            print(f"Silla número: {silla.darNumero()}, Clase: {silla.darClase()}, Ubicación: {silla.darUbicacion()}")
    except Exception as e:
        print(f"Error al acceder a las sillas: {e}")
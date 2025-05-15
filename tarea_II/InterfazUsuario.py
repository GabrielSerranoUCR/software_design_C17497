from FabricaVehiculos import FabricaVehiculos
from Flota import Flota
from Flota import Vehiculo
class InterfazUsuario:
    """
    Clase para manejar la interacción con el usuario.
    
    Separa la lógica de presentación de la lógica de negocio.
    """
    
    def __init__(self):
        """Inicializa la interfaz con una flota vacía."""
        self._flota = Flota()
        self._fabrica = FabricaVehiculos()
    
    def mostrar_menu(self) -> str:
        """Muestra el menú principal."""
        print("\n===== SISTEMA DE GESTIÓN DE FLOTAS =====")
        print("1. Agregar vehículo")
        print("2. Generar reporte")
        print("3. Salir")
        return input("Seleccione una opción: ")
    
    def solicitar_datos_vehiculo(self) -> Vehiculo:
        """
        Solicita los datos para crear un vehículo.
        
        Returns:
            Vehiculo: El vehículo creado o None si hubo un error.
        """
        try:
            print("\n--- Agregar nuevo vehículo ---")
            tipo: str = input("Tipo (auto/moto/camion): ").lower()
            if tipo not in ['auto', 'moto', 'camion']:
                print("Error: Tipo de vehículo no válido.")
                return None
                
            color: str = input("Color: ")
            
            try:
                peso: float = float(input("Peso (kg): "))
                if peso <= 0:
                    print("Error: El peso debe ser un valor positivo.")
                    return None
            except ValueError:
                print("Error: El peso debe ser un número.")
                return None
                
            es_electrico: bool = input("¿Es eléctrico? (s/n): ").lower() == 's'
            
            # Solo pedimos capacidad de pasajeros para camiones
            capacidad: int = None
            if tipo == 'camion':
                try:
                    capacidad = int(input("Capacidad de pasajeros: "))
                    if capacidad < 0:
                        print("Error: La capacidad no puede ser negativa.")
                        return None
                except ValueError:
                    print("Error: La capacidad debe ser un número entero.")
                    return None
            
            return self._fabrica.crear_vehiculo(tipo, color, peso, es_electrico, capacidad)
        except Exception as e:
            print(f"Error al procesar los datos: {e}")
            return None
    
    def mostrar_vehiculo(self, datos: dict) -> None:
        """
        Muestra los datos de un vehículo.
        
        Args:
            datos (dict): Diccionario con los datos del vehículo.
        """
        print("\n------------------------")
        print(f"Vehículo tipo: {datos['tipo']}")
        print(f"Color: {datos['color']}")
        print(f"Peso: {datos['peso']} kg")
        print(f"Ruedas: {datos['ruedas']}")
        print(f"Eléctrico: {'Sí' if datos['es_electrico'] else 'No'}")
        print(f"Capacidad: {datos['capacidad_pasajeros']} pasajeros")
        print(f"Costo: ${datos['costo']}")
        print(f"Requiere inspección: {'Sí' if datos['necesita_inspeccion'] else 'No'}")
        print("------------------------")
    
    def mostrar_reporte(self, reporte: dict) -> None:
        """
        Muestra el reporte de la flota.
        
        Args:
            reporte (dict): Diccionario con el reporte de la flota.
        """
        if "mensaje" in reporte:
            print(f"\n{reporte['mensaje']}")
            return
            
        print("\n===== REPORTE DE FLOTA =====")
        for vehiculo in reporte["vehiculos"]:
            self.mostrar_vehiculo(vehiculo)
            
        print("\nRESUMEN FLOTA:")
        print(f"Total vehículos: {reporte['total_vehiculos']}")
        print(f"Vehículos eléctricos: {reporte['vehiculos_electricos']}")
        print(f"Requieren inspección: {reporte['requieren_inspeccion']}")
        print(f"Valor total: ${reporte['valor_total']}")
        print("=============================")
    
    def ejecutar(self):
        """Ejecuta la interfaz principal."""
        while True:
            opcion : str = self.mostrar_menu()
            
            if opcion == '1':
                vehiculo : Vehiculo = self.solicitar_datos_vehiculo()
                if vehiculo:
                    self._flota.agregar_vehiculo(vehiculo)
                    print("Vehículo agregado con éxito!")
                    
            elif opcion == '2':
                reporte: dict = self._flota.generar_reporte()
                self.mostrar_reporte(reporte)
                
            elif opcion == '3':
                print("¡Gracias por usar el sistema!")
                break
                
            else:
                print("Opción no válida. Intente de nuevo.")
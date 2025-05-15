from Auto import Auto
from Camion import Camion
from Moto import Moto
from Vehiculo import Vehiculo
class FabricaVehiculos:
    """
    Fábrica para crear diferentes tipos de vehículos.
    """
    
    @staticmethod
    def crear_vehiculo(tipo: str, color: str, peso: float, es_electrico: bool = False, capacidad_pasajeros: int = None) -> Vehiculo:
        """
        Crea un vehículo del tipo especificado.
        
        Args:
            tipo (str): Tipo de vehículo ('auto', 'moto', 'camion').
            color (str): Color del vehículo.
            peso (float): Peso del vehículo en kg.
            es_electrico (bool, optional): Si es eléctrico. Por defecto False.
            capacidad_pasajeros (int, optional): Capacidad de pasajeros. Por defecto None.
        
        Returns:
            Vehiculo: Una instancia del tipo de vehículo solicitado.
            
        Raises:
            ValueError: Si el tipo de vehículo no es válido.
        """
        tipo = tipo.lower()
        try:
            if tipo == 'auto':
                return Auto(color, peso, es_electrico)
            elif tipo == 'moto':
                return Moto(color, peso, es_electrico)
            elif tipo == 'camion':
                cap = capacidad_pasajeros if capacidad_pasajeros is not None else 2
                return Camion(color, peso, es_electrico, cap)
            else:
                raise ValueError(f"Tipo de vehículo no reconocido: {tipo}")
        except Exception as e:
            print(f"Error al crear vehículo: {e}")
            raise

from Vehiculo import Vehiculo
class Camion(Vehiculo):
    """
    Clase que representa un camión.
    
    Hereda de la clase Vehiculo.
    """
    
    def __init__(self, color: str, peso: float, es_electrico: bool = False, capacidad_pasajeros: int = 2):
        """
        Inicializa un nuevo camión.
        
        Args:
            color (str): Color del camión.
            peso (float): Peso del camión en kg.
            es_electrico (bool, optional): Si es eléctrico. Por defecto False.
            capacidad_pasajeros (int, optional): Capacidad de pasajeros. Por defecto 2
        """
        super().__init__(color, peso, ruedas = 4, es_electrico = es_electrico, capacidad_pasajeros = capacidad_pasajeros)
    
    def calcular_costo(self) -> float:
        """
        Calcula el costo del camión dependiendo del peso.
        
        Returns:
            float: Costo calculado.
        """
        base: int = 45000
        extra: float = self.get_peso() * 200
        return base + extra
        
    def necesita_inspeccion(self) -> bool:
        """
        Determina si el camión necesita inspección a tráves del peso.
        
        Returns:
            bool: Siempre es True para los camiones
        """
        return True
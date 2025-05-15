from Vehiculo import Vehiculo
class Moto(Vehiculo):
    """
    Clase que representa una moto.
    
    Hereda de la clase Vehiculo.
    """
    
    def __init__(self, color: str, peso: float, es_electrico: bool = False):
        """
        Inicializa una nueva moto.
        
        Args:
            color (str): Color de la moto.
            peso (float): Peso de la moto en kg.
            es_electrico (bool, optional): Si es eléctrica. Por defecto False.
        """
        super().__init__(color, peso, ruedas = 2, es_electrico = es_electrico, capacidad_pasajeros = 2)
    
    def calcular_costo(self) -> float:
        """
        Calcula el costo de la moto dependiendo del peso y si es eléctrica.
        
        Returns:
            float: Costo calculado.
        """
        base: int = 8000
        extra: float = self.get_peso() * 50
        if self.get_es_electrico():
            extra += 3000
        return base + extra
        
    def necesita_inspeccion(self) -> bool:
        """
        Determina si la moto necesita inspección a tráves del peso.
        
        Returns:
            bool: True si necesita inspección, False en caso contrario.
        """
        return self.get_peso() > 300
    

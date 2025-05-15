from Vehiculo import Vehiculo
class Auto(Vehiculo):
    """
    Clase que representa un auto.
    
    Hereda de la clase Vehiculo.
    """
    
    def __init__(self, color: str, peso: float, es_electrico: bool = False):
        """
        Inicializa un nuevo auto.
        
        Args:
            color (str): Color del auto.
            peso (float): Peso del auto en kg.
            es_electrico (bool, optional): Si es eléctrico. Por defecto False.
        """
        super().__init__(color, peso, ruedas = 4, es_electrico = es_electrico, capacidad_pasajeros = 5)
    
    def calcular_costo(self) -> float:
        """
        Calcula el costo del auto dependiendo del peso y si es eléctrico.
        
        Returns:
            float: Costo calculado.
        """
        base: int = 15000
        extra: float = self.get_peso() * 100
        if self.get_es_electrico():
            extra += 5000
        return base + extra
        
    def necesita_inspeccion(self) -> bool:
        """
        Determina si el auto necesita inspección a tráves del peso.
        
        Returns:
            bool: True si necesita inspección, False en caso contrario.
        """
        return self.get_peso() > 2000
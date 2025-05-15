import ValidadorVehiculo
class Vehiculo:
    """
    Clase base que representa un vehículo.
    
    Attributes:
        _color (str): Color del vehículo.
        _peso (float): Peso del vehículo en kg.
        _ruedas (int): Número de ruedas del vehículo.
        _es_electrico (bool): Indica si el vehículo es eléctrico.
        _capacidad_pasajeros (int): Capacidad máxima de pasajeros.
        _estado (str): Estado del vehículo (nuevo, usado, etc).
    """
    
    def __init__(self, color: str, peso: float, ruedas: int, es_electrico: bool = False, capacidad_pasajeros: int = 0):
        """
        Inicializa un nuevo vehículo.
        
        Args:
            color (str): Color del vehículo.
            peso (float): Peso del vehículo en kg.
            ruedas (int): Número de ruedas.
            es_electrico (bool, optional): Si el vehículo es eléctrico. Por defecto False.
            capacidad_pasajeros (int, optional): Capacidad de pasajeros. Por defecto 0.
        
        Raises:
            ValueError: Si el peso es negativo o la capacidad de pasajeros es negativa.
        """
        ValidadorVehiculo.validar_peso(peso)
        ValidadorVehiculo.validar_capacidad_pasajeros(capacidad_pasajeros)
        
        self._color = color
        self._peso = peso
        self._ruedas = ruedas
        self._es_electrico = es_electrico
        self._capacidad_pasajeros = capacidad_pasajeros
        self._estado = "nuevo"
    
    # Getters y setters para encapsulamiento
    def get_color(self) -> str:
        return self._color
    
    def set_color(self, color: str ) -> None:
        self._color = color
    
    def get_peso(self)-> float:
        return self._peso
    
    def set_peso(self, peso: float) -> None:
        ValidadorVehiculo.validar_peso(peso)
        self._peso = peso
    
    def get_ruedas(self) -> int:
        return self._ruedas
    
    def get_es_electrico(self) -> bool:
        return self._es_electrico
    
    def set_es_electrico(self, valor)-> None:
        self._es_electrico = bool(valor)
    
    def get_capacidad_pasajeros(self) -> int:
        return self._capacidad_pasajeros
    
    def get_estado(self) -> str:
        return self._estado
    
    def set_estado(self, valor):
        self._estado = valor
    
    def get_tipo(self):
        """
        Obtiene el tipo de vehículo basado en el nombre de la clase.
        
        Returns:
            str: Nombre de la clase (tipo de vehículo).
        """
        return self.__class__.__name__
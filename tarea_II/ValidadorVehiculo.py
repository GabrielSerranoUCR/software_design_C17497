class ValidadorVehiculo:
    """
    Clase responsable de validar datos de vehículos.
    Separada según el Principio de Responsabilidad Única (SRP).
    """
    
    @staticmethod
    def validar_peso(peso: float) -> None: 
        """
        Valida que el peso sea un valor positivo.
        
        Args:
            peso (float): Peso a validar.
            
        Raises:
            ValueError: Si el peso no es un valor positivo.
        """
        if peso <= 0:
            raise ValueError("El peso debe ser un valor positivo")
    
    @staticmethod
    def validar_capacidad_pasajeros(capacidad: int) -> None:
        """
        Valida que la capacidad de pasajeros sea un valor no negativo.
        
        Args:
            capacidad (int): Capacidad a validar.
            
        Raises:
            ValueError: Si la capacidad es negativa.
        """
        if capacidad < 0:
            raise ValueError("La capacidad de pasajeros no puede ser negativa")
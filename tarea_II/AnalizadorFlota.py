class AnalizadorFlota:
    """
    Clase responsable de analizar datos de una flota de vehículos.
    """
    
    @staticmethod
    def contar_electricos(vehiculos_datos: list) -> int:
        """
        Cuenta el número de vehículos eléctricos en la flota.
        
        Args:
            vehiculos_datos (list): Lista de diccionarios con datos de vehículos.
            
        Returns:
            int: Número de vehículos eléctricos.
        """
        return sum(1 for datos in vehiculos_datos if datos["es_electrico"])
    
    @staticmethod
    def contar_requieren_inspeccion(vehiculos_datos: list) -> int:
        """
        Cuenta el número de vehículos que requieren inspección.
        
        Args:
            vehiculos_datos (list): Lista de diccionarios con datos de vehículos.
            
        Returns:
            int: Número de vehículos que requieren inspección.
        """
        return sum(1 for datos in vehiculos_datos if datos["necesita_inspeccion"])
    
    @staticmethod
    def calcular_valor_total(vehiculos_datos: list)-> float:
        """
        Calcula el valor total de todos los vehículos.
        
        Args:
            vehiculos_datos (list): Lista de diccionarios con datos de vehículos.
            
        Returns:
            float: Valor total de la flota.
        """
        return sum(datos["costo"] for datos in vehiculos_datos)
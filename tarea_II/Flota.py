from AnalizadorFlota import AnalizadorFlota
from Vehiculo import Vehiculo
class Flota:
    """
    Clase para gestionar una flota de vehículos.
    """
    
    def __init__(self):
        """Inicializa una flota vacía."""
        self._vehiculos = []
    
    def get_vehiculos(self) -> list:
        """
        Retorna una copia de la lista de vehículos.
        """
        return self._vehiculos.copy()
    
    def agregar_vehiculo(self, vehiculo: Vehiculo) -> None:
        """
        Agrega un vehículo a la flota.
        
        Args:
            vehiculo (Vehiculo): Vehículo a agregar.
            
        Raises:
            TypeError: Si el objeto no es una instancia de Vehiculo.
        """
        if not isinstance(vehiculo, Vehiculo):
            raise TypeError("El objeto debe ser una instancia de Vehiculo")
        self._vehiculos.append(vehiculo)
    
    def generar_reporte(self) -> dict:
        """
        Genera un reporte de la flota.
        
        Returns:
            dict: Diccionario con el resumen de la flota y la lista de vehículos.
        """
        if not self._vehiculos:
            return {"mensaje": "No hay vehículos en la flota", "vehiculos": []}
        
        # Recolectamos los datos de cada vehículo
        vehiculos_datos = [v.get_datos() for v in self._vehiculos]
        
        # Delegamos el análisis a la clase especializada
        electricos = AnalizadorFlota.contar_electricos(vehiculos_datos)
        requiere_inspeccion = AnalizadorFlota.contar_requieren_inspeccion(vehiculos_datos)
        valor_total = AnalizadorFlota.calcular_valor_total(vehiculos_datos)
        
        return {
            "total_vehiculos": len(self._vehiculos),
            "vehiculos_electricos": electricos,
            "requieren_inspeccion": requiere_inspeccion,
            "valor_total": valor_total,
            "vehiculos": vehiculos_datos
        }

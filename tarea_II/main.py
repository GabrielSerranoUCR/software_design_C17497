from InterfazUsuario import InterfazUsuario
if __name__ == "__main__":
    try:
        interfaz = InterfazUsuario()
        interfaz.ejecutar()
    except Exception as e:
        print(f"Error inesperado: {e}")
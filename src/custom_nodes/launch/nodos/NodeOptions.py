class NodeOptions:
    """Clase base para opciones de configuración de un nodo."""
    def create_widgets(self, parent):
        raise NotImplementedError("Este método debe ser implementado por subclases.")
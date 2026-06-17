class Pieza:
    """Representa una ficha de las damas."""
    def __init__(self, color):
        self.color = color  # 'B' para Blancas, 'N' para Negras
        self.es_rey = False

    def coronar(self):
        """Convierte la ficha en Rey/Dama cuando llega al otro extremo."""
        self.es_rey = True

    def __str__(self):
        # Retorna el símbolo que se verá en pantalla
        if self.color == 'B':
            return 'B' if not self.es_rey else 'BB'
        else:
            return 'N' if not self.es_rey else 'NN'
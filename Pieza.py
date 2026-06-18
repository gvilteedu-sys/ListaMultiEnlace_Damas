class Pieza:
    """
    Representa una ficha de las damas.
    
    Esta clase maneja las propiedades individuales de una pieza en el tablero,
    tales como su color (bando) y si ha sido promovida a rey/dama.
    """
    def __init__(self, color):
        """
        Inicializa una nueva pieza con un color específico.
        
        Args:
            color (str): El color de la pieza. Típicamente 'B' para Blancas o 'N' para Negras.
        """
        self.color = color  # 'B' para Blancas, 'N' para Negras
        self.es_rey = False

    def coronar(self):
        """
        Convierte la ficha en Rey/Dama cuando llega al otro extremo del tablero.
        
        Al coronar una pieza, se le permite moverse en múltiples direcciones
        según las reglas estándar de las damas (no implementado en el movimiento aún).
        """
        self.es_rey = True

    def __str__(self):
        """
        Retorna la representación en cadena (string) de la pieza.
        
        Returns:
            str: 'B' o 'N' para piezas normales, 'BB' o 'NN' para reyes.
        """
        # Retorna el símbolo que se verá en pantalla o en consola
        if self.color == 'B':
            return 'B' if not self.es_rey else 'BB'
        else:
            return 'N' if not self.es_rey else 'NN'
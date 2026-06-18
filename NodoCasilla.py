class NodoCasilla:
    """
    Representa una casilla en el tablero. 
    Actúa como un nodo de una lista cuádruplemente enlazada.
    
    Cada nodo guarda información de su posición matricial teórica, su color visual,
    y mantiene referencias a las casillas adyacentes (arriba, abajo, izquierda, derecha)
    para formar el grafo ortogonal del tablero.
    """
    def __init__(self, fila, columna, color_casilla):
        """
        Inicializa un nuevo nodo del tablero.
        
        Args:
            fila (int): Índice de la fila donde se ubica la casilla (0 a 7).
            columna (int): Índice de la columna donde se ubica la casilla (0 a 7).
            color_casilla (str): Color de la casilla, 'B' (blanca) o 'N' (negra).
        """
        # Coordenadas y color de la casilla (no de la pieza)
        self.fila = fila
        self.columna = columna
        self.color_casilla = color_casilla # 'B' (blanca) o 'N' (negra)
        
        # Objeto Pieza que pueda estar en esta casilla
        self.pieza = None

        # Los 4 enlaces (punteros) que conectan el tablero.
        # Al iniciar son None; se asignan dinámicamente al construir la topología del juego.
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        """
        Retorna una representación en formato texto del nodo.
        
        Se utiliza principalmente para depuración e impresión del tablero en consola.
        
        Returns:
            str: El símbolo de la pieza contenida, un punto para casillas negras vacías,
                 o espacios en blanco para casillas blancas.
        """
        # Imprime la pieza si la hay, o el fondo de la casilla
        if self.pieza:
            return f" {self.pieza} "
        elif self.color_casilla == 'N':
            return " · " # Casilla negra vacía (donde se juega)
        else:
            return "   " # Casilla blanca vacía (no se usa en damas)
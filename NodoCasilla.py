class NodoCasilla:
    """
    Representa una casilla en el tablero. 
    Actúa como un nodo de una lista cuádruplemente enlazada.
    """
    def __init__(self, fila, columna, color_casilla):
        # Coordenadas y color de la casilla (no de la pieza)
        self.fila = fila
        self.columna = columna
        self.color_casilla = color_casilla # 'B' (blanca) o 'N' (negra)
        
        # Objeto Pieza que pueda estar en esta casilla
        self.pieza = None

        # Los 4 enlaces (punteros) que conectan el tablero
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        # Imprime la pieza si la hay, o el fondo de la casilla
        if self.pieza:
            return f" {self.pieza} "
        elif self.color_casilla == 'N':
            return " · " # Casilla negra vacía (donde se juega)
        else:
            return "   " # Casilla blanca vacía (no se usa en damas)
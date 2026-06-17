from NodoCasilla import NodoCasilla
from Pieza import Pieza

class Tablero:
    """Maneja la lógica del tablero construido mediante nodos enlazados."""
    def __init__(self):
        # Solo necesitamos guardar el primer nodo. 
        # A partir de él llegaremos a todo el tablero navegando.
        self.nodo_inicial = None 
        self._construir_tablero()
        self._colocar_piezas_iniciales()

    def _construir_tablero(self):
        """Crea 64 nodos y los enlaza en las 4 direcciones."""
        # Usamos una lista temporal 2D solo para facilitar el proceso de enlazado
        nodos = [[NodoCasilla(f, c, 'B' if (f + c) % 2 == 0 else 'N') for c in range(8)] for f in range(8)]

        # Enlazar los nodos (arriba, abajo, izquierda, derecha)
        for f in range(8):
            for c in range(8):
                if f > 0: nodos[f][c].arriba = nodos[f-1][c]
                if f < 7: nodos[f][c].abajo = nodos[f+1][c]
                if c > 0: nodos[f][c].izquierda = nodos[f][c-1]
                if c < 7: nodos[f][c].derecha = nodos[f][c+1]

        # Guardar la esquina superior izquierda
        self.nodo_inicial = nodos[0][0]

    def _colocar_piezas_iniciales(self):
        """Navega usando los enlaces de los nodos para colocar las piezas."""
        actual_fila = self.nodo_inicial
        
        # Recorremos el tablero bajando fila a fila
        while actual_fila is not None:
            actual_columna = actual_fila
            
            # Recorremos la fila de izquierda a derecha
            while actual_columna is not None:
                # En damas solo se juega en las casillas negras
                if actual_columna.color_casilla == 'N':
                    if actual_columna.fila < 3: # Arriba van las negras
                        actual_columna.pieza = Pieza('N')
                    elif actual_columna.fila > 4: # Abajo van las blancas
                        actual_columna.pieza = Pieza('B')
                
                # Avanzamos al nodo de la derecha usando el puntero
                actual_columna = actual_columna.derecha
                
            # Avanzamos a la fila de abajo usando el puntero
            actual_fila = actual_fila.abajo

    def obtener_nodo(self, fila, columna):
        """Busca un nodo específico navegando por la estructura de red."""
        if not (0 <= fila < 8 and 0 <= columna < 8):
            return None
            
        actual = self.nodo_inicial
        # Navegar hacia abajo
        for _ in range(fila):
            actual = actual.abajo
        # Navegar hacia la derecha
        for _ in range(columna):
            actual = actual.derecha
            
        return actual

    def mover_pieza(self, f_origen, c_origen, f_destino, c_destino):
        """Mueve una pieza de un nodo a otro de forma funcional y básica."""
        origen = self.obtener_nodo(f_origen, c_origen)
        destino = self.obtener_nodo(f_destino, c_destino)

        # Validaciones muy básicas: Nodos existen, hay pieza origen y destino está vacío
        if origen and destino and origen.pieza is not None and destino.pieza is None:
            # Aquí se puede añadir la lógica estricta (movimiento diagonal, saltos para comer)
            destino.pieza = origen.pieza
            origen.pieza = None
            return True
        return False

    def imprimir(self):
        """Muestra el estado actual del tablero en consola."""
        print("\n    0   1   2   3   4   5   6   7")
        print("  " + "-"*33)
        
        actual_fila = self.nodo_inicial
        f = 0
        while actual_fila is not None:
            actual_columna = actual_fila
            fila_str = f"{f} |"
            
            while actual_columna is not None:
                fila_str += str(actual_columna) + "|"
                actual_columna = actual_columna.derecha
                
            print(fila_str)
            print("  " + "-"*33)
            actual_fila = actual_fila.abajo
            f += 1
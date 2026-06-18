from NodoCasilla import NodoCasilla
from Pieza import Pieza

class Tablero:
    """
    Maneja la lógica del tablero construido mediante nodos enlazados.
    
    Esta clase abstrae la construcción y el manejo del grafo de casillas, manteniendo
    únicamente la referencia al nodo superior izquierdo y navegando a través de los
    punteros de los nodos para interactuar con las piezas.
    """
    def __init__(self):
        """
        Inicializa la estructura del tablero.
        
        Crea las casillas enlazadas y posteriormente posiciona las piezas en su
        distribución inicial reglamentaria.
        """
        # Solo necesitamos guardar el primer nodo. 
        # A partir de él llegaremos a todo el tablero navegando.
        self.nodo_inicial = None 
        self._construir_tablero()
        self._colocar_piezas_iniciales()

    def _construir_tablero(self):
        """
        Crea 64 nodos y los enlaza en las 4 direcciones.
        
        Se crea una matriz bidimensional temporal para facilitar la resolución topológica
        de aristas. Una vez que todos los punteros ortogonales (arriba, abajo, izquierda, derecha)
        se establecen con éxito, la matriz es destruida y el estado enlazado persiste por sí solo.
        """
        # Usamos una lista temporal 2D solo para facilitar el proceso de enlazado.
        # Condicional inline: if (f + c) % 2 == 0 asigna 'B' basándose en la paridad de la suma cartesiana, pintando el tablero en damero.
        nodos = [[NodoCasilla(f, c, 'B' if (f + c) % 2 == 0 else 'N') for c in range(8)] for f in range(8)]

        # Enlazar los nodos (arriba, abajo, izquierda, derecha) iterando la lista
        for f in range(8):
            for c in range(8):
                if f > 0: nodos[f][c].arriba = nodos[f-1][c]
                if f < 7: nodos[f][c].abajo = nodos[f+1][c]
                if c > 0: nodos[f][c].izquierda = nodos[f][c-1]
                if c < 7: nodos[f][c].derecha = nodos[f][c+1]

        # Guardar la esquina superior izquierda
        self.nodo_inicial = nodos[0][0]

    def _colocar_piezas_iniciales(self):
        """
        Navega usando los enlaces de los nodos para colocar las piezas.
        
        Coloca piezas negras en las tres primeras filas y piezas blancas en las tres
        últimas, únicamente sobre las casillas de color negro.
        """
        actual_fila = self.nodo_inicial
        
        # Recorremos el tablero bajando fila a fila
        while actual_fila is not None:
            actual_columna = actual_fila
            
            # Recorremos la fila de izquierda a derecha usando el puntero "derecha"
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
        """
        Busca un nodo específico navegando por la estructura de red.
        
        Dado que el sistema no retiene un array de acceso directo, simula la iteración O(1)
        matricial con una complejidad temporal de O(F+C), atravesando punteros paso a paso.
        
        Args:
            fila (int): Coordenada de fila buscada.
            columna (int): Coordenada de columna buscada.
            
        Returns:
            NodoCasilla: El nodo ubicado en las coordenadas indicadas, o None si está fuera de los límites.
        """
        # Validación defensiva: previene excepciones si se intentan buscar coordenadas fuera del rango [0,7]
        if not (0 <= fila < 8 and 0 <= columna < 8):
            return None
            
        actual = self.nodo_inicial
        # Navegar hacia abajo iterativamente
        for _ in range(fila):
            actual = actual.abajo
        # Navegar hacia la derecha iterativamente
        for _ in range(columna):
            actual = actual.derecha
            
        return actual

    def mover_pieza(self, f_origen, c_origen, f_destino, c_destino):
        """
        Mueve una pieza de un nodo a otro de forma funcional y básica.
        
        Esta operación es transaccional a nivel de punteros: realiza una transferencia
        de la referencia del objeto 'Pieza' entre los objetos 'NodoCasilla'.
        
        Args:
            f_origen (int): Fila del nodo donde se encuentra la pieza actualmente.
            c_origen (int): Columna del nodo actual.
            f_destino (int): Fila del nodo destino para la pieza.
            c_destino (int): Columna del nodo destino.
            
        Returns:
            bool: True si el movimiento lógico fue exitoso, False si no se cumplen las precondiciones de existencia.
        """
        origen = self.obtener_nodo(f_origen, c_origen)
        destino = self.obtener_nodo(f_destino, c_destino)

        # Validaciones muy básicas: Nodos existen, hay pieza origen y destino está vacío.
        # No valida reglas de damas complejas (movimientos diagonales puros o sistema de saltos/captura).
        if origen and destino and origen.pieza is not None and destino.pieza is None:
            # Aquí se puede añadir la lógica estricta (movimiento diagonal, saltos para comer)
            destino.pieza = origen.pieza
            origen.pieza = None
            return True
        return False

    def imprimir(self):
        """
        Muestra el estado actual del tablero en consola.
        
        Ideal para depuración (CLI). Extrae secuencialmente el grafo interconectado
        y reconstruye un log formateado emulando la cuadrícula del juego visual.
        """
        print("\n    0   1   2   3   4   5   6   7")
        print("  " + "-"*33)
        
        actual_fila = self.nodo_inicial
        f = 0
        while actual_fila is not None:
            actual_columna = actual_fila
            fila_str = f"{f} |"
            
            while actual_columna is not None:
                # Conversión implícita de nodo a string invocando el dunder method __str__
                fila_str += str(actual_columna) + "|"
                actual_columna = actual_columna.derecha
                
            print(fila_str)
            print("  " + "-"*33)
            actual_fila = actual_fila.abajo
            f += 1
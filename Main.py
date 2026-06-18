import pygame
import sys
from Tablero import Tablero

# Constantes de Pygame
ANCHO = 640
ALTO = 640
FILAS = 8
COLUMNAS = 8
# Discretiza la resolución espacial determinando los píxeles cuadrados por cada casilla.
TAMANO_CASILLA = ANCHO // COLUMNAS

# Colores (RGB)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
MARRON_CLARO = (240, 217, 181)
MARRON_OSCURO = (181, 136, 99)
ROJO = (255, 0, 0) # Resaltado
GRIS = (128, 128, 128) # Borde de las piezas

def dibujar_tablero(pantalla, tablero, casilla_seleccionada):
    """
    Renderiza el tablero y sus piezas en la ventana de Pygame.
    
    Procesa síncronamente el grafo del tablero recorriéndolo con los punteros
    derecha/abajo, inyectando primitivas geométricas (rectángulos y círculos) 
    sobre la superficie principal por cada cuadro renderizado (Frame).
    
    Args:
        pantalla (pygame.Surface): Superficie principal de dibujado proporcionada por Pygame.
        tablero (Tablero): Instancia lógica de la cuadrícula multi-enlazada.
        casilla_seleccionada (tuple o None): Coordenadas de tipo (fila, columna) de la ficha cliqueada activamente.
    """
    # Llena el fondo de toda la pantalla actuando como las "casillas claras".
    pantalla.fill(MARRON_CLARO)
    
    actual_fila = tablero.nodo_inicial
    # Atraviesa el grafo dimensional moviéndose hacia abajo en el eje Y.
    while actual_fila is not None:
        actual_columna = actual_fila
        # Atraviesa la capa horizontal usando el puntero en el eje X.
        while actual_columna is not None:
            f = actual_columna.fila
            c = actual_columna.columna
            
            # Dibujar casilla oscura si corresponde según la lógica de asignación
            if actual_columna.color_casilla == 'N':
                pygame.draw.rect(pantalla, MARRON_OSCURO, (c * TAMANO_CASILLA, f * TAMANO_CASILLA, TAMANO_CASILLA, TAMANO_CASILLA))
            
            # Resaltar casilla seleccionada añadiendo un borde perimetral de grosor 4
            if casilla_seleccionada == (f, c):
                pygame.draw.rect(pantalla, ROJO, (c * TAMANO_CASILLA, f * TAMANO_CASILLA, TAMANO_CASILLA, TAMANO_CASILLA), 4)

            # Dibujar pieza si existe verificando la referencia de objeto del NodoCasilla
            if actual_columna.pieza is not None:
                color_pieza = BLANCO if actual_columna.pieza.color == 'B' else NEGRO
                # Centrado matemático del círculo dentro del cuadrado lógico.
                centro_x = c * TAMANO_CASILLA + TAMANO_CASILLA // 2
                centro_y = f * TAMANO_CASILLA + TAMANO_CASILLA // 2
                radio = TAMANO_CASILLA // 2 - 10
                
                # Sombra/Borde exterior para darle profundidad estética a la ficha 2D
                pygame.draw.circle(pantalla, GRIS, (centro_x, centro_y), radio + 2)
                # Pieza interior real
                pygame.draw.circle(pantalla, color_pieza, (centro_x, centro_y), radio)
                
                # Si es rey, estampa una corona de color dorado sobre la pieza original
                if actual_columna.pieza.es_rey:
                    pygame.draw.circle(pantalla, (255, 215, 0), (centro_x, centro_y), radio // 2)

            # Iterador del ciclo interno: Siguiente nodo de la misma fila
            actual_columna = actual_columna.derecha
            
        # Iterador del ciclo externo: Desciende a la siguiente fila del grafo
        actual_fila = actual_fila.abajo

def iniciar_juego():
    """
    Configura y arranca el ciclo principal de eventos (Game Loop) del juego.
    
    Inicializa los subsistemas gráficos (pygame), genera el dominio principal y mantiene
    un bucle infinito iterativo que capta de forma bloqueante las interrupciones
    de teclado y ratón, ejecutando el Pipeline de lógica y renderizado.
    """
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Juego de Damas - Nodos POO")
    reloj = pygame.time.Clock()

    tablero = Tablero()
    casilla_seleccionada = None # (fila, columna)

    corriendo = True
    while corriendo:
        # Pila de eventos de hardware disparados desde el último frame
        for evento in pygame.event.get():
            # Intercepta comando OS de cierre y rompe el loop principal
            if evento.type == pygame.QUIT:
                corriendo = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1: # Clic izquierdo del ratón
                    # Recupera la tupla de coordenadas espaciales reales en base a la resolución
                    x, y = pygame.mouse.get_pos()
                    # Transforma píxeles continuos a índices discretos de fila/columna por división entera.
                    f = y // TAMANO_CASILLA
                    c = x // TAMANO_CASILLA

                    # Lógica de estados para el movimiento (Si una pieza ya estaba seleccionada)
                    if casilla_seleccionada:
                        fo, co = casilla_seleccionada
                        if fo == f and co == c:
                            # Deseleccionar si clicamos redundante en la misma casilla
                            casilla_seleccionada = None
                        else:
                            # Intentar mover la pieza delegando la regla transaccional al Tablero
                            if tablero.mover_pieza(fo, co, f, c):
                                print(f">> Movimiento de ({fo},{co}) a ({f},{c}) exitoso.")
                            else:
                                print(f">> Movimiento inválido a ({f},{c}).")
                            casilla_seleccionada = None
                    else:
                        # Seleccionar una pieza si existe en la casilla clickeada
                        # Delegación al motor subyacente para recuperar el nodo
                        nodo = tablero.obtener_nodo(f, c)
                        if nodo and nodo.pieza:
                            casilla_seleccionada = (f, c)

        # Flujo de Output a la tarjeta gráfica y renderizado sincrónico del tablero
        dibujar_tablero(pantalla, tablero, casilla_seleccionada)
        pygame.display.flip()
        
        # Limita los ticks de iteración a 60 FPS fijos (evita un uso de CPU excesivo).
        reloj.tick(60)

    # Limpieza final de recursos subyacentes
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    iniciar_juego()
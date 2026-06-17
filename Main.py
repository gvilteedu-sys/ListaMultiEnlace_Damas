import pygame
import sys
from Tablero import Tablero

# Constantes de Pygame
ANCHO = 640
ALTO = 640
FILAS = 8
COLUMNAS = 8
TAMANO_CASILLA = ANCHO // COLUMNAS

# Colores (RGB)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
MARRON_CLARO = (240, 217, 181)
MARRON_OSCURO = (181, 136, 99)
ROJO = (255, 0, 0) # Resaltado
GRIS = (128, 128, 128) # Borde de las piezas

def dibujar_tablero(pantalla, tablero, casilla_seleccionada):
    pantalla.fill(MARRON_CLARO)
    
    actual_fila = tablero.nodo_inicial
    while actual_fila is not None:
        actual_columna = actual_fila
        while actual_columna is not None:
            f = actual_columna.fila
            c = actual_columna.columna
            
            # Dibujar casilla oscura si corresponde
            if actual_columna.color_casilla == 'N':
                pygame.draw.rect(pantalla, MARRON_OSCURO, (c * TAMANO_CASILLA, f * TAMANO_CASILLA, TAMANO_CASILLA, TAMANO_CASILLA))
            
            # Resaltar casilla seleccionada
            if casilla_seleccionada == (f, c):
                pygame.draw.rect(pantalla, ROJO, (c * TAMANO_CASILLA, f * TAMANO_CASILLA, TAMANO_CASILLA, TAMANO_CASILLA), 4)

            # Dibujar pieza si existe
            if actual_columna.pieza is not None:
                color_pieza = BLANCO if actual_columna.pieza.color == 'B' else NEGRO
                centro_x = c * TAMANO_CASILLA + TAMANO_CASILLA // 2
                centro_y = f * TAMANO_CASILLA + TAMANO_CASILLA // 2
                radio = TAMANO_CASILLA // 2 - 10
                
                # Sombra/Borde exterior
                pygame.draw.circle(pantalla, GRIS, (centro_x, centro_y), radio + 2)
                # Pieza interior
                pygame.draw.circle(pantalla, color_pieza, (centro_x, centro_y), radio)
                
                # Si es rey
                if actual_columna.pieza.es_rey:
                    pygame.draw.circle(pantalla, (255, 215, 0), (centro_x, centro_y), radio // 2)

            actual_columna = actual_columna.derecha
        actual_fila = actual_fila.abajo

def iniciar_juego():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Juego de Damas - Nodos POO")
    reloj = pygame.time.Clock()

    tablero = Tablero()
    casilla_seleccionada = None # (fila, columna)

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1: # Clic izquierdo
                    x, y = pygame.mouse.get_pos()
                    f = y // TAMANO_CASILLA
                    c = x // TAMANO_CASILLA

                    # Si ya hay una casilla seleccionada
                    if casilla_seleccionada:
                        fo, co = casilla_seleccionada
                        if fo == f and co == c:
                            # Deseleccionar si clicamos en la misma casilla
                            casilla_seleccionada = None
                        else:
                            # Intentar mover la pieza usando la lógica existente en Tablero
                            if tablero.mover_pieza(fo, co, f, c):
                                print(f">> Movimiento de ({fo},{co}) a ({f},{c}) exitoso.")
                            else:
                                print(f">> Movimiento inválido a ({f},{c}).")
                            casilla_seleccionada = None
                    else:
                        # Seleccionar una pieza si existe en la casilla clickeada
                        nodo = tablero.obtener_nodo(f, c)
                        if nodo and nodo.pieza:
                            casilla_seleccionada = (f, c)

        dibujar_tablero(pantalla, tablero, casilla_seleccionada)
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    iniciar_juego()
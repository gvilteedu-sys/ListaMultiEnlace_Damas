# ♟️ ListaMultiEnlace_Damas

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.x-green.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)
![Build Status](https://img.shields.io/badge/build-passing-success.svg)

**ListaMultiEnlace_Damas** es una implementación interactiva y educativa del clásico juego de mesa Damas (Checkers). Lo que hace a este proyecto especial no es solo la jugabilidad, sino su arquitectura de datos subyacente: el tablero de juego no está construido sobre una matriz tradicional (array bidimensional), sino sobre una **lista cuádruplemente enlazada** (un grafo ortogonal). Cada casilla del tablero es un nodo conectado explícitamente a sus vecinos mediante punteros, ofreciendo una excelente demostración práctica de estructuras de datos complejas aplicadas al desarrollo de videojuegos.

---

## 📑 Tabla de Contenidos
1. [Características Principales](#-características-principales)
2. [Tecnologías Utilizadas](#-tecnologías-utilizadas)
3. [Requisitos Previos](#-requisitos-previos)
4. [Guía de Instalación](#-guía-de-instalación)
5. [Ejecución y Uso](#-ejecución-y-uso)
6. [Estructura del Proyecto](#-estructura-del-proyecto)
7. [Contribución](#-contribución)
8. [Licencia](#-licencia)

---

## ✨ Características Principales

* **Estructura de Grafo Custom:** Navegación espacial lograda a través de una malla de nodos interconectados (arriba, abajo, izquierda, derecha) en lugar de índices matriciales estáticos.
* **Interfaz Gráfica Interactiva:** Interfaz 2D fluida a 60 FPS construida desde cero. Renderizado en tiempo real leyendo el estado del grafo in-memory.
* **Diseño Orientado a Objetos (POO):** Responsabilidades claramente separadas entre el controlador del bucle principal, el orquestador del grafo, la topología de los nodos y la entidad pieza.
* **Selección y Movimiento Visual:** Feedback de usuario inmediato al interactuar con las fichas a través del ratón.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Descripción / Propósito |
| :--- | :--- |
| **Python 3.x** | Lenguaje de programación principal (Runtime lógico). |
| **Pygame** | Motor multimedia para el Game Loop, renderizado 2D y captura de eventos. |
| **venv & pip** | Aislamiento del entorno virtual y gestión de paquetes. |

---

## ⚙️ Requisitos Previos

Asegúrate de tener instalados los siguientes componentes antes de clonar y ejecutar el repositorio:

* **Python 3.8+**: [Descargar aquí](https://www.python.org/downloads/)
* **Git** (Para clonar el repositorio): [Descargar aquí](https://git-scm.com/downloads)

Para verificar tus instalaciones, abre tu terminal y ejecuta:
```bash
python --version
git --version
```

---

## 🚀 Guía de Instalación

Sigue estos pasos para levantar el proyecto en tu entorno local en menos de dos minutos.

**1. Clona el repositorio:**
```bash
git clone [URL_DEL_REPOSITORIO]
```

**2. Navega al directorio del proyecto:**
```bash
cd ListaMultiEnlace_Damas
```

**3. Crea un entorno virtual (Recomendado):**
```bash
# En Windows
python -m venv venv

# En macOS/Linux
python3 -m venv venv
```

**4. Activa el entorno virtual:**
```bash
# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

**5. Instala las dependencias necesarias:**
```bash
pip install -r requirements.txt
```

---

## 🎮 Ejecución y Uso

Una vez instaladas las dependencias, asegúrate de tener tu entorno virtual activo e inicia el juego.

**Iniciar el Entorno de Desarrollo:**
Ejecuta el punto de entrada principal del proyecto:
```bash
python Main.py
```

**Controles Básicos:**
1. Al iniciar, verás el tablero renderizado con las fichas blancas y negras en sus posiciones iniciales.
2. Haz **Clic Izquierdo** sobre una ficha tuya para seleccionarla (la casilla se resaltará en rojo).
3. Haz **Clic Izquierdo** nuevamente sobre una casilla vacía de destino para mover la ficha (la lógica del tablero validará e intercambiará los punteros internamente).
4. Para anular una selección, simplemente vuelve a hacer clic en la misma ficha.

---

## 📁 Estructura del Proyecto

```ascii
ListaMultiEnlace_Damas/
 ├── .git/                 # Control de versiones del repositorio
 ├── venv/                 # Entorno virtual de Python aislado (no rastreado)
 ├── .gitignore            # Exclusión de archivos binarios o temporales
 ├── requirements.txt      # Listado de dependencias externas (pygame)
 ├── Main.py               # Punto de entrada; contiene la UI y el Controlador Pygame
 ├── Tablero.py            # Orquestador del Dominio; construye y maneja la lista cuádruple
 ├── NodoCasilla.py        # Modelo; representa una celda del grafo con 4 referencias
 └── Pieza.py              # Modelo; entidad lógica que define las características de la ficha
```

---

## 🤝 Contribución

¡Las contribuciones son lo que hacen a la comunidad open source un lugar increíble para aprender, inspirar y crear! Cualquier contribución que hagas será **muy apreciada**.

Si tienes una sugerencia que mejore este proyecto (como añadir la lógica completa de los movimientos de las damas o la coronación de reinas), por favor haz un _fork_ del repositorio y crea un Pull Request. También puedes abrir un _issue_ con la etiqueta "enhancement".

1. Haz un Fork del proyecto.
2. Crea tu rama de características (`git checkout -b feature/MecanicaIncreible`).
3. Haz commit de tus cambios (`git commit -m 'Add: Nueva mecánica de captura'`).
4. Haz Push a la rama (`git push origin feature/MecanicaIncreible`).
5. Abre un Pull Request.

---

## 📄 Licencia

Distribuido bajo la Licencia MIT. Consulta el archivo `LICENSE` (o el equivalente en el repositorio) para más información.

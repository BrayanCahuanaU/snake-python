import tkinter
import random  

# Constantes del juego
FILAS = 25  # Número de filas en el tablero
COLUMNAS = 25  # Número de columnas en el tablero
TAMAÑO_CASILLA = 25  # Tamaño en píxeles de cada casilla

ANCHO_VENTANA = TAMAÑO_CASILLA * COLUMNAS  # Ancho total de la ventana
ALTO_VENTANA = TAMAÑO_CASILLA * FILAS  # Alto total de la ventana

class Casilla:
    def __init__(self, x, y):
        self.x = x  # Posición horizontal
        self.y = y  # Posición vertical

# Configuración de la ventana principal
ventana = tkinter.Tk()
ventana.title("Snake")  # Título de la ventana
ventana.resizable(False, False)  # Ventana no redimensionable

# Creación del lienzo (canvas) donde se dibuja el juego
lienzo = tkinter.Canvas(ventana, bg="black", width=ANCHO_VENTANA, height=ALTO_VENTANA, 
                       borderwidth=0, highlightthickness=0)
lienzo.pack()
ventana.update()  # Actualiza la ventana para obtener sus dimensiones reales

# Centrar la ventana en la pantalla
ancho_ventana = ventana.winfo_width()
alto_ventana = ventana.winfo_height()
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

pos_x = int((ancho_pantalla/2) - (ancho_ventana/2))
pos_y = int((alto_pantalla/2) - (alto_ventana/2))

# Establecer geometría de la ventana: "ancho x alto + posX + posY"
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Inicialización de variables del juego
serpiente = Casilla(TAMAÑO_CASILLA * 5, TAMAÑO_CASILLA * 5)  # Cabeza de la serpiente
comida = Casilla(TAMAÑO_CASILLA * 10, TAMAÑO_CASILLA * 10)  # Posición de la comida
velocidadX = 0  # Velocidad horizontal inicial
velocidadY = 0  # Velocidad vertical inicial
cuerpo_serpiente = []  # Lista para almacenar los segmentos del cuerpo
juego_terminado = False  # Estado del juego
puntuacion = 0  # Puntuación del jugador

# Función para cambiar la dirección de la serpiente
def cambiar_direccion(evento):
    global velocidadX, velocidadY, juego_terminado
    
    if juego_terminado:
        return  # Si el juego terminó, no se procesan movimientos
    
    # Cambiar dirección según la tecla presionada (evitando movimiento opuesto)
    if (evento.keysym == "Up" and velocidadY != 1):  # Arriba
        velocidadX = 0
        velocidadY = -1
    elif (evento.keysym == "Down" and velocidadY != -1):  # Abajo
        velocidadX = 0
        velocidadY = 1
    elif (evento.keysym == "Left" and velocidadX != 1):  # Izquierda
        velocidadX = -1
        velocidadY = 0
    elif (evento.keysym == "Right" and velocidadX != -1):  # Derecha
        velocidadX = 1
        velocidadY = 0

# Función para mover la serpiente
def mover():
    global serpiente, comida, cuerpo_serpiente, juego_terminado, puntuacion
    
    if juego_terminado:
        return  # Si el juego terminó, no se mueve
    
    # Detectar colisión con los bordes
    if (serpiente.x < 0 or serpiente.x >= ANCHO_VENTANA or 
        serpiente.y < 0 or serpiente.y >= ALTO_VENTANA):
        juego_terminado = True
        return
    
    # Detectar colisión con el propio cuerpo
    for segmento in cuerpo_serpiente:
        if (serpiente.x == segmento.x and serpiente.y == segmento.y):
            juego_terminado = True
            return
    
    # Detectar colisión con la comida
    if (serpiente.x == comida.x and serpiente.y == comida.y):
        cuerpo_serpiente.append(Casilla(comida.x, comida.y))  # Añadir nuevo segmento
        # Mover la comida a posición aleatoria
        comida.x = random.randint(0, COLUMNAS-1) * TAMAÑO_CASILLA
        comida.y = random.randint(0, FILAS-1) * TAMAÑO_CASILLA
        puntuacion += 1  # Incrementar puntuación
    
    # Mover el cuerpo de la serpiente
    for i in range(len(cuerpo_serpiente)-1, -1, -1):
        segmento = cuerpo_serpiente[i]
        if i == 0:  # El primer segmento sigue a la cabeza
            segmento.x = serpiente.x
            segmento.y = serpiente.y
        else:  # Los demás segmentos siguen al anterior
            segmento_previo = cuerpo_serpiente[i-1]
            segmento.x = segmento_previo.x
            segmento.y = segmento_previo.y
    
    # Mover la cabeza según la velocidad
    serpiente.x += velocidadX * TAMAÑO_CASILLA
    serpiente.y += velocidadY * TAMAÑO_CASILLA

# Función principal de dibujo y actualización del juego
def dibujar():
    global serpiente, comida, cuerpo_serpiente, juego_terminado, puntuacion
    
    mover()  # Actualizar posiciones
    
    lienzo.delete("all")  # Limpiar el lienzo
    
    # Dibujar la comida (roja)
    lienzo.create_rectangle(comida.x, comida.y, 
                          comida.x + TAMAÑO_CASILLA, comida.y + TAMAÑO_CASILLA, 
                          fill='red')
    
    # Dibujar la cabeza de la serpiente (verde lima)
    lienzo.create_rectangle(serpiente.x, serpiente.y, 
                          serpiente.x + TAMAÑO_CASILLA, serpiente.y + TAMAÑO_CASILLA, 
                          fill='lime green')
    
    # Dibujar el cuerpo de la serpiente
    for segmento in cuerpo_serpiente:
        lienzo.create_rectangle(segmento.x, segmento.y, 
                              segmento.x + TAMAÑO_CASILLA, segmento.y + TAMAÑO_CASILLA, 
                              fill='lime green')
    
    # Mostrar mensaje de juego terminado o puntuación
    if juego_terminado:
        lienzo.create_text(ANCHO_VENTANA/2, ALTO_VENTANA/2, 
                          font="Arial 20", text=f"Game Over: {puntuacion}", 
                          fill="white")
    else:
        lienzo.create_text(30, 20, font="Arial 10", 
                         text=f"Puntuación: {puntuacion}", fill="white")
    
    # Programar próximo frame (10 FPS)
    ventana.after(100, dibujar)

# Iniciar el juego
dibujar()
ventana.bind("<KeyRelease>", cambiar_direccion)  # Configurar controles
ventana.mainloop()  # Bucle principal de la aplicación
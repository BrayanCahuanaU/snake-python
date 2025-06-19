import tkinter
import random

class Casilla:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class JuegoSnake:
    def __init__(self, filas=25, columnas=25, tamaño_casilla=25):
        self.FILAS = filas
        self.COLUMNAS = columnas
        self.TAMAÑO_CASILLA = tamaño_casilla
        self.ANCHO_VENTANA = self.TAMAÑO_CASILLA * self.COLUMNAS
        self.ALTO_VENTANA = self.TAMAÑO_CASILLA * self.FILAS
        
        self.serpiente = Casilla(self.TAMAÑO_CASILLA * 5, self.TAMAÑO_CASILLA * 5)
        self.comida = Casilla(self.TAMAÑO_CASILLA * 10, self.TAMAÑO_CASILLA * 10)
        self.cuerpo_serpiente = []
        self.velocidadX = 0
        self.velocidadY = 0
        self.juego_terminado = False
        self.puntuacion = 0
    
    def cambiar_direccion(self, tecla):
        if self.juego_terminado:
            return

        if tecla == "Up" and self.velocidadY != 1:
            self.velocidadX = 0
            self.velocidadY = -1
        elif tecla == "Down" and self.velocidadY != -1:
            self.velocidadX = 0
            self.velocidadY = 1
        elif tecla == "Left" and self.velocidadX != 1:
            self.velocidadX = -1
            self.velocidadY = 0
        elif tecla == "Right" and self.velocidadX != -1:
            self.velocidadX = 1
            self.velocidadY = 0
    
    def generar_comida(self):
        # Generar comida en posición aleatoria que no esté en la serpiente
        while True:
            self.comida.x = random.randint(0, self.COLUMNAS-1) * self.TAMAÑO_CASILLA
            self.comida.y = random.randint(0, self.FILAS-1) * self.TAMAÑO_CASILLA
            
            # Verificar que no esté en la serpiente
            posiciones_serpiente = [(self.serpiente.x, self.serpiente.y)]
            for segmento in self.cuerpo_serpiente:
                posiciones_serpiente.append((segmento.x, segmento.y))
            
            if (self.comida.x, self.comida.y) not in posiciones_serpiente:
                break
    
    def mover(self):
        if self.juego_terminado:
            return

        # Detectar colisión con los bordes
        if (self.serpiente.x < 0 or self.serpiente.x >= self.ANCHO_VENTANA or 
            self.serpiente.y < 0 or self.serpiente.y >= self.ALTO_VENTANA):
            self.juego_terminado = True
            return

        # Detectar colisión con el propio cuerpo
        for segmento in self.cuerpo_serpiente:
            if (self.serpiente.x == segmento.x and self.serpiente.y == segmento.y):
                self.juego_terminado = True
                return

        # Detectar colisión con la comida
        if (self.serpiente.x == self.comida.x and self.serpiente.y == self.comida.y):
            self.cuerpo_serpiente.append(Casilla(self.comida.x, self.comida.y))
            self.generar_comida()
            self.puntuacion += 1

        # Mover el cuerpo
        for i in range(len(self.cuerpo_serpiente)-1, -1, -1):
            segmento = self.cuerpo_serpiente[i]
            if i == 0:
                segmento.x = self.serpiente.x
                segmento.y = self.serpiente.y
            else:
                segmento_previo = self.cuerpo_serpiente[i-1]
                segmento.x = segmento_previo.x
                segmento.y = segmento_previo.y

        # Mover la cabeza
        self.serpiente.x += self.velocidadX * self.TAMAÑO_CASILLA
        self.serpiente.y += self.velocidadY * self.TAMAÑO_CASILLA
    
    def reiniciar(self):
        self.serpiente = Casilla(self.TAMAÑO_CASILLA * 5, self.TAMAÑO_CASILLA * 5)
        self.comida = Casilla(self.TAMAÑO_CASILLA * 10, self.TAMAÑO_CASILLA * 10)
        self.cuerpo_serpiente = []
        self.velocidadX = 0
        self.velocidadY = 0
        self.juego_terminado = False
        self.puntuacion = 0
        self.generar_comida()

class SnakeGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake")
        self.root.resizable(False, False)
        
        self.juego = JuegoSnake()
        
        # Configurar lienzo
        self.lienzo = tkinter.Canvas(
            root, 
            bg="black", 
            width=self.juego.ANCHO_VENTANA, 
            height=self.juego.ALTO_VENTANA,
            borderwidth=0, 
            highlightthickness=0
        )
        self.lienzo.pack()
        
        # Centrar ventana
        self.root.update()
        ancho_ventana = self.root.winfo_width()
        alto_ventana = self.root.winfo_height()
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()
        pos_x = int((ancho_pantalla/2) - (ancho_ventana/2))
        pos_y = int((alto_pantalla/2) - (alto_ventana/2))
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
        
        # Configurar eventos
        self.root.bind("<KeyRelease>", self.cambiar_direccion)
        self.root.bind("<space>", self.reiniciar_juego)
        
        # Iniciar juego
        self.dibujar()
    
    def cambiar_direccion(self, evento):
        self.juego.cambiar_direccion(evento.keysym)
    
    def reiniciar_juego(self, evento):
        if self.juego.juego_terminado:
            self.juego.reiniciar()
    
    def dibujar(self):
        self.juego.mover()
        self.lienzo.delete("all")
        
        # Dibujar comida
        self.lienzo.create_rectangle(
            self.juego.comida.x, 
            self.juego.comida.y,
            self.juego.comida.x + self.juego.TAMAÑO_CASILLA, 
            self.juego.comida.y + self.juego.TAMAÑO_CASILLA,
            fill='red'
        )
        
        # Dibujar cabeza
        self.lienzo.create_rectangle(
            self.juego.serpiente.x, 
            self.juego.serpiente.y,
            self.juego.serpiente.x + self.juego.TAMAÑO_CASILLA, 
            self.juego.serpiente.y + self.juego.TAMAÑO_CASILLA,
            fill='lime green'
        )
        
        # Dibujar cuerpo
        for segmento in self.juego.cuerpo_serpiente:
            self.lienzo.create_rectangle(
                segmento.x, 
                segmento.y,
                segmento.x + self.juego.TAMAÑO_CASILLA, 
                segmento.y + self.juego.TAMAÑO_CASILLA,
                fill='lime green'
            )
        
        # Mostrar mensaje de juego terminado o puntuación
        if self.juego.juego_terminado:
            self.lienzo.create_text(
                self.juego.ANCHO_VENTANA/2, 
                self.juego.ALTO_VENTANA/2, 
                font="Arial 20", 
                text=f"Game Over: {self.juego.puntuacion}\nPresiona ESPACIO para reiniciar", 
                fill="white"
            )
        else:
            self.lienzo.create_text(
                30, 
                20, 
                font="Arial 10", 
                text=f"Puntuación: {self.juego.puntuacion}", 
                fill="white"
            )
        
        # Programar próximo frame
        self.root.after(100, self.dibujar)

if __name__ == "__main__":
    root = tkinter.Tk()
    app = SnakeGameApp(root)
    root.mainloop()
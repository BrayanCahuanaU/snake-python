import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from behave import *
from snake import JuegoSnake, Casilla

@given('el juego está recién iniciado')
def step_impl(context):
    context.juego = JuegoSnake()
    context.juego.velocidadX = 0
    context.juego.velocidadY = 0

@when('no se presiona ninguna tecla')
def step_impl(context):
    # No se realiza ninguna acción
    pass

@then('la serpiente debe permanecer inmóvil')
def step_impl(context):
    pos_inicial = (context.juego.serpiente.x, context.juego.serpiente.y)
    context.juego.mover()
    pos_final = (context.juego.serpiente.x, context.juego.serpiente.y)
    assert pos_inicial == pos_final, f"La serpiente se movió de {pos_inicial} a {pos_final}"

@given('la serpiente se mueve hacia la derecha')
def step_impl(context):
    context.juego = JuegoSnake()
    context.juego.velocidadX = 1
    context.juego.velocidadY = 0

@when('presiono la tecla "{tecla}"')
def step_impl(context, tecla):
    context.juego.cambiar_direccion(tecla)

@then('la serpiente debe moverse hacia abajo')
def step_impl(context):
    assert context.juego.velocidadX == 0
    assert context.juego.velocidadY == 1

@then('la serpiente debe seguir moviéndose a la derecha')
def step_impl(context):
    assert context.juego.velocidadX == 1
    assert context.juego.velocidadY == 0

@given('la cabeza de la serpiente está sobre la comida')
def step_impl(context):
    context.juego = JuegoSnake()
    # Posicionamos la comida debajo de la serpiente
    context.juego.comida.x = context.juego.serpiente.x
    context.juego.comida.y = context.juego.serpiente.y

@when('ocurre un movimiento')
def step_impl(context):
    context.juego.mover()

@then('la serpiente debe crecer un segmento')
def step_impl(context):
    assert len(context.juego.cuerpo_serpiente) == 1

@then('la comida debe reposicionarse')
def step_impl(context):
    # Verificar que la comida ya no está en la posición original
    assert not (context.juego.comida.x == context.juego.serpiente.x and 
                context.juego.comida.y == context.juego.serpiente.y)
    # Verificar que está dentro de los límites
    assert 0 <= context.juego.comida.x < context.juego.ANCHO_VENTANA
    assert 0 <= context.juego.comida.y < context.juego.ALTO_VENTANA

@then('la puntuación debe aumentar en 1')
def step_impl(context):
    assert context.juego.puntuacion == 1

@given('la serpiente está en el borde derecho')
def step_impl(context):
    context.juego = JuegoSnake()
    context.juego.serpiente.y = 100  # cualquier valor válido
    context.juego.velocidadX = 1
    context.juego.velocidadY = 0
    context.juego.serpiente.x = context.juego.ANCHO_VENTANA - context.juego.TAMAÑO_CASILLA

@given('se mueve hacia la derecha')
def step_impl(context):
    context.juego.velocidadX = 1
    context.juego.velocidadY = 0

@then('el juego debe terminar')
def step_impl(context):
    assert context.juego.juego_terminado is True

@given('la serpiente tiene 3 segmentos')
def step_impl(context):
    context.juego = JuegoSnake()
    # Creamos 3 segmentos de cuerpo
    context.juego.cuerpo_serpiente = [
        Casilla(context.juego.serpiente.x, context.juego.serpiente.y),
        Casilla(context.juego.serpiente.x, context.juego.serpiente.y),
        Casilla(context.juego.serpiente.x, context.juego.serpiente.y)
    ]
    # Movemos la cabeza a una posición diferente
    context.juego.serpiente.x = context.juego.TAMAÑO_CASILLA * 10
    context.juego.serpiente.y = context.juego.TAMAÑO_CASILLA * 10

@given('la cabeza se dirige hacia el segundo segmento')
def step_impl(context):
    # Colocar el segundo segmento justo delante de la cabeza
    x = context.juego.serpiente.x
    y = context.juego.serpiente.y - context.juego.TAMAÑO_CASILLA

    context.juego.cuerpo_serpiente = [
        Casilla(x, y + context.juego.TAMAÑO_CASILLA),  # debajo de la cabeza (posición previa)
        Casilla(x, y),  # justo encima de la cabeza
        Casilla(x, y - context.juego.TAMAÑO_CASILLA)   # aún más arriba
    ]

    context.juego.velocidadX = 0
    context.juego.velocidadY = -1  # Mover hacia arriba

@given('el juego ha terminado')
def step_impl(context):
    context.juego = JuegoSnake()
    context.juego.juego_terminado = True

@when('se presiona cualquier tecla')
def step_impl(context):
    # Simular intento de cambio de dirección
    context.juego.cambiar_direccion("Right")

@then('no ocurre ninguna acción')
def step_impl(context):
    # Como el juego terminó, las velocidades deben seguir en 0
    assert context.juego.velocidadX == 0
    assert context.juego.velocidadY == 0
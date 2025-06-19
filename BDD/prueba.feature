Pruebas BDD (Escenarios Gherkin)

Feature: Movimiento de la Serpiente
  Scenario: Movimiento inicial
    Given el juego está en estado inicial
    When no se presiona ninguna tecla
    Then la serpiente no debe moverse

  Scenario: Cambio de dirección válido
    Given la serpiente se mueve hacia la derecha
    When presiono la tecla "Down"
    Then la serpiente debe moverse hacia abajo

  Scenario: Cambio de dirección inválido
    Given la serpiente se mueve hacia la derecha
    When presiono la tecla "Left"
    Then la serpiente debe seguir moviéndose a la derecha

Feature: Comida
  Scenario: Consumir comida
    Given la cabeza de la serpiente está en la misma posición que la comida
    When ocurre un movimiento
    Then la serpiente crece un segmento
    And la comida se reposiciona aleatoriamente
    And la puntuación aumenta en 1

Feature: Colisiones
  Scenario: Colisión con borde superior
    Given la serpiente se mueve hacia arriba
    And su cabeza está en la fila 0
    When ocurre un movimiento
    Then el juego debe terminar

  Scenario: Colisión con el propio cuerpo
    Given la serpiente tiene al menos 3 segmentos
    And la cabeza se mueve hacia un segmento del cuerpo
    When ocurre un movimiento
    Then el juego debe terminar

Feature: Sistema de Juego
  Scenario: Reinicio implícito
    Given el juego ha terminado
    When se presiona cualquier tecla
    Then no ocurre ninguna acción

  Scenario: Actualización de puntuación
    Given la serpiente ha consumido 3 comidas
    When consulto la puntuación
    Then debe mostrar "Puntuación: 3"


Feature: Sistema de Juego

  Scenario: Reinicio implícito
    Given el juego ha terminado
    When se presiona cualquier tecla
    Then no ocurre ninguna acción

  Scenario: Actualización de puntuación
    Given la cabeza de la serpiente está sobre la comida
    When ocurre un movimiento
    And ocurre un movimiento
    And ocurre un movimiento
    Then la puntuación debe aumentar en 1
Feature: Comida

  Scenario: Consumir comida
    Given la cabeza de la serpiente está sobre la comida
    When ocurre un movimiento
    Then la serpiente debe crecer un segmento
    And la comida debe reposicionarse
    And la puntuación debe aumentar en 1
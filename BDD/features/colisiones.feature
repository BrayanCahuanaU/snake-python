Feature: Colisiones

  Scenario: Colisión con borde derecho
    Given la serpiente está en el borde derecho
    And se mueve hacia la derecha
    When ocurre un movimiento
    Then el juego debe terminar

  Scenario: Colisión con el propio cuerpo
    Given la serpiente tiene 3 segmentos
    And la cabeza se dirige hacia el segundo segmento
    When ocurre un movimiento
    Then el juego debe terminar
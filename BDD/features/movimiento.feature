Feature: Movimiento de la Serpiente

  Scenario: Movimiento inicial
    Given el juego está recién iniciado
    When no se presiona ninguna tecla
    Then la serpiente debe permanecer inmóvil

  Scenario: Cambio de dirección válido
    Given la serpiente se mueve hacia la derecha
    When presiono la tecla "Down"
    Then la serpiente debe moverse hacia abajo

  Scenario: Cambio de dirección inválido
    Given la serpiente se mueve hacia la derecha
    When presiono la tecla "Left"
    Then la serpiente debe seguir moviéndose a la derecha
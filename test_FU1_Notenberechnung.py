from FU1_Notenberechnung import *

def test_berechne_prozentwert__beispielhafte_Rechnung():
    # Arrange
    erreichte_punkte: int = 15
    gesamtpunkte: int = 86
    erwartetes_ergebnis: int = 17

    # Act
    ergebnis = berechne_prozentwert(erreichte_punkte, gesamtpunkte)

    # Assert
    assert erwartetes_ergebnis == ergebnis
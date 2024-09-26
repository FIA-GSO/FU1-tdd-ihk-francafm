def berechne_prozentwert(erreichte_punkte, gesamtpunkte)-> int:
    return int((erreichte_punkte / gesamtpunkte) * 100)

def get_note(prozent):
    if prozent >= 92:
        return "sehr gut"
    elif prozent >= 81:
        return "gut"
    elif prozent >= 67:
        return "befriedigend"
    elif prozent >= 50:
        return "ausreichend"
    else:
        return "mangelhaft"

if(__name__ == "__main__"):   
        print(berechne_prozentwert(51, 100))
        print(get_note(51))
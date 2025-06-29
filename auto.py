from rad import Rad

class Auto:
    def __init__(self, farbe, marke="Standard", reifenart="Sommerreifen"):
        self.farbe = farbe
        self.marke = marke
        self.fahrzeughalter = None
        self.raeder = [Rad(reifenart) for _ in range(4)]

    def zeige_reifen(self):
        if self.raeder:
            return self.raeder[0].radart
        return "Keine Reifen vorhanden"

    def __str__(self):
        besitzer = self.fahrzeughalter.nachname if self.fahrzeughalter else "kein Besitzer"
        return f"{self.marke} in {self.farbe} ({besitzer})"

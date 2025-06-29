class Parkhaus:
    def __init__(self, kapazitaet):
        self.kapazitaet = kapazitaet
        self.auslastung = [None] * kapazitaet

    def auto_parken(self, auto, platznummer):
        if 0 <= platznummer < self.kapazitaet:
            if self.auslastung[platznummer] is None:
                self.auslastung[platznummer] = auto
                print(f"{auto.marke} in {auto.farbe} wurde auf Platz {platznummer} geparkt.")
            else:
                print(f"Platz {platznummer} ist bereits belegt.")
        else:
            print("Ungültiger Parkplatz.")

    def zeige_besitzer(self, platznummer):
        if 0 <= platznummer < self.kapazitaet:
            auto = self.auslastung[platznummer]
            if auto and auto.fahrzeughalter:
                return auto.fahrzeughalter.nachname
            elif auto:
                return "Auto ohne Besitzer"
            else:
                return "Kein Auto geparkt"
        return "Ungültiger Parkplatz"

    def zeige_reifen(self, platznummer):
        if 0 <= platznummer < self.kapazitaet:
            auto = self.auslastung[platznummer]
            if auto:
                return auto.zeige_reifen()
            else:
                return "Kein Auto geparkt"
        return "Ungültiger Parkplatz"

    def auto_ausparken(self, platznummer):
        if 0 <= platznummer < self.kapazitaet:
            if self.auslastung[platznummer]:
                auto = self.auslastung[platznummer]
                self.auslastung[platznummer] = None
                print(f"{auto.marke} in {auto.farbe} wurde von Platz {platznummer} ausgeparkt.")
            else:
                print("Auf diesem Platz steht kein Auto.")
        else:
            print("Ungültiger Parkplatz.")


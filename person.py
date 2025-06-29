class Person:
    def __init__(self, nachname):
        self.nachname = nachname
        self.autos_pro_person = []

    def auto_hinzufuegen(self, auto):
        if len(self.autos_pro_person) < 5:
            self.autos_pro_person.append(auto)
            auto.fahrzeughalter = self
            print(f"{auto.marke} in {auto.farbe} wurde {self.nachname} zugewiesen.")
        else:
            print("Maximale Anzahl an Autos erreicht.")

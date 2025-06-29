import json
from auto import Auto
from person import Person
from parkhaus import Parkhaus

DATEINAME = "daten.json"

def speichern(personen, autos, parkhaus):
    daten = {
        "personen": [p.nachname for p in personen],
        "autos": [
            {
                "farbe": a.farbe,
                "marke": a.marke,
                "reifenart": a.zeige_reifen(),
                "besitzer_index": personen.index(a.fahrzeughalter) if a.fahrzeughalter in personen else None
            }
            for a in autos
        ],
        "parkhaus": {
            "kapazitaet": parkhaus.kapazitaet,
            "auslastung": [autos.index(a) if a in autos else None for a in parkhaus.auslastung]
        }
    }
    with open(DATEINAME, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=2)

def laden():
    try:
        with open(DATEINAME, "r", encoding="utf-8") as f:
            daten = json.load(f)
    except FileNotFoundError:
        return [], [], Parkhaus(20)  # Standardgröße

    personen = [Person(name) for name in daten["personen"]]

    autos = []
    for eintrag in daten["autos"]:
        auto = Auto(eintrag["farbe"], eintrag["marke"], eintrag["reifenart"])
        besitzer_index = eintrag["besitzer_index"]
        if besitzer_index is not None:
            personen[besitzer_index].auto_hinzufuegen(auto)
        autos.append(auto)

    ph_daten = daten["parkhaus"]
    parkhaus = Parkhaus(ph_daten["kapazitaet"])
    for i, idx in enumerate(ph_daten["auslastung"]):
        if idx is not None:
            parkhaus.auslastung[i] = autos[idx]

    return personen, autos, parkhaus

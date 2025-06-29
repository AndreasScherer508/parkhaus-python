from speicher import speichern, laden
from person import Person
from auto import Auto
from parkhaus import Parkhaus

personen, autos, parkhaus = laden()
print("🔁 Daten geladen.")


def neue_person():
    name = input("Name der Person: ")
    p = Person(name)
    personen.append(p)
    print(f"Person {name} erstellt.")

def neues_auto():
    farbe = input("Farbe des Autos: ")

    marke = input("Marke (Enter für 'Standard'): ")
    if not marke:
        marke = "Standard"

    reifenart = input("Reifentyp (Enter für 'Sommerreifen'): ")
    if not reifenart:
        reifenart = "Sommerreifen"

    a = Auto(farbe, marke, reifenart)
    autos.append(a)
    print(f"{marke} in {farbe} mit {reifenart}-Reifen erstellt.")


def auto_zuweisen():
    if not personen or not autos:
        print("Erstelle zuerst Personen und Autos.")
        return
    for i, p in enumerate(personen):
        print(f"{i}: {p.nachname}")
    pi = int(input("Wähle Person (Index): "))
    for i, a in enumerate(autos):
        print(f"{i}: {a}")
    ai = int(input("Wähle Auto (Index): "))
    personen[pi].auto_hinzufuegen(autos[ai])

def auto_parken():
    freie_plaetze = [i for i, platz in enumerate(parkhaus.auslastung) if platz is None]

    if not autos:
        print("Keine Autos vorhanden.")
        return

    print("Autos:")
    for i, a in enumerate(autos):
        print(f"{i}: {a}")
    ai = int(input("Wähle Auto (Index): "))

    if not freie_plaetze:
        print("Kein freier Parkplatz verfügbar.")
        return

    print("Freie Parkplätze:", freie_plaetze)
    platz = int(input(f"Wähle Parkplatznummer aus dieser Liste {freie_plaetze}: "))
    if platz not in freie_plaetze:
        print("Ungültiger oder belegter Platz!")
        return

    parkhaus.auto_parken(autos[ai], platz)


def besitzer_anzeigen():
    platz = int(input(f"Platznummer (0–{parkhaus.kapazitaet - 1}): "))
    print("Besitzer:", parkhaus.zeige_besitzer(platz))

def reifen_anzeigen():
    belegte_autos = [(i, a) for i, a in enumerate(parkhaus.auslastung) if a]

    if not belegte_autos:
        print("Keine Autos im Parkhaus.")
        return

    print("Geparkte Autos:")
    for index, (platznummer, auto) in enumerate(belegte_autos):
        print(f"{index}: {auto} (Platz {platznummer})")

    auswahl = int(input("Wähle Auto (Index): "))
    platznummer, auto = belegte_autos[auswahl]
    print("Reifentyp:", auto.zeige_reifen())


def belegte_plaetze():
    for i, a in enumerate(parkhaus.auslastung):
        if a:
            print(f"Platz {i}: {a}")

def auto_ausparken():
    belegte_autos = [(i, a) for i, a in enumerate(parkhaus.auslastung) if a]

    if not belegte_autos:
        print("Keine Autos geparkt.")
        return

    print("Geparkte Autos:")
    for index, (platznummer, auto) in enumerate(belegte_autos):
        print(f"{index}: {auto} (Platz {platznummer})")

    auswahl = int(input("Wähle Auto (Index) zum Ausparken: "))
    platznummer, _ = belegte_autos[auswahl]
    parkhaus.auto_ausparken(platznummer)


def menue():
    while True:
        print("\n--- PARKHAUS MENÜ ---")
        print("1. Neue Person erstellen")
        print("2. Neues Auto erstellen")
        print("3. Auto einer Person zuweisen")
        print("4. Auto im Parkhaus parken")
        print("5. Besitzer eines Parkplatzes anzeigen")
        print("6. Reifen eines Autos anzeigen")
        print("7. Belegte Plätze anzeigen")
        print("8. Auto ausparken")
        print("0. Beenden")
        wahl = input("Deine Wahl: ")

        if wahl == "1":
            neue_person()
        elif wahl == "2":
            neues_auto()
        elif wahl == "3":
            auto_zuweisen()
        elif wahl == "4":
            auto_parken()
        elif wahl == "5":
            besitzer_anzeigen()
        elif wahl == "6":
            reifen_anzeigen()
        elif wahl == "7":
            belegte_plaetze()
        elif wahl == "8":
            auto_ausparken()
        elif wahl == "0":
            speichern(personen, autos, parkhaus)
            print("Programm beendet und Daten gespeichert.")
            break
        else:
            print("Ungültige Eingabe.")

if __name__ == "__main__":
    menue()

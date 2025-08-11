# Berechnung der Montagekosten

class MontageKosten:
    def __init__(self, stundenlohn):
        self.stundenlohn = stundenlohn
        # Definiere die Montagezeiten und Preise für verschiedene Geräte
        self.geraete = {
            "Wasserzaehler": {
                "UP-MK Zähler": {"zeit": 0.33, "preis": 12.00},
                "Aufputzzähler, Zapfhahnzähler + Zählwerkkopf": {"zeit": 0.33, "preis": 15.00},
                "Hauswasserzähler (bis Q3=16)": {"zeit": 0.5, "preis": 20.00},
                "Funkmodule WZ": {"zeit": 0.17, "preis": 5.00},
                "Funkmodule WMZ": {"zeit": 0.17, "preis": 5.00}
            },
            "Waermezaehler": {
                "Split WMZ bis QN 10,0 m³/h": {"zeit": 0.75, "preis": 75.00},
                "Split WMZ QN 15,0 - QN 40,0 m³/h": {"zeit": 0.92, "preis": 120.00},
                "Split WMZ größer QN 40,0 m³/h": {"zeit": 1.01, "preis": 170.00},
                "MK- und Verschraubungszähler bis QN 2,5m³/h": {"zeit": 0.5, "preis": 30.00}
            },
            "AMR": {
                "Montage Gateway": {"zeit": 0.5, "preis": 30.00},
                "Montage Netzwerkknoten": {"zeit": 0.42, "preis": 30.00}
            },
            "HKVE": {
                "Neuausstattung und Austausch": {"zeit": 0.75, "preis": 7.50},
                "Neuasstattung und Austausch Fernfühler": {"zeit": 0.5, "preis": 15.00}
            },
            "Rauchmelder": {
                "Neuausstattung und Austausch": {"zeit": 0.25, "preis": 8.00}
            }
        }

    def berechne_kosten(self, geraet, anzahl):
        # Berechnung der Kosten für ein bestimmtes Gerät
        if geraet not in self.geraete:
            return f"Gerät {geraet} nicht gefunden"

        gesamtzeit = 0
        gesamtpreis = 0

        for name, details in self.geraete[geraet].items():
            gesamtzeit += details["zeit"] * anzahl
            gesamtpreis += details["preis"] * anzahl

        arbeitskosten = gesamtzeit * self.stundenlohn
        gesamtpreis_mit_arbeitskosten = gesamtpreis + arbeitskosten

        return {
            "gesamtzeit_stunden": gesamtzeit,
            "gesamtpreis_geraet": gesamtpreis,
            "arbeitskosten": arbeitskosten,
            "gesamtpreis_mit_arbeitskosten": gesamtpreis_mit_arbeitskosten
        }

    def drucke_berechnung(self, geraet, anzahl):
        kosten = self.berechne_kosten(geraet, anzahl)

        if isinstance(kosten, str):
            print(kosten)
        else:
            print(f"\nBerechnung für Gerät: {geraet}")
            print(f"Gesamtzeit (in Stunden): {kosten['gesamtzeit_stunden']}")
            print(f"Gesamtpreis für {geraet} (ohne Arbeitskosten): {kosten['gesamtpreis_geraet']} €")
            print(f"Arbeitskosten: {kosten['arbeitskosten']} €")
            print(f"Gesamtpreis (inkl. Arbeitskosten): {kosten['gesamtpreis_mit_arbeitskosten']} €")

# Hauptprogramm
def main():
    stundenlohn = 28  # Stundenlohn des Monteurs
    montage_kosten = MontageKosten(stundenlohn)

    # Wählen Sie das Gerät und die Anzahl der Installationen
    geraet = input("Geben Sie das Gerät ein (z.B. 'Wasserzaehler', 'Waermezaehler', 'AMR', 'HKVE', 'Rauchmelder'): ").strip()
    anzahl = int(input("Geben Sie die Anzahl der Installationen ein: ").strip())

    montage_kosten.drucke_berechnung(geraet, anzahl)

if __name__ == "__main__":
    main()

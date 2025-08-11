# Montagekosten Rechner

Dieses Python-Projekt berechnet die Wirtschaftlichkeit von Montagen basierend auf einem Stundensatz von 28 Euro pro Stunde und einer vorgegebenen Liste von Geräten und deren Montagekosten.

## Funktionen

- Berechnung der Gesamtarbeitszeit und der Arbeitskosten für die Montage von Geräten.
- Berechnung der Gesamtkosten (inklusive Arbeitskosten) für verschiedene Geräte, abhängig von der Anzahl der Installationen.
- Möglichkeit, unterschiedliche Geräte zu wählen (Wasserzähler, Wärmezähler, AMR, HKVE, Rauchmelder).

## Installation

1. Stelle sicher, dass du [Python 3.x](https://www.python.org/downloads/) auf deinem Rechner installiert hast.
2. Erstelle ein virtuelles Environment (optional, aber empfohlen):
    ```bash
    python -m venv venv
    source venv/bin/activate   # Auf Windows: venv\Scripts\activate
    ```

3. Installiere die notwendigen Python-Bibliotheken (falls vorhanden):
    ```bash
    pip install -r requirements.txt
    ```

4. Lade das Projekt herunter und speichere die Datei als `montagekosten_rechner.py`.

## Benutzung

1. Starte das Python-Skript:
    ```bash
    python montagekosten_rechner.py
    ```

2. Folge den Anweisungen im Terminal:
    - Gib das Gerät ein, für das du die Kosten berechnen möchtest (z.B. `Wasserzaehler`, `Waermezaehler`).
    - Gib die Anzahl der Installationen an.

3. Die Berechnungen (Gesamtarbeitszeit, Gesamtpreis, Arbeitskosten und Gesamtpreis inkl. Arbeitskosten) werden ausgegeben.

## Beispiel

```bash
Geben Sie das Gerät ein (z.B. 'Wasserzaehler', 'Waermezaehler', 'AMR', 'HKVE', 'Rauchmelder'): Wasserzaehler
Geben Sie die Anzahl der Installationen ein: 10

Berechnung für Gerät: Wasserzaehler
Gesamtzeit (in Stunden): 3.3
Gesamtpreis für Wasserzaehler (ohne Arbeitskosten): 118.00 €
Arbeitskosten: 92.4 €
Gesamtpreis (inkl. Arbeitskosten): 210.40 €
```

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.


import pandas as pd

# Data
data = {
    "Gerät": [
        "UP-MK Zähler", "Aufputzzähler, Zapfhahnzähler + Zählwerkkopf", "Hauswasserzähler (bis Q3=16)",
        "Funkmodule WZ", "Funkmodule WMZ", "Split WMZ bis QN 10,0 m³/h", "Split WMZ QN 15,0 - QN 40,0 m³/h",
        "Split WMZ größer QN 40,0 m³/h", "MK- und Verschraubungszähler bis QN 2,5m³/h", "Montage Gateway",
        "Montage Netzwerkknoten", "Neuausstattung und Austausch HKVE", "Neuasstattung und Austausch Fernfühler",
        "Neuausstattung und Austausch Rauchmelder"
    ],
    "Montageaufwand (h)": [
        0.33, 0.33, 0.5, 0.17, 0.17, 0.75, 0.92, 1.01, 0.5, 0.5, 0.42, 0.75, 0.5, 0.25
    ],
    "Montagevergütung (€)": [
        12.00, 15.00, 20.00, 5.00, 5.00, 75.00, 120.00, 170.00, 30.00, 30.00, 30.00, 7.50, 15.00, 8.00
    ],
}

# Create DataFrame
df = pd.DataFrame(data)

# Add a column for number of montages and update the cost calculation based on the number of montages
df["Anzahl Montagen"] = 1  # Default value for the number of montages (can be adjusted)

# Update the cost columns to account for the number of montages
for monteure in range(1, 6):
    df[f"Kosten bei {monteure} Monteuren (€)"] = df["Anzahl Montagen"] * df["Montageaufwand (h)"] * df["Montagevergütung (€)"] * monteure

# Save to Excel file
output_file = "wirtschaftlichkeit_montage_mit_anzahl.xlsx"
df.to_excel(output_file, index=False)
print(f"Die Datei wurde erfolgreich gespeichert: {output_file}")
import os
import subprocess
import sys

# Funktion zur Installation der erforderlichen Systempakete
def install_system_dependencies():
    try:
        print("Installiere Systemabhängigkeiten...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        subprocess.check_call(["sudo", "apt-get", "update"])
        subprocess.check_call(["sudo", "apt-get", "install", "-y", "build-essential", "python3-dev"])
        print("Systemabhängigkeiten erfolgreich installiert!")
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Installation der Systempakete: {e}")
        sys.exit(1)

# Funktion zur Installation der Pandas Version 1.5.3
def install_pandas():
    try:
        print("Installiere Pandas 1.5.3...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas==1.5.3"])
        print("Pandas erfolgreich installiert!")
    except subprocess.CalledProcessError as e:
        print(f"Fehler bei der Installation von Pandas: {e}")
        sys.exit(1)

# Hauptfunktion
def main():
    install_system_dependencies()  # Systemabhängigkeiten installieren
    install_pandas()  # Pandas installieren
    # Dein vorhandenes Code hier

if __name__ == "__main__":
    main()

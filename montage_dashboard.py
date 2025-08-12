import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Montage-Daten: Name, Stundenaufwand, Erlös pro Einheit
montage_daten = {
    "UP-MK Zähler": (0.33, 12.00),
    "Aufputzzähler, Zapfhahnzähler + Zählwerkkopf": (0.33, 15.00),
    "Hauswasserzähler (bis Q3=16)": (0.5, 20.00),
    "Funkmodule WZ": (0.17, 5.00),
    "Funkmodule WMZ": (0.17, 5.00),
    "Split WMZ bis QN 10,0 m³/h": (0.75, 75.00),
    "Split WMZ QN 15,0 - QN 40,0 m³/h": (0.92, 120.00),
    "Split WMZ größer QN 40,0 m³/h": (1.01, 170.00),
    "MK- und Verschraubungszähler bis QN 2,5m³/h": (0.5, 30.00),
    "Montage Gateway": (0.5, 30.00),
    "Montage Netzwerkknoten": (0.42, 30.00),
    "HKVE Neuausstattung und Austausch": (0.75, 7.50),
    "HKVE Neuasstattung und Austausch Fernfühler": (0.5, 15.00),
    "Rauchmelder Neuausstattung und Austausch": (0.25, 8.00)
}

st.title("beatz.services GmbH Wirtschaftlichkeits-Dashboard für Montagen")

# Eingabe: Stundensatz und Anzahl Monteure
st.sidebar.header("Allgemeine Einstellungen")
stundensatz = st.sidebar.number_input("Stundensatz pro Monteur (€)", min_value=0.0, value=28.0, step=1.0)
anzahl_monteure = st.sidebar.number_input("Anzahl Monteure", min_value=1, value=1, step=1)
wochenstunden_pro_monteur = 40
gesamt_kapazitaet = anzahl_monteure * wochenstunden_pro_monteur

st.sidebar.markdown(f"**Gesamtkapazität pro Woche:** {gesamt_kapazitaet} Stunden")

# Eingabe: Anzahl Montagen pro Typ
st.sidebar.header("Montageanzahl eingeben")
anzahl_dict = {}
for montage in montage_daten:
    anzahl_dict[montage] = st.sidebar.number_input(f"{montage}", min_value=0, value=0, step=1)

# Berechnung
ergebnisse = []
for montage, (stunden, erloes) in montage_daten.items():
    anzahl = anzahl_dict[montage]
    kosten = stunden * stundensatz * anzahl
    gesamt_erloes = erloes * anzahl
    wirtschaftlichkeit = gesamt_erloes - kosten
    ergebnisse.append({
        "Montageart": montage,
        "Anzahl": anzahl,
        "Kosten (€)": round(kosten, 2),
        "Erlös (€)": round(gesamt_erloes, 2),
        "Wirtschaftlichkeit (€)": round(wirtschaftlichkeit, 2)
    })

df = pd.DataFrame(ergebnisse)
df = df[df["Anzahl"] > 0]

st.subheader("Ergebnisse")
st.dataframe(df)

# Diagramm
if not df.empty:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df["Montageart"], df["Wirtschaftlichkeit (€)"], color="skyblue")
    for i, row in df.iterrows():
        ax.text(i, row["Wirtschaftlichkeit (€)"], f'{row["Wirtschaftlichkeit (€)"]:.2f} €', ha='center', va='bottom')
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Wirtschaftlichkeit (€)")
    plt.title("Wirtschaftlichkeit pro Montageart")
    st.pyplot(fig)

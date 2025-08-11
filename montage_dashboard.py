import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Stundensatz
stundensatz = 28.0

# Montagearten mit Stunden und Erlösen
montagen = {
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

st.title("Wirtschaftlichkeits-Dashboard für Montagen")

st.sidebar.header("Anzahl der Montagen eingeben")
anzahl_dict = {}
for montage in montagen:
    anzahl_dict[montage] = st.sidebar.number_input(montage, min_value=0, value=0)

# Berechnung
daten = []
for montage, (stunden, erloes) in montagen.items():
    anzahl = anzahl_dict[montage]
    kosten = stunden * stundensatz * anzahl
    ges_erloes = erloes * anzahl
    wirtschaftlichkeit = ges_erloes - kosten
    daten.append([montage, anzahl, round(kosten, 2), round(ges_erloes, 2), round(wirtschaftlichkeit, 2)])

df = pd.DataFrame(daten, columns=["Montageart", "Anzahl", "Kosten (€)", "Erlös (€)", "Wirtschaftlichkeit (€)"])
st.subheader("Ergebnisse")
st.dataframe(df)

# Diagramm
st.subheader("Wirtschaftlichkeit pro Montageart")
fig, ax = plt.subplots()
df_plot = df[df["Anzahl"] > 0]
ax.barh(df_plot["Montageart"], df_plot["Wirtschaftlichkeit (€)"], color="green")
ax.set_xlabel("Wirtschaftlichkeit (€)")
st.pyplot(fig)

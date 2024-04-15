#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st

def Inhalator():
    class Patient:
        def __init__(self, spontane_atmung, gute_koordination, inspirationsfluss):
            self.spontane_atmung = spontane_atmung
            self.gute_koordination = gute_koordination
            self.inspirationsfluss = inspirationsfluss

    def empfehlung_für_inhalationssystem(patient):
        if patient.spontane_atmung == "Nein":
            return "Überdruckinhalator mit Spacer oder Vernebler (z.B. intubierter, beatmeter Patient)"
        if patient.gute_koordination == "Nein":
            if patient.inspirationsfluss > 30:
                return "Dosieraerosol mit Spacer oder atemzugsgesteuert, Vernebler"
            return "Dosieraerosol mit Spacer oder Vernebler (z.B. Kinder, geriatrische Patienten)"
        if patient.inspirationsfluss > 30:
            return "Dosieraerosol, Trockenpulverinhalation oder Vernebler"
        return "Dosieraerosol oder Vernebler (z.B. bei Patienten mit schwerer Störung des Atemflusses)"

    def show_empfehlung():
        st.header("Der richtige Inhalator?")

        spontane_atmung = st.radio("Hat der Patient eine spontane Atmung?", ("Ja", "Nein"))
        gute_koordination = st.radio("Hat der Patient eine gute Koordination?", ("Ja", "Nein"))
        inspirationsfluss = st.number_input("Bitte geben Sie den Inspirationsfluss des Patienten ein:", min_value=0, max_value=100, step=1, value=30)

        patient = Patient(spontane_atmung, gute_koordination, inspirationsfluss)

        if st.button("Empfehlung anzeigen"):
            empfehlung = empfehlung_für_inhalationssystem(patient)
            st.success(f"Empfohlenes Inhalationssystem: {empfehlung}")  # Verwendung von st.success für eine hervorgehobene Anzeige

            # Zusätzliche Informationen zu Inhalationssystemen
            st.subheader("Zusätzliche Informationen")
            st.markdown("""
            - **Dosieraerosole (MDI):** Geeignet für Patienten mit geringem maximalen inspiratorischen Druck (PImax) und guten Koordinationsfähigkeiten.
            - **Pulverinhalatoren (DPI):** Erfordern einen gerätespezifischen minimalen Inspirationsfluss. Bei schwerer Obstruktion mit stark eingeschränkten Flussraten kann die Inhalation mittels MDI der Pulverinhalation überlegen sein.
            - **Sprühvernebler:** Geeignet für Patienten mit geringem maximalen inspiratorischen Druck (PImax) und langsamer, kontinuierlicher Inhalation.
            - **Vernebler zur Feuchtinhalation:** Inhalation erfolgt möglichst langsam und tief. Geeignet für Patienten mit normalem Atemzugvolumen.
            - **Checklisten:** Hilfreich zur Überprüfung der Inhalationstechnik.
            """)
            st.markdown("---")

    show_empfehlung()


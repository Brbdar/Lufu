#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

def Inhalator():

    st.header("Der richtige Inhalator?")
    
    spontane_atmung = st.radio("Hat der Patient eine spontane Atmung?", ("Ja", "Nein"))
    gute_koordination = st.radio("Hat der Patient eine gute Koordination?", ("Ja", "Nein"))
    inspirationsfluss = st.number_input("Bitte geben Sie den Inspirationsfluss des Patienten ein:", min_value=0, max_value=100, step=1, value=30)
    
    def empfehlung_für_inhalationssystem(spontane_atmung, gute_koordination, inspirationsfluss):
        if spontane_atmung == "Ja":
            if gute_koordination == "Ja":
                if inspirationsfluss > 30:
                    return "Dosieraerosol, Trockenpulverinhalation oder Vernebler"
                else:
                    return "Dosieraerosol oder Vernebler (z.B. bei Patienten mit schwerer Störung des Atemflusses)"
            else:
                if inspirationsfluss > 30:
                    return "Dosieraerosol mit Spacer oder atemzugsgesteuert, Vernebler"
                else:
                    return "Dosieraerosol mit Spacer oder Vernebler (z.B. Kinder, geriatrische Patienten)"
        else:
            return "Überdruckinhalator mit Spacer oder Vernebler (z.B. intubierter, beatmeter Patient)"

    if st.button("Empfehlung anzeigen"):
        empfehlung = empfehlung_für_inhalationssystem(spontane_atmung, gute_koordination, inspirationsfluss)
        st.write("Empfohlenes Inhalationssystem:", empfehlung)
        
        # Zusätzliche Informationen zu Inhalationssystemen
        st.subheader("Zusätzliche Informationen:")
        st.markdown("""
        - **Dosieraerosole (MDI):** Geeignet für Patienten mit geringem maximalen inspiratorischen Druck (PImax) und guten Koordinationsfähigkeiten.
        - **Pulverinhalatoren (DPI):** Erfordern einen gerätespezifischen minimalen Inspirationsfluss. Bei schwerer Obstruktion mit stark eingeschränkten Flussraten kann die Inhalation mittels MDI der Pulverinhalation überlegen sein.
        - **Sprühvernebler:** Geeignet für Patienten mit geringem maximalen inspiratorischen Druck (PImax) und langsamer, kontinuierlicher Inhalation.
        - **Vernebler zur Feuchtinhalation:** Inhalation erfolgt möglichst langsam und tief. Geeignet für Patienten mit normalem Atemzugvolumen.
        - **Checklisten:** Hilfreich zur Überprüfung der Inhalationstechnik.
        """)


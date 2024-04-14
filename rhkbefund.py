#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st

def rhkbefund():
    st.header("### in ARBEIT")
    
    # Benutzereingaben


    # Titel der Streamlit-App
    st.title('Befundgenerator für pulmonale Hypertonie (in Arbeit)')

    # Benutzereingaben für pulmonale Hypertonie
    PAPm = st.number_input('PAPm (mmHg):', min_value=0.0, format='%f')
    PAWP = st.number_input('PAWP (mmHg):', min_value=0.0, format='%f')
    PVR = st.number_input('PVR (WE):', min_value=0.0, format='%f')
    HZV = st.number_input('HZV (l/min) [nur für Belastung PH]:', min_value=0.0, format='%f', help='Bitte nur ausfüllen, wenn Belastung PH bewertet wird.')

    # Logik zur Bestimmung der PH-Kategorie
    def determine_ph_category(PAPm, PAWP, PVR, HZV):
        if PAPm <= 20:
            return 'Keine PH'
        elif PAWP <= 15 and PVR > 2:
            return 'Präkapilläre PH'
        elif PAWP > 15 and PVR <= 2:
            return 'Isoliert postkapilläre PH (IpcPH)'
        elif PAWP > 15 and PVR > 2:
            return 'Kombiniert post- und präkapillare PH (CpcPH)'
        elif HZV > 0 and (PAPm / HZV) > 3:
            return 'Belastung PH'
        else:
            return 'PH, aber die Kategorie kann nicht bestimmt werden aufgrund der gegebenen Werte'

    # NYHA Klassifikation Abfrage
    nyha_class = st.radio(
        "Wählen Sie die NYHA-Klasse des Patienten:",
        ('NYHA Klasse I', 'NYHA Klasse II', 'NYHA Klasse III', 'NYHA Klasse IV')
    )

    # Beschreibungstexte für jede Klassifikation
    class_descriptions = {
        'NYHA I',
        'NYHA II',
        'NYHA III',
        'NYHA IV',
    }

    # Zusammenfassung der Befunde
    ph_category = determine_ph_category(PAPm, PAWP, PVR, HZV)
    nyha_description = class_descriptions[nyha_class]

    # Anzeigen des zusammenhängenden Fließtextes
    st.write(f"**Zusammenfassung des Befundes:** Basierend auf den Eingaben ist die Diagnose {ph_category}. Bezüglich der NYHA-Klassifikation fällt der Patient unter {nyha_class}: {nyha_description}")


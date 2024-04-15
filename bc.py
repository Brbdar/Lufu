#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st
import numpy as np
def bc():

    st.title('Klinisches Vorhersagemodell für Lungenknötchen')

    st.markdown("""
    <style>
    small-font {
        font-size:10px;
    }
    </style>
    <div class='small-font'>
    <b>Titel:</b> The probability of malignancy in solitary pulmonary nodules. Application to small radiologically indeterminate nodules<br>
    <b>Autoren:</b> S J Swensen, M D Silverstein, D M Ilstrup, C D Schleck, E S Edell
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("Hintergrund"):
        st.write("""
        Ein klinisches Vorhersagemodell zur Identifikation maligner Knötchen wurde unter Verwendung einer logistischen Regression aus einer zufälligen Stichprobe von Patienten (n = 419) abgeleitet und an Daten einer separaten Patientengruppe (n = 210) getestet.
        """)

    with st.expander("Ziel"):
        st.write("""
        Ziel ist es, die Wahrscheinlichkeit einer Malignität bei radiologisch unbestimmten solitären pulmonalen Noduli (SPNs) mit einem Durchmesser von 4 bis 30 mm in einer klinisch relevanten Untergruppe von Patienten mittels multivariater logistischer Regression zu schätzen.
        """)

    with st.expander("Patienten und Methoden"):
        st.write("""
        Eine retrospektive Kohortenstudie in einer multidisziplinären Gruppenpraxis umfasste 629 Patienten (320 Männer, 309 Frauen) mit neu entdeckten (zwischen dem 1. Januar 1984 und dem 1. Mai 1986) 4- bis 30-mm großen radiologisch unbestimmten SPNs auf der Thoraxradiographie. Patienten mit einer Krebsdiagnose innerhalb der letzten 5 Jahre vor der Entdeckung des Knötchens wurden ausgeschlossen. Klinische Daten umfassten Alter, Geschlecht, Zigarettenraucherstatus und Vorgeschichte einer extrathorakalen malignen Neoplasie, Asbestexposition sowie chronische interstitielle oder obstruktive Lungenerkrankung; radiologische Daten des Brustkorbs umfassten Durchmesser, Lage, Randcharakteristika (z.B. Lobulation, Spikulation und Zottigkeit) und andere Merkmale (z.B. Kavitation) der SPNs.
        """)


    def calculate_probability(x):
        return 100 * np.exp(x) / (1 + np.exp(x))

    def calculate_probability_with_fdg_pet(y):
        return 100 / (1 + np.exp(-y))

    def calculate_x(age, diameter, smoker, cancer, upper_lobe, spiculation):
        return (0.0391 * age) + (0.1274 * diameter) + (0.7917 * smoker) + (1.3388 * cancer) + (0.7838 * upper_lobe) + (1.0407 * spiculation) - 6.8272

    def calculate_y(probability, uptake):
        y_base = -4.739 + (3.691 * probability)
        uptake_dict = {'schwach': 2.322, 'moderat': 4.617, 'intensiv': 4.771}
        return y_base + uptake_dict.get(uptake, 0)

    st.title('Wahrscheinlichkeit einer Malignität')

    age = st.number_input('Alter in Jahren', value=30, min_value=0, max_value=100)
    diameter = st.number_input('Durchmesser des Knotens in mm', value=10, min_value=0, max_value=500)
    smoker = st.selectbox('Raucher?', options=['Nein', 'Ja'], index=0)
    cancer = st.selectbox('Frühere Krebsdiagnose ≥5 Jahre?', options=['Nein', 'Ja'], index=0)
    upper_lobe = st.selectbox('Lage im oberen Lappen?', options=['Nein', 'Ja'], index=0)
    spiculation = st.selectbox('Spikulation des Knotens?', options=['Nein', 'Ja'], index=0)
    uptake = st.selectbox('FDG-Aufnahme', options=['keine', 'faint', 'moderate', 'intense'], index=0)

    smoker_points = 1 if smoker == 'Ja' else 0
    cancer_points = 1 if cancer == 'Ja' else 0
    upper_lobe_points = 1 if upper_lobe == 'Ja' else 0
    spiculation_points = 1 if spiculation == 'Ja' else 0

    x = calculate_x(age, diameter, smoker_points, cancer_points, upper_lobe_points, spiculation_points)
    probability = calculate_probability(x)

    if uptake != 'keine':
        y = calculate_y(probability / 100, uptake)
        probability_with_fdg = calculate_probability_with_fdg_pet(y)
        st.write(f'Wahrscheinlichkeit einer Malignität mit FDG-PET: {probability_with_fdg:.2f}%')
    else:
        st.write('FDG-PET Daten nicht verfügbar')

    st.write(f'##Wahrscheinlichkeit einer Malignität: {probability:.2f}%')
    

    def management_recommendation(size_mm, nodule_type, risk_level, multiplicity):
        if nodule_type == 'solid':
            if diameter < 6:
                return 'Keine routinemäßige Nachsorge' if risk_level == 'niedrig' and multiplicity == 'einzeln' else 'Optionale CT nach 12 Monaten'
            elif 6 <= diameter <= 8:
                if risk_level == 'niedrig':
                    return 'CT nach 6-12 Monaten, dann Erwägung einer CT nach 18-24 Monaten'
                else:
                    return 'CT nach 6-12 Monaten, dann CT nach 18-24 Monaten'
            else:
                return 'Erwägung einer CT nach 3 Monaten, PET/CT oder Gewebeprobe'
        else:  # subsolide Knötchen
            if diameter < 6:
                return 'Keine routinemäßige Nachsorge' if nodule_type == 'Milchglas' else 'CT nach 3-6 Monaten, bei Stabilität Erwägung einer CT nach 2 und 4 Jahren'
            else:
                if nodule_type == 'teilweise solide':
                    return 'CT nach 3-6 Monaten zur Bestätigung der Persistenz. Wenn unverändert und solide Komponente <6 mm, dann jährliche CT für 5 Jahre'
                else:
                    return 'CT nach 6-12 Monaten zur Bestätigung der Persistenz, dann CT alle 2 Jahre bis 5 Jahre'

    st.title('Management von Lungenknötchen nach Fleischner Society')

    nodule_type = st.selectbox('Typ des Knötchens', options=['solide', 'Milchglas', 'teilweise solide'])
    risk_level = st.selectbox('Risikostufe', options=['niedrig', 'hoch'])
    multiplicity = st.selectbox('Anzahl der Knötchen', options=['einzeln', 'mehrfach'])

    recommendation = management_recommendation(diameter, nodule_type, risk_level, multiplicity)

    if age < 35 and recommendation.startswith('CT'):
        recommendation += " (Beachten Sie, dass bei Patienten unter 35 Jahren infektiöse Ursachen wahrscheinlicher als Krebs sind, daher sollte eine serielle CT begrenzt werden.)"

    st.write('##Empfehlung für das weitere Vorgehen:', recommendation)

    # Link zu weiterführenden Informationen
    st.image('nodes.jpg', caption='Visualisierung von Lungenknötchen')
    st.markdown(
    'Für weitere Informationen besuchen Sie die [Fleischner Society 2017 Richtlinie](https://radiologyassistant.nl/chest/plumonary-nodules/fleischner-2017-guideline).'
    )
    
    # Hinweis zur Formel für die Berechnung der Größe der Knötchen
    st.markdown("""
    **Berechnung der Durchschnittsgröße der Knötchen:**
    Verwenden Sie den Durchschnitt der langen und kurzen Achsen und runden Sie auf den nächsten Millimeter.
    """)
    
    
    # Trennlinie hinzufügen
    st.markdown("---")


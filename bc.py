#!/usr/bin/env python
# coding: utf-8

# In[28]:


import streamlit as st
import numpy as np

# Hilfsfunktionen
def calculate_probability(x):
    return 100 * np.exp(x) / (1 + np.exp(x))

def calculate_x(age, diameter, smoker, cancer, upper_lobe, spiculation):
    return (0.0391 * age) + (0.1274 * diameter) + (0.7917 * smoker) + (1.3388 * cancer) + (0.7838 * upper_lobe) + (1.0407 * spiculation) - 6.8272

def calculate_probability_with_fdg_pet(y):
    return 100 / (1 + np.exp(-y))

def calculate_y(probability, uptake):
    y_base = -4.739 + (3.691 * probability)
    uptake_dict = {'schwach': 2.322, 'moderat': 4.617, 'intensiv': 4.771}
    return y_base + uptake_dict.get(uptake, 0)



# Remember to adjust the user interface in Streamlit to ensure that inputs for nodule type, size, multiplicity, and risk level are correctly captured and passed to this function.

# Streamlit Benutzeroberfläche
def bc():
    st.title('Klinisches Vorhersagemodell für Lungenknötchen')

    with st.expander("Literaturhinweis"):
        st.markdown("**Titel:** The probability of malignancy in solitary pulmonary nodules. Application to small radiologically indeterminate nodules")
        st.markdown("**Autoren:** S J Swensen, M D Silverstein, D M Ilstrup, C D Schleck, E S Edell")

    with st.expander("Hintergrund"):
        st.write("Ein klinisches Vorhersagemodell zur Identifikation maligner Knötchen wurde unter Verwendung einer logistischen Regression abgeleitet und an Daten getestet.")

    with st.expander("Ziel"):
        st.write("Ziel ist es, die Wahrscheinlichkeit einer Malignität bei SPNs zu schätzen.")

    with st.expander("Patienten und Methoden"):
        st.write("Eine retrospektive Kohortenstudie umfasste 629 Patienten mit neu entdeckten 4- bis 30-mm großen SPNs.")

    age = st.number_input('Alter in Jahren', value=30, min_value=0, max_value=100)
    diameter = st.number_input('Durchmesser des Knotens in mm', value=10, min_value=0, max_value=500)
    smoker = st.selectbox('Raucher?', ['Nein', 'Ja'])
    cancer = st.selectbox('Frühere Krebsdiagnose ≥5 Jahre?', ['Nein', 'Ja'])
    upper_lobe = st.selectbox('Lage im oberen Lappen?', ['Nein', 'Ja'])
    spiculation = st.selectbox('Spikulation des Knotens?', ['Nein', 'Ja'])
    uptake = st.selectbox('FDG-Aufnahme', ['keine', 'schwach', 'moderat', 'intensiv'])

    # Ergebnisse berechnen und anzeigen
    x = calculate_x(age, diameter, 1 if smoker == 'Ja' else 0, 1 if cancer == 'Ja' else 0, 1 if upper_lobe == 'Ja' else 0, 1 if spiculation == 'Ja' else 0)
    probability = calculate_probability(x)
    result_text = f'## Wahrscheinlichkeit einer Malignität: {probability:.2f}%'

    if uptake != 'keine':
        y = calculate_y(probability / 100, uptake)
        probability_with_fdg = calculate_probability_with_fdg_pet(y)
        result_text += f' - Wahrscheinlichkeit mit FDG-PET: {probability_with_fdg:.2f}%'

    st.write(result_text)

    # Klinische Empfehlungen basierend auf der Wahrscheinlichkeit
    if probability < 2:
        st.success('Empfehlung: Beobachtung')
    elif 2 <= probability <= 20:
        st.warning('Empfehlung: Biopsie')
    elif probability > 70:
        st.error('Empfehlung: Operation')

    if uptake == 'keine':
        st.info('FDG-PET Daten nicht verfügbar')

    st.title('Management von Lungenknötchen nach Fleischner Society')
    
    nodule_type = st.selectbox('Typ des Knötchens', ['solide', 'Milchglas', 'teilweise solide'])
    risk_level = st.selectbox('Risikostufe', ['niedrig', 'hoch'])
    multiplicity = st.selectbox('Anzahl der Knötchen', ['einzeln', 'mehrfach'])
    
    def management_recommendation(diameter, nodule_type, risk_level, multiplicity):
    # Solid nodules
        if nodule_type == 'solide':
            if diameter < 6:
                if multiplicity == 'einzeln':
                    return 'Keine routinemäßige Nachsorge'
                else:  # Multiple
                    return 'Optionale CT nach 12 Monaten'
            elif 6 <= diameter <= 8:
                if multiplicity == 'einzeln':
                    if risk_level == 'niedrig':
                        return 'CT nach 6-12 Monaten, dann Erwägung einer CT nach 18-24 Monaten'
                    else:
                        return 'CT nach 6-12 Monaten, dann CT nach 18-24 Monaten'
                else:  # Multiple
                    if risk_level == 'niedrig':
                        return 'CT nach 3-6 Monaten, dann Erwägung einer CT nach 18-24 Monaten'
                    else:
                        return 'CT nach 3-6 Monaten, dann CT nach 18-24 Monaten'
            else:  # size_mm > 8
                if multiplicity == 'einzeln':
                    return 'Erwägung einer CT nach 3 Monaten, PET/CT oder Gewebeprobe'
                else:
                    return 'CT nach 3-6 Monaten, dann CT nach 18-24 Monaten'

        # Subsolid nodules
        elif nodule_type == 'Milchglas' or nodule_type == 'teilweise solide':
            if diameter < 6:
                return 'Keine routinemäßige Nachsorge'
            else:
                if nodule_type == 'Milchglas':
                    return 'CT nach 3-6 Monaten. Wenn stabil, Erwägung einer CT nach 2 und 4 Jahren'
                elif nodule_type == 'teilweise solide':
                    if multiplicity == 'einzeln':
                        return 'CT nach 6-12 Monaten zur Bestätigung der Persistenz, dann CT alle 2 Jahre bis 5 Jahre'
                    else:
                        return 'CT nach 3-6 Monaten zur Bestätigung der Persistenz. Wenn unverändert und solide Komponente <6 mm, dann jährliche CT für 5 Jahre'

        return 'Bitte überprüfen Sie die Eingaben, keine passende Empfehlung gefunden.'

    recommendation = management_recommendation(diameter, nodule_type, risk_level, multiplicity)
    st.info(f'Empfehlung für das weitere Vorgehen: {recommendation}')

    # Link zu weiterführenden Informationen und Visualisierung
    st.image('nodes.jpg', caption='Visualisierung von Lungenknötchen')
    st.markdown('Für weitere Informationen besuchen Sie die [Fleischner Society 2017 Richtlinie](https://radiologyassistant.nl/chest/plumonary-nodules/fleischner-2017-guideline).')



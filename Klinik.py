#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st

def Klinik():
    st.header("Klinik")

    # Datenstruktur für Symptome und Beschreibungen
    symptome = {
        "Belastungsdyspnoe": "Dyspnoe, die typischerweise bei körperlicher Anstrengung auftritt und durch eine Dysfunktion des rechten Ventrikels verursacht wird.",
        "Fatigue und Abgeschlagenheit": "Allgemeines Gefühl der Ermüdung, das sich mit fortschreitender Krankheit verschlimmert.",
        "Dyspnoe beim Vorüberbeugen": "Atemnot, die beim Vorbeugen auftritt, bekannt als Bendopnoe.",
        "Palpitationen": "Unangenehm spürbare Herzschläge, die durch den erhöhten Arbeitsaufwand des Herzens entstehen können.",
        "Hämoptysen": "Aushusten von Blut, was auf schwere Krankheitszustände hinweisen kann.",
        # Fügen Sie hier weitere Symptome und deren Beschreibungen hinzu
    }

    # Titel der App
    st.title('Lerneinheit zur Klinik bei PH-Patienten')

    # Einführungstext
    st.markdown('''
    Die pulmonale Hypertonie (PH) ist eine ernsthafte Erkrankung, die vor allem durch eine Dysfunktion des rechten Ventrikels charakterisiert wird.
    Die Symptome und klinischen Zeichen variieren je nach Stadium und Schweregrad der Erkrankung. Hier eine Übersicht der Symptome:
    ''')

    # Auswahlbox für Symptome
    symptom_auswahl = st.selectbox('Wählen Sie ein Symptom aus der Liste:', list(symptome.keys()))

    # Anzeige der Beschreibung zum ausgewählten Symptom
    st.subheader('Beschreibung des Symptoms:')
    st.write(symptome[symptom_auswahl])

    # Erklärung der Dysfunktion des rechten Ventrikels
    st.subheader('Dysfunktion des rechten Ventrikels und PH:')
    st.markdown('''
    Die Symptome der PH sind hauptsächlich auf eine Dysfunktion des rechten Ventrikels zurückzuführen. Diese manifestieren sich im Frühstadium der Erkrankung typischerweise bei körperlicher Anstrengung.
    Ein Schlüsselsymptom ist die Dyspnoe, die zunehmend auch unter geringerer Belastung auftritt.
    ''')

    # Hinweis für die Nutzer, wie sie die App verwenden können
    st.sidebar.info('Nutzen Sie diese App, um durch die verschiedenen Symptome der pulmonalen Hypertonie zu navigieren und lernen Sie mehr über deren Zusammenhang mit der rechten Ventrikeldysfunktion.')


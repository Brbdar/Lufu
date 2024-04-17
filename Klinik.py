#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st

def Klinik():
    st.header("Diagnoste Algorithmus PH - Klinik bei pulmonaler Hypertonie")

    # Datenstruktur für Symptome und deren detaillierte physiologische Beschreibungen
    symptome = {
        "Belastungsdyspnoe": "Dyspnoe bei Belastung durch erhöhte Nachlast, verminderte Compliance und erschwerte Rechtsherzauswurfleistung.",
        "Fatigue und Abgeschlagenheit": "Resultiert aus unzureichender Sauerstoffversorgung der Muskulatur und gesteigerter metabolischer Anforderung bei chronischer Herzbelastung.",
        "Dyspnoe beim Vorüberbeugen": "Bendopnoe, ausgelöst durch die Verlagerung intrathorakaler Blutvolumina, was den Druck im rechten Herzen weiter erhöht.",
        "Palpitationen": "Häufig durch Tachyarrhythmien als Antwort auf Hypoxie und rechtsventrikuläre Belastung.",
        "Hämoptysen": "Typischerweise ein Indikator für eine extreme Belastung der pulmonalen Zirkulation, die zu Kapillarrupturen führen kann.",
        # Weitere Symptome und deren Beschreibungen
    }


    # Einführungstext
    st.markdown('''
    Pulmonale Hypertonie ist gekennzeichnet durch den progressiven Anstieg des pulmonalen arteriellen Drucks, der zu einer schweren Belastung und schließlich zum Versagen des rechten Ventrikels führt.
    Die folgende Übersicht bietet Einblick in die vielfältigen Symptome, die mit verschiedenen Stadien dieser komplexen Erkrankung assoziiert sind:
    ''')

    # Auswahlbox für Symptome
    symptom_auswahl = st.selectbox('Wählen Sie ein Symptom aus:', list(symptome.keys()))

    # Anzeige der Beschreibung zum ausgewählten Symptom
    st.subheader('Beschreibung des Symptoms:')
    st.write(symptome[symptom_auswahl])

    # Erweiterte Erklärung der Pathophysiologie
    st.subheader('Pathophysiologie der pulmonalen Hypertonie:')
    st.markdown('''
    Pulmonale Hypertonie führt zu einer progressiven Belastung des rechten Ventrikels, die initial bei körperlicher Anstrengung symptomatisch wird und in fortgeschrittenen Stadien auch in Ruhe manifest sein kann. Eine zentrale Rolle spielen dabei die chronische Druckerhöhung im kleinen Kreislauf und die daraus resultierende Hypertrophie und Dilatation des rechten Ventrikels.
    ''')


    
    # Bild einfügen
    st.image("klinik.jpg", caption="Visualisierung der Klinik")

    # Link zu den Leitlinien
    st.markdown('''
    Weitere Informationen finden Sie in den [Leitlinien zur pulmonalen Hypertonie](https://academic.oup.com/eurheartj/article/43/38/3618/6673929?login=false#413902448).
    ''')

    # Hinweis für die Nutzer, wie sie die App verwenden können
    st.sidebar.info('Nutzen Sie diese App, um durch die verschiedenen Symptome der pulmonalen Hypertonie zu navigieren und lernen Sie mehr über deren Zusammenhang mit der rechten Ventrikeldysfunktion.')


# In[ ]:





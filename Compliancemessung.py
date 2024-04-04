#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

def Compliancemessung():
    st.header("Compliancemessung")
    
    st.write("Die Dehnbarkeit der Lunge, oder Lungencompliance, beschreibt über eine physikalische Kennzahl die elastischen Charakteristika der Lunge. Sie repräsentiert das Verhältnis zwischen der Änderung im Lungenvolumen und der damit verbundenen Druckänderung, gemessen in ml/mbar.")

    with st.expander("Basisinformationen:"):
        st.write("""
        - Erwachsene Lungencompliance: Circa 200 ml/cm H₂O für beide Lungen zusammen.
        - Die mechanischen Eigenschaften der Lunge, gemessen durch die pulmonale Compliance, verstärken sich mit Versteifung und schwächen ab bei Erschlaffung.
        - Bester Parameter zur Beurteilung restriktiver Ventilationsstörungen
        - Höchste Empfindlichkeit und gut Reproduzierbar
        - Compliance = dP/dV
        - Der transpulmonale Druck ist die Druckdifferenz zwischen Alveole und Pleuraspalt
        - Reziprokwert der Compliance ist die Elastance
        - Der Ösophagusdruck dient als Ersatz für den Pleuraspaltdruck bei Messungen, wobei sich der Alveolardruck dem Munddruck nach Angleichung anpasst.
        """)

    with st.expander("Erweitert:"):
        st.write("""
        - Untersuchungsdauer 30 Minuten
        - Vom Patienten als unangenehm empfundene Messung
        - Unabhängig von Mitarbeit des Patienten
        - Steife Lungen müssen hohe transpulmonale Druckänderungen für geforderte Volumenänderungen aufbringen. Daher Korrelation der Compliance mit Atemarbeit bei restriktiven Ventilationsstörungen. 
        """)

    with st.expander("Relevante Erkrankungen, die die Lungencompliance beeinflussen:"):
        st.write("""
        - **Emphysem oder COPD:** Verursacht durch genetische Faktoren oder äußere Einflüsse wie Rauchen; beschädigt die elastische Rückstellkraft der Lunge, was zu einer erhöhten Compliance führt.
        - **Pulmonale Fibrose:** Durch Umweltgifte, Chemikalien oder Infektionen verursacht; ersetzt elastische Fasern durch weniger elastische Kollagene, was die Compliance verringert.
        - **Neugeborenen-Atemnotsyndrom:** Fehlendes Surfactant bei Frühgeborenen führt zu verringerter Compliance und erhöhter Kollapsneigung der Lunge.
        - **Atelektase/ARDS:** Alveolarkollaps, häufig nach Operationen, verringert die Lungencompliance und erfordert höheren Druck für die Alveolenbelüftung.
        """)

      # Bilder als Platzhalter für interaktive Auswahl
    with st.columns(1)[0]:  # Direkter Zugriff auf das erste Element der Liste
        if st.button('Compliance'):
            st.session_state.selected_curve = 'Compliance'   
    
    if 'selected_curve' in st.session_state:
        if st.session_state.selected_curve == 'Compliance':
            st.image("compliance.jpg")
    
    eingabe_compliance = st.number_input("Geben Sie die Compliance in ml/cm H₂O ein:", value=200.0, step=1.0)

    if st.button('Compliance beurteilen', key='compliance_evaluate'):
        befund = beurteile_compliance(eingabe_compliance)
        st.write(befund)
        
def beurteile_compliance(eingabe_compliance):
    normal_min = 180.0  # Untergrenze des Normalbereichs in ml/cm H₂O
    normal_max = 220.0  # Obergrenze des Normalbereichs in ml/cm H₂O
    normal_mittelwert = (normal_min + normal_max) / 2
    abweichung_prozent = ((eingabe_compliance - normal_mittelwert) / normal_mittelwert) * 100

    if normal_min <= eingabe_compliance <= normal_max:
        befund = "Die eingegebene Compliance liegt im normalen Bereich."
        empfehlung = "Keine spezifischen Maßnahmen erforderlich."
    elif eingabe_compliance < normal_min:
        befund = "Die eingegebene Compliance ist niedriger als normal. Dies könnte auf eine restriktive Ventilationsstörung hinweisen."
        empfehlung = "Weitere diagnostische Abklärung empfohlen, um zugrunde liegende Ursachen wie pulmonale Fibrose oder Atelektase zu identifizieren."
    else:  # eingabe_compliance > normal_max
        befund = "Die eingegebene Compliance ist höher als normal. Dies könnte auf eine obstruktive Lungenerkrankung wie COPD oder Emphysem hinweisen."
        empfehlung = "Eine weiterführende Untersuchung zur Bestätigung der Diagnose und zur Einleitung einer geeigneten Behandlung wird empfohlen."

    return f"{befund}\n{empfehlung}"

# Hauptfunktion aufrufen
# Compliancemessung()

    st.markdown("[Mehr Informationen zur Compliance](https://www.ncbi.nlm.nih.gov/books/NBK538324/)")


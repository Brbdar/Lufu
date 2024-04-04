#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

def spirometrie_qualitativ():
    st.header("Spirometrie qualitativ")
    
    st.write('Die Patientenmitarbeit beeinflusst wesentlich alle Parameter, **vor allem den exspiratorischen Fluss bis MEF 75**, während Flüsse ab MEF 50 weitestgehend unabhängig sind. **Diese Mitarbeit ist bei der Diagnose zu berücksichtigen**')
    
    st.write('Bei der Spirometrie führt der Patient ein Tiffeneau-Manöver durch: Nach vollständiger Ausatmung atmet er so tief wie möglich ein und anschließend so schnell wie möglich aus. Diese Prozedur ermöglicht die Messung von FEV1, Vitalkapazität und weiteren Werten. Die dabei entstehende Fluss-Volumen-Kurve ist ein zentrales Instrument zur Beurteilung der Lungenfunktion.Die Form dieser Kurve und ihre Reaktion auf Bronchodilatatoren geben Aufschluss über obstruktive und restriktive Lungenkrankheiten sowie das Vorhandensein eines Emphysems.')

    # Erster Informationstext in einem ausklappbaren Bereich
    with st.expander("Basisinformationen:"):
        st.write("""
        **Spirometrie: Tiffeneau-Manöver** umfasst vollständige Ausatmung, maximale Einatmung, schnelle Ausatmung.
        - **Messungen:** FEV1, Vitalkapazität, Atemstromstärke.
        - **Fluss-Volumen-Schleife:** Atemvolumen vs. Atemstromstärke.
        - **Einatmung:** bauchförmige Kurve, rechts nach links.
        - **Ausatmung:** steiler Anstieg, langsamer Abfall.
        - **Ventilationsstörungen:** Eiform (Restriktion), Sesselform (Obstruktion, Emphysem), Bockwurstform (Trachealstenose).
        """)

    # Zweiter Informationstext in einem ausklappbaren Bereich
    with st.expander("Erweitert:"):
        st.write("""
        **Atemfluss:** negativ bei Einatmung (Inspiration nach unten), positiv bei Ausatmung (Exspiration nach oben).
        - **Kurvenform:** Inspiration steigt an, fällt ab (bauchförmig nach unten); forcierte Exspiration erreicht schnell maximalen Atemstrom (peak flow), linearer Abfall.
        - **Restriktion:** Verminderte Vitalkapazität, Atemfluss wenig beeinflusst (außer niedrigerer peak flow). Kurve verschmälert auf Volumen-Achse, kaum gestaucht auf Fluss-Achse → Eiform.
        - **Obstruktion:** Veränderter Atemfluss durch erhöhten Widerstand in Bronchien. Vitalkapazität nur bei Emphysem mit erhöhtem Residualvolumen verändert. Typische Sesselform durch Stauchung auf Fluss-Achse.
        - **Emphysem:** Mögliche normale/erhöhte Vitalkapazität trotz erhöhtem Residualvolumen. Verlust elastischer Fasern → reduzierte Retraktionskraft und Lungenkapazität, normalisiert Vitalkapazität. Elastische Fasern wichtig für Bronchienstabilität bei Ausatmung, deren Verlust führt zu Obstruktion.
        """)
        
    with st.expander("Kriterien für richtige Mitarbeit - Die Spirometrie verlangt vom Patienten maximale Kooperation, was leicht zu Anleitungsmissverständnissen und suboptimalen Atemmanövern führen kann, insbesondere bei der forcierten Exspiration."):
        st.write("""
        - Ein Peak Flow, der später als 0,12 Sekunden erreicht wird, deutet stets auf ungenügende Mitarbeit hin.
        - Ein abrupter Flow-Abfall am Ende der Exspiration (Kurve B) weist auf einen vorzeitigen Abbruch der Ausatmung hin.
        - Nichterreichen der totalen Lungenkapazität (TLC) bei der Inspiration signalisiert mangelnde Kooperation.
        """)


    # Bilder als Platzhalter für interaktive Auswahl
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Obstruktive Kurve'):
            st.session_state.selected_curve = 'Obstruktiv'
    with col2:
        if st.button('Restriktive Kurve'):
            st.session_state.selected_curve = 'Restriktiv'
    with col3:
        if st.button('Emphysem Kurve'):
            st.session_state.selected_curve = 'Emphysem'

    # Logik zur Anzeige der Erklärung basierend auf der Auswahl
    if 'selected_curve' in st.session_state:
        if st.session_state.selected_curve == 'Obstruktiv':
            st.write("Erklärung für Obstruktiv...")
            st.image("obstruktiv.jpg")
        elif st.session_state.selected_curve == 'Restriktiv':
            st.write("Erklärung für Restriktiv...")
            st.image("restriktiv.jpg")
        elif st.session_state.selected_curve == 'Emphysem':
            st.write("Erklärung für Emphysem...")
            st.image("emphysem.jpg")

    st.markdown("[Mehr Informationen zur Spirometrie](https://www.atsjournals.org/doi/epdf/10.1164/rccm.201908-1590ST?role=tab)")
            


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

def Bodyplethysmographie_Fluss_Druck_Kurve():
    st.header("Bodyplethysmographie - Fluss-Druck-Kurve")
    
    st.write('Zur Bestimmung des Widerstandes wird der Munddruck gemessen. Dieser wird dann graphisch in der Fluss-Druck-Kurve (= Atemschleife) dargestellt. Es werden Fluss und Munddruck gegen das Verschiebevolumen aufgetragen, wodurch zwei Schleifen entstehen.')

    st.write('Aussagekräftigste Methode bei Obstruktion, zuverlässigste Methode zur Residualvolumenbestimmung und mitarbeitsunabhängig, weil in Ruheatmung gemessen wird')
    st.write('auch bei Dyspnoe einsetzbar')
    
    # Erster Informationstext in einem ausklappbaren Bereich
    with st.expander("Basisinformationen:"):
        st.write("""
        - Untersuchung dauer fünf Minuten pro Messung
        - Messfehler < 5%
        - Wichtig. Die Differenzierung von obstruktiver Ventilationsstörungen mittels FEV1, FEV1/VC (Spirometrie), Residualvolumen und Atemwegswiderstand.
        - Messung von Residualvolumen und Atemwegswiderstand exklusiv durch Bodyplethysmographie.
        - Widerstandsbestimmung über Munddruckmessung, visualisiert in der Fluss-Druck-Kurve (Atemschleife) durch Auftragung gegen Verschiebevolumen.
        - Diagnosekriterium für Obstruktion: Schnittpunkt der Schleifen bei >90°; bei Gesunden oder restriktiven Störungen <90°.
        - Emphysem induziert eine charakteristische Keulenform der Atemschleife.
        """)

    # Zweiter Informationstext in einem ausklappbaren Bereich
    with st.expander("Erweitert:"):
        st.write("""
        - Einatmung und Ausatmung in der Fluss-Druck-Kurve gegenläufig zur Fluss-Volumen-Kurve dargestellt.
        - Gerade durch Schleifen bei Gesunden steil (kleiner Schnittwinkel), bei Obstruktiven flach (großer Schnittwinkel), bedingt durch den höheren Widerstand bei Obstruktion.
        - Notwendigkeit eines größeren Drucks bei Obstruktion, um gleichen Atemfluss zu erzeugen, entsprechend dem physikalischen Gesetz: Widerstand = Druck / Atemstrom.
        - Emphysem und Air Trapping führen zu endexspiratorischem Bronchiolenkollaps, erhöhtem notwendigen Atmungsdruck und Residualvolumen.
        - Graphische Darstellung als Keulenform der Kurve in der Exspiration, erweiterte untere Schleife, die x-Achse an unterschiedlichen Punkten schneidet.
        """)


    # Bilder als Platzhalter für interaktive Auswahl
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button('Normale Atemflusskurve'):
            st.session_state.selected_curve = 'Normal'
    with col2:
        if st.button('Emphysematöse Atemflusskurve'):
            st.session_state.selected_curve = 'Emphysem'
    with col3:
        if st.button('Obstruktion'):
            st.session_state.selected_curve = 'Obstruktion'
    with col4:
        if st.button('Reversible Obstruktion'):
            st.session_state.selected_curve = 'Reversible Obstruktion'

    # Logik zur Anzeige der Erklärung basierend auf der Auswahl
    if 'selected_curve' in st.session_state:
        if st.session_state.selected_curve == 'Normal':
            st.write("In der Schleife geht die Einatmung nach oben, die Ausatmung nach unten (umgekehrt der Fluss-Volumen-Kurve). Die Gerade durch die Schleifen ist beim Gesunden steil (hierdurch kleiner Schnittwinkel)")
            st.image("Atemschleife_normal.jpg")
        elif st.session_state.selected_curve == 'Emphysem':
            st.write("Befund Schnittwinkel der Schleifen > 90° als Zeichen der Obstruktion. Ausgeprägte Keulenform als Zeichen eines Emphysems. Kaum ein Unterschied vor (blau) und nach (rot) Broncholyse.")
            st.image("Emphysem_verschiebevolumen.jpg")
        elif st.session_state.selected_curve == 'Obstruktion':
            st.write("Schnittwinkel der Schleifen > 90° als Zeichen der Obstruktion. Keulenform als Zeichen eines Emphysems. Unter Broncholyse geringe Verkleinerung des Winkels mit leichter Verschmälerung der Keulenform als Hinweis auf ein geringes Air Trapping.")
            st.image("Obstruktion_flussvolumenkurve.jpg")
        elif st.session_state.selected_curve == 'Reversible Obstruktion':
            st.write("Schnittwinkel der Schleifen > 90° als Zeichen der Obstruktion. Geringe Keulenform als Zeichen eines erhöhten Residualvolumens. Unter Broncholyse (rot) normale Atemschleife als Zeichen einer reversiblen Obstruktion und eines Air Trappings.")
            st.image("Reversible_Obstruktion.jpg")



    st.title("Analyse der Atemschleifen")

    # Erweitere die Fragen, um spezifischere pathophysiologische Zustände zu adressieren
    frage1 = st.radio(
        "Schneiden sich die Schleifen der Atemkurve in einem Winkel größer als 90°?",
        ('Ja', 'Nein'),
        help="Ein Winkel > 90° kann auf eine Obstruktion hinweisen."
    )

    frage2 = st.radio(
        "Zeigt die Atemschleife eine Keulenform?",
        ('Ja', 'Nein'),
        help="Eine Keulenform deutet oft auf ein Emphysem hin."
    )

    frage3 = st.radio(
        "Ist die Steigung der Schleife während der Ausatmung deutlich flacher im Vergleich zur Einatmung?",
        ('Ja', 'Nein'),
        help="Eine flachere Steigung bei Ausatmung spricht für einen erhöhten Widerstand."
    )

    frage4 = st.radio(
        "Endet die exspiratorische Schleife auf einem höheren Niveau als sie begonnen hat?",
        ('Ja', 'Nein'),
        help="Ein höheres Ende der exspiratorischen Schleife kann auf Air Trapping hinweisen."
    )

    frage5 = st.radio(
        "Ist eine 'Bauchbildung' im exspiratorischen Teil der Atemschleife erkennbar?",
        ('Ja', 'Nein'),
        help="Eine 'Bauchbildung' kann bei Übergewichtigen vorkommen oder auf eine restriktive Störung hinweisen."
    )

    frage6 = st.radio(
        "Gibt es Anzeichen für ein 'stehendes Ei' oder eine 'Kofferkurve' in der Schleife?",
        ('Ja', 'Nein'),
        help="'Stehendes Ei' oder 'Kofferkurve' können auf eine zentrale Atemwegsstenose hinweisen."
    )

    # Analyse basierend auf den Antworten und Generierung des Befundes
    def generiere_befund(antworten):
        befund = []

        # Obstruktive Ventilationsstörung
        if antworten[0] == 'Ja':
            befund.append("Hinweis auf obstruktive Ventilationsstörung.")

        # Emphysem oder Air Trapping
        if antworten[1] == 'Ja':
            befund.append("Möglicher Befund eines Emphysems oder Air Trapping.")

        # Erhöhter exspiratorischer Widerstand
        if antworten[2] == 'Ja':
            befund.append("Erhöhter exspiratorischer Widerstand festgestellt.")

        # Erhöhtes Residualvolumen
        if antworten[3] == 'Ja':
            befund.append("Anzeichen für erhöhtes Residualvolumen.")

        # Restriktive Störung bei Übergewicht oder Lungenfibrose
        if antworten[4] == 'Ja':
            befund.append("Restriktive Ventilationsstörung möglich, besonders bei Patienten mit Übergewicht.")

        # Zentrale Atemwegsstenose
        if antworten[5] == 'Ja':
            befund.append("Befund deutet auf eine zentrale Atemwegsstenose hin.")

        if not befund:
            return "Keine spezifischen Auffälligkeiten basierend auf den Antworten gefunden."

        return "Befund:\n" + "\n".join(befund)

    antworten = [frage1, frage2, frage3, frage4, frage5, frage6]
    befund = generiere_befund(antworten)

    st.markdown(befund)


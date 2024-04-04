#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

def P0_Atemkraftmessung():
    st.header("P0_Atemkraftmessung")
    
    st.write("Die P0.1-Messung dient der Überprüfung der Atemmuskulatur, um festzustellen, ob diese ausreichend Luft in die Lungen befördert. Sie ist wichtig für die Diagnose von Atemschwäche und die Entscheidung über den Beginn einer Heimbeatmung. Diese Messung betrifft sowohl das Zwerchfell als auch unterstützende Muskeln. Eine ungenügende Atemleistung kann zu einem Anstieg des Kohlendioxidgehalts im Blut führen. Funktionsstörungen der Atempumpe können durch zentrale Nervensystemprobleme, neuromuskuläre Erkrankungen, Skelettdeformitäten oder Lungenerkrankungen verursacht werden.")
    
    with st.expander("Durchführung der Messung - Last der Atemmuskulatur = P0.1-Wert"):
        st.write("""
        - Elektromagnetisches Ventil verschließt Atemweg direkt nach Einatmung für 0,15 Sekunden..
        - Inspirationsdruck wird nach 100 Millisekunden (0,1s) gemessen.
        - Druck am Mund zeigt den Unterdruck in Alveolen und somit Krafteinsatz der Atemmuskulatur.
        - Kurze Atmungsunterbrechung, vom Patienten unbemerkt, beeinflusst Atmung nicht.
        - Messung erfolgt etwa 10-mal zu zufälligen Zeiten, Mittelwertbildung.
        - P0.1-Wert (kPa) reflektiert Atemmuskulaturbelastung bei Ruheatmung.
        - P0.1-Messung allein zeigt keine atemmuskuläre Schwäche auf.
        - Es gilt ein geschlechtsunabhängiger Grenzwert von ≤ 0,3 kPa als normal.
        """)

    with st.expander("Die Maximale Atemmuskelkraft"):
        st.write("""
        - Patient atmet vollständig aus und inhaliert dann maximal gegen geschlossenes Ventil.
        - Ventil bleibt für 3–5 Sekunden geschlossen, mindestens bis maximaler Druck erreicht ist.
        - Manöver wird 6-mal wiederholt.
        - Höchster ermittelter Druck definiert als Pimax (maximale Atemmuskelkraft).
        """)
        
    with st.expander("Indikationen"):
        st.write("""
        - Bewertung der Atemmuskelfunktion bei Verdacht auf Muskelschwäche.
        - Diagnose und Überwachung von Atemwegserkrankungen wie COPD und Asthma.
        - Einschätzung von Atemantriebsstörungen, z.B. bei Hypoventilationssyndromen.
        - Beurteilung der Effektivität therapeutischer Interventionen.
        - Langzeitüberwachung von Patienten mit neuromuskulären Erkrankungen.
        """)
        
    with st.expander("Maßnahmen"):
        st.write("""
        - Physiotherapie und Atemübungen: Stärkung der Atemmuskulatur, Verbesserung der Atemeffizienz.
        - Nicht-invasive Beatmung (NIV): Reduktion der Atemarbeit, Normalisierung der Blutgase.
        - Medikamentöse Therapieanpassung: Verringerung der Atemwegsobstruktion, Erleichterung der Atmung.
        - Lebensstiländerungen: Gewichtsabnahme, Raucherentwöhnung zur Verbesserung der Lungenfunktion.
        - Invasive Beatmung: Bei akutem respiratorischem Versagen oder schweren neuromuskulären Erkrankungen.
        - Chirurgische Maßnahmen: Z.B. Lungenvolumenreduktion bei schwerer COPD.
        """)

    st.write("""
        Dieses Tool hilft bei der Interpretation von Schlüsselparametern zur Beurteilung der Atemmuskulatur:
        - **P0.1 (kPa):** Misst die Last der Atemmuskulatur bei Ruheatmung.
        - **PImax (kPa):** Gibt die maximale inspiratorische Atemmuskelkraft an.
        Der Quotient **P0.1/PImax** reflektiert die prozentuale Beanspruchung der Atemmuskulatur, was Aufschlüsse über die respiratorische Kapazität gibt.
    """)



    # Funktion zur Interpretation des P0.1-Werts
    def interpret_p01(p01_value):
        if p01_value < 0.3:
            return "Der P0.1-Wert liegt im Normbereich."
        else:
            return "Der P0.1-Wert überschreitet den Normbereich und könnte auf eine erhöhte Atemlast hinweisen."

    def interpret_pimax(pimax_value, gender, age):
        st.write("Interpretiert den PImax-Wert basierend auf Alter, Geschlecht und den gegebenen Interpretationsrichtlinien")
    
    
        # Normwerte für PImax basierend auf Alter und Geschlecht
        normwerte = {
            'm': [(40, 6.2), (60, 5.4), (80, 4.6), (float('inf'), 4.1)],
            'f': [(40, 5.7), (60, 4.9), (80, 4.2), (float('inf'), 3.7)]
        }

        # Ermitteln der entsprechenden Normwerte
        for age_threshold, pimax_norm in normwerte[gender]:
            if age <= age_threshold:
                pimax_norm_value = pimax_norm
                break

        # Interpretation basierend auf dem Vergleich des gemessenen Werts mit dem Normwert
        if pimax_value >= pimax_norm_value:
            return f"Der PImax-Wert von {pimax_value} kPa liegt im Normbereich oder darüber (Normwert für Ihre Altersgruppe: {pimax_norm_value} kPa)."
        else:
            return f"Der PImax-Wert von {pimax_value} kPa ist niedriger als der Normwert für Ihre Altersgruppe ({pimax_norm_value} kPa) und könnte auf eine Schwäche der Inspirationsmuskulatur hinweisen."

    # Funktion zur Berechnung und Interpretation des P0.1/PImax-Quotienten
    def calculate_and_interpret_p01_pimax_ratio(p01_value, pimax_value):
        if pimax_value == 0:
            return "PImax darf nicht 0 sein."
        ratio = (p01_value / pimax_value) * 100
        if ratio < 4:
            return f"Mit einem Quotienten von {ratio:.2f}% liegt die Beanspruchung im normalen Bereich."
        elif 4 <= ratio < 10:
            return f"Mit einem Quotienten von {ratio:.2f}% liegt eine leicht erhöhte Beanspruchung vor."
        elif 10 <= ratio < 15:
            return f"Mit einem Quotienten von {ratio:.2f}% liegt eine mittelgradig erhöhte Beanspruchung vor."
        elif 15 <= ratio <= 20:
            return f"Mit einem Quotienten von {ratio:.2f}% liegt eine schwergradig erhöhte Beanspruchung vor."
        else:
            return f"Mit einem Quotienten von {ratio:.2f}% wird von einer Erschöpfung der Atempumpe ausgegangen."

    # Geschlechts- und Altersauswahl hinzufügen
    gender = st.radio("Geschlecht:", ('m', 'f'), key='gender_select')
    age = st.number_input("Alter (Jahre):", min_value=0, max_value=120, step=1, format="%d")

    # P0.1-Wert Eingabe und Interpretation
    p01_value = st.number_input("Geben Sie den P0.1-Wert ein (in kPa):", min_value=0.0, max_value=1.0, step=0.01, format="%.2f")

    # PImax-Wert Eingabe
    pimax_value = st.number_input("Geben Sie den PImax-Wert ein (in kPa):", min_value=0.0, max_value=20.0, step=0.1, key='pimax_input')

    # Sofortige Interpretation der P0.1 und PImax Werte
    st.write(interpret_p01(p01_value))
    st.write(interpret_pimax(pimax_value, gender, age))

    # Interpretation des P0.1/PImax-Quotienten
    st.write(calculate_and_interpret_p01_pimax_ratio(p01_value, pimax_value))


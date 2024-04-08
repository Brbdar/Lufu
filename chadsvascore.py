#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st

def chadsvascore():
    st.header("CHA₂DS₂-VASc Score Rechner")


    with st.expander("Hintergrund"):
        st.write("""
        Zeitgenössische klinische Risikostratifizierungsschemata zur Vorhersage von Schlaganfall und Thromboembolie (TE) bei Patienten mit Vorhofflimmern (AF) basieren größtenteils auf Risikofaktoren, die aus Studienkohorten identifiziert wurden. Daher wurden viele potenzielle Risikofaktoren nicht berücksichtigt.
        """)

    with st.expander("Methoden"):
        st.write("""
        Wir haben das Birmingham/National Institute for Health and Clinical Excellence (NICE) Schlaganfallrisikostratifizierungsschema von 2006 verfeinert, indem wir einen risikofaktorbasierten Ansatz durch Neueinstufung und/oder Einbeziehung zusätzlicher neuer Risikofaktoren, wo relevant, anwandten. Dieses Schema wurde dann mit bestehenden Schlaganfallrisikostratifizierungsschemata in einer realen Kohorte von Patienten mit AF (n = 1.084) aus der Euro Heart Survey für AF verglichen.
        """)

    with st.expander("Ergebnisse"):
        st.write("""
        Die Risikokategorisierung unterschied sich stark zwischen den verschiedenen verglichenen Schemata. Patienten, die als hochriskant eingestuft wurden, reichten von 10,2% mit dem Framingham-Schema bis zu 75,7% mit dem Birmingham 2009 Schema. Das klassische CHADS2-Schema (Herzinsuffizienz, Hypertonie, Alter > 75, Diabetes, vorheriger Schlaganfall/transitorische ischämische Attacke) kategorisierte den größten Anteil (61,9%) in die mittlere Risikostrata, während das Birmingham 2009 Schema 15,1% in diese Kategorie einstufte. Das Birmingham 2009 Schema klassifizierte nur 9,2% als niedriges Risiko, während das Framingham-Schema 48,3% als niedriges Risiko einstufte. Berechnete C-Statistiken deuteten auf einen bescheidenen prädiktiven Wert aller Schemata für TE hin. Das Birmingham 2009 Schema schnitt marginal besser ab (C-Statistik, 0.606) als CHADS2. Allerdings waren die als niedriges Risiko durch das Birmingham 2009 und NICE Schema klassifizierten tatsächlich niedriges Risiko mit keinen aufgezeichneten TE-Ereignissen, während bei 1,4% der niedrigriskanten CHADS2-Subjekte TE-Ereignisse auftraten. Als Punktesystem ausgedrückt, zeigte das Birmingham 2009 Schema (CHA2DS2-VASc Akronym) einen Anstieg der TE-Rate mit zunehmenden Punktzahlen (P-Wert für Trend = .003).
        """)
    
    # Benutzereingaben über Streamlit-Widgets erfassen
    age = st.selectbox(
        'Alter:',
        ('<65 Jahre', '65-74 Jahre', '≥75 Jahre')
    )

    sex = st.selectbox(
        'Geschlecht:',
        ('Männlich', 'Weiblich')
    )

    congestive_heart_failure = st.checkbox('Vorgeschichte mit Herzinsuffizienz')
    hypertension = st.checkbox('Vorgeschichte mit Hypertonie')
    stroke_tia_thromboembolism = st.checkbox('Vorgeschichte mit Schlaganfall/TIA/Thromboembolismus')
    vascular_disease = st.checkbox('Vorgeschichte mit Gefäßerkrankungen (früherer MI, periphere Arterienkrankheit oder Aortenplaque)')
    diabetes_mellitus = st.checkbox('Vorgeschichte mit Diabetes mellitus')

    # Berechnung des Scores basierend auf Benutzereingaben
    score = 0

    if age == '65-74 Jahre':
        score += 1
    elif age == '≥75 Jahre':
        score += 2

    if sex == 'Weiblich':
        score += 1

    if congestive_heart_failure:
        score += 1
    if hypertension:
        score += 1
    if stroke_tia_thromboembolism:
        score += 2
    if vascular_disease:
        score += 1
    if diabetes_mellitus:
        score += 1

    # Interpretation des Scores anzeigen
    st.write(f'### Ihr CHA₂DS₂-VASc Score: {score}')

    if score == 0:
        st.write('Risiko eines ischämischen Schlaganfalls: 0.2%, Risiko eines Schlaganfalls/TIA/systemischer Embolie: 0.3%')
    elif score == 1:
        st.write('Risiko eines ischämischen Schlaganfalls: 0.6%, Risiko eines Schlaganfalls/TIA/systemischer Embolie: 0.9%')
    elif score == 2:
        st.write('Risiko eines ischämischen Schlaganfalls: 2.2%, Risiko eines Schlaganfalls/TIA/systemischer Embolie: 2.9%')
    elif score == 3:
        st.write('Risiko eines ischämischen Schlaganfalls: 3.2%, Risiko eines Schlaganfalls/TIA/systemischer Embolie: 4.6%')
    elif score >= 4 and score <= 5:
        st.write(f'Risiko eines ischämischen Schlaganfalls: {4.8 + (score - 4) * 2.4}%, Risiko eines Schlaganfalls/TIA/systemischer Embolie: {6.7 + (score - 4) * 3.3}%')
    elif score >= 6 and score <= 9:
        st.write(f'Risiko eines ischämischen Schlaganfalls: {9.7 + (score - 6) * 1.5}%, Risiko eines Schlaganfalls/TIA/systemischer Embolie: {13.6 + (score - 6) * 2.1}%')
    else:
        st.write('Bitte geben Sie gültige Werte ein.')


    # Definition der Risiko- und Behandlungsempfehlungen
    if sex == 'Männlich':
        if score == 0:
            treatment_recommendation = 'Keine antithrombotische Behandlung'
        elif score == 1:
            treatment_recommendation = 'Eine orale Antikoagulation sollte erwogen werden'
        else:  # score >= 2
            treatment_recommendation = 'Eine orale Antikoagulation wird empfohlen'
    else:  # Weiblich
        if score <= 1:
            treatment_recommendation = 'Keine antithrombotische Behandlung'
        elif score == 2:
            treatment_recommendation = 'Eine orale Antikoagulation sollte erwogen werden'
        else:  # score >= 3
            treatment_recommendation = 'Eine orale Antikoagulation wird empfohlen'

    # Anzeige der Behandlungsempfehlung
    st.write(f'### Empfohlenes Vorgehen: {treatment_recommendation}')
    
    markdown_content = """
    Refining Clinical Risk Stratification for Predicting Stroke and Thromboembolism in Atrial Fibrillation Using a Novel Risk Factor-Based Approach: The Euro Heart Survey on Atrial Fibrillation

    **Authors:** Gregory Y H Lip, Robby Nieuwlaat, Ron Pisters, Deirdre A Lane, Harry J G M Crijns

    **[Read the Abstract](https://journal.chestnet.org/article/S0012-3692(10)60067-0/abstract)**

    PMID: 19762550 | DOI: 10.1378/chest.09-1584
    """
    st.markdown(markdown_content)


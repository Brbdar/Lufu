#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st

def chadsvascore():
    st.header("CHA₂DS₂-VASc Score / HASBLED Score")
    
   # Titel der Anwendung
    st.title('CHA₂DS₂-VASc')
    
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

    # Altersangabe als Eingabefeld
    age = st.number_input('Alter:', min_value=0, max_value=120)

    # Weitere Eingaben aus CHA₂DS₂-VASc Score
    sex = st.selectbox('Geschlecht:', ('Männlich', 'Weiblich'))
    hypertension = st.checkbox('Vorgeschichte mit Hypertonie')
    congestive_heart_failure = st.checkbox('Vorgeschichte mit Herzinsuffizienz')
    stroke_tia_thromboembolism = st.checkbox('Vorgeschichte mit Schlaganfall/TIA/Thromboembolismus')
    vascular_disease = st.checkbox('Vorgeschichte mit Gefäßerkrankungen (früherer MI, periphere Arterienkrankheit oder Aortenplaque)')
    diabetes_mellitus = st.checkbox('Vorgeschichte mit Diabetes mellitus')

    # CHA₂DS₂-VASc Score Berechnung
    chads_score = 0
    if age >= 75:
        chads_score += 2
    elif age >= 65:
        chads_score += 1
    if sex == 'Weiblich':
        chads_score += 1
    if congestive_heart_failure:
        chads_score += 1
    if hypertension:
        chads_score += 1
    if stroke_tia_thromboembolism:
        chads_score += 2
    if vascular_disease:
        chads_score += 1
    if diabetes_mellitus:
        chads_score += 1

    # CHA₂DS₂-VASc Score Risikostratifizierung
    chads_risks = [
        (0.2, 0.3), (0.6, 0.9), (2.2, 2.9), (3.2, 4.6), (4.8, 6.7),
        (7.2, 10.0), (9.7, 13.6), (11.2, 15.7), (10.8, 15.2), (12.2, 17.4)
    ]
    risk_ischemic, risk_embolism = chads_risks[chads_score] if chads_score < 10 else chads_risks[9]

    st.write(f'### Ihr CHA₂DS₂-VASc Score: {chads_score}')
    st.write(f'Risiko eines ischämischen Schlaganfalls: {risk_ischemic}%')
    st.write(f'Risiko eines Schlaganfalls/TIA/systemischer Embolie: {risk_embolism}%')

    # HAS-BLED Score
    st.title('HAS-BLED Score')
             
    with st.expander("Ziel"):
        st.write("""
        Ziel der Studie war die Entwicklung eines praktischen Risikoscores, der das 1-Jahres-Risiko für schwere Blutungen bei Patienten mit Vorhofflimmern (AF) einschätzt. Schwere Blutungen beinhalten intrakranielle Blutungen, Krankenhausaufenthalte, einen Hämoglobinabfall von mehr als 2 g/L und/oder Transfusionen. Der Score soll bei der Entscheidungsfindung zur oralen Antikoagulationstherapie (OAC) helfen, die trotz ihres Nutzens mit einem erhöhten Blutungsrisiko verbunden ist.
        """)

    with st.expander("Methoden und Ergebnisse"):
        st.write("""
        **Methoden:** Unter Verwendung von 3,978 Patienten aus der Euro Heart Survey on AF, die komplett nachverfolgt wurden, wurden alle univariaten Blutungsrisikofaktoren in einer multivariaten Analyse berücksichtigt, um den HAS-BLED Score zu entwickeln. Dieser Score berücksichtigt Hypertonie, abnormale Nieren-/Leberfunktion, Schlaganfall, Blutungsanamnese oder -neigung, labile INR, Alter über 65 Jahre und gleichzeitigen Drogen-/Alkoholkonsum.

        **Ergebnisse:** Während des einjährigen Follow-ups traten bei 1,5% der Patienten schwere Blutungen auf. Die jährliche Blutungsrate stieg mit zunehmender Anzahl von Risikofaktoren. Die Vorhersagegenauigkeit für die gesamte Population lag bei einem C-Wert von 0,72 und zeigte in verschiedenen Untergruppen konsistente Ergebnisse. Die Anwendung des HAS-BLED Scores ergab ähnliche C-Werte, außer bei Patienten, die nur mit Thrombozytenaggregationshemmern oder ohne antithrombotische Therapie behandelt wurden, mit C-Werten von 0,91 bzw. 0,85.

        **Schlussfolgerung:** Der HAS-BLED Score bietet ein praktisches Werkzeug zur Bewertung des individuellen Blutungsrisikos bei Patienten mit Vorhofflimmern und unterstützt die klinische Entscheidungsfindung bezüglich der antithrombotischen Therapie.
        """)

    renal_disease = st.checkbox('Nierenerkrankung (Dialyse, Transplantation, Cr >2.26 mg/dL oder 200 µmol/L)')
    liver_disease = st.checkbox('Lebererkrankung (Zirrhose oder Bilirubin >2x normal mit AST/ALT/AP >3x normal)')
    prior_major_bleeding = st.checkbox('Vorgeschichte mit größeren Blutungen oder Blutungsneigung')
    labile_inr = st.checkbox('Labiles INR (instabile/hohe INRs, Zeit im therapeutischen Bereich <60%)')
    medication_usage = st.checkbox('Medikamenteneinnahme, die zu Blutungen prädisponiert (Aspirin, Clopidogrel, NSAIDs)')
    alcohol_usage = st.checkbox('Alkoholkonsum (≥8 Getränke/Woche)')

    hasbled_score = sum([
        hypertension, renal_disease, liver_disease, stroke_tia_thromboembolism,
        prior_major_bleeding, labile_inr, (age > 65), medication_usage, alcohol_usage
    ])

    # HAS-BLED Risk level mapping
    risk_levels = {
        0: ("Relativ gering", "1.13", "Antikoagulation sollte erwogen werden"),
        1: ("Moderat", "1.02", "Antikoagulation sollte erwogen werden"),
        2: ("Moderat", "1.88", "Antikoagulation kann erwogen werden"),
        3: ("Hoch", "3.72", "Alternativen zur Antikoagulation sollten erwogen werden"),
        4: ("Sehr hoch", "8.70", "Alternativen zur Antikoagulation sollten erwogen werden"),
        5: ("Sehr hoch", "12.50", "Alternativen zur Antikoagulation sollten erwogen werden"),
    }

    st.write(f'### Ihr HAS-BLED Score: {hasbled_score}')
    if hasbled_score > 5:
        st.write("Risiko einer großen Blutung: Sehr hoch")
        st.write("Empfehlung: Alternativen zur Antikoagulation sollten erwogen werden")
    else:
        risk, bleed_per_100, recommendation = risk_levels[hasbled_score]
        st.write(f"Risiko einer großen Blutung: {risk}")
        st.write(f"Blutungen pro 100 Patientenjahre: {bleed_per_100}")
        st.write(f"Empfehlung: {recommendation}")
        

    with st.expander("HAS-BLED Score Details"):
        st.write("""
        | HAS-BLED Score | Risikogruppe | Risiko schwerer Blutungen | Blutungen pro 100 Patientenjahre | Empfehlung |
        |----------------|--------------|---------------------------|----------------------------------|------------|
        | 0              | Relativ gering | 0.9%                    | 1.13                             | Antikoagulation sollte erwogen werden |
        | 1              | Moderat       | 3.4%                     | 1.02                             | - |
        | 2              | Moderat       | 4.1%                     | 1.88                             | Antikoagulation kann erwogen werden |
        | 3              | Hoch          | 5.8%                     | 3.72                             | Alternativen zur Antikoagulation sollten erwogen werden |
        | 4              | Sehr hoch     | 8.9%                     | 8.70                             | - |
        | 5              | Sehr hoch     | 9.1%                     | 12.50                            | - |
        | >5             | Sehr hoch     | Wahrscheinlich über 10%   | -                                | - |
        """, unsafe_allow_html=True)

    # Vergleich der Risiken
    risk_message = "Das Risiko einer Thrombose ist höher." if chads_score > hasbled_score else "Das Risiko einer Blutung ist höher."
    if chads_score == hasbled_score:
        risk_message = "Das Risiko einer Thrombose und einer Blutung sind gleich."

    st.write(f'### Vergleich der Risiken: {risk_message}')
    
    markdown_content = """
    Refining Clinical Risk Stratification for Predicting Stroke and Thromboembolism in Atrial Fibrillation Using a Novel Risk Factor-Based Approach: The Euro Heart Survey on Atrial Fibrillation

    **Authors:** Gregory Y H Lip, Robby Nieuwlaat, Ron Pisters, Deirdre A Lane, Harry J G M Crijns

    **[Read the Abstract](https://journal.chestnet.org/article/S0012-3692(10)60067-0/abstract)**

    PMID: 19762550 | DOI: 10.1378/chest.09-1584
    """
    st.markdown(markdown_content)
    
    markdown_content = """
    A Novel User-Friendly Score (HAS-BLED) To Assess 1-Year Risk of Major Bleeding in Patients With Atrial Fibrillation: The Euro Heart Survey

    **Authors:** Ron Pisters, MD, Deirdre A. Lane, PhD, Robby Nieuwlaat, PhD, Cees B. de Vos, MD

    **[Read the Abstract](https://journal.chestnet.org/article/S0012-3692(10)60585-5/abstract)**

    PMID: 20579545 | DOI: 10.1378/chest.10-60585
    """
    st.markdown(markdown_content)
    
    markdown_content = """
    Use of the CHA2DS2-VASc and HAS-BLED Scores to Aid Decision Making for Thromboprophylaxis in Nonvalvular Atrial Fibrillation

    **Authors:** Deirdre A. Lane and Gregory Y.H. Lip

    **Originally published:** 14 Aug 2012

    **[Read the Abstract](https://www.ahajournals.org/doi/full/10.1161/circulationaha.111.060061)**

    PMID: Not provided | DOI: 10.1161/CIRCULATIONAHA.111.060061
    """
    st.markdown(markdown_content)


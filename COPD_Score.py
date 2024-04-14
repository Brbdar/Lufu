#!/usr/bin/env python
# coding: utf-8

# In[29]:


import streamlit as st

def COPD_Score():
    import streamlit as st

    st.header("##COPD Klassifizieren")
    
    st.subheader("mMRC Dyspnoe-Skala")
    st.write("Bitte bewerten Sie Ihren Grad der Atemnot anhand der folgenden Beschreibungen. Wählen Sie die Beschreibung, die am besten zu Ihrer aktuellen Erfahrung passt.")

    mMRC_options = [
        "0 - Nur bei anstrengender Bewegung",
        "1 - Bei Eile auf ebenem Grund oder beim leichten Anstieg",
        "2 - Geht langsamer als Gleichaltrige auf ebenem Grund oder muss zum Atmen anhalten",
        "3 - Muss nach 100 Metern oder nach wenigen Minuten auf ebenem Grund anhalten",
        "4 - Zu atemlos, um das Haus zu verlassen oder atemlos beim Anziehen"
    ]
    mMRC_score = st.selectbox("Wählen Sie Ihren Grad der Atemnot:", mMRC_options, key="mMRC_score_selector")
    
    # Umwandlung der Auswahl in einen Punktwert
    mMRC_score_index = mMRC_options.index(mMRC_score)  # Integer-Wert der Auswahl

    st.header("COPD Klassifizieren")
    st.subheader("CAT-Score")

    symptome = {
    "Husten": ["nie", "selten", "gelegentlich", "regelmäßig", "häufig", "ständig"],
    "Schleim": ["kein", "wenig", "manchmal", "oft", "viel", "vollständig"],
    "Brustenge": ["frei", "leicht", "gelegentlich", "oft", "stark", "sehr stark"],
    "Atemnot": ["keine", "leicht", "mäßig", "mäßig+", "stark", "sehr stark"],
    "Aktivitäten": ["keine", "leicht", "moderat", "deutlich", "stark", "vollständig"],
    "Vertrauen": ["voll", "größtenteils", "leicht unsicher", "oft unsicher", "stark unsicher", "keines"],
    "Schlaf": ["fest", "leicht gestört", "gelegentlich gestört", "oft gestört", "stark gestört", "sehr schlecht"],
    "Energie": ["viel", "gut", "mäßig", "wenig", "sehr wenig", "keine"]
    }

    scores = {}
    for symptom, beschreibungen in symptome.items():
        selected_option = st.radio(
            f"{symptom}:",
            options=beschreibungen,
            horizontal=True,
            key=symptom  # Eindeutiger Schlüssel für jedes radio
        )
        scores[symptom] = beschreibungen.index(selected_option)  # Speichern des Index als Score

    # Berechnung der Gesamtpunktzahl
    total_score = sum(scores.values())
    st.write("### Gesamtpunktzahl Ihrer Symptome: ", total_score)

    # Exazerbationshistorie
    exacerbation_history = st.number_input("Anzahl der Exazerbationen im letzten Jahr:", min_value=0)


    # Klassifizierung in COPD-Gruppen gemäß den neuen ABE-Leitlinien
    if exacerbation_history >= 2 or (exacerbation_history == 1 and st.checkbox("Stationäre Behandlung benötigt")):
        copd_group = 'E'
        initial_therapy = "LAMA + LABA und ggf. ICS bei Asthma in der Vorgeschichte und/oder Eosinophilenzahlen von ≥300/μL"
    elif exacerbation_history == 1 or (mMRC_score_index >= 2 or total_score >= 10):
        copd_group = 'B'
        initial_therapy = "LAMA + LABA"
    else:
        copd_group = 'A'
        initial_therapy = "Monotherapie mit einem Bronchodilatator (LAMA oder LABA)"

    # Anzeige der COPD-Gruppe, Initialtherapie und weitere Empfehlungen
    st.write(f"### COPD-Gruppe: {copd_group}")
    st.write(f"### Empfohlene Initialtherapie: {initial_therapy}")
    st.write("### Weiterführende Empfehlungen basieren auf der Eskalationstherapie, abhängig von den spezifischen Anforderungen und dem Verlauf der Erkrankung.")
    st.write("Bitte beachten Sie, dass diese Bewertungen auf Ihren Angaben basieren und eine professionelle medizinische Bewertung nicht ersetzen können.")
    
    st.subheader("Eskalationstherapie")

    dyspnoe_focus = st.checkbox("Steht Dyspnoe im Vordergrund?")
    exacerbation_focus = st.checkbox("Stehen Exazerbationen im Vordergrund?")
    prev_treatment = st.selectbox(
        "Vorbehandlung auswählen:",
        ["Keine Vorbehandlung", "LABA", "LAMA", "LABA + LAMA", "LAMA + ICS"]
    )
    eosinophils = st.number_input("Eosinophilenzahl (falls bekannt):", min_value=0, step=10, format="%d")

    if dyspnoe_focus:
        if prev_treatment in ["LABA", "LAMA"]:
            st.success("Empfehlung: Erweitern auf LAMA + LABA.")
        elif prev_treatment == "LABA + LAMA":
            st.warning("Empfehlung: Wirkstoff- und/oder Inhalatorwechsel erwägen.")

    if exacerbation_focus:
        if prev_treatment in ["LABA", "LAMA"]:
            st.success("Empfehlung: Erweitern auf LAMA + LABA.")
        elif prev_treatment == "LAMA + LABA" and eosinophils >= 100:
            st.success("Empfehlung: Erweitern auf LAMA + LABA + ICS.")
        elif prev_treatment == "LAMA + LABA" and eosinophils < 100:
            st.info("Weitere Optionen zur Therapieeskalation prüfen.")
        elif prev_treatment == "LAMA + ICS":
            if eosinophils >= 300:
                st.success("Empfehlung: Umstellung auf LAMA + LABA + ICS.")
            else:
                st.info("Bei guter Therapieeinstellung: Beibehalten möglich. Bei unzureichendem Ansprechen: Umstellung erwägen.")

    fev1 = st.number_input("FEV1 in % (falls bekannt):", min_value=0, max_value=100, step=1, format="%d")
    chronic_bronchitis = st.checkbox("Chronische Bronchitis?")
    hospitalization_last_year = st.checkbox("Mindestens eine Hospitalisierung wegen COPD im Vorjahr?")

    if fev1 < 50 and chronic_bronchitis and hospitalization_last_year:
        st.error("Empfehlung: Roflumilast in Erwägung ziehen.")

    if exacerbation_focus:
        st.success("Empfehlung: Azithromycin in Erwägung ziehen, falls entsprechend indiziert.")

    st.info("""
    **Wichtige Informationen:**
    - Von einer Azithromycin-Gabe profitieren v.a. Patient:innen, die nicht mehr rauchen. Allerdings sollte die Gefahr der Resistenzentwicklung bei längerfristiger Gabe in die Therapieentscheidung mit einbezogen werden.
    - Bei Patienten mit obstruktiven Atemwegserkrankungen wie Asthma und COPD soll eine Therapie mit Inhalatoren nicht begonnen oder geändert werden, ohne dass der Patient im Gebrauch des Inhalationssystems geschult ist und die korrekte Anwendung der Inhalatoren überprüft wurde.
    """)

    st.markdown("""
    Development and first validation of the COPD Assessment Test

    P. W. Jones, G. Harding, P. Berry, I. Wiklund, W-H. Chen, N. Kline Leidy  
    *European Respiratory Journal* 2009 34: 648-654; DOI: [10.1183/09031936.00102509](https://erj.ersjournals.com/content/34/3/648.long)
    """)
    
    st.markdown("""
    **Verteilung und prognostische Validität der neuen Einstufung nach der Global Initiative for Chronic Obstructive Lung Disease**

    Joan B Soriano  1 , Inmaculada Alfageme  2 , Pere Almagro  3 , Ciro Casanova  4 , Cristobal Esteban  5 , Juan J Soler-Cataluña  6 , Juan P de Torres  7 , Pablo Martinez-Camblor  8 , Marc Miravitlles  9 , Bartolome R Celli  10 , Jose M Marin  11
    *Affiliationen erweitern*
    PMID: 23187891  DOI: [10.1378/chest.12-1053](https://pubmed.ncbi.nlm.nih.gov/23187891/)
    """)



# In[ ]:





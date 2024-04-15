#!/usr/bin/env python
# coding: utf-8

# In[26]:


import streamlit as st

def COPD_Score():

    st.header("COPD Klassifizieren")
    
    st.subheader("mMRC Dyspnoe-Skala")
    st.write("Bitte bewerten Sie Ihren Grad der Atemnot anhand der folgenden Beschreibungen. Wählen Sie die Beschreibung, die am besten zu Ihrer aktuellen Erfahrung passt.")
    with st.expander("mMRC (modified Medical Research Council) Skala für COPD"):
        st.write("""
        **Wichtigstes Symptom der COPD - Belastungsdyspnoe:**
        Die Belastungsdyspnoe wird mittels einer 5-Stufenskala gemessen, um die Schwere der Symptome zu bestimmen.

        **Skalierung:**
        - **Stufe 0:** Keine Belastungsdyspnoe
        - **Stufe 1:** Dyspnoe bei starker Belastung
        - **Stufe 2:** Dyspnoe beim schnellen Gehen oder leichten Anstiegen
        - **Stufe 3:** Dyspnoe, die schnelleres Gehen oder Gehen über kurze Distanzen behindert
        - **Stufe 4:** Zu kurzatmig, um das Haus zu verlassen, oder Dyspnoe beim An- und Auskleiden

        **Einstufung als wenig symptomatisch:**
        Patienten in den Stufen 0 und 1 gelten als wenig symptomatisch (Stadium A oder C).
        """)
    
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

    # User inputs
    dyspnoe_focus = st.checkbox("Steht Dyspnoe im Vordergrund?")
    exacerbation_focus = st.checkbox("Stehen Exazerbationen im Vordergrund?")
    prev_treatment = st.selectbox(
        "Vorbehandlung auswählen:",
        ["Keine Vorbehandlung", "LABA", "LAMA", "LABA + LAMA", "LAMA + ICS"]
    )
    eosinophils = st.number_input("Eosinophilenzahl (falls bekannt):", min_value=0, step=10, format="%d")
    fev1 = st.number_input("FEV1 in % (falls bekannt):", min_value=0, max_value=100, step=1, format="%d")
    chronic_bronchitis = st.checkbox("Chronische Bronchitis?")
    hospitalization_last_year = st.checkbox("Mindestens eine Hospitalisierung wegen COPD im Vorjahr?")

    # Therapeutic recommendations based on focus
    if dyspnoe_focus:
        if prev_treatment == "LABA" or prev_treatment == "LAMA":
            st.success("Empfehlung: Erweitern auf LAMA + LABA.")
            with st.expander("Kombinationspräparate LABA + LAMA"):
                st.write("""
                **Indikation:**
                Ab Gruppe B (gemäß COPD-Einteilung in ABE-Gruppen) einsetzbar. Kombinationspräparate verschiedener Hersteller stehen zur Verfügung, die Dosierungsfrequenz beträgt 1× oder 2× täglich.

                **Gängige Kombinationen:**
                - **Indacaterol + Glycopyrronium** (z.B. Ultibro® Breezhaler®, Xoterna® Breezhaler®, Ulunar® Breezhaler®):
                  - Dosis: 85/43 μg/Hub inhalativ 1-0-0, Tagesmaximaldosis 1 Hub
                  - Geeignet zur Dauertherapie, bei Niereninsuffizienz nur nach strenger Nutzen-Risiko-Abwägung, Anwendung in Schwangerschaft/Stillzeit nicht empfohlen, Wirkdauer ca. 24 h
                - **Vilanterol + Umeclidinium** (z.B. Anoro®):
                  - Dosis: 22/55 μg/Hub inhalativ 1-0-0, Tagesmaximaldosis 1 Hub
                  - Geeignet zur Dauertherapie, keine Dosisreduktion bei Niereninsuffizienz erforderlich, Anwendung in Schwangerschaft/Stillzeit nicht empfohlen, Wirkdauer ca. 24 h
                - **Formoterol + Aclidiniumbromid** (z.B. Duaklir® Genuair®, Brimica® Genuair®):
                  - Dosis: 12/340 μg/Hub inhalativ 1-0-1, Tagesmaximaldosis 2 Hub
                  - Geeignet zur Dauertherapie, keine Dosisreduktion bei Niereninsuffizienz erforderlich, Anwendung in Schwangerschaft/Stillzeit nicht empfohlen, Wirkdauer ca. 12 h
                - **Olodaterol + Tiotropium** (z.B. Spiolto® Respimat®):
                  - Dosis: 2,5/2,5 μg inhalativ 2-0-0, Tagesmaximaldosis 2 Hub
                  - Geeignet zur Dauertherapie, keine Dosisreduktion bei Niereninsuffizienz erforderlich, Anwendung in Schwangerschaft/Stillzeit nicht empfohlen, Wirkdauer ca. 24 h
                """)
        elif prev_treatment == "LABA + LAMA":
            st.warning("Empfehlung: Wirkstoff- und/oder Inhalatorwechsel erwägen.")
            with st.expander("Kombinationspräparate LABA + LAMA"):
                st.write("""
                **Indikation:**
                Ab Gruppe B (gemäß COPD-Einteilung in ABE-Gruppen) einsetzbar. Kombinationspräparate verschiedener Hersteller stehen zur Verfügung, die Dosierungsfrequenz beträgt 1× oder 2× täglich.

                **Gängige Kombinationen:**
                - **Indacaterol + Glycopyrronium** (z.B. Ultibro® Breezhaler®, Xoterna® Breezhaler®, Ulunar® Breezhaler®):
                  - Dosis: 85/43 μg/Hub inhalativ 1-0-0, Tagesmaximaldosis 1 Hub
                  - Geeignet zur Dauertherapie, bei Niereninsuffizienz nur nach strenger Nutzen-Risiko-Abwägung, Anwendung in Schwangerschaft/Stillzeit nicht empfohlen, Wirkdauer ca. 24 h
                - **Vilanterol + Umeclidinium** (z.B. Anoro®):
                  - Dosis: 22/55 μg/Hub inhalativ 1-0-0, Tagesmaximaldosis 1 Hub
                  - Geeignet zur Dauertherapie, keine Dosisreduktion bei Niereninsuffizienz erforderlich, Anwendung in Schwangerschaft/Stillzeit nicht empfohlen, Wirkdauer ca. 24 h
                - **Formoterol + Aclidiniumbromid** (z.B. Duaklir® Genuair®, Brimica® Genuair®):
                  - Dosis: 12/340 μg/Hub inhalativ 1-0-1, Tagesmaximaldosis 2 Hub
                  - Geeignet zur Dauertherapie, keine Dosisreduktion bei Niereninsuffizienz erforderlich, Anwendung in Schwangerschaft/Stillzeit nicht empfohlen, Wirkdauer ca. 12 h
                - **Olodaterol + Tiotropium** (z.B. Spiolto® Respimat®):
                  - Dosis: 2,5/2,5 μg inhalativ 2-0-0, Tagesmaximaldosis 2 Hub
                  - Geeignet zur Dauertherapie, keine Dosisreduktion bei Niereninsuffizienz erforderlich, Anwendung in Schwangerschaft/Stillzeit nicht empfohlen, Wirkdauer ca. 24 h
                """)

    if exacerbation_focus:
        if prev_treatment == "LABA" or prev_treatment == "LAMA":
            st.success("Empfehlung: Erweitern auf LAMA + LABA.")
        elif prev_treatment == "LAMA + LABA":
            if eosinophils >= 100:
                st.success("Empfehlung: Erweitern auf LAMA + LABA + ICS.")
                with st.expander("Dreifach-Kombinationstherapie für COPD Gruppe E"):
                    st.write("""
                    **Therapievorschlag: Beclometason + Formoterol + Glycopyrronium (z.B. Trimbow® Druckgasinhalation)**
                    - **Dosis:** 87/5/9 μg/Hub inhalativ
                    - **Dosierungsschema:** 2-0-2, Tagesmaximaldosis 2-0-2
                    - **Besondere Hinweise:** Bei Niereninsuffizienz nur nach strenger Nutzen-Risiko-Abwägung anwenden. Anwendung in Schwangerschaft/Stillzeit nicht empfohlen.
                    - **Wirkdauer:** ca. 12 Stunden

                    **Therapievorschlag: Fluticason + Umeclidinium + Vilanterol (z.B. Trelegy® Ellipta®)**
                    - **Dosis:** 92/55/22 μg/Hub inhalativ
                    - **Dosierungsschema:** 1-0-0, Tagesmaximaldosis 1-0-0
                    - **Besondere Hinweise:** Keine Dosisreduktion bei Niereninsuffizienz erforderlich. Anwendung in Schwangerschaft/Stillzeit nicht empfohlen.
                    - **Wirkdauer:** ca. 24 Stunden
                    """)
            else:
                st.info("Weitere Optionen zur Therapieeskalation prüfen.")
        elif prev_treatment == "LAMA + ICS":
            if eosinophils >= 300:
                st.success("Empfehlung: Umstellung auf LAMA + LABA + ICS.")
                with st.expander("Dreifach-Kombinationstherapie für COPD Gruppe E"):
                    st.write("""
                    **Therapievorschlag: Beclometason + Formoterol + Glycopyrronium (z.B. Trimbow® Druckgasinhalation)**
                    - **Dosis:** 87/5/9 μg/Hub inhalativ
                    - **Dosierungsschema:** 2-0-2, Tagesmaximaldosis 2-0-2
                    - **Besondere Hinweise:** Bei Niereninsuffizienz nur nach strenger Nutzen-Risiko-Abwägung anwenden. Anwendung in Schwangerschaft/Stillzeit nicht empfohlen.
                    - **Wirkdauer:** ca. 12 Stunden

                    **Therapievorschlag: Fluticason + Umeclidinium + Vilanterol (z.B. Trelegy® Ellipta®)**
                    - **Dosis:** 92/55/22 μg/Hub inhalativ
                    - **Dosierungsschema:** 1-0-0, Tagesmaximaldosis 1-0-0
                    - **Besondere Hinweise:** Keine Dosisreduktion bei Niereninsuffizienz erforderlich. Anwendung in Schwangerschaft/Stillzeit nicht empfohlen.
                    - **Wirkdauer:** ca. 24 Stunden
                    """)
            else:
                st.info("Bei guter Therapieeinstellung: Beibehalten möglich. Bei unzureichendem Ansprechen: Umstellung erwägen.")
                with st.expander("Kombinationspräparate LABA + ICS"):
                    st.write("""
                    **Hinweis gemäß NVL und GOLD 2023:**
                    Die Kombination aus LABA + ICS ist nicht mehr zur Ersttherapie empfohlen. Bei gut eingestellten Patient:innen kann die Therapie jedoch fortgesetzt werden.

                    **Eigenschaften:**
                    - Verschiedene Applikationssysteme wie Diskus-Inhalatoren und Dosieraerosole
                    - Vereinfacht die Compliance durch Aufnahme beider Wirkstoffe mittels Inhalation

                    **Gängige Kombinationen:**
                    - **Budesonid + Formoterol**:
                      - Als Pulverinhalator, z.B. Symbicort® Turbohaler®: 320/9 μg/Hub inhalativ 1-0-1, Tagesmaximaldosis als Dauertherapeutikum 2-0-2
                      - Als Pulverinhalator, z.B. DuoResp® Spiromax®: 160/4,5 oder 320/9 μg/Hub inhalativ 1-0-1, Tagesmaximaldosis als Dauertherapeutikum 2-0-2
                    - **Beclometason + Formoterol**:
                      - Als Dosieraerosol, z.B. Foster®: 100/6 μg/Hub inhalativ 2-0-2, Tagesmaximaldosis 800 μg Beclometason
                    - **Fluticason propionat + Salmeterol**:
                      - Als Dosieraerosol, z.B. Viani®: 250/25 oder 500/50 μg/Hub inhalativ 1-0-1, Tagesmaximaldosis 1.000 μg Fluticason
                      - Als Pulverinhalator, z.B. Viani® Diskus: 250/50 oder 500/50 μg/Hub inhalativ 1-0-1, Tagesmaximaldosis 1.000 μg Fluticason
                    - **Fluticasonfuroat + Vilanterol**:
                      - Als Pulverinhalator, z.B. Relvar® Ellipta®: 92/22 μg/Hub inhalativ 1-0-0, Tagesmaximaldosis 1-0-0
                    """)

    # Consideration for Roflumilast and Azithromycin
    if fev1 < 50 and chronic_bronchitis and hospitalization_last_year:
        st.error("Empfehlung: Roflumilast in Erwägung ziehen.")
        with st.expander("Roflumilast - Wichtige Informationen"):
            st.write("""
            **Wirkmechanismus:**
            Roflumilast hemmt das Enzym Phosphodiesterase-4, das eine Rolle bei der Aufrechterhaltung von chronischen Entzündungszuständen bei COPD spielt. Es reduziert die entzündliche Aktivität, besitzt jedoch keine bronchodilatatorische Wirkung.

            **Indikation:**
            - Letzte Eskalationsstufe bei unverändert häufigen Exazerbationen unter Triple-Therapie (LAMA + LABA + ICS), FEV1 <50% und bei vorherrschenden Symptomen der chronischen Bronchitis.
            - Laut Nationaler VersorgungsLeitlinie COPD (2021) kann Roflumilast in Ausnahmefällen auch nur in Kombination mit LAMA + LABA eingesetzt werden, wenn Kontraindikationen gegenüber ICS bestehen.

            **Vorsichtsmaßnahmen:**
            - Langsames Aufdosieren zur Vermeidung gastrointestinaler Nebenwirkungen.
            - Keine Anwendung bei Kachexie, Depression und Suizidalität aufgrund von häufigen gastrointestinalen Nebenwirkungen wie Inappetenz und Gewichtsabnahme, was im Rahmen einer COPD prognostisch ungünstig ist.
            - Psychopathologische Störwirkungen und Suizide in Zusammenhang mit der Einnahme bzw. dem Absetzen von Roflumilast sind beschrieben.

            **Dosierung:**
            - [Bitte fügen Sie die spezifische Dosierungsanweisung hier ein.]
            """)

    if exacerbation_focus:
        st.success("Empfehlung: Azithromycin in Erwägung ziehen, falls entsprechend indiziert.")
        with st.expander("Azithromycin in der COPD-Behandlung"):
            st.write("""
            **Wirkung und Studienergebnisse:**
            Laut einer Studie, die im [New England Journal of Medicine](https://www.nejm.org/doi/full/10.1056/NEJMoa1104623) veröffentlicht wurde, kann die tägliche Einnahme von Azithromycin über ein Jahr, zusätzlich zur üblichen Behandlung, die Häufigkeit von Exazerbationen verringern und die Lebensqualität verbessern. Allerdings wurde bei einem kleinen Prozentsatz der Teilnehmer eine Beeinträchtigung des Gehörs festgestellt.

            **Dauertherapie mit Antibiotika:**
            Neuere Studien zeigen, dass eine Langzeitantibiose mit Makroliden wie Azithromycin (250 mg/Tag oder 500 mg dreimal pro Woche) oder Erythromycin (zweimal 500 mg/Tag) bei COPD-Patienten mit häufigen Exazerbationen die Exazerbationsrate innerhalb von 12 Monaten reduzieren kann. Jedoch wurden unter Azithromycin eine Zunahme von Resistenzen gegenüber S. pneumoniae und eine meist reversible Beeinträchtigung des Gehörs beobachtet. Aufgrund der potenziellen Risiken wie Resistenzentwicklung und Beeinträchtigung des Gehörs sowie dem Fehlen von Langzeitergebnissen kann eine generelle Empfehlung für die Langzeitbehandlung mit Makroliden derzeit nicht ausgesprochen werden. Eine Ausnahme bilden COPD-Patienten mit rezidivierenden Exazerbationen (≥ 2 pro Jahr) und Nachweis von P. aeruginosa. Weitere Details finden sich in den [Leitlinien zur COPD](https://register.awmf.org/assets/guidelines/020-006l_S2k_COPD_chronisch-obstruktive-Lungenerkrankung_2018-01.pdf).

            **Kontraindikationen:**
            Eine Kontraindikation besteht bei relevanten Rhythmusstörungen bzw. schwerer kardialer Komorbidität.
            """)
        
    

    # Eosinophil-Level bestimmen
    eosinophil_level = "geringgradig" if eosinophils < 150 else "mittelgradig" if 150 <= eosinophils < 300 else "hochgradig"

    # Farbdefinition basierend auf dem Eosinophil-Level
    color = "red" if eosinophil_level == "hochgradig" else "yellow" if eosinophil_level == "mittelgradig" else "blue"

    # Eosinophil-basierte Empfehlungen mit farblichem Hintergrund
    if eosinophil_level == "hochgradig" or (eosinophil_level == "mittelgradig" and exacerbation_focus):
        st.markdown(f"<div style='color: white; background-color: {color}; padding: 10px; border-radius: 10px;'>Empfehlung: Inhalative Steroide angezeigt ({eosinophil_level}).</div>", unsafe_allow_html=True)
    elif eosinophil_level == "geringgradig":
        st.markdown(f"<div style='color: white; background-color: {color}; padding: 10px; border-radius: 10px;'>Empfehlung: Erwägung des Absetzens inhalativer Steroide bei geringgradiger eosinophiler Inflammation.</div>", unsafe_allow_html=True)

    
    
    st.info(
    "COPD geht häufig mit einer erhöhten Zahl eosinophiler Granulozyten einher. "
    "Die Eosinophilenzahl kann als klinische Entscheidungshilfe dienen, besonders bei der Wahl der Therapie. "
    "Werte über 100-300 Zellen/μl korrelieren mit einem höheren Risiko für Exazerbationen und sprechen gut auf Steroide an."
    )
    
    st.info("""
    **Wichtige Informationen:**
    - Von einer Azithromycin-Gabe profitieren v.a. Patientinnen, die nicht mehr rauchen. Allerdings sollte die Gefahr der Resistenzentwicklung bei längerfristiger Gabe in die Therapieentscheidung mit einbezogen werden.
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
    
    st.markdown("""
    ### S2k-Leitlinie zur Diagnostik und Therapie von Patienten mit COPD
    Die [S2k-Leitlinie zur Diagnostik und Therapie von Patienten mit chronisch obstruktiver Bronchitis und Lungenemphysem (COPD)](https://register.awmf.org/assets/guidelines/020-006l_S2k_COPD_chronisch-obstruktive-Lungenerkrankung_2018-01.pdf) bietet umfassende Informationen und Richtlinien für die Behandlung dieser Erkrankung.
    """)





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[14]:


import streamlit as st

def tvt():
    st.header("Risikostratifizierung und Prophylaxe von tiefer Beinvenenthrombose")
    st.markdown("Bezugnehmend auf die Studien: *Prevention Registry on Venous Thromboembolism Risk Assessment Model*, *Padua Prediction Score for Risk of VTE* und *Accuracy of clinical assessment of deep-vein thrombosis von P S Wells et al.*")
    st.subheader("PADUA: Ist eine Thromboseprophylaxe notwendig?")
    st.subheader("IMPROVE-RAM: Wie hoch ist das drei Monats Risiko für eine TVT? bei hospitalisierten Pat.")
    st.subheader("Wells-Score (TVT): Wahrscheinlichkeit für eine TVT u. weitere empfohlene Maßnahmen")

    
    # Initialisierung der Eingaben
    age = st.number_input("Alter", min_value=0, max_value=120, step=1)
    cancer = st.checkbox("Aktiver Krebs")
    vte = st.checkbox("Vorangegangene VTE")
    thrombophilia = st.checkbox("Bekannte Thrombophilie")
    paralysis = st.checkbox("Lähmung der unteren Gliedmaßen")
    immobilization = st.checkbox("Immobilisierung")
    icu_stay = st.checkbox("Aufenthalt in der Intensivstation oder Herzüberwachungsstation")

    # Spezifische Kriterien für weitere Scores
    bedridden = st.checkbox("Kürzlich bettlägerig >3 Tage oder größere Operation innerhalb von 12 Wochen")
    calf_swelling = st.checkbox("Wadenschwellung >3 cm verglichen mit dem anderen Bein")
    superficial_veins = st.checkbox("Vorhandensein von Kollateralvenen (nicht Krampfadern)")
    leg_swollen = st.checkbox("Gesamtes Bein geschwollen")
    tenderness = st.checkbox("Lokale Empfindlichkeit entlang des tiefen Venensystems")
    pitting_edema = st.checkbox("Grubenödem, beschränkt auf das symptomatische Bein")
    previous_dvt = st.checkbox("Früher dokumentierte DVT")
    alternative_diagnosis = st.checkbox("Alternative Diagnose zu DVT wahrscheinlich oder wahrscheinlicher")

    # Berechnung der Scores
    def calculate_scores():
        base_score = 0
        padua_score = 0
        wells_score = 0

        # Gemeinsame Faktoren
        base_score += 3 * vte + 2 * (thrombophilia + paralysis + cancer) + 1 * (immobilization + icu_stay) + (1 if age > 60 else 0)
        padua_score += 3 * (cancer + vte + immobilization + thrombophilia) + 2 * bedridden + 1 * (age >= 70 + paralysis + previous_dvt + leg_swollen + pitting_edema)
        wells_score += 1 * (cancer + bedridden + calf_swelling + superficial_veins + leg_swollen + tenderness + pitting_edema + paralysis + previous_dvt) - 2 * alternative_diagnosis

        return base_score, padua_score, wells_score

    # Interpretation des IMPROVE RAM Scores
    def interpret_improve_score(base_score):
        return "Geringes Risiko für venöse Thromboembolie (VTE)" if base_score <= 2 else "Risiko für VTE"

    # Interpretation des Padua Prediction Scores
    def interpret_padua_score(padua_score):
        if padua_score < 4:
            return "Niedriges Risiko für VTE. Thromboprophylaxe sollte fallweise in Betracht gezogen werden."
        else:
            return ("Hohes Risiko für VTE. Eine Thromboprophylaxe (z.B. Heparin/Enoxaparin) wird für nicht-schwangere Patienten ohne Kontraindikationen " 
                    "(große Blutungen, niedrige Thrombozytenzahlen, Kreatininclearance <30 mL/min) empfohlen, die älter als 18 Jahre sind.")

    # Interpretation des Wells’ Scores
    def interpret_wells_score(wells_score):
        if wells_score <= 0:
            return ("Niedriges Risiko (5% Wahrscheinlichkeit): Ein negativer hoch- oder moderat sensitiver D-Dimer-Test führt zu einer Wahrscheinlichkeit von <1%, keine weitere Bildgebung erforderlich. "
                    "Ein positiver D-Dimer-Test sollte zu einer Ultraschalluntersuchung führen.")
        elif 1 <= wells_score <= 2:
            return ("Moderates Risiko (17% Wahrscheinlichkeit): Es sollte ein hochsensitiver D-Dimer-Test durchgeführt werden (moderate Sensitivität ist nicht ausreichend). "
                    "Ein negativer hochsensitiver D-Dimer-Test reicht aus, um DVT bei einem Patienten mit moderatem Risiko auszuschließen. Ein positiver hochsensitiver D-Dimer-Test sollte zu einer Ultraschalluntersuchung führen.")
        else:
            return ("Hohes Risiko (17-53% Wahrscheinlichkeit): Alle Patienten, bei denen DVT wahrscheinlich ist, sollten einen Ultraschall erhalten. "
                    "D-Dimer-Tests sollten genutzt werden, um diese Patienten weiter zu stratifizieren. Bei negativem D-Dimer kann ein negativer Ultraschall ausreichen, um DVT auszuschließen, und eine Entlassung in Erwägung gezogen werden. "
                    "Ein positiver Ultraschall ist besorgniserregend, eine Behandlung mit Antikoagulanzien sollte stark in Betracht gezogen werden. Bei positivem D-Dimer und negativem Ultraschall sollte ein wiederholter Ultraschall innerhalb einer Woche zur erneuten Bewertung durchgeführt werden.")

    # Kombinierte Interpretation aller Scores
    def interpret_scores(base_score, padua_score, wells_score):
        risk_category = interpret_improve_score(base_score)
        padua_category = interpret_padua_score(padua_score)
        wells_category = interpret_wells_score(wells_score)
        return risk_category, padua_category, wells_category

    if st.button("Risiko und Prophylaxe bewerten"):
        base_score, padua_score, wells_score = calculate_scores()
        risk_category, padua_category, wells_category = interpret_scores(base_score, padua_score, wells_score)
    
        st.subheader(f"Padua Prediction Score beträgt: {padua_score}")
        if padua_score < 4:
            st.warning(padua_category)
        else:
            st.error(padua_category)
            
        st.subheader(f"IMPROVE RAM Score beträgt: {base_score}")
        if base_score <= 2:
            st.success(risk_category)
        else:
            st.error(risk_category)

        st.subheader(f"Wells' Score beträgt: {wells_score}")
        if wells_score <= 0:
            st.success(wells_category)
        elif 1 <= wells_score <= 2:
            st.warning(wells_category)
        else:
            st.error(wells_category)
    
    # Expander for study references
    with st.expander("Studienreferenzen und weitere Informationen"):
        st.markdown("""
        **Predictive and associative models to identify hospitalized medical patients at risk for VTE**

        Alex C Spyropoulos  1 , Frederick A Anderson Jr  2 , Gordon FitzGerald  2 , Herve Decousus  3 , Mario Pini  4 , Beng H Chong  5 , Rainer B Zotz  6 , Jean-François Bergmann  7 , Victor Tapson  8 , James B Froehlich  9 , Manuel Monreal  10 , Geno J Merli  11 , Ricardo Pavanello  12 , Alexander G G Turpie  13 , Mashio Nakamura  14 , Franco Piovella  15 , Ajay K Kakkar  16 , Frederick A Spencer  17 ; IMPROVE Investigators.  
        **PMID**: 21436241  
        **DOI**: 10.1378/chest.10-1944

        **A risk assessment model for the identification of hospitalized medical patients at risk for venous thromboembolism: the Padua Prediction Score**

        S Barbar  1 , F Noventa, V Rossetto, A Ferrari, B Brandolin, M Perlati, E De Bon, D Tormene, A Pagnan, P Prandoni.  
        **PMID**: 20738765  
        **DOI**: 10.1111/j.1538-7836.2010.04044.x

        **Accuracy of clinical assessment of deep-vein thrombosis**

        P S Wells  1 , J Hirsh, D R Anderson, A W Lensing, G Foster, C Kearon, J Weitz, R D'Ovidio, A Cogo, P Prandoni.  
        **PMID**: 7752753  
        **DOI**: 10.1016/s0140-6736(95)92535-x
        """, unsafe_allow_html=True)


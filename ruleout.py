#!/usr/bin/env python
# coding: utf-8

# In[14]:


import streamlit as st

def ruleout():
    from math import exp

    # Logistische Regressionsfunktion
    def calculate_acs_probability(E, A, R, V, S, H, T):
        exponent = -(1.713*E + 0.847*A + 0.607*R + 1.417*V + 2.058*S + 1.208*H + 0.0897*T - 4.766)
        probability = 1 / (1 + exp(exponent))
        return probability

    # Funktion zur Interpretation der Wahrscheinlichkeit
    def interpret_risk(probability):
        if probability < 0.02:
            return 'Sehr gering', 'ACS ausgeschlossen. Entlassung in Erwägung ziehen.'
        elif 0.02 <= probability < 0.05:
            return 'Gering', 'Erwägen Sie serielle Troponinmessungen im Notfallbereich, z. B. 3-Stunden-Troponin; Entlassung erwägen, wenn normal.'
        elif 0.05 <= probability < 0.95:
            return 'Mäßig', 'Serielle Troponinmessungen auf der Allgemeinstation und anschließend Belastungstests und/oder CT-Koronarangiographie in Betracht ziehen.'
        else:
            return 'Hoch', 'ACS bestätigt. An Kardiologie überweisen, ACS behandeln.'

    st.title('ACS-Wahrscheinlichkeitsrechner')

    # Hinweis zur Spezifität von hs-cTnT anzeigen
    st.info("Beachten Sie, dass hs-cTnT eine geringe Spezifität hat — Troponin kann durch eine Reihe von nicht-ACS-Ätiologien erhöht sein, einschließlich kardialer Ursachen wie Herzinsuffizienz und nicht-kardialer Ursachen wie Nierenversagen.")

    with st.form("acs_form", clear_on_submit=False):
        st.write("Bitte geben Sie die folgenden klinischen Zeichen und Symptome an:")

        E = st.selectbox('EKG-Ischämie', options=[('Nein', 0), ('Ja', 1)], format_func=lambda x: x[0])
        A = st.selectbox('Verschlechterung oder Crescendo-Angina', options=[('Nein', 0), ('Ja', 1)], format_func=lambda x: x[0])
        R = st.selectbox('Schmerzausstrahlung in den rechten Arm oder die Schulter', options=[('Nein', 0), ('Ja', 1)], format_func=lambda x: x[0])
        V = st.selectbox('Schmerz verbunden mit Erbrechen', options=[('Nein', 0), ('Ja', 1)], format_func=lambda x: x[0])
        S = st.selectbox('Beobachtetes Schwitzen', options=[('Nein', 0), ('Ja', 1)], format_func=lambda x: x[0])
        H = st.selectbox('Hypotonie', options=[('Nein', 0), ('Ja', 1)], format_func=lambda x: x[0])
        T = st.number_input('hs-cTnT-Konzentration bei Ankunft', min_value=0.0, step=0.01, format="%.2f")

        submit_button = st.form_submit_button("Wahrscheinlichkeit berechnen")

    if submit_button:
        probability = calculate_acs_probability(E[1], A[1], R[1], V[1], S[1], H[1], T)
        risk_level, interpretation = interpret_risk(probability)
        st.success(f'Die berechnete Wahrscheinlichkeit für ACS beträgt: {probability:.2%} ({risk_level} Risiko)')
        st.info(interpretation)

    st.write("## Fakten & Zahlen")
    st.write("### Interpretation basierend auf der ACS-Wahrscheinlichkeit:")
    st.write("""
    - **<0,02:** Sehr gering - ACS ausgeschlossen. Entlassung in Erwägung ziehen.
    - **≥0,02 und <0,05:** Gering - Erwägen Sie serielle Troponinmessungen; Entlassung erwägen, wenn normal.
    - **≥0,05 und <0,95:** Mäßig - Serielle Troponinmessungen und anschließend weitere Tests.
    - **≥0,95:** Hoch - ACS bestätigt. An Kardiologie überweisen, ACS behandeln.
    """)

    with st.expander("Schlussfolgerung"):
        st.markdown("""
            **Schlussfolgerungen:** T-MACS könnte bei 40% der Patienten ACS 'ausschließen' und gleichzeitig 5% der Patienten mit dem höchsten Risiko bei Ankunft mit einer einzelnen hs-cTnT-Messung 'bestätigen'. Als klinische Entscheidungshilfe könnte T-MACS daher dazu beitragen, Gesundheitsressourcen zu schonen.
            """)
    
    with st.expander("Informationen zu nicht-ACS-Ätiologien für erhöhtes Troponin"):
        st.write("""
        **Kardiale Ursachen:**
        - Kardiale Kontusion (Trauma)
        - Herzinsuffizienz, akut und chronisch
        - Tachy- oder Bradyarrhythmie, Herzblock
        - Herzoperation
        - Aortendissektion
        - Apikales Ballonierungs-Syndrom
        - Kardioversion
        - Aortenklappenerkrankung
        - Post-PCI
        - Endomyokardbiopsie
        - Hypertrophe Kardiomyopathie
        - Rhabdomyolyse mit Myozytennekrose
        - Myokarditis
        - Endokarditis
        - Perikarditis

        **Nicht-kardiale Ursachen:**
        - Lungenembolie (PE)
        - Schwere pulmonale Hypertonie
        - Nierenversagen
        - Schlaganfall, SAH
        - Amyloidose, andere infiltrative Krankheiten
        - Kardiotoxische Drogen
        - Kritische Krankheit
        - Sepsis
        - Umfangreiche Verbrennungen
        - Extremes Ausüben

        Quelle: Mahajan 2011.
        """)

    

    st.markdown("""
        Troponin-only Manchester Acute Coronary Syndromes (T-MACS) decision aid: single biomarker re-derivation and external validation in three cohorts 
        Richard Body1,2, [http://orcid.org/0000-0002-2064-4618](http://orcid.org/0000-0002-2064-4618)Edward Carlton3, Matthew Sperrin1, Philip S Lewis4, Gillian Burrows5, Simon Carley2,6, Garry McDowell1,6, Iain Buchan1, Kim Greaves7, Kevin Mackway-Jones1,2,6
        Korrespondenz an Dr. Richard Body, Notfallabteilung, Manchester Royal Infirmary, Oxford Road, Manchester M13 9WL, UK;
        [Zum Artikel](https://emj.bmj.com/content/34/6/349.long)
        """, unsafe_allow_html=True)


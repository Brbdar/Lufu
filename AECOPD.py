#!/usr/bin/env python
# coding: utf-8

# In[32]:


import streamlit as st

def AECOPD():
    def calculate_decaf(emrcd, eosinopenia, consolidation, acidemia, afib):
        score = 0
        score += emrcd
        score += eosinopenia
        score += consolidation
        score += acidemia
        score += afib
        return score

    def interpret_decaf(score):
        recommendations = {
            0: ("Geringes Risiko, Routinebehandlung, Sterblichkeit ~0%", "Routinemäßige Behandlung"),
            1: ("Sterblichkeit ~1,5%", "Routinemäßige Behandlung"),
            2: ("Mittleres Risiko, Einsatz des klinischen Urteils bezüglich der Disposition, Sterblichkeit ~5,4%", "Klinisches Urteil bezüglich der Disposition verwenden"),
            3: ("Hohes Risiko, Erwägung einer Eskalation der Versorgung vs. palliative Betreuung, Sterblichkeit ~15,3%", "Erwägung einer Eskalation der Versorgung oder palliativer Betreuung"),
            4: ("Sterblichkeit ~31%", "Hochintensive Betreuung empfohlen"),
            5: ("Sterblichkeit ~40,5%", "Hochintensive Betreuung empfohlen"),
            6: ("Sterblichkeit ~50%", "Hochintensive Betreuung empfohlen")
        }
        return recommendations.get(score, ("Unbekanntes Risiko", "Keine Empfehlung verfügbar"))

    st.title('Risikostratifizierung der AECOPD')
    st.write('DECAF Score Rechner für COPD-Patienten')
    st.write('Der DECAF-Score hilft Klinikern, das Management von COPD-Patienten durch Einschätzungen zur frühen Entlassung, intensivierter Betreuung oder Festlegung von Behandlungszielen zu optimieren.')

    with st.form("decaf_form"):
        emrcd = st.selectbox('Wählen Sie die eMRCD Kategorie:', [0, 1, 2], format_func=lambda x: {0:'Nicht zu atemlos, um das Haus zu verlassen eMRCD 1–4', 1:' Zu atemlos, um das Haus zu verlassen, aber selbstständig beim Waschen/Anziehen eMRCD 5a', 2:' Zu atemlos, um das Haus zu verlassen und sich zu waschen/anziehen eMRCD 5b'}.get(x))
        eosinopenia = st.radio('Eosinopenie (<0,05×10⁹/L):', [0, 1], format_func=lambda x: {0:'Nein', 1:'Ja'}.get(x))
        consolidation = st.radio('Konsolidierung im Thorax-Röntgenbild:', [0, 1], format_func=lambda x: {0:'Nein', 1:'Ja'}.get(x))
        acidemia = st.radio('Azidämie (pH <7,30):', [0, 1], format_func=lambda x: {0:'Nein', 1:'Ja'}.get(x))
        afib = st.radio('Vorhofflimmern:', [0, 1], format_func=lambda x: {0:'Nein', 1:'Ja'}.get(x))
        submitted = st.form_submit_button("DECAF Score berechnen")

        if submitted:
            score = calculate_decaf(emrcd, eosinopenia, consolidation, acidemia, afib)
            result_text, recommendation = interpret_decaf(score)
            st.subheader(f'DECAF Score: {score}')
            st.write(result_text)
            st.info(f'Empfehlung: {recommendation}')

    def calculate_bap_65(bun, mental_status, pulse, age):
        points = 0
        points += bun
        points += mental_status
        points += pulse
        
        if points == 0:
            if age < 65:
                bap_class = "I"
            else:
                bap_class = "II"
        elif points == 1:
            bap_class = "III"
        elif points == 2:
            bap_class = "IV"
        elif points >= 3:
            bap_class = "V"
        else:
            bap_class = "Unknown"
        
        return points, bap_class
    
    def interpret_bap_65(bap_class):
        interpretations = {
        "I": ("0,3%", "0,3%", "Routinemäßiges Management der COPD-Exazerbation"),
        "II": ("1,0%", "0,2%", "Routinemäßiges Management der COPD-Exazerbation"),
        "III": ("2,2%", "1,2%", "Frühzeitige nicht-invasive Beatmung und/oder Intensivpflege in Betracht ziehen"),
        "IV": ("6,4%", "5,5%", "Frühzeitige nicht-invasive Beatmung und/oder Intensivpflege in Betracht ziehen"),
        "V": ("14,1%", "12,4%", "Frühzeitige nicht-invasive Beatmung und/oder Intensivpflege in Betracht ziehen")
        }
        return interpretations.get(bap_class, ("Unbekannt", "Unbekannt", "Unbekannt"))

    # DECAF UI hier wie zuvor
    
    st.header('BAP-65 Score Rechner für COPD-Patienten')
    st.write('Der BAP-65 Score hilft Klinikern, das Risiko für Krankenhausmortalität und die Notwendigkeit mechanischer Beatmung innerhalb der nächsten 48h bei Patienten mit akuten Exazerbationen der COPD zu bewerten.')
    
    with st.form("bap_form"):
        bun = st.radio('BUN ≥25 mg/dL (8.9 mmol/L):', [0, 1], format_func=lambda x: {0:'Nein', 1:'Ja'}.get(x))
        mental_status = st.radio('Veränderte geistige Verfassung:', [0, 1], format_func=lambda x: {0:'Nein', 1:'Ja'}.get(x))
        pulse = st.radio('Puls ≥109 Schläge/min:', [0, 1], format_func=lambda x: {0:'Nein', 1:'Ja'}.get(x))
        age = st.number_input('Alter des Patienten:', min_value=40, max_value=120)
        submitted_bap = st.form_submit_button("BAP-65 Score berechnen")
        
        if submitted_bap:
            points, bap_class = calculate_bap_65(bun, mental_status, pulse, age)
            mortality, ventilation_need, recommendation = interpret_bap_65(bap_class)
            st.subheader(f'BAP-65 Klasse: {bap_class}')
            st.write(f'Mortalität: {mortality}')
            st.write(f'Notwendigkeit einer mechanischen Beatmung innerhalb von 48 Stunden: {ventilation_need}')
            st.info(f'Empfehlung: {recommendation}')
    
    st.markdown("""
    Mortality and Need for Mechanical Ventilation in Acute Exacerbations of Chronic Obstructive Pulmonary Disease
    Development and Validation of a Simple Risk Score

    **Authors:** Ying P. Tabak, PhD; Xiaowu Sun, PhD; Richard S. Johannes, MD, MS; Vikas Gupta, PharmD; Andrew F. Shorr, MD, MPH  
    **Published in:** Arch Intern Med, 2009, Volume 169, Issue 17, Pages 1595-1602  
    **DOI:** [10.1001/archinternmed.2009.270](https://doi.org/10.1001/archinternmed.2009.270)
    """)
    
    st.markdown("""
    The DECAF Score: Predicting Hospital Mortality in Exacerbations of Chronic Obstructive Pulmonary Disease

    **Authors:** John Steer, John Gibson, Stephen C Bourke  
    **PMID:** 22895999  
    **DOI:** [10.1136/thoraxjnl-2012-202103](https://doi.org/10.1136/thoraxjnl-2012-202103)
    """)

    
    
    


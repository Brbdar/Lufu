#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st

def Blutkultur():
    st.header("Blutkultur")
    
    # Shapiro-Regel Tool
    st.title('Shapiro-Regel Tool für Blutkulturindikation')
    
    with st.expander("Studienziel und Methodik"):
        st.write("""
        Das Ziel der Studie war, eine klinische Entscheidungsregel für die Entnahme von Blutkulturen bei Notaufnahme-Patienten mit Verdacht auf Infektion abzuleiten und zu validieren. Es handelte sich um eine prospektive, beobachtende Kohortenstudie mit konsekutiven erwachsenen Notaufnahme-Patienten, bei denen Blutkulturen entnommen wurden. Die Studie lief vom 1. Februar 2000 bis zum 1. Februar 2001. Die Patienten wurden zufällig den Derivations- (2/3) oder Validierungsgruppen (1/3) zugeordnet. Das Ergebnis war "echte Bakteriämie".
        """)

    with st.expander("Ergebnisse und Entscheidungsregel"):
        st.write("""
            Unter 3901 Patienten wurden 3730 (96%) eingeschlossen, mit 305 (8,2%) Episoden von echter Bakteriämie. Eine Entscheidungsregel wurde mit "Hauptkriterien" erstellt: Temperatur > 39,5 Grad Celsius, vorhandener vaskulärer Katheter oder klinischer Verdacht auf Endokarditis. "Nebenkriterien" waren: Temperatur 38,3-39,4 Grad Celsius, Alter > 65 Jahre, Schüttelfrost, Erbrechen, Hypotonie (systolischer Blutdruck < 90 mm Hg), Neutrophilenanteil > 80%, weiße Blutkörperchen > 18k, Bands > 5%, Thrombozyten < 150k und Kreatinin > 2,0. Eine Blutkultur ist nach der Regel indiziert, wenn mindestens ein Hauptkriterium oder zwei Nebenkriterien vorhanden sind. Andernfalls werden Patienten als "niedriges Risiko" eingestuft und Kulturen können ausgelassen werden.
        """)

    with st.expander("Sensitivität und Validierung"):
        st.write("""
            Nur 4 (0,6%) Patienten mit niedrigem Risiko in der Derivationsgruppe und 3 (0,9%) Patienten mit niedrigem Risiko in der Validierungsgruppe hatten positive Kulturen. Die Sensitivität betrug 98% (95% Konfidenzintervall [KI] 96-100%) (Derivation) und 97% (95% KI 94-100%) (Validierung). Wir haben eine vielversprechende klinische Entscheidungsregel zur Vorhersage von Bakteriämie bei Patienten mit Verdacht auf Infektion entwickelt und validiert.
        """)
        
    st.write("""
    ### Shapiro-Regel
    Zeigt an, ob ein Patient in der Notaufnahme für eine Blutkultur in Frage kommt.

    #### Anleitung
    Bestimmt, ob ein Arzt eine Blutkultur auf Grundlage von Symptomen und klinischen Befunden in Betracht ziehen sollte.

    #### Wann verwenden
    Verwenden Sie dieses Tool bei einem Patienten in der Notaufnahme mit Verdacht auf eine Infektion, um zu unterstützen bei der Entscheidung, ob eine Blutkultur entnommen werden sollte.
    Bei Verdacht auf Sepsis empfiehlt die Gesellschaft für Intensivmedizin (SCCM) die Verwendung der SIRS-Kriterien, NEWS oder MEWS als Werkzeuge zum Screening auf Sepsis.
    """)



    # Major Criteria
    st.header('Major Criteria')
    suspect_endocarditis = st.radio('Verdacht auf Endokarditis', ('Nein', 'Ja'))
    temp_39_4 = st.radio('Temperatur ≥39.4°C (103.0°F)', ('Nein', 'Ja'))
    indwelling_catheter = st.radio('Vorhandensein eines intravaskulären Katheters', ('Nein', 'Ja'))

    # Minor Criteria
    st.header('Minor Criteria')
    age = st.slider('Alter in Jahren', 0, 120, 25)
    temp_38_3_39_3 = st.radio('Temperatur 38.3–39.3°C (101.0–102.9°F)', ('Nein', 'Ja'))
    chills = st.radio('Schüttelfrost', ('Nein', 'Ja'))
    vomiting = st.radio('Erbrechen', ('Nein', 'Ja'))
    hypotension = st.radio('Hypotonie (SBP <90 mm Hg)', ('Nein', 'Ja'))
    white_blood_cell_count = st.radio('Leukozyten >18,000 Zellen/mm3', ('Nein', 'Ja'))
    bands_over_5 = st.radio('Bands >5%', ('Nein', 'Ja'))
    platelets_under_150 = st.radio('Thrombozyten <150,000 Zellen/mm3', ('Nein', 'Ja'))
    creatinine_over_2 = st.radio('Kreatinin >2.0 mg/dL', ('Nein', 'Ja'))

    # Berechnung der Punkte
    points = 0
    # Major Criteria
    points += 3 if suspect_endocarditis == 'Ja' else 0
    points += 3 if temp_39_4 == 'Ja' else 0
    points += 2 if indwelling_catheter == 'Ja' else 0

    # Minor Criteria
    points += 1 if age > 65 else 0
    points += 1 if temp_38_3_39_3 == 'Ja' else 0
    points += 1 if chills == 'Ja' else 0
    points += 1 if vomiting == 'Ja' else 0
    points += 1 if hypotension == 'Ja' else 0
    points += 1 if white_blood_cell_count == 'Ja' else 0
    points += 1 if bands_over_5 == 'Ja' else 0
    points += 1 if platelets_under_150 == 'Ja' else 0
    points += 1 if creatinine_over_2 == 'Ja' else 0

    # Anzeige des Ergebnisses
    st.header('Ergebnis')
    if points >= 3:
        st.success('Eine Blutkultur ist nach der Shapiro-Regel angezeigt.')
    else:
        st.error('Eine Blutkultur ist nach der Shapiro-Regel nicht angezeigt.')
        
    st.markdown("""
    **Wer benötigt eine Blutkultur? Eine prospektiv abgeleitete und validierte Vorhersageregel**

    *Nathan I Shapiro  1 , Richard E Wolfe, Sharon B Wright, Richard Moore, David W Bates*

    [Pubmed-Quelle](https://pubmed.ncbi.nlm.nih.gov/18486413/)
    """)

        
        


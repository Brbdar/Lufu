#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st

def embo():

    import streamlit as st

    # App-Titel
    st.title("Rechner für den überarbeiteten Genfer Score")

    # Altersabfrage einmal zu Beginn
    age = st.number_input("Geben Sie Ihr Alter ein:", min_value=18, max_value=120, step=1)
    
    # Eingaben sammeln
    alter_65_oder_älter = age >= 65
    frühere_pe_dvt = st.checkbox("Frühere DVT/PE")
    kürzliche_trauma_chirurgie = st.checkbox("Kürzliche Operation oder Fraktur (< 4 Wochen)")
    aktive_krebserkrankung = st.checkbox("Aktive Malignität")
    schmerzen_im_unteren_bein = st.checkbox("Schmerzen im unteren Bein")
    hämoptysen = st.checkbox("Hämoptysen")
    pulse_options = ["< 75 bpm", "75-94 bpm", ">= 95 bpm"]
    puls = st.radio("Pulsfrequenz", options=pulse_options)
    schmerzen_oder_ödem = st.checkbox("Schmerzen bei tiefer Venenpalpation des Beins oder einseitiges Ödem")

    # Score berechnen
    score = 0
    if alter_65_oder_älter:
        score += 1
    if frühere_pe_dvt:
        score += 3
    if kürzliche_trauma_chirurgie:
        score += 2
    if aktive_krebserkrankung:
        score += 2
    if schmerzen_im_unteren_bein:
        score += 3
    if hämoptysen:
        score += 2
    if puls == "75-94 bpm":
        score += 3
    elif puls == ">= 95 bpm":
        score += 5
    if schmerzen_oder_ödem:
        score += 4

    # Ergebnis und Managementoptionen anzeigen
    st.write(f"Ihr überarbeiteter Genfer Score beträgt: {score}")

    if score <= 3:
        st.write("Risiko: Niedrig (Vortestwahrscheinlichkeit ~8%)")
        st.write("Eine D-Dimer-Testung kann in Betracht gezogen werden. Bei negativem Ergebnis kann der Ausschluss weiterer Arbeiten erwogen werden.")
    elif score <= 10:
        st.write("Risiko: Mittel")
        st.write("Bei positivem D-Dimer-Test sollten Sie eine CT und eine Ultraschalluntersuchung in Erwägung ziehen.")
        st.write("Wenn die CT nicht schlüssig ist, sollten Sie einen V/Q-Scan oder eine Angiographie in Betracht ziehen.")
    else:
        st.write("Risiko: Hoch (>60% Vortestwahrscheinlichkeit)")
        st.write("Eine sofortige CT und Ultraschalluntersuchung sollte in Betracht gezogen werden.")
        st.write("Wenn die Bildgebung negativ ist, sollte eine Angiographie in Betracht gezogen werden.")
   
    st.title("PERC-Regel für den Ausschluss einer Lungenembolie")

    # PERC-Regel für Pulmonary Embolism
    st.subheader("PERC-Regel zur Einschätzung der Notwendigkeit weiterer Tests für eine Lungenembolie")
    alter_50_oder_älter = age >= 50
    herzfrequenz_100_oder_mehr = st.checkbox("Herzfrequenz ≥ 100 bpm")
    sauerstoffsättigung_unter_95 = st.checkbox("Sauerstoffsättigung bei Raumluft < 95%")
    einseitige_beinschwellung = st.checkbox("Einseitige Beinschwellung")
    hormonnutzung = st.checkbox("Nutzung von Hormonen (orale Kontrazeptiva, Hormonersatztherapie oder östrogene Hormone bei männlichen oder weiblichen Patienten)")

    # Auswertung der PERC-Regel
    perc_criteria = [alter_50_oder_älter, herzfrequenz_100_oder_mehr, sauerstoffsättigung_unter_95, einseitige_beinschwellung, hämoptysen, kürzliche_trauma_chirurgie, frühere_pe_dvt, hormonnutzung]
    if any(perc_criteria):
        st.error("Mindestens eines der PERC-Kriterien ist positiv. Die PERC-Regel ist nicht erfüllt und kann nicht verwendet werden, um PE bei diesem Patienten auszuschließen.")
    else:
        st.success("Keines der PERC-Kriterien ist positiv. PE kann unter Verwendung der PERC-Regel ausgeschlossen werden, wenn klinisch angezeigt.")

    # Hinweis zur Anwendung der PERC-Regel
    st.info("Die PERC-Regel sollte nur bei Patienten angewendet werden, bei denen die klinische Wahrscheinlichkeit einer Lungenembolie als niedrig eingeschätzt wird. Sie dient dazu, die Notwendigkeit weiterer Tests zu minimieren.")

    st.title("Altersadjustierter D-Dimer-Rechner - nur bei Pat. über 50 anzuwenden")

    # Alter und Assay-Typ abfragen
    assay_type = st.radio("Wählen Sie den D-Dimer-Assay Typ:", ("FEU (Fibrinogen Equivalent Units)", "DDU (D-Dimer Units)"))

    # Einheit für die Eingabe und Anzeige wählen
    unit_choice = st.radio("Wählen Sie die Einheit für die Anzeige der D-Dimer-Werte:", ("µg/L", "µg/mL"))

    # Berechnung des altersadjustierten D-Dimer-Grenzwerts
    if assay_type == "FEU (Fibrinogen Equivalent Units)":
        cutoff = age * 10
    else:
        cutoff = age * 5

    # Umrechnung des Grenzwerts, falls notwendig
    if unit_choice == "µg/mL":
        display_cutoff = cutoff / 1000  # Umrechnung von µg/L zu µg/mL
        display_unit = "µg/mL"
    else:
        display_cutoff = cutoff  # Keine Umrechnung notwendig, da bereits in µg/L
        display_unit = "µg/L"

    st.write(f"Der altersadjustierte D-Dimer-Grenzwert beträgt: {display_cutoff} {display_unit}")

    # D-Dimer-Wert des Benutzers abfragen und umrechnen, falls notwendig
    user_ddimer_input = st.number_input(f"Geben Sie Ihren D-Dimer-Wert ein (in {display_unit}):", min_value=0.0, format="%.3f")
    if unit_choice == "µg/mL":
        user_ddimer = user_ddimer_input * 1000  # Umrechnung von µg/mL zu µg/L für die Berechnung
    else:
        user_ddimer = user_ddimer_input  # Keine Umrechnung notwendig

    # Vergleich des Benutzerwerts mit dem Grenzwert und Empfehlungen
    if user_ddimer > 0:
        if user_ddimer < cutoff:
            st.success(f"Ihr D-Dimer-Wert von {user_ddimer_input} {display_unit} liegt unter dem Grenzwert von {display_cutoff} {display_unit}.")
            st.write("### Interpretation und Empfehlung:")
            st.write("Ihr D-Dimer-Wert liegt **unter dem altersadjustierten Grenzwert**. Eine venöse Thromboembolie (VTE) ist daher weniger wahrscheinlich.")
            st.write("Empfehlung: Erwägen Sie alternative Diagnosen.")
        else:
            st.error(f"Ihr D-Dimer-Wert von {user_ddimer_input} {display_unit} liegt über dem Grenzwert von {display_cutoff} {display_unit}.")
            st.write("### Interpretation und Empfehlung:")
            st.write("Ihr D-Dimer-Wert liegt **über dem altersadjustierten Grenzwert**. Eine venöse Thromboembolie (VTE) ist daher wahrscheinlicher.")
            st.write("Empfehlung: Erwägen Sie eine Bestätigungsdiagnostik mittels CT-Angiographie (CTA) oder Ventilations-Perfusions-Szintigraphie (V/Q-Scan).")

    st.markdown("""
    **Hinweis:** Diese Berechnung sollte nur bei Patienten angewendet werden, die 50 Jahre oder älter sind. Überprüfen Sie Ihre Labordaten sorgfältig auf die Maßeinheit (z. B. µg/L oder µg/mL) und den Assay-Typ (FEU vs DDU).
    """)

    with st.expander("2. Physiologie der D-Dimere"):
        st.write("""
        **Physiologie der Gerinnung und Fibrinolyse:**

        - Die Endstufe der sekundären Gerinnung ist die Bildung von Fibrin-Polymeren.
        - Die D-Domänen des Fibrin-Moleküls werden durch den aktivierten Faktor XIII quervernetzt.
        - Ein regulatorischer Gegenmechanismus ist die Spaltung der Fibrinpolymere durch die Peptidase Plasmin, wobei D-Dimere entstehen.

        **Klinische Bedeutung der D-Dimere:**

        D-Dimere zeigen unspezifisch eine Gerinnungsaktivierung an und sind nachweisbar bei:

        - Phlebothrombose
        - Lungenembolie
        - Disseminierte intravasale Koagulation (DIC)
        - Herzinfarkt
        - Sepsis
        - Nach chirurgischen Eingriffen
        - Leberzirrhose (verzögerter Abbau)
        - Hämolytisch-urämischem Syndrom
        - Fortgeschrittenem Alter
        - Schwangerschaft
        """)

    with st.expander("3. Anwendung und Interpretation von D-Dimer Tests"):
        st.write("""
        D-Dimer Tests werden häufig eingesetzt, um die Wahrscheinlichkeit von Thrombosen und Lungenembolien einzuschätzen, insbesondere wenn klinisch ein niedriges bis mittleres Risiko besteht. Ein negatives Testergebnis kann helfen, diese Bedingungen auszuschließen. Allerdings sollten positive Ergebnisse immer im Kontext anderer klinischer Befunde interpretiert werden, da D-Dimere auch aus anderen Gründen erhöht sein können.
        """)
        

    st.markdown("""
    ## Referenzen

    Die folgenden Quellen wurden für die medizinischen Informationen und Richtlinien in dieser App verwendet:

    1. **PERC Rule for Pulmonary Embolism**
       - *Clinical criteria to prevent unnecessary diagnostic testing in emergency department patients with suspected pulmonary embolism*  
       Autoren: J A Kline, A M Mitchell, C Kabrhel, P B Richman, D M Courtney  
       [Link zur Studie](https://pubmed.ncbi.nlm.nih.gov/15304025/)

    2. **Revised Geneva Score**
       - *Prediction of pulmonary embolism in the emergency department: the revised Geneva score*  
       Autoren: Grégoire Le Gal, Marc Righini, Pierre-Marie Roy, Olivier Sanchez, Drahomir Aujesky, Henri Bounameaux, Arnaud Perrier  
       [Link zur Studie](https://pubmed.ncbi.nlm.nih.gov/16461960/)

    3. **Age Adjusted D-dimer Cutoff Values**
       - *Diagnostic accuracy of conventional or age adjusted D-dimer cut-off values in older patients with suspected venous thromboembolism: systematic review and meta-analysis*  
       Quelle: BMJ 2013; 346 doi: [https://doi.org/10.1136/bmj.f2492](https://www.bmj.com/content/346/bmj.f2492.full)  
       [Link zum Artikel](https://www.bmj.com/content/346/bmj.f2492.full)

    """)


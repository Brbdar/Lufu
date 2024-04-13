#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

def ane1():
    st.header("Anämiediagnostik bei mikrozytärer Anämie")

    st.title('Bewertung der mikrozytären Anämie')


    st.header('Schritt 1: Überprüfung des Serum-Ferritinwertes')
    ferritin = st.number_input('Geben Sie den Serum-Ferritinwert ein:', min_value=0.0, format='%f')

    normal_stfr_upper = 30.0  # This value should be adjusted based on medical guidelines

    if ferritin is not None:
        if ferritin < 30:
            st.warning('Ferritinwert niedrig: Indikator für Eisenmangel. Eisenmangelanämie in Betracht ziehen.')
            transferrin_saturation = st.number_input('Geben Sie den Wert der Transferrinsättigung ein:', min_value=0.0, format='%f')
            if transferrin_saturation is not None:
                if transferrin_saturation < 20:
                    st.error('Transferrinsättigung erniedrigt: Bestätigt Eisenmangel.')
                    sTfR = st.number_input('Geben Sie den Wert des löslichen Transferrinrezeptors ein:', min_value=0.0, format='%f')
                    if sTfR:
                        if sTfR > normal_stfr_upper:
                            st.success('sTfR erhöht: Bestätigung der eisendefizitären Erythropoese. Eisenmangel trotz niedrigem Ferritin.')
                        else:
                            st.info('sTfR normal: Weitere Untersuchungen erforderlich.')
                elif 20 <= transferrin_saturation <= 45:
                    st.success('Transferrinsättigung im normalen Bereich, aber Ferritin niedrig: Überprüfung erforderlich.')
                else:
                    st.info('Transferrinsättigung erhöht: Unüblich bei Eisenmangel.')
        elif 30 <= ferritin <= 100:
            st.success('Ferritinwert im normalen Bereich (30–100 ng/mL).')
            sTfR = st.number_input('Überprüfung des sTfR-Werts:', min_value=0.0, format='%f')
            if sTfR:
                if sTfR > normal_stfr_upper:
                    st.warning('sTfR erhöht: Möglicher verdeckter Eisenmangel trotz normalem Ferritin. Weitere Untersuchungen empfohlen.')
                else:
                    st.success('sTfR im normalen Bereich.')
        else:
            st.warning('Ferritinwert erhöht: Kann bei chronischen Entzündungen, ACD, Thalassämie oder Myelodysplastischem Syndrom vorkommen.')
            sTfR = st.number_input('Überprüfung des sTfR-Werts bei erhöhtem Ferritin:', min_value=0.0, format='%f')
            if sTfR:
                if sTfR > normal_stfr_upper:
                    st.warning('sTfR erhöht: Indikator für Eisenmangel trotz erhöhtem Ferritin. Fachkonsultation empfohlen.')
                else:
                    st.info('sTfR normal: Kein verdeckter Eisenmangel.')
    else:
        st.error('Ferritinwert nicht verfügbar. Bitte Ferritin messen lassen.')

    st.header('Schritt 2: Ist die Mikrozytose neu?')
    microcytosis_new = st.radio('Ist die Mikrozytose neu?', ('Ja', 'Nein'))

    if microcytosis_new == 'Ja':
        st.write('Anämie bei chronischen Krankheiten in Betracht ziehen.')
    elif microcytosis_new == 'Nein':
        st.write('Thalassämie in Betracht ziehen. Heterozygote β-Thalassaemia minor (HbA2 erhöht; RDW normal) α-Thalassaemia minor (RDW normal; molekulargenetischer Nachweis)weitere seltene Hämoglobinopathien (z. B. HbSC, HbCC, HbS-β-Thalassämie, thalassämische Hämoglobinopathie)')

    # Optionale Abfrage für Retikulozyten-Hämoglobin
    reticulocyte_hb = st.number_input("Geben Sie das Retikulozyten-Hämoglobin ein (pg), falls verfügbar:", min_value=0.0, format='%f')

    if reticulocyte_hb:
        if reticulocyte_hb < 29:
            st.warning('Niedriges Retikulozyten-Hämoglobin: Aktuelle Eisenversorgung der Erythropoese ist unzureichend. Dies könnte ein weiterer Hinweis auf eine eisendefizitäre Erythropoese sein.')
        else:
            st.success('Retikulozyten-Hämoglobin ist ≥29 pg, was auf eine adäquate aktuelle Eisenversorgung hinweist.')
    else:
        st.info('Retikulozyten-Hämoglobin wurde nicht angegeben. Ohne diesen Wert ist eine vollständige Beurteilung der Eisenversorgung der Erythropoese nicht möglich.')

    # Zusammenfassung der Ergebnisse basierend auf allen verfügbaren Werten
    if ferritin < 30 and transferrin_saturation < 20 and sTfR > normal_stfr_upper:
        diagnosis_message = "Diagnose: Verdacht auf eisendefizitäre Erythropoese."
        if reticulocyte_hb and reticulocyte_hb < 29:
            diagnosis_message += " Niedriges Retikulozyten-Hämoglobin bestätigt die Diagnose weiter."
        st.error(diagnosis_message)
    else:
        if not reticulocyte_hb:
            st.warning('Für eine genaue Diagnose fehlen vollständige Daten. Bitte geben Sie alle relevanten Werte an.')

    # Normwerte als Referenz
    normal_values = {
        "MCH": (27, 34),  # MCH-Normbereich in pg
        "MCV": (83, 95),  # MCV-Normbereich in fL
        "MCHC": (32, 36),  # MCHC-Normbereich in g/dL
        "CRP": 5,  # CRP-Obergrenze in mg/L
        "Ferritin": 30,  # Ferritin-Untergrenze in ng/mL
        "Reticulocyte_Hb": 29,  # Retikulozyten Hb in pg
        "sTfR": 1.76  # Oberer Normwert für sTfR in mg/L
    }

    # Geschlecht und Alter des Benutzers abfragen
    gender = st.selectbox('Geschlecht auswählen:', ['Frau', 'Mann'])
    age = st.number_input('Alter eingeben:', min_value=0, max_value=120)

    # Geschlechts- und altersspezifische Hämoglobin-Normwerte festlegen
    normal_hb = (12, 16) if gender == 'Frau' else (14, 18)

    # Zusätzliche Werte vom Benutzer abfragen
    hb = st.number_input("Geben Sie den Hämoglobinwert (Hb) ein (g/dL):", min_value=0.0, format='%f')
    mcv = st.number_input("Geben Sie das mittlere korpuskuläre Volumen (MCV) ein (fL):", min_value=0.0, format='%f')
    mch = st.number_input("Geben Sie das mittlere korpuskuläre Hämoglobin (MCH) ein (pg):", min_value=0.0, format='%f')
    mchc = st.number_input("Geben Sie die mittlere korpuskuläre Hämoglobinkonzentration (MCHC) ein (g/dL):", min_value=0.0, format='%f')
    crp = st.number_input("Geben Sie den CRP-Wert ein (mg/L), falls verfügbar:", min_value=0.0, format='%f')

    # Annahme: 'ferritin', 'reticulocyte_hb', und 'sTfR' sind bereits definiert

    # Klassifikation des Eisenmangels
    if ferritin < normal_values["Ferritin"] and hb >= normal_hb[0] and mcv >= normal_values["MCV"][0] and mch >= normal_values["MCH"][0]:
        st.success("Latenter Eisenmangel: Speichereisen vermindert, aber noch ohne funktionelle Auswirkungen.")
    elif ferritin < normal_values["Ferritin"] and (hb < normal_hb[0] or mcv < normal_values["MCV"][0] or reticulocyte_hb < normal_values["Reticulocyte_Hb"]) and sTfR > normal_values["sTfR"]:
        st.error("Klinisch manifester Eisenmangel mit vermindertem Gesamtkörpereisen: Keine ausreichenden Eisenspeicher für eine normale Erythropoese.")
    elif ferritin >= normal_values["Ferritin"] and (hb < normal_hb[0] or mcv < normal_values["MCV"][0] or reticulocyte_hb < normal_values["Reticulocyte_Hb"]) and sTfR <= normal_values["sTfR"] and crp > normal_values["CRP"]:
        st.error("Klinisch manifester Eisenmangel mit normalem oder erhöhtem Gesamtkörpereisen: Gefüllte Eisenspeicher, die wegen eines gestörten Recycling aus dem RHS für die Erythropoese nicht verfügbar sind.")
    else:
        st.info("Weitere Diagnostik erforderlich, um den Eisenstatus präzise zu bestimmen.")

    # Hier müssten die "normwert_*" Variablen durch die tatsächlichen Normwerte ersetzt werden, die von den jeweiligen Laborrichtlinien abhängen.

    # Zusätzliche Informationen und Handlungsempfehlungen
    st.info('Bei einer Verlaufskontrolle des Blutbildes nach begonnener oraler Substitutionsbehandlung, die eine Retikulozytenkrise nach einer Woche und einen Hb-Anstieg zeigt, ist die Diagnose eines alimentären Eisenmangels belegt. Andernfalls muss eine weitergehende Diagnostik erfolgen.')

    st.title('Diagnostik nicht alimentärer Ursachen eines Eisenmangels')

    with st.expander("Anamnese"):
        st.write("""
        - **Blutungsereignisse**: Achten Sie auf Blutiger Urin, Teerstuhl, Zahnfleischbluten, Nasenbluten.
        - **Medikamenteneinnahme**: Verwendung von NSAR, Antikoagulanzien.
        - **Menstruationszyklus und Blutungen**: Bei Frauen, Überprüfung auf ungewöhnliche Blutungen.
        - **Ernährung**: Besondere Ernährungsweisen, die zu Mängeln führen können.
        - **Symptome von Malabsorption**: Diarrhö, Gewichtsverlust, trophische Störungen an den Fingernägeln.
        - **Frühere Laborbefunde**: Vergleich mit früheren Blutbildern und anderen relevanten Tests.
        """)

    with st.expander("Körperliche Untersuchung"):
        st.write("""
        - **Allgemeine Inspektion**: Suchen Sie nach Anzeichen weiterer Mangelzustände.
        - **Digital-rektale Untersuchung**: Teil der Standarduntersuchung, besonders wenn Verdacht auf interne Blutungsquellen besteht.
        """)

    with st.expander("Basisdiagnostik"):
        st.write("""
        - **Urin-Stix**: Schnelltest zur Überprüfung von Blut oder anderen Anomalien im Urin.
        - **Stuhltest auf okkultes Blut**: Überprüfung auf verborgene Blutungen im Gastrointestinaltrakt.
        - **Abdomensonografie**: Bildgebung zur Visualisierung von Strukturen im Bauchraum.
        """)

    with st.expander("Ergänzende Laborwerte"):
        st.write("""
        - **Hämolyseparameter**: Haptoglobin, Laktatdehydrogenase (LDH) zur Beurteilung einer möglichen Hämolyse.
        """)

    with st.expander("Weiterführende Diagnostik"):
        st.write("""
        - **Gastrointestinale Blutungsquellen**: Koloskopie, Ösophagogastroduodenoskopie (ÖGD), weitergehende Diagnostik je nach Verdacht.
        - **Urologische Untersuchung**: Zystoskopie zur Inspektion der Blase bei Verdacht auf Blutungen.
        - **Gynäkologische Untersuchung**: Vaginale Sonografie, besonders bei Verdacht auf Zustände wie Uterus myomatosus.
        """)

    st.write("Bitte alle relevanten Bereiche überprüfen und notwendige Untersuchungen durchführen.")


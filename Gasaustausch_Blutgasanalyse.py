#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

def Gasaustausch_Blutgasanalyse():
    st.header("Gasaustausch - Blutgasanalyse")
    
    st.write("Die Konstellation von pH, paCO2 und BE Standardbirkarbonat erlaubt Rückschlüsse auf die verursachende Störung des Säure-Base-Haushaltes.")
    
    with st.expander("Häufige Ursachen für Ventilationsinsuffizienz (Globalinsuffizienz)"):
        st.write("""
        - Atempumpversagen.
        - Funktionelle Atemdepression (metabolische Alkalose, Sedativa).
        - Zerebrale Schädigungen (Beispiel: Ischämie, Blutung, Raumforderung, Myelitis, Enzephalitis, Atemregulationsstörungen).
        - Neuromuskuläre Erkrankungen (z.B. Muskeldystrophie, spinale Muskelatrophien, Polymyositis, Myasthenia gravis, Guillain-Barre).
        - Atemwegsstenose (obstruktives Schlafapnoesyndrom, Trachealstenose).
        """)

    with st.expander("Wichtige Ursachen der alveolären Hyperventilation:"):
        st.write("""
        - Pulmonale Stimulation (Hypoxie, vermehrte Atemarbeit).
        - Zentrale Stimulation (Schmerz, Angst, Erregung, Fieber, arterielle Hypotension, zerebrale Läsion [Ischämie, Metastase], metabolische Azidose). 
        - Andere Stimuli (Schwangerschaft).
        """)
    
    # Eingabefelder für die Messwerte
    geschlecht = st.radio("Geschlecht:", ('Männlich', 'Weiblich'), key='gender_select2')
    alter = st.number_input("Alter (Jahre):", min_value=0, max_value=120, step=1, format="%d")
    pH = st.number_input("pH-Wert:", value=7.40, format="%.2f")
    PaO2 = st.number_input("PaO2 in mmHg:", value=95.0, format="%.1f")
    PaCO2 = st.number_input("PaCO2 in mmHg:", value=40.0, format="%.1f")
    HCO3 = st.number_input("HCO3 in mEq/L:", value=24.0, format="%.1f")
    BE = st.number_input("Base Excess (BE) in mEq/L:", value=0.0, format="%.1f")
    Na = st.number_input("Na in mEq/L:", value=140.0, format="%.1f")
    K = st.number_input("K in mEq/L:", value=4.0, format="%.1f")
    Cl = st.number_input("Cl in mEq/L:", value=100.0, format="%.1f")
    Ca = st.number_input("Ca in mmol/L:", value=2.4, format="%.2f")
    
    # Berechnung des korrigierten PaO2
    PaO2_korr = PaO2 - 1.6 * (40 - PaCO2)
    PaO2_korr_rundung = round(PaO2_korr, 1)  # Optional: Runden des Ergebnisses auf eine Dezimalstelle
    summe_PaCO2_PaO2 = PaCO2 + PaO2
    
    if st.button("Analyse durchführen"):
        results = []
    
        # Hinzufügen der korrigierten PaO2 Information
        results.append(f"**Korrigiertes PaO2: {PaO2_korr_rundung} mmHg**")
        
        # Alveoläre Hypoventilation und AHS
        if PaCO2 > 45:
            results.append("Hinweis auf alveoläre Hypoventilation. Bei Vorliegen von Adipositas könnte dies auf ein Adipositas-Hypoventilations-Syndrom (AHS) hinweisen.")

        # Schweregradbeurteilung
        PaO2_Abweichung = 40 - PaO2
        PaCO2_Abweichung = PaCO2 - 45

        if PaO2_Abweichung > 10 or PaCO2_Abweichung > 10:
            schweregrad = "schwer"
        elif 6 <= PaO2_Abweichung <= 10 or 6 <= PaCO2_Abweichung <= 10:
            schweregrad = "mittel"
        elif 5 <= PaO2_Abweichung < 6 or 5 <= PaCO2_Abweichung < 6:
            schweregrad = "leicht"
        else:
            schweregrad = "kein"

        if schweregrad != "kein":
            results.append(f"Schweregrad der respiratorischen Insuffizienz: {schweregrad}.")
        


        # Kritische Werte, die eine sofortige ärztliche Abklärung erfordern
        if pH < 7.25 and BE > 30:
            results.append("⚠️ Kritischer Zustand: pH < 7,25 und BE > 30 mmol/l. Sofortige ärztliche Abklärung erforderlich.")
        if PaCO2 > 55 and PaO2 < 50:
            results.append("⚠️ Neu aufgetretener kritischer Zustand: PaCO2 > 55mmHg und PaO2 < 50mmHg. Sofortige ärztliche Abklärung erforderlich.")
        
        # Analyse der respiratorischen Insuffizienz
        if PaO2 < 80:  # Annahme eines allgemeinen Schwellenwertes für "erniedrigt"
            if PaCO2 < 45:  # Schwellenwert für "normal/erniedrigt"
                results.append("**Hypoxämische Insuffizienz (Typ 1):** Erniedrigter PaO2 mit normalem oder erniedrigtem PaCO2. Mögliche Ursachen sind Gasaustauscheinschränkungen wie Pneumonie oder Lungenembolie.")
            elif PaCO2 > 45:
                results.append("**Ventilatorische Insuffizienz (Typ 2):** Erniedrigter PaO2 mit erhöhtem PaCO2. Dies deutet auf eine ventilatorische Problematik hin.")
        else:
            results.append("Keine Anzeichen für hypoxämische oder ventilatorische Insuffizienz basierend auf PaO2 und PaCO2 Werten.")
        
        # Berechnung des Sollwerts von PaO2 basierend auf Alter und Geschlecht
        
        if geschlecht == "Männlich":
            PaO2_Soll = 100 - (alter / 3)
        else:  # Weiblich
            PaO2_Soll = 100 - (alter / 3) - 1
        PaO2_Soll_rundung = round(PaO2_Soll, 1)

        # Pathologischer Bereich
        if geschlecht == "Männlich":
            paO2_pathologisch_untergrenze = PaO2_Soll - 14
        else:  # Weiblich
            paO2_pathologisch_untergrenze = PaO2_Soll - 15
        paO2_pathologisch_untergrenze_rundung = round(paO2_pathologisch_untergrenze, 1)

        results.append(f"**Sollwert PaO2 (basierend auf Alter und Geschlecht): {PaO2_Soll_rundung} mmHg.**")
        results.append(f"**Pathologische Untergrenze des PaO2: {paO2_pathologisch_untergrenze_rundung} mmHg.**")
        
        # Prüfung der Summe von PaCO2 und PaO2 ohne O2-Gabe
        if summe_PaCO2_PaO2 > 140:
            results.append("⚠️ Achtung: Die Summe von PaCO2 und PaO2 überschreitet 140 mmHg ohne O2-Gabe. "
                       "Dies könnte auf eine unzureichende Oxygenierung oder eine inkorrekte Messung hinweisen.")
        
        # Hyperventilation und korrigiertes PaO2
        if PaCO2 < 35:
            results.append("Hinweis: Bei Hyperventilation (erniedrigtem PaCO2) wurde der Sauerstoffwert entsprechend korrigiert. "
                           "Dies berücksichtigt, dass Hyperventilation ein Kompensationsmechanismus des Körpers bei Sauerstoffmangel darstellt.")

        # Überprüfung der Indikation zur Einleitung einer NIV bei erhöhtem PaCO2
        if PaCO2 > 45:
            results.append("Wichtig: Bei einer Erhöhung des PaCO2 ist stets die Indikation zur Einleitung einer NIV (nicht-invasive Ventilation) zu überprüfen.")

        # LTOT und dessen Überprüfung
        # Angenommen, es gibt eine Variable `ltot_indiziert` (True/False), die angibt, ob LTOT indiziert ist.
        # Sie müssten diese Logik basierend auf Ihren spezifischen Kriterien definieren.
        ltot_indiziert = PaO2 < 60  # Beispielbedingung für die Indikation zur LTOT
        if ltot_indiziert:
            results.append("LTOT indiziert. Der Effekt der Therapie unter der gewählten Flussrate muss überprüft werden: "
                           "Ein Anstieg des PaO2 auf mindestens 60 mmHg bzw. um mindestens 10 mmHg wird angestrebt. "
                           "Ggf. muss die Messung mit einer höheren Sauerstoff-Flussrate wiederholt werden.")
        
        # Analyse des pH-Wertes
        if pH > 7.45:
            primar_storung = "Alkalose"
        elif pH < 7.35:
            primar_storung = "Azidose"
        else:
            primar_storung = "normalem pH-Bereich"
        
        # Berücksichtigung des PaCO2 für die respiratorische Komponente
        if PaCO2 < 35:
            respiratorisch = "niedrigem PaCO2 (respiratorische Alkalose)"
        elif PaCO2 > 45:
            respiratorisch = "hohem PaCO2 (respiratorische Azidose)"
        else:
            respiratorisch = "normalem PaCO2"

        if PaO2 < 70:
            results.append(f"PaO2 niedrig: {PaO2} mmHg → ggf.Hypoxämie.")
        else:
            results.append("PaO2 normal.")

        if PaO2 < 60:
            results.append(f"PaO2 zu niedrig: {PaO2} mmHg → Hypoxämie - bitte LTOT erwägen.")
        else:
            results.append("PaO2 normal.")
        
        if PaCO2 < 35 and BE < -2:
            results.append("Mögliche respiratorische Alkalose mit Anzeichen einer metabolischen Kompensation.")
        elif PaCO2 > 45 and BE > 2:
            results.append("Mögliche respiratorische Azidose mit Anzeichen einer metabolischen Kompensation.")
        elif BE > 2 and PaCO2 < 35:
            results.append("Mögliche metabolische Alkalose mit Anzeichen einer respiratorischen Kompensation.")
        elif BE < -2 and PaCO2 > 45:
            results.append("Mögliche metabolische Azidose mit Anzeichen einer respiratorischen Kompensation.")
        
        # pCO2 Analyse
        if PaCO2 < 35:
            results.append("PaCO2-Wert zu niedrig → Mögliche respiratorische Alkalose.")
        elif PaCO2 > 45:
            results.append("PaCO2-Wert zu hoch → Mögliche respiratorische Azidose.")
        else:
            results.append("PaCO2-Wert normal.")

        # BE und HCO3 Analyse
        if BE < -2:
            results.append("BE zu niedrig → Metabolische Azidose.")
        elif BE > 2:
            results.append("BE zu hoch → Metabolische Alkalose.")
        else:
            results.append("BE normal.")

        if HCO3 < 22:
            results.append("HCO3-Wert zu niedrig → Metabolische Azidose.")
        elif HCO3 > 28:
            results.append("HCO3-Wert zu hoch → Metabolische Alkalose.")
        else:
            results.append("HCO3-Wert normal.")

        # Zusammenfassung der Befunde
        results.append(f"Der Patient hat einen pH-Wert im {primar_storung}, mit {respiratorisch}.")
        
        if "normalem pH-Bereich" in primar_storung and ("niedrigem PaCO2" in respiratorisch or "hohem PaCO2" in respiratorisch):
            results.append("Dies deutet auf eine vollständige Kompensation der primären Störung hin.")
        else:
            results.append("Es liegt eine primäre Störung ohne vollständige Kompensation vor.")
        
        
        # Elektrolyte Analyse und Graduierung der Störung
        if Na < 135:
            results.append("Hyponatriämie: Vorsicht bei zu schneller Korrektur (Risiko für osmotische Demyelinisierung).")
        elif Na > 145:
            results.append("Hypernatriämie: Flüssigkeitszufuhr und Ursachenklärung sind wichtig.")

        if K < 3.5:
            results.append("Hypokaliämie: Achten auf Herzrhythmusstörungen.")
        elif K > 5.0:
            results.append("Hyperkaliämie: Notfallmaßnahmen bei signifikanter Hyperkaliämie und EKG-Veränderungen nötig.")

        if Cl < 96:
            results.append("Hypochlorämie: Oft verbunden mit Alkalose oder Flüssigkeitsverlust.")
        elif Cl > 106:
            results.append("Hyperchlorämie: Kann auf eine Azidose oder Dehydration hinweisen.")

        if Ca < 2.2:
            results.append("Hypokalzämie: Kann zu Tetanie oder Krämpfen führen.")
        elif Ca > 2.6:
            results.append("Hyperkalzämie: Achten auf Nierensteine, Knochenschmerzen und psychiatrische Symptome.")
            
        fehler_bga = """
        ### Wesentliche Fehler bei der Blutgasanalyse und deren Auswirkungen:

        - **Patient hält die Luft an:** PaCO2 leicht erhöht, PaO2 noch normal.
        - **Ungenügende Hyperämie:** PaO2 zu niedrig, PaCO2 kann normal sein.
        - **Luftblase in Kapillare:** PaO2 zu hoch und/oder PaCO2 zu niedrig.
        - **Hyperventilation:** korrigiertes PaO2 beachten!
        """
        st.markdown(fehler_bga)
        
        detailed_diagnosis = "\n".join(results)
        st.markdown("### Befundergebnisse:")
        st.markdown(detailed_diagnosis)


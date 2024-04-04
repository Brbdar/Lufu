#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st

def tiffeneau_index_berechnung1():
    st.header("Lungenfunktionsprüfung - Detaillierter Befundbericht")

    # Erster Informationstext in einem ausklappbaren Bereich
    
    with st.expander("Statische Atemparameter"):
        st.write("""
        **Atemzugvolumen/ AZV - Liter:** Gasvolumen, welches während der Ruheatmung ein- oder ausgeatmet wird. 
        - **Vitalkapazität/ VC - Liter** Atemvolumen zwischen maximaler In- und Exspirationsstellung. Wird In- oder exspiratorisch gemessen
        - **Exspiratorisches Reservevolumen/ ERV - Liter:** Gasvolumen, das aus der Atemruhelage noch ausgeatmet werden kann. Atemruhelage: ekastische Lungenkräfte (zentripetal) und Thoraxkräfte (zentrifugal) sind im Gleichgewicht
        - **Inspiratorisches Reservevolumen/ IRV - Liter** Gasvolumen, das zusätzlich zum normalen Atemzugvolumen eingeatmet werden kann. 
        - **Residualvolumen/ RV - Liter** Gasvolumen, das nach maximaler Ausatmung in der Lunge verbleibt.
        - **Funktionelle Residualkapazität/ FRC - Liter** durch Fremdgasmethode gemessenes Luftvolumen, das bei Atemruhelage in der Lunge verbleibt
        - **thorakales Gasvolumen/ TGV - Liter** durch Ganzkörperplethysmografie gemessenes Luftvolumen, das bei Atemruhelage in der Lunge verbleibt; es beinhaltet auch das nicht ventilierte VOlumen (auch ITGV, intrathorakales GV)
        - **Inspiratorische Reservekapazität/IRC - Liter** - Gasvolumen, das aus der Atemruhelage noch maximal eingeatmet werden kann
        - **Totalkapazität/TLC - Liter** - Gesamtlungenvolumen nach maximaler Inspiration
        """)
    
    with st.expander("Basisinformation"):
        st.write("""
        **Spirometrie: Tiffeneau-Manöver** umfasst vollständige Ausatmung, maximale Einatmung, schnelle Ausatmung.
        - **Messungen:** FEV1, Vitalkapazität, Atemstromstärke.
        - **Fluss-Volumen-Schleife:** Atemvolumen vs. Atemstromstärke.
        - **Einatmung:** bauchförmige Kurve, rechts nach links.
        - **Ausatmung:** steiler Anstieg, langsamer Abfall.
        - **Ventilationsstörungen:** Eiform (Restriktion), Sesselform (Obstruktion, Emphysem), Bockwurstform (Trachealstenose).
        """)
    
    # Zweiter Informationstext in einem ausklappbaren Bereich
    with st.expander("Erweiterte Informationen"):
        st.write("""
        **Atemfluss:** negativ bei Einatmung (Inspiration nach unten), positiv bei Ausatmung (Exspiration nach oben).
        - **Kurvenform:** Inspiration steigt an, fällt ab (bauchförmig nach unten); forcierte Exspiration erreicht schnell maximalen Atemstrom (peak flow), linearer Abfall.
        - **Restriktion:** Verminderte Vitalkapazität, Atemfluss wenig beeinflusst (außer niedrigerer peak flow). Kurve verschmälert auf Volumen-Achse, kaum gestaucht auf Fluss-Achse → Eiform.
        - **Obstruktion:** Veränderter Atemfluss durch erhöhten Widerstand in Bronchien. Vitalkapazität nur bei Emphysem mit erhöhtem Residualvolumen verändert. Typische Sesselform durch Stauchung auf Fluss-Achse.
        - **Emphysem:** Mögliche normale/erhöhte Vitalkapazität trotz erhöhtem Residualvolumen. Verlust elastischer Fasern → reduzierte Retraktionskraft und Lungenkapazität, normalisiert Vitalkapazität. Elastische Fasern wichtig für Bronchienstabilität bei Ausatmung, deren Verlust führt zu Obstruktion.
        """)


   # Bewertungsfunktionen
    def grade_obstruction(percent):
        if percent < 80:
            return "eine leichte Obstruktion"
        elif 60 <= percent < 70:
            return "eine moderate Obstruktion"
        elif 50 <= percent < 60:
            return "eine mittelschwere Obstruktion"
        else:
            return "eine schwere Obstruktion"

    def vc_grade(percent):
        if percent >= 70:
            return "eine leichte Obstruktion"
        elif 60 <= percent < 70:
            return "eine moderate Obstruktion"
        elif 50 <= percent < 60:
            return "eine mittelschwere Obstruktion"
        else:
            return "eine schwere Obstruktion"
    
    def graduiere_fev1_vc(prozent):
        if prozent >= 70:
            return "I (leicht)"
        elif 60 <= prozent < 70:
            return "II (mäßig)"
        elif 50 <= prozent < 60:
            return "III (mittelschwer)"
        elif 35 <= prozent < 50:
            return "IV (schwer)"
        else:
            return "V (sehr schwer)"

    def assess_rv(percent):
        if percent < 140:
            return "leicht erhöht"
        elif 140 <= percent <= 170:
            return "mittel"
        else:
            return "schwer"

    def assess_tlc(percent):
        if percent >101:
            return "leicht erhöht"
        elif 50 <= percent <= 100:
            return "niedrig bis normal"
        elif 130 <= percent <= 150:
            return "mittel"
        else:
            return "schwer"

    def grade_emphysema(rv, tlc):
        quotient = rv / tlc
        if quotient >= 0.6:
            return "ein schweres Emphysem"
        elif quotient >= 0.5:
            return "ein mittelschweres Emphysem"
        elif quotient >= 0.4:
            return "ein leichtes Emphysem"
        else:
            return "kein Emphysem"
        
    def classify_copd(fev1_percent):
        if fev1_percent >= 80:
            return "GOLD 1: Leichte COPD"
        elif fev1_percent >= 50:
            return "GOLD 2: Mittelschwere COPD"
        elif fev1_percent >= 30:
            return "GOLD 3: Schwere COPD"
        else:
            return "GOLD 4: Sehr schwere COPD"
        
    def classify_restriktion(fvc_percent):
        if fvc_percent >= 60:
            return "I Schweregrad: leichte Restriktion"
        elif 40 <= fvc_percent <= 60:
            return "II Schweregrad: mittelschwere Restriktion"
        else:
            return "III Schweregrad: schwere Restriktion"
        

    # Benutzereingaben über Streamlit Widgets
    fev1_percent = st.number_input("FEV1 (% vom Sollwert) vor Broncholyse:", value=100.0)
    fvc_percent = st.number_input("Forcierte Vitalkapazität (% vom Sollwert):", value=100.0)

    # Berechnung des Tiffeneau-Index
    tiffeneau_index = (fev1_percent / fvc_percent) * 100

    # Initialisierung von Variablen
    report = ""
    tlc_percent = 100  # Standardwert, um den UnboundLocalError zu vermeiden

    
    # Logik für den Bericht
    if tiffeneau_index < 80:
        obstruction_grade = grade_obstruction(fev1_percent)
        grad_vc = graduiere_fev1_vc(fvc_percent)
        
        report += f"Der Tiffeneau-Index beträgt {tiffeneau_index:.2f}%, was auf {obstruction_grade} hinweist. "
        report += f"Die Vitalkapazität ist als {grad_vc} klassifiziert. "

        if fvc_percent < 80:
            tlc_percent = st.number_input("Totale Lungenkapazität (TLC) in Prozent vom Sollwert bei Obstruktion:", value=100.0)
            tlc_grade = assess_tlc(tlc_percent)
            report += f"Die Totale Lungenkapazität (TLC) ist {tlc_grade}, was die Diagnose eines Überlappungssyndroms unterstützt. "
        else:
            report += "Es liegt ein reines obstruktives Syndrom vor. "
            dlco_sb_percent = st.number_input("DLCO_SB in Prozent vom Sollwert bei normaler VC und reduzierter FEV1:", value=100.0)
            if dlco_sb_percent > 80:
                report += " Mögliche Diagnose: Asthma Bronchiale - obstruktiv -> Funktionstest Broncholyse. "
            else:
                report += " Mögliche Diagnose: COPD "
                
        # Zusätzliche Informationen, wenn der Tiffeneau-Index unter 71 liegt und DLCO erniedrigt ist
        if tiffeneau_index < 71 and dlco_sb_percent < 80:
            report += "\n\nZusatzinformation: Der Tiffeneau-Index unter 0,71 zusammen mit einer erniedrigten DLCO weist auf eine signifikante Atemwegsobstruktion hin, die mit einem erhöhten Risiko für Hospitalisierung oder Tod bei COPD-Patienten assoziiert ist. Dies unterstreicht die Bedeutung einer gründlichen Diagnostik und Überwachung des Zustands."
            report += "Tiffeneau-Index < LLN = Voraussetzung für Obstruktion"
        # Anpassung der Berichtslogik
        if tiffeneau_index < 71 and dlco_sb_percent < 80:
            copd_classification = classify_copd(fev1_percent)
            report += f"\n\nBasierend auf der GOLD-Klassifikation wird der COPD-Schweregrad als {copd_classification} eingestuft."
    
        # Überprüfung, ob FEV1 > 80%
    if fev1_percent > 80:
        # MEF 25-Abfrage, wenn FEV1 > 80%
        mef_25 = st.number_input("MEF 25 (% vom Sollwert):", value=100.0)
        
        # Bewertung und Berichtserstellung basierend auf MEF 25
        if mef_25 < 75:
            report += ("Es liegt eine isolierte Erniedrigung des MEF 25 vor, was auf eine Obstruktion der kleinen Atemwege hinweist. "
                       "Pathophysiologisch kann dies auf Veränderungen in den Bronchiolen zurückgeführt werden, "
                       "wie sie bei Erkrankungen wie COPD oder fortgeschrittenem Asthma auftreten können. ")
        else:
            report += "Der MEF 25-Wert liegt im normalen Bereich, was gegen eine isolierte Obstruktion der kleinen Atemwege spricht. "
        
    if tiffeneau_index >= 80:
        
        if fvc_percent < 80:
                dlco_sb_percent = st.number_input("DLCO_SB in Prozent vom Sollwert ohne Restriktion:", value=100.0)
                if dlco_sb_percent < 80:
                    report += "was auf eine Lungengefäßerkrankung, beginnende Lungenfibrose oder isoliertes Emphysem hindeutet. "
                else:
                    report += "was eine normale Lungenfunktion nahelegt. "
        else:
            tlc_percent = st.number_input("Totale Lungenkapazität (TLC) in Prozent vom Sollwert bei normaler VC:", value=100.0)
            if tlc_percent >= 80:
                rv_percent = st.number_input("Residualvolumen (RV) in Prozent vom Sollwert:", value=100.0)
                rv_grade = assess_rv(rv_percent)
                if rv_percent > 101:
                    emphysem_grad = grade_emphysema(rv_percent, tlc_percent)
                    report += f"Gas Trapping - Blässchen, Emphyseme a.e.: {emphysem_grad} hin. "
                else:
                    report += "Es liegen keine Anzeichen von Emphysem vor. "
            else:
                dlco_sb_percent = st.number_input("DLCO_SB in Prozent vom Sollwert bei normaler VC und reduzierter TLC:", value=100.0)
                if dlco_sb_percent < 80:
                    report += "Restriktives Syndrom mit Hinweis auf Lungenfibrosen. "
                else:
                    report += "Restriktives Syndrom mit Hinweis auf eine extrapulmonale Restriktion (Neuromuslkuläre Erkrankung? Kyphoskoliose, Adipositas?)"
        if tlc_percent < 80:
            copd_classification = classify_copd(fev1_percent)
            report += f"\n\nBasierend auf der GOLD-Klassifikation wird der COPD-Schweregrad als {copd_classification} eingestuft."


    # Button zur Bestätigung der Berichtsanzeige
    if st.button('Bericht anzeigen'):
        st.write("### Befundbericht")
        st.write(report)
   

    with st.columns(1)[0]:  # Direkter Zugriff auf das erste Element der Liste
        if st.button('Algorithmus'):
            st.session_state.selected_curve = 'Algorithmus'

    # Logik zur Anzeige der Erklärung basierend auf der Auswahl
    if 'selected_curve' in st.session_state:
        if st.session_state.selected_curve == 'Algorithmus':
            st.write("Befundungsalgorithmus...")
            st.image("algorithmus.jpg") 


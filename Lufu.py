#!/usr/bin/env python
# coding: utf-8

# In[192]:


import streamlit as st

# Hauptteil der App
st.title("Analysebereich Lungenfunktion")


# In[14]:


import streamlit as st

def spirometrie_qualitativ():
    st.header("Spirometrie qualitativ")
    
    st.write('Die Patientenmitarbeit beeinflusst wesentlich alle Parameter, **vor allem den exspiratorischen Fluss bis MEF 75**, während Flüsse ab MEF 50 weitestgehend unabhängig sind. **Diese Mitarbeit ist bei der Diagnose zu berücksichtigen**')
    
    st.write('Bei der Spirometrie führt der Patient ein Tiffeneau-Manöver durch: Nach vollständiger Ausatmung atmet er so tief wie möglich ein und anschließend so schnell wie möglich aus. Diese Prozedur ermöglicht die Messung von FEV1, Vitalkapazität und weiteren Werten. Die dabei entstehende Fluss-Volumen-Kurve ist ein zentrales Instrument zur Beurteilung der Lungenfunktion.Die Form dieser Kurve und ihre Reaktion auf Bronchodilatatoren geben Aufschluss über obstruktive und restriktive Lungenkrankheiten sowie das Vorhandensein eines Emphysems.')

    # Erster Informationstext in einem ausklappbaren Bereich
    with st.expander("Basisinformationen:"):
        st.write("""
        **Spirometrie: Tiffeneau-Manöver** umfasst vollständige Ausatmung, maximale Einatmung, schnelle Ausatmung.
        - **Messungen:** FEV1, Vitalkapazität, Atemstromstärke.
        - **Fluss-Volumen-Schleife:** Atemvolumen vs. Atemstromstärke.
        - **Einatmung:** bauchförmige Kurve, rechts nach links.
        - **Ausatmung:** steiler Anstieg, langsamer Abfall.
        - **Ventilationsstörungen:** Eiform (Restriktion), Sesselform (Obstruktion, Emphysem), Bockwurstform (Trachealstenose).
        """)

    # Zweiter Informationstext in einem ausklappbaren Bereich
    with st.expander("Erweitert:"):
        st.write("""
        **Atemfluss:** negativ bei Einatmung (Inspiration nach unten), positiv bei Ausatmung (Exspiration nach oben).
        - **Kurvenform:** Inspiration steigt an, fällt ab (bauchförmig nach unten); forcierte Exspiration erreicht schnell maximalen Atemstrom (peak flow), linearer Abfall.
        - **Restriktion:** Verminderte Vitalkapazität, Atemfluss wenig beeinflusst (außer niedrigerer peak flow). Kurve verschmälert auf Volumen-Achse, kaum gestaucht auf Fluss-Achse → Eiform.
        - **Obstruktion:** Veränderter Atemfluss durch erhöhten Widerstand in Bronchien. Vitalkapazität nur bei Emphysem mit erhöhtem Residualvolumen verändert. Typische Sesselform durch Stauchung auf Fluss-Achse.
        - **Emphysem:** Mögliche normale/erhöhte Vitalkapazität trotz erhöhtem Residualvolumen. Verlust elastischer Fasern → reduzierte Retraktionskraft und Lungenkapazität, normalisiert Vitalkapazität. Elastische Fasern wichtig für Bronchienstabilität bei Ausatmung, deren Verlust führt zu Obstruktion.
        """)


    # Bilder als Platzhalter für interaktive Auswahl
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Obstruktive Kurve'):
            st.session_state.selected_curve = 'Obstruktiv'
    with col2:
        if st.button('Restriktive Kurve'):
            st.session_state.selected_curve = 'Restriktiv'
    with col3:
        if st.button('Emphysem Kurve'):
            st.session_state.selected_curve = 'Emphysem'

    # Logik zur Anzeige der Erklärung basierend auf der Auswahl
    if 'selected_curve' in st.session_state:
        if st.session_state.selected_curve == 'Obstruktiv':
            st.write("Erklärung für Obstruktiv...")
            st.image("obstruktiv.jpg")
        elif st.session_state.selected_curve == 'Restriktiv':
            st.write("Erklärung für Restriktiv...")
            st.image("restriktiv.jpg")
        elif st.session_state.selected_curve == 'Emphysem':
            st.write("Erklärung für Emphysem...")
            st.image("emphysem.jpg")

    st.markdown("[Mehr Informationen zur Spirometrie](https://www.atsjournals.org/doi/epdf/10.1164/rccm.201908-1590ST?role=tab)")
            


# In[114]:


### Abschnitt Spiro Quantitativ

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
        if percent >= 70:
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


# In[33]:


def Bodyplethysmographie_Residualvolumen():
    st.header("Bodyplethysmographie - Residualvolumen")
    
     # Erster Informationstext in einem ausklappbaren Bereich
    with st.expander("Basiswissen anzeigen:"):
        st.write("""
        - Spirometrie erfasst ein- und ausatembare Volumina, nicht jedoch das Residualvolumen (RV).
        - RV = Residualvolumen, das auch nach maximaler Ausatmung in der Lunge bleibt, ist nur durch Bodyplethysmographie messbar.
        - Totale Lungenkapazität (TLC), funktionelle Residualkapazität (FRC), und thorakales Gasvolumen (TGV) inkludieren RV und werden ebenfalls nur mit Bodyplethysmographie bestimmt.
        - Ein **erhöhtes RV** ist typisch für Emphysem (irreversibel) und Air Trapping (unter Broncholyse reversibel).
        - Ein **erniedrigtes RV** weist auf **Restriktion** hin, bei der alle Volumina vermindert sind.
        - **„Kapazität“** bezeichnet ein aus verschiedenen Volumina zusammengesetztes Volumen, z.B. setzt sich die Vitalkapazität (VC) aus Atemzugvolumen, inspiratorischem Reservevolumen und exspiratorischem Reservevolumen zusammen. 
        """)
    
    # Zweiter Informationstext in einem ausklappbaren Bereich
    with st.expander("Erweiterte Informationen:"):
        st.write("""
        - Emphysem und Air Trapping** führen oft zu erhöhtem Residualvolumen auf Kosten der Vitalkapazität.
        - Die totale Lungenkapazität (TLC)** ist bei Emphysem oft nur gering erhöht.
        - Zur Bestimmung des Emphysemausmaßes wird der RV/TLC Quotient herangezogen.
        - Eine Obstruktion und typische **Sesselform** in der Spirometrie deuten auf Emphysem hin; bestätigt durch Bodyplethysmographie.
        - Bei erhöhtem Residualvolumen ist eine Broncholyse zur Unterscheidung zwischen Emphysem und Air Trapping indiziert, unabhängig von Obstruktion.
        - Die funktionelle Residualkapazität (FRC) entspricht RV + ERV; sie bleibt bei normaler Atmung im Thorax und steht für den Gasaustausch zur Verfügung.
        - Der Atemwegswiderstand korreliert gut mit der Atemarbeit, die es brauch um visköse Widerstände zu überwinden
        """)
    
    # Erläuterung der Bodyplethysmographie
    st.write("""
    Die Bodyplethysmographie ermöglicht es uns, präzise das Residualvolumen (RV), die totale Lungenkapazität (TLC) und das thorakale Gasvolumen (TGV) zu messen. Diese Messungen sind entscheidend, um das Vorhandensein und das Ausmaß von Zuständen wie Emphysem und Air Trapping zu beurteilen.
    """)

        # Nutzung der zuvor eingegebenen Werte aus dem Session State, falls vorhanden
    fev1_prozent = st.session_state.get('fev1_prozent', 100.0)
    fev1_prozent_post_broncholyse = st.session_state.get('fev1_prozent_post_broncholyse', 0.0)
    awr_post_broncholyse = st.session_state.get('awr_post_broncholyse', 0.0)
    mef_25_prozent = st.session_state.get('mef_25_prozent', 100.0)

    # Nutzung der zuvor eingegebenen Werte aus dem Session State
    fev1_prozent = st.session_state.get('fev1_prozent', 100.0)

    # Bestimmung von Obstruktion oder Restriktion basierend auf FEV1%
    if fev1_prozent >= 80:
        lungenfunktion_typ = "Normal"
    elif fev1_prozent < 80:
        lungenfunktion_typ = "Obstruktion"

    # Graduierung der Obstruktion basierend auf FEV1%
    if lungenfunktion_typ == "Obstruktion":
        if fev1_prozent >= 70:
            grad = "Leichte Obstruktion"
        elif 60 <= fev1_prozent < 70:
            grad = "Moderate Obstruktion"
        elif 50 <= fev1_prozent < 60:
            grad = "Mittelschwere Obstruktion"
        else:
            grad = "Schwere Obstruktion"
    else:
        grad = "Normal"

    # Eingabefelder für die Messwerte
    rv = st.number_input("Residualvolumen (RV) in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f")
    tlc = st.number_input("Totale Lungenkapazität (TLC) in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f")
    tgv = st.number_input("Thorakales Gasvolumen (TGV) in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f")
    awr_post_broncholyse = st.number_input("Atemwegswiderstand nach Broncholyse (optional, in Pa/s):", value=0.0, format="%.2f")
    
    rv_absolut = st.number_input("Residualvolumen (RV in Liter):", value=1.5, min_value=0.0, format="%.1f")
    tlc_absolut = st.number_input("Residualvolumen (RV in Liter):", value=6.0, min_value=0.0, format="%.1f")
    befund_text_bodyspleth = "### Befundbericht:\n"



    # RV-Bewertung und Graduierung
    rv_bewertung = "leicht erhöht" if rv < 140 else "mittel" if 140 <= rv <= 170 else "schwer"

    # TLC-Bewertung und Graduierung
    tlc_bewertung = "leicht erhöht" if tlc < 130 else "mittel" if 130 <= tlc <= 150 else "schwer"

    # TGV-Bewertung und Graduierung
    tgv_bewertung = "leicht erhöht" if rv < 140 else "mittel" if 140 <= rv <= 170 else "schwer" 

    # Funktion zur Bewertung des AWR und Unterscheidung zwischen Strömungshindernissen
    def bewerte_awr_und_hindernisse(awr_post_broncholyse):
        if awr_post_broncholyse < 170:
            awr_bewertung = "Normal"
            hindernis_typ = "Kein Hinweis auf signifikantes Strömungshindernis"
        elif 170 <= awr_post_broncholyse <= 350:
            awr_bewertung = "Erhöht"
            hindernis_typ = "Möglicherweise intrathorakales Strömungshindernis"
        else:
            awr_bewertung = "Deutlich erhöht"
            hindernis_typ = "Möglicherweise extrathorakales Strömungshindernis"
        return awr_bewertung, hindernis_typ

    awr_bewertung, hindernis_typ = bewerte_awr_und_hindernisse(awr_post_broncholyse)


    # Berechnung des RV/TLC-Quotienten und Graduierung des Emphysems
    rv_tlc_quotient = rv_absolut / tlc_absolut
    emphysem_grad = "kein Emphysem"
    if rv_tlc_quotient >= 0.6:
        emphysem_grad = "Schweres Emphysem (> 60%)"
    elif rv_tlc_quotient >= 0.5:
        emphysem_grad = "Mittelschweres Emphysem (50% bis 60%)"
    elif rv_tlc_quotient >= 0.4:
        emphysem_grad = "Leichtes Emphysem (< 50%)"

   # Initialisierung des Befundberichts
    befund_text_bodyspleth = "### Befundbericht:\n"

    lungenfunktion_typ = st.session_state.get('lungenfunktionstyp', 'Nicht spezifiziert')
    grad = st.session_state.get('grad', 'Nicht bewertet')

    # Initialisierung des Befundberichts
    befund_text_bodyspleth = "### Befundbericht:\n"

    # 1. Graduierung der Obstruktion und physiologische Erläuterungen
    befund_text_bodyspleth += f"\nLungenfunktionsstatus: {lungenfunktion_typ} - {grad}."
    if lungenfunktion_typ == "Obstruktion":
        befund_text_bodyspleth += " Dies deutet auf eine Einschränkung des Luftflusses hin, die bei Krankheiten wie Asthma oder COPD üblich ist."
    elif lungenfunktion_typ == "Restriktion":
        befund_text_bodyspleth += " Dies weist auf eine verminderte Expansion der Lunge hin, möglicherweise aufgrund von Fibrose oder anderen interstitiellen Lungenerkrankungen."

    # 2. Bewertung des Atemwegswiderstands (AWR) nach Broncholyse und physiologische Bedeutung
    befund_text_bodyspleth += f"\nAtemwegswiderstand nach Broncholyse ist {awr_bewertung}. "
    befund_text_bodyspleth += f"Dies deutet auf ein {hindernis_typ} hin, was auf spezifische Pathologien wie Bronchialobstruktion oder Luftröhrenverengung hinweisen kann.\n"

    # 3. Berechnung des RV/TLC-Quotienten, Graduierung des Emphysems und Erläuterung
    befund_text_bodyspleth += f"Der RV/TLC Quotient beträgt {rv_tlc_quotient*100:.2f}%, was auf ein {emphysem_grad} hindeutet. "
    befund_text_bodyspleth += "Ein erhöhter RV/TLC-Quotient ist ein Marker für ein Emphysem, ein Zustand, der durch die Zerstörung der Alveolarwände gekennzeichnet ist."

    # 4. Detaillierte Bewertung von RV, TLC und TGV mit Erläuterungen
    befund_text_bodyspleth += "\n**Detaillierte Bewertung:**\n"
    befund_text_bodyspleth += f"- Das Residualvolumen (RV) ist {rv_bewertung}, basierend auf einem Wert von {rv}% vom Soll. Erhöhte RV-Werte können auf eine Obstruktion der kleinen Atemwege hinweisen.\n"
    befund_text_bodyspleth += f"- Die Totale Lungenkapazität (TLC) wird als {tlc_bewertung} eingestuft, basierend auf einem Wert von {tlc}% vom Soll. Veränderungen in der TLC können auf restriktive oder obstruktive Lungenkrankheiten hindeuten.\n"
    befund_text_bodyspleth += f"- Das Thorakale Gasvolumen (TGV) wird als {tgv_bewertung} bewertet, basierend auf einem Wert von {tgv}% vom Soll. TGV-Veränderungen reflektieren Veränderungen im Lungenvolumen, die bei verschiedenen pulmonalen Pathologien auftreten können.\n"

    # 5. Abschließende Bewertung und Empfehlungen mit Hinweis auf Differentialdiagnosen
    befund_text_bodyspleth += "\nBasierend auf den vorliegenden Messwerten und dem Atemwegswiderstand empfehlen wir "
    befund_text_bodyspleth += "eine detaillierte klinische Bewertung, um zwischen reversiblen und irreversiblen Lungenveränderungen sowie zwischen "
    befund_text_bodyspleth += "extrathorakalen und intrathorakalen Strömungshindernissen zu differenzieren. Mögliche Differentialdiagnosen umfassen Asthma, COPD, interstitielle Lungenerkrankungen und Lungenfibrose. Die weitere Diagnostik sollte auch bildgebende Verfahren und ggf. eine Lungenbiopsie umfassen.\n"

    # Anzeige des gesamten Befundberichts
    st.markdown(befund_text_bodyspleth)


# In[11]:


def Bodyplethysmographie_Fluss_Druck_Kurve():
    st.header("Bodyplethysmographie - Fluss-Druck-Kurve")
    
    st.write('Zur Bestimmung des Widerstandes wird der Munddruck gemessen. Dieser wird dann graphisch in der Fluss-Druck-Kurve (= Atemschleife) dargestellt. Es werden Fluss und Munddruck gegen das Verschiebevolumen aufgetragen, wodurch zwei Schleifen entstehen.')

    st.write('Aussagekräftigste Methode bei Obstruktion, zuverlässigste Methode zur Residualvolumenbestimmung und mitarbeitsunabhängig, weil in Ruheatmung gemessen wird')
    st.write('auch bei Dyspnoe einsetzbar')
    
    # Erster Informationstext in einem ausklappbaren Bereich
    with st.expander("Basisinformationen:"):
        st.write("""
        - Untersuchung dauer fünf Minuten pro Messung
        - Messfehler < 5%
        - Wichtig. Die Differenzierung von obstruktiver Ventilationsstörungen mittels FEV1, FEV1/VC (Spirometrie), Residualvolumen und Atemwegswiderstand.
        - Messung von Residualvolumen und Atemwegswiderstand exklusiv durch Bodyplethysmographie.
        - Widerstandsbestimmung über Munddruckmessung, visualisiert in der Fluss-Druck-Kurve (Atemschleife) durch Auftragung gegen Verschiebevolumen.
        - Diagnosekriterium für Obstruktion: Schnittpunkt der Schleifen bei >90°; bei Gesunden oder restriktiven Störungen <90°.
        - Emphysem induziert eine charakteristische Keulenform der Atemschleife.
        """)

    # Zweiter Informationstext in einem ausklappbaren Bereich
    with st.expander("Erweitert:"):
        st.write("""
        - Einatmung und Ausatmung in der Fluss-Druck-Kurve gegenläufig zur Fluss-Volumen-Kurve dargestellt.
        - Gerade durch Schleifen bei Gesunden steil (kleiner Schnittwinkel), bei Obstruktiven flach (großer Schnittwinkel), bedingt durch den höheren Widerstand bei Obstruktion.
        - Notwendigkeit eines größeren Drucks bei Obstruktion, um gleichen Atemfluss zu erzeugen, entsprechend dem physikalischen Gesetz: Widerstand = Druck / Atemstrom.
        - Emphysem und Air Trapping führen zu endexspiratorischem Bronchiolenkollaps, erhöhtem notwendigen Atmungsdruck und Residualvolumen.
        - Graphische Darstellung als Keulenform der Kurve in der Exspiration, erweiterte untere Schleife, die x-Achse an unterschiedlichen Punkten schneidet.
        """)


    # Bilder als Platzhalter für interaktive Auswahl
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button('Normale Atemflusskurve'):
            st.session_state.selected_curve = 'Normal'
    with col2:
        if st.button('Emphysematöse Atemflusskurve'):
            st.session_state.selected_curve = 'Emphysem'
    with col3:
        if st.button('Obstruktion'):
            st.session_state.selected_curve = 'Obstruktion'
    with col4:
        if st.button('Reversible Obstruktion'):
            st.session_state.selected_curve = 'Reversible Obstruktion'

    # Logik zur Anzeige der Erklärung basierend auf der Auswahl
    if 'selected_curve' in st.session_state:
        if st.session_state.selected_curve == 'Normal':
            st.write("In der Schleife geht die Einatmung nach oben, die Ausatmung nach unten (umgekehrt der Fluss-Volumen-Kurve). Die Gerade durch die Schleifen ist beim Gesunden steil (hierdurch kleiner Schnittwinkel)")
            st.image("Atemschleife_normal.jpg")
        elif st.session_state.selected_curve == 'Emphysem':
            st.write("Befund Schnittwinkel der Schleifen > 90° als Zeichen der Obstruktion. Ausgeprägte Keulenform als Zeichen eines Emphysems. Kaum ein Unterschied vor (blau) und nach (rot) Broncholyse.")
            st.image("Emphysem_verschiebevolumen.jpg")
        elif st.session_state.selected_curve == 'Obstruktion':
            st.write("Schnittwinkel der Schleifen > 90° als Zeichen der Obstruktion. Keulenform als Zeichen eines Emphysems. Unter Broncholyse geringe Verkleinerung des Winkels mit leichter Verschmälerung der Keulenform als Hinweis auf ein geringes Air Trapping.")
            st.image("Obstruktion_flussvolumenkurve.jpg")
        elif st.session_state.selected_curve == 'Reversible Obstruktion':
            st.write("Schnittwinkel der Schleifen > 90° als Zeichen der Obstruktion. Geringe Keulenform als Zeichen eines erhöhten Residualvolumens. Unter Broncholyse (rot) normale Atemschleife als Zeichen einer reversiblen Obstruktion und eines Air Trappings.")
            st.image("Reversible_Obstruktion.jpg")

# Visuelle Bewertungsfragen
    frage1 = st.radio("Schneiden sich die Schleifen der Atemkurve in einem Winkel größer als 90°?", ('Ja', 'Nein'))
    frage2 = st.radio("Zeigt die Atemschleife eine Keulenform?", ('Ja', 'Nein'))
    frage3 = st.radio("Ist die Steigung der Schleife während der Ausatmung deutlich flacher im Vergleich zur Einatmung?", ('Ja', 'Nein'))
    frage4 = st.radio("Endet die exspiratorische Schleife auf einem höheren Niveau als sie begonnen hat?", ('Ja', 'Nein'))

    # Analyse und automatisierter Befund basierend auf visueller Bewertung
    if frage1 == 'Ja':
        st.write("Befund: Ein Winkel größer als 90° deutet auf eine obstruktive Ventilationsstörung hin.")
    else:
        st.write("Befund: Ein Winkel kleiner als 90° spricht gegen eine ausgeprägte obstruktive Ventilationsstörung.")

    if frage2 == 'Ja':
        st.write("Zusatzbefund: Eine Keulenform der Atemschleife weist auf das Vorliegen eines Emphysems oder Air Trapping hin.")

    if frage3 == 'Ja':
        st.write("Hinweis: Eine flachere Steigung während der Ausatmung im Vergleich zur Einatmung signalisiert einen erhöhten exspiratorischen Widerstand.")

    if frage4 == 'Ja':
        st.write("Weiterer Befund: Ein höheres Ende der exspiratorischen Schleife deutet auf ein erhöhtes Residualvolumen hin, was typisch für Emphysem oder Air Trapping ist.")

    st.write("Bitte beachten: Diese Analyse ersetzt nicht die umfassende Bewertung durch einen Facharzt. Weitere Untersuchungen könnten erforderlich sein, um eine abschließende Diagnose zu stellen.")
            
### Abschnitt Ende


# In[ ]:


def Funktionstests_Broncholyse():
    st.header("Funktionstests - Broncholyse")
    
    st.write("XX")
    
    with st.expander("XX"):
        st.write("""
        - XX.
        - XX
        - XX
        - XX
        - XX
        """)

    with st.expander("XX"):
        st.write("""
        - XX
        - XX
        - XX
        """)


# In[ ]:


def Funktionstests_Provokation():
    st.header("Funktionstests - Provokation")
    
    st.write("XX")
    
    with st.expander("XX"):
        st.write("""
        - XX.
        - XX
        - XX
        - XX
        - XX
        """)

    with st.expander("XX"):
        st.write("""
        - XX
        - XX
        - XX
        """)


# In[186]:


def P0_Atemkraftmessung():
    st.header("P0_Atemkraftmessung")
    
    st.write("Die P0.1-Messung dient der Überprüfung der Atemmuskulatur, um festzustellen, ob diese ausreichend Luft in die Lungen befördert. Sie ist wichtig für die Diagnose von Atemschwäche und die Entscheidung über den Beginn einer Heimbeatmung. Diese Messung betrifft sowohl das Zwerchfell als auch unterstützende Muskeln. Eine ungenügende Atemleistung kann zu einem Anstieg des Kohlendioxidgehalts im Blut führen. Funktionsstörungen der Atempumpe können durch zentrale Nervensystemprobleme, neuromuskuläre Erkrankungen, Skelettdeformitäten oder Lungenerkrankungen verursacht werden.")
    
    with st.expander("Durchführung der Messung - Last der Atemmuskulatur = P0.1-Wert"):
        st.write("""
        - Elektromagnetisches Ventil verschließt Atemweg direkt nach Einatmung für 0,15 Sekunden..
        - Inspirationsdruck wird nach 100 Millisekunden (0,1s) gemessen.
        - Druck am Mund zeigt den Unterdruck in Alveolen und somit Krafteinsatz der Atemmuskulatur.
        - Kurze Atmungsunterbrechung, vom Patienten unbemerkt, beeinflusst Atmung nicht.
        - Messung erfolgt etwa 10-mal zu zufälligen Zeiten, Mittelwertbildung.
        - P0.1-Wert (kPa) reflektiert Atemmuskulaturbelastung bei Ruheatmung.
        - P0.1-Messung allein zeigt keine atemmuskuläre Schwäche auf.
        - Es gilt ein geschlechtsunabhängiger Grenzwert von ≤ 0,3 kPa als normal.
        """)

    with st.expander("Die Maximale Atemmuskelkraft"):
        st.write("""
        - Patient atmet vollständig aus und inhaliert dann maximal gegen geschlossenes Ventil.
        - Ventil bleibt für 3–5 Sekunden geschlossen, mindestens bis maximaler Druck erreicht ist.
        - Manöver wird 6-mal wiederholt.
        - Höchster ermittelter Druck definiert als Pimax (maximale Atemmuskelkraft).
        """)
        
    with st.expander("Indikationen"):
        st.write("""
        - Bewertung der Atemmuskelfunktion bei Verdacht auf Muskelschwäche.
        - Diagnose und Überwachung von Atemwegserkrankungen wie COPD und Asthma.
        - Einschätzung von Atemantriebsstörungen, z.B. bei Hypoventilationssyndromen.
        - Beurteilung der Effektivität therapeutischer Interventionen.
        - Langzeitüberwachung von Patienten mit neuromuskulären Erkrankungen.
        """)
        
    with st.expander("Maßnahmen"):
        st.write("""
        - Physiotherapie und Atemübungen: Stärkung der Atemmuskulatur, Verbesserung der Atemeffizienz.
        - Nicht-invasive Beatmung (NIV): Reduktion der Atemarbeit, Normalisierung der Blutgase.
        - Medikamentöse Therapieanpassung: Verringerung der Atemwegsobstruktion, Erleichterung der Atmung.
        - Lebensstiländerungen: Gewichtsabnahme, Raucherentwöhnung zur Verbesserung der Lungenfunktion.
        - Invasive Beatmung: Bei akutem respiratorischem Versagen oder schweren neuromuskulären Erkrankungen.
        - Chirurgische Maßnahmen: Z.B. Lungenvolumenreduktion bei schwerer COPD.
        """)

    st.write("""
        Dieses Tool hilft bei der Interpretation von Schlüsselparametern zur Beurteilung der Atemmuskulatur:
        - **P0.1 (kPa):** Misst die Last der Atemmuskulatur bei Ruheatmung.
        - **PImax (kPa):** Gibt die maximale inspiratorische Atemmuskelkraft an.
        Der Quotient **P0.1/PImax** reflektiert die prozentuale Beanspruchung der Atemmuskulatur, was Aufschlüsse über die respiratorische Kapazität gibt.
    """)



    # Funktion zur Interpretation des P0.1-Werts
    def interpret_p01(p01_value):
        if p01_value < 0.3:
            return "Der P0.1-Wert liegt im Normbereich."
        else:
            return "Der P0.1-Wert überschreitet den Normbereich und könnte auf eine erhöhte Atemlast hinweisen."

    def interpret_pimax(pimax_value, gender, age):
        st.write("Interpretiert den PImax-Wert basierend auf Alter, Geschlecht und den gegebenen Interpretationsrichtlinien")
    
    
        # Normwerte für PImax basierend auf Alter und Geschlecht
        normwerte = {
            'm': [(40, 6.2), (60, 5.4), (80, 4.6), (float('inf'), 4.1)],
            'f': [(40, 5.7), (60, 4.9), (80, 4.2), (float('inf'), 3.7)]
        }

        # Ermitteln der entsprechenden Normwerte
        for age_threshold, pimax_norm in normwerte[gender]:
            if age <= age_threshold:
                pimax_norm_value = pimax_norm
                break

        # Interpretation basierend auf dem Vergleich des gemessenen Werts mit dem Normwert
        if pimax_value >= pimax_norm_value:
            return f"Der PImax-Wert von {pimax_value} kPa liegt im Normbereich oder darüber (Normwert für Ihre Altersgruppe: {pimax_norm_value} kPa)."
        else:
            return f"Der PImax-Wert von {pimax_value} kPa ist niedriger als der Normwert für Ihre Altersgruppe ({pimax_norm_value} kPa) und könnte auf eine Schwäche der Inspirationsmuskulatur hinweisen."

    # Funktion zur Berechnung und Interpretation des P0.1/PImax-Quotienten
    def calculate_and_interpret_p01_pimax_ratio(p01_value, pimax_value):
        if pimax_value == 0:
            return "PImax darf nicht 0 sein."
        ratio = (p01_value / pimax_value) * 100
        if ratio < 4:
            return f"Mit einem Quotienten von {ratio:.2f}% liegt die Beanspruchung im normalen Bereich."
        elif 4 <= ratio < 10:
            return f"Mit einem Quotienten von {ratio:.2f}% liegt eine leicht erhöhte Beanspruchung vor."
        elif 10 <= ratio < 15:
            return f"Mit einem Quotienten von {ratio:.2f}% liegt eine mittelgradig erhöhte Beanspruchung vor."
        elif 15 <= ratio <= 20:
            return f"Mit einem Quotienten von {ratio:.2f}% liegt eine schwergradig erhöhte Beanspruchung vor."
        else:
            return f"Mit einem Quotienten von {ratio:.2f}% wird von einer Erschöpfung der Atempumpe ausgegangen."

    # Geschlechts- und Altersauswahl hinzufügen
    gender = st.radio("Geschlecht:", ('m', 'f'), key='gender_select')
    age = st.number_input("Alter (Jahre):", min_value=0, max_value=120, step=1, format="%d")

    # P0.1-Wert Eingabe und Interpretation
    p01_value = st.number_input("Geben Sie den P0.1-Wert ein (in kPa):", min_value=0.0, max_value=1.0, step=0.01, format="%.2f")

    # PImax-Wert Eingabe
    pimax_value = st.number_input("Geben Sie den PImax-Wert ein (in kPa):", min_value=0.0, max_value=20.0, step=0.1, key='pimax_input')

    # Sofortige Interpretation der P0.1 und PImax Werte
    st.write(interpret_p01(p01_value))
    st.write(interpret_pimax(pimax_value, gender, age))

    # Interpretation des P0.1/PImax-Quotienten
    st.write(calculate_and_interpret_p01_pimax_ratio(p01_value, pimax_value))


# In[97]:


def Gasaustausch_Transferfaktor():
    st.header("Gasaustausch - Transferfaktor")
    
    st.write("Für die Lungenfunktionsbeurteilung ist die Diffusion der Atemgase neben der Ventilation entscheidend, klinisch gemessen durch den Transferfaktor (TLCO) der CO-Aufnahme ins Blut.")
    st.write("Gasaustauschvermögen zwischenventilierten Alveolarraum und dem erythrozytären Hämoglobin")
    
    # Erster Informationstext in einem ausklappbaren Bereich
    with st.expander("Basisinformationen:"):
        st.write("""
        - Bestimmung des Alveolarvolumens (VA) mittels Helium in Verbindung mit TLCO.
        - Bezeichnung des Verhältnisses als Transferkoeffizient oder Krogh-Index (TLCO/VA).
        - Kombination von TLCO und TLCO/VA differenziert zwischen Diffusions- und Verteilungsstörungen.
        - Deutlich verminderte TLCO im Vergleich zu TLCO/VA indiziert Verteilungsstörungen.
        - Compliance = dP/dV
        - Gleichsame Verminderung von TLCO und TLCO/VA deutet auf echte Reduktion des Transferfaktors hin.
        """)
        
    # Erster Informationstext in einem ausklappbaren Bereich
    with st.expander("Erweitert:"):
        st.write("""
        - Messung der TLCO erfasst unspezifisch auch pulmonale Durchblutung, alveoläre Membranleitfähigkeit und Hämoglobin-Reaktionsfähigkeit.
        - Bezeichnung "Diffusionskapazität (DLCO)" als ungenauer angesehen; "TLCO" wird bevorzugt.
        - Single-Breath-Methode als verbreitetstes Verfahren zur TLCO-Bestimmung; Werte als TLCOSB unterschieden.
        - Verfahren: Forcierte Inspiration eines Gasgemischs aus Kohlenmonoxid, Helium, Raumluft, gefolgt von 10 Sekunden Atemanhaltezeit und Analyse der Ausatemluft.
        - Höherer TLCO-Wert indiziert effektiveren CO-Transport aus der Ausatemluft in die Lunge.
        - Single Breath Methode ist bei starker Atemnot (Apnoezeit = 10 s) und sehr kleiner VS von < 1,5l nicht durchführbar
        - **Ursachen verminderte TLCO:** Interstitlelle Lungenerkrankungen wg. Dominanz des Membranfaktors: Verdickung der alveolo-kapillären-Membran, Verlust der Membranoberfläche, Ventilations-Perfusions-Verteilungsstörungen. Lungenemphysem und chronisch obstruktive Atemwegserkrankung. Lungenembolien wg. Verlust der Gasaustauschfläche. Nikotinkonsum (Erhöhung des HbCO).Anämie, Verlust von Hämoglobin.
        - **Ursachen erhöhter TLCO:** Alveoläre Hämorrhagie wg. der Bindung von CO an alveoläres Hb. Polycthaemie und Polyglobulie wg. vermehrter Bindung an kapilläres Hb. Pulmonale Rechts-Links-Shunts wg. vermehrter Bindung an kapillärem Hb.
        """)
        
    def diffusionskapazitaet_analyse(tlco_sb, tlco_va):
        befund = ""
        zusammenfassung = ""  # Variable für die Zusammenfassung

        if tlco_sb < 80:
            befund += "Eine reduzierte TLCO_SB weist auf eine eingeschränkte Diffusionskapazität hin. "
            if tlco_sb < 40:
                befund += "Dies deutet auf eine schwere Störung hin. "
                zusammenfassung += "**Schwere Diffusionsstörung.** "
            elif tlco_sb < 60:
                befund += "Dies deutet auf eine mittelschwere Störung hin. "
                zusammenfassung += "**Mittelschwere Diffusionsstörung.** "
            else:
                befund += "Dies deutet auf eine leichte Störung hin. "
                zusammenfassung += "**Leichte Diffusionsstörung.** "
        else:
            befund += "Die TLCO_SB liegt im normalen Bereich, was auf eine angemessene Diffusionskapazität hindeutet. "
            zusammenfassung += "**Normale Diffusionskapazität.** "

        if tlco_va < 80:
            befund += "Ein verminderter Transferkoeffizient (TLCO/VA) deutet auf eine Diffusionsstörung hin. "
            if tlco_va < tlco_sb:
                befund += "Dies spricht für das Vorliegen einer relevanten Verteilungsstörung. "
                zusammenfassung += "**Relevante Verteilungsstörung.** "
            elif tlco_va > tlco_sb:
                befund += "Dies weist auf eine primär durch die Membran bedingte Diffusionsstörung hin. "
                zusammenfassung += "**Primär membranbedingte Diffusionsstörung.** "
        else:
            befund += "Der Transferkoeffizient (TLCO/VA) liegt im normalen Bereich, was auf eine effektive Diffusionskapazität hinweist. "
            zusammenfassung += "**Effektive Diffusionskapazität.** "

        if tlco_sb < 80 and tlco_va < 80:
            befund += "Die gleichzeitige Verminderung von TLCO_SB und TLCO/VA deutet auf eine echte Reduktion des Transferfaktors hin. "
            zusammenfassung += "**Echte Reduktion des Transferfaktors.** "

        befund += "Um die Diffusionsstörung weiter einzugrenzen, sind zusätzliche Untersuchungen empfehlenswert. "
        befund += "Es ist wichtig, die Ergebnisse im Kontext weiterer klinischer Informationen zu interpretieren. "
        befund += "Die Diffusionskapazität gibt an, wie effektiv Gase zwischen Alveolen und dem Blut ausgetauscht werden. "

        # Kompakte Zusammenfassung des Befundes am Ende der Ausgabe
        kompakte_zusammenfassung = f"**Zusammenfassung:** {zusammenfassung}"

        return befund, kompakte_zusammenfassung

    # Eingabefelder für die Messwerte
    tlco_sb = st.number_input("TLCO_SB in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f")
    tlco_va = st.number_input("Transferkoeffizient (TLCO/VA) in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f")

        # Befund erstellen und anzeigen - Korrekter Ort für den Button und die Anzeige
    if st.button('Diffusionskapazität analysieren'):
        befund, kompakte_zusammenfassung = diffusionskapazitaet_analyse(tlco_sb, tlco_va)
        st.markdown(befund)
        st.markdown(kompakte_zusammenfassung)  # Ausgabe der kompakten Zusammenfassun


# In[130]:


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
    pH = st.number_input("pH-Wert:", value=7.40, format="%.2f")
    PaO2 = st.number_input("PaO2 in mmHg:", value=95.0, format="%.1f")
    PaCO2 = st.number_input("PaCO2 in mmHg:", value=40.0, format="%.1f")
    HCO3 = st.number_input("HCO3 in mEq/L:", value=24.0, format="%.1f")
    BE = st.number_input("Base Excess (BE) in mEq/L:", value=0.0, format="%.1f")
    Na = st.number_input("Na in mEq/L:", value=140.0, format="%.1f")
    K = st.number_input("K in mEq/L:", value=4.0, format="%.1f")
    Cl = st.number_input("Cl in mEq/L:", value=100.0, format="%.1f")
    Ca = st.number_input("Ca in mmol/L:", value=2.4, format="%.2f")
    
    if st.button("Analyse durchführen"):
        results = []
        
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
            
        detailed_diagnosis = "\n".join(results)
        st.markdown("### Befundergebnisse:")
        st.markdown(detailed_diagnosis)



# In[125]:


def Compliancemessung():
    st.header("Compliancemessung")
    
    st.write("Die Dehnbarkeit der Lunge, oder Lungencompliance, beschreibt über eine physikalische Kennzahl die elastischen Charakteristika der Lunge. Sie repräsentiert das Verhältnis zwischen der Änderung im Lungenvolumen und der damit verbundenen Druckänderung, gemessen in ml/mbar.")

    with st.expander("Basisinformationen:"):
        st.write("""
        - Erwachsene Lungencompliance: Circa 200 ml/cm H₂O für beide Lungen zusammen.
        - Die mechanischen Eigenschaften der Lunge, gemessen durch die pulmonale Compliance, verstärken sich mit Versteifung und schwächen ab bei Erschlaffung.
        - Bester Parameter zur Beurteilung restriktiver Ventilationsstörungen
        - Höchste Empfindlichkeit und gut Reproduzierbar
        - Compliance = dP/dV
        - Der transpulmonale Druck ist die Druckdifferenz zwischen Alveole und Pleuraspalt
        - Reziprokwert der Compliance ist die Elastance
        - Der Ösophagusdruck dient als Ersatz für den Pleuraspaltdruck bei Messungen, wobei sich der Alveolardruck dem Munddruck nach Angleichung anpasst.
        """)

    with st.expander("Erweitert:"):
        st.write("""
        - Untersuchungsdauer 30 Minuten
        - Vom Patienten als unangenehm empfundene Messung
        - Unabhängig von Mitarbeit des Patienten
        - Steife Lungen müssen hohe transpulmonale Druckänderungen für geforderte Volumenänderungen aufbringen. Daher Korrelation der Compliance mit Atemarbeit bei restriktiven Ventilationsstörungen. 
        """)

    with st.expander("Relevante Erkrankungen, die die Lungencompliance beeinflussen:"):
        st.write("""
        - **Emphysem oder COPD:** Verursacht durch genetische Faktoren oder äußere Einflüsse wie Rauchen; beschädigt die elastische Rückstellkraft der Lunge, was zu einer erhöhten Compliance führt.
        - **Pulmonale Fibrose:** Durch Umweltgifte, Chemikalien oder Infektionen verursacht; ersetzt elastische Fasern durch weniger elastische Kollagene, was die Compliance verringert.
        - **Neugeborenen-Atemnotsyndrom:** Fehlendes Surfactant bei Frühgeborenen führt zu verringerter Compliance und erhöhter Kollapsneigung der Lunge.
        - **Atelektase/ARDS:** Alveolarkollaps, häufig nach Operationen, verringert die Lungencompliance und erfordert höheren Druck für die Alveolenbelüftung.
        """)

      # Bilder als Platzhalter für interaktive Auswahl
    with st.columns(1)[0]:  # Direkter Zugriff auf das erste Element der Liste
        if st.button('Compliance'):
            st.session_state.selected_curve = 'Compliance'   
    
    if 'selected_curve' in st.session_state:
        if st.session_state.selected_curve == 'Compliance':
            st.image("compliance.jpg")
    
    eingabe_compliance = st.number_input("Geben Sie die Compliance in ml/cm H₂O ein:", value=200.0, step=1.0)

    if st.button('Compliance beurteilen', key='compliance_evaluate'):
        befund = beurteile_compliance(eingabe_compliance)
        st.write(befund)
        
def beurteile_compliance(eingabe_compliance):
    normal_min = 180.0  # Untergrenze des Normalbereichs in ml/cm H₂O
    normal_max = 220.0  # Obergrenze des Normalbereichs in ml/cm H₂O
    normal_mittelwert = (normal_min + normal_max) / 2
    abweichung_prozent = ((eingabe_compliance - normal_mittelwert) / normal_mittelwert) * 100

    if normal_min <= eingabe_compliance <= normal_max:
        befund = "Die eingegebene Compliance liegt im normalen Bereich."
        empfehlung = "Keine spezifischen Maßnahmen erforderlich."
    elif eingabe_compliance < normal_min:
        befund = "Die eingegebene Compliance ist niedriger als normal. Dies könnte auf eine restriktive Ventilationsstörung hinweisen."
        empfehlung = "Weitere diagnostische Abklärung empfohlen, um zugrunde liegende Ursachen wie pulmonale Fibrose oder Atelektase zu identifizieren."
    else:  # eingabe_compliance > normal_max
        befund = "Die eingegebene Compliance ist höher als normal. Dies könnte auf eine obstruktive Lungenerkrankung wie COPD oder Emphysem hinweisen."
        empfehlung = "Eine weiterführende Untersuchung zur Bestätigung der Diagnose und zur Einleitung einer geeigneten Behandlung wird empfohlen."

    return f"{befund}\n{empfehlung}"

# Hauptfunktion aufrufen
# Compliancemessung()

    st.markdown("[Mehr Informationen zur Compliance](https://www.ncbi.nlm.nih.gov/books/NBK538324/)")


# In[191]:


def main():
    # Benutzerdefiniertes CSS anwenden
    custom_css = """
    <style>
        /* Anpassungen für die Sidebar */
        .css-1d391kg { /* Ändert die Farbe des Titels */
            color: #333;
        }
        .stRadio > div{ /* Anpassung der Radiobuttons */
            background-color: #f0f2f6;
            border-radius: 20px;
            padding: 5px;
        }
    </style>
    """
    
    st.sidebar.title("🌬️ Analysebereiche - Lungenfunktion")
    analyse_bereich = st.sidebar.radio(
        "",
        ("Spirometrie qualitativ", "Spirometrie quantitativ", "Bodyplethysmographie - Residualvolumen", 
         "Bodyplethysmographie - Fluss-Druck-Kurve", "Funktionstests - Broncholyse", "Funktionstests - Provokation", 
         "Gasaustausch - Transferfaktor", "Gasaustausch - Blutgasanalyse","P0-Atemkraftmessung","Compliancemessung"),
        key="analysebereich_radio"
    )

    if analyse_bereich == "Spirometrie qualitativ":
        spirometrie_qualitativ()
    elif analyse_bereich == "Spirometrie quantitativ":
        tiffeneau_index_berechnung1()
    elif analyse_bereich == "Bodyplethysmographie - Residualvolumen":
        Bodyplethysmographie_Residualvolumen()
    elif analyse_bereich == "Bodyplethysmographie - Fluss-Druck-Kurve":
        Bodyplethysmographie_Fluss_Druck_Kurve()
    elif analyse_bereich == "Funktionstests - Broncholyse":
        Funktionstests_Broncholyse()
    elif analyse_bereich == "Funktionstests - Provokation":
        Funktionstests_Provokation()
    elif analyse_bereich == "Gasaustausch - Transferfaktor":
        Gasaustausch_Transferfaktor()
    elif analyse_bereich == "Gasaustausch - Blutgasanalyse":
        Gasaustausch_Blutgasanalyse()
    elif analyse_bereich == "P0-Atemkraftmessung":
        P0_Atemkraftmessung()    
    elif analyse_bereich == "Compliancemessung":
        Compliancemessung()

if __name__ == "__main__":
    main()
    
def main():
    st.sidebar.title("📊 Analysebereiche - Spiroergometrie")
    analyse_bereich = st.sidebar.radio(
        "",
        ("noch in Arbeit","xxx"),
        key="analysebereich_Spiroergometrie"
    )

    if analyse_bereich == "Spirometrie qualitativ":
        spirometrie_qualitativ()
    elif analyse_bereich == "Spirometrie quantitativ":
        tiffeneau_index_berechnung()

if __name__ == "__main__":
    main()
    
def main():
    st.sidebar.title("🩺 Analysebereiche - Rechtsherzkatheter")
    analyse_bereich = st.sidebar.radio(
        "",
        ("noch in Arbeit", "xxx"),
        key="analysebereich_Rechtsherzkatheter"
    )

    if analyse_bereich == "Spirometrie qualitativ":
        spirometrie_qualitativ()
    elif analyse_bereich == "Spirometrie quantitativ":
        tiffeneau_index_berechnung()


if __name__ == "__main__":
    main()
    
   # Versionsnummer und Datum in der Sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Version:** 1.6")
    st.sidebar.markdown("**Datum:** 2024-03-31")


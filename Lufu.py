#!/usr/bin/env python
# coding: utf-8

# In[16]:


import streamlit as st

# Hauptteil der App
st.title("Spirometrische Analyse")


# In[9]:


import streamlit as st

def spirometrie_qualitativ():
    st.header("Spirometrie qualitativ")
    
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

### Abschnitt Spiro Quantitativ


def graduiere_fev1_vc(fev1_prozent, vc_prozent):
    """
    Graduiert FEV1 und Vitalkapazität (VC) basierend auf den gegebenen Prozentwerten.
    """
    if fev1_prozent >= 70:
        grad_fev1 = "I (leicht)"
    elif 60 <= fev1_prozent < 70:
        grad_fev1 = "II (mäßig)"
    elif 50 <= fev1_prozent < 60:
        grad_fev1 = "III (mittelschwer)"
    elif 35 <= fev1_prozent < 50:
        grad_fev1 = "IV (schwer)"
    else:
        grad_fev1 = "Sehr schwer"

    if vc_prozent >= 70:
        grad_vc = "I (leicht)"
    elif 60 <= vc_prozent < 70:
        grad_vc = "II (mäßig)"
    elif 50 <= vc_prozent < 60:
        grad_vc = "III (mittelschwer)"
    elif 35 <= vc_prozent < 50:
        grad_vc = "IV (schwer)"
    else:
        grad_vc = "Sehr schwer"

    return grad_fev1, grad_vc

def graduiere_awr(awr_post_broncholyse):
    """
    Graduiert den Atemwegswiderstand (AWR) nach Broncholyse.
    """
    if awr_post_broncholyse < 170:
        return "I (leicht)"
    elif 170 <= awr_post_broncholyse <= 350:
        return "II (mittelschwer)"
    else:
        return "III (schwer)"
    
# Korrektur im Kontext der Befunderstellung
def befunderstellung(fev1_prozent, vc_prozent, awr_post_broncholyse):
    tiffeneau_index_vor = (fev1_prozent / vc_prozent) * 100
    grad_fev1, grad_vc = graduiere_fev1_vc(fev1_prozent, vc_prozent)
    grad_awr = graduiere_awr(awr_post_broncholyse)  # korrekte Zuweisung

def tiffeneau_index_berechnung():
    st.header("Lungenfunktionsprüfung - Detaillierter Befundbericht")

    # Erster Informationstext in einem ausklappbaren Bereich
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
    
    # Eingabe der Werte durch den Nutzer
    fev1_prozent = st.number_input("FEV1 (% vom Sollwert) vor Broncholyse:", value=100.0, format="%.2f")
    vc_prozent = st.number_input("Vitalkapazität (% vom Sollwert):", value=100.0, format="%.2f")
    fev1_prozent_post_broncholyse = st.number_input("FEV1 (% vom Sollwert) nach Broncholyse (optional):", value=0.0, format="%.2f")
    awr_post_broncholyse = st.number_input("Atemwegswiderstand nach Broncholyse (optional, in Pa/s):", value=0.0, format="%.2f")
    mef_25_prozent = st.number_input("MEF 25 (% vom Sollwert):", value=100.0, format="%.2f")

    # Speichern der Werte im Session State
    st.session_state['fev1_prozent'] = fev1_prozent
    st.session_state['vc_prozent'] = vc_prozent
    st.session_state['fev1_prozent_post_broncholyse'] = fev1_prozent_post_broncholyse
    st.session_state['awr_post_broncholyse'] = awr_post_broncholyse
    st.session_state['mef_25_prozent'] = mef_25_prozent

    # Berechnungen und initiale Befundung
    tiffeneau_index_vor = (fev1_prozent / vc_prozent) * 100
    grad_fev1, grad_vc = graduiere_fev1_vc(fev1_prozent, vc_prozent)

    befund_text = "### Befund:\n"
    
    # Unterscheidung zwischen Obstruktion und Restriktion
    if tiffeneau_index_vor < 80:
        befund_text += "Es liegt eine Obstruktion vor. Dies deutet auf eine Verengung der Atemwege hin, die den Luftstrom behindert. "
        if fev1_prozent_post_broncholyse > 0 and fev1_prozent_post_broncholyse != fev1_prozent:
            tiffeneau_index_post = (fev1_prozent_post_broncholyse / vc_prozent) * 100
            befund_text += "Nach Broncholyse zeigt sich "
            befund_text += "eine signifikante Verbesserung " if tiffeneau_index_post > tiffeneau_index_vor else "keine signifikante Veränderung "
            befund_text += "im Tiffeneau-Index, was auf "
            befund_text += "eine reversible " if tiffeneau_index_post > tiffeneau_index_vor else "eine potenziell chronische "
            befund_text += "Obstruktion hindeutet. "
            befund_text += f"Graduierung des AWR nach Broncholyse: {awr_post_broncholyse}. "
    else:
        befund_text += "Es liegt keine Obstruktion vor. Die normwertigen Tiffeneau-Index-Werte können auf eine Restriktion hinweisen, falls die VC vermindert ist. "

    # Spezifische Bedingungen und Empfehlungen
    if mef_25_prozent < 70 and fev1_prozent >= 70:
        befund_text += "Eine isolierte Erniedrigung des MEF 25 deutet auf eine Obstruktion der kleinen Atemwege hin, was spezifische Behandlungsansätze erfordern könnte. "

    # Graduierungen und weitere Diagnostik
    befund_text += f"\n**Graduierung von FEV1:** {grad_fev1}\n**Graduierung von VC:** {grad_vc}\n"
    
    
    befund_text += "\n### Weiterführende Empfehlungen:\n"
    if "Obstruktion" in befund_text:
        befund_text += "- Eine detaillierte Analyse mittels Spirometrie nach Broncholyse ist empfohlen, um das Ausmaß der Reversibilität zu bestimmen. "
        if "reversible" in befund_text:
            befund_text += "- Langwirksame Bronchodilatatoren könnten zur Behandlung in Betracht gezogen werden. "
        if "chronische" in befund_text:
            befund_text += "- Eine Überprüfung auf chronisch obstruktive Lungenerkrankung (COPD) ist angezeigt. "

        else:
            befund_text += "- Intensive Untersuchung auf chronisch obstruktive Lungenerkrankung (COPD) und mögliche schwerwiegende Obstruktionen. "
    if "Restriktion" in befund_text:
        befund_text += "- Eine Bodyplethysmografie kann zur Bestätigung einer restriktiven Lungenerkrankung und zur Beurteilung des Lungenvolumens hilfreich sein. "
    if "kleine Atemwege" in befund_text:
        befund_text += "- Eine hochauflösende Computertomographie (HRCT) der Lunge kann zur Untersuchung der kleinen Atemwege und zum Ausschluss weiterer Pathologien dienen. "

        
     # Verwendung von grad_awr im Kontext der Befunderstellung
    if fev1_prozent_post_broncholyse > 0 and fev1_prozent_post_broncholyse != fev1_prozent:
        # [Logik zur Verwendung von grad_awr]
        if awr_post_broncholyse == "I (leicht)" or awr_post_broncholyse == "II (mittelschwer)":
            befund_text += "- Überprüfung der Effektivität von Bronchodilatatoren zur Senkung des AWR. "
        else:
            befund_text += "- Intensive Untersuchung auf chronisch obstruktive Lungenerkrankung (COPD) und mögliche schwerwiegende Obstruktionen. "
    
    st.markdown(befund_text)



def Bodyplethysmographie_Residualvolumen():
    st.header("Bodyplethysmographie - Residualvolumen")
    
     # Erster Informationstext in einem ausklappbaren Bereich
    with st.expander("Basiswissen anzeigen"):
        st.write("""
        **Spirometrie erfasst ein- und ausatembare Volumina, nicht jedoch das Residualvolumen (RV).
        - **RV = Residualvolumen, das auch nach maximaler Ausatmung in der Lunge bleibt, ist nur durch Bodyplethysmographie messbar.
        - **Totale Lungenkapazität (TLC), funktionelle Residualkapazität (FRC), und thorakales Gasvolumen (TGV) inkludieren RV und werden ebenfalls nur mit Bodyplethysmographie bestimmt.
        - **Ein erhöhtes RV ist typisch für Emphysem (irreversibel) und Air Trapping (unter Broncholyse reversibel).
        - **Ein erniedrigtes RV weist auf Restriktion hin, bei der alle Volumina vermindert sind.
        - **„Kapazität“ bezeichnet ein aus verschiedenen Volumina zusammengesetztes Volumen, z.B. setzt sich die Vitalkapazität (VC) aus Atemzugvolumen, inspiratorischem Reservevolumen und exspiratorischem Reservevolumen zusammen. 
        """)
    
    # Zweiter Informationstext in einem ausklappbaren Bereich
    with st.expander("Informationstext 2 anzeigen"):
        st.write("""
        **Emphysem und Air Trapping führen oft zu erhöhtem Residualvolumen auf Kosten der Vitalkapazität.
        - **Die totale Lungenkapazität (TLC) ist bei Emphysem oft nur gering erhöht.
        - **Zur Bestimmung des Emphysemausmaßes wird der RV/TLC Quotient herangezogen.
        - **Eine Obstruktion und typische Sesselform in der Spirometrie deuten auf Emphysem hin; bestätigt durch Bodyplethysmographie.
        - **Bei erhöhtem Residualvolumen ist eine Broncholyse zur Unterscheidung zwischen Emphysem und Air Trapping indiziert, unabhängig von Obstruktion.
        - **Die funktionelle Residualkapazität (FRC) entspricht RV + ERV; sie bleibt bei normaler Atmung im Thorax und steht für den Gasaustausch zur Verfügung.
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
    
    # Eingabefelder für die Messwerte
    fev1_prozent = st.number_input("FEV1 (% vom Sollwert):", value=100.0, min_value=0.0, format="%.1f", key="fev1_prozent_2")
    rv = st.number_input("Residualvolumen (RV) in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f")
    tlc = st.number_input("Totale Lungenkapazität (TLC) in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f")
    tgv = st.number_input("Thorakales Gasvolumen (TGV) in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f")

    
    befund_text_bodyspleth = "### Befundbericht:\n"

    # Graduierung der Obstruktion basierend auf FEV1%
    grad_text = "Normalbefund"
    if fev1_prozent < 70:
        grad_text = "Grad I - Leichte Obstruktion"
        if fev1_prozent < 60:
            grad_text = "Grad II - Mäßige Obstruktion"
            if fev1_prozent < 50:
                grad_text = "Grad III - Mittelschwere Obstruktion"
                if fev1_prozent < 35:
                    grad_text = "Grad IV - Schwere Obstruktion"
                    if fev1_prozent < 30:
                        grad_text = "Grad V - Sehr schwere Obstruktion"
    
    befund_text_bodyspleth += f"Obstruktion: {grad_text}, basierend auf einem FEV1 von {fev1_prozent}% vom Soll.\n"

    # Detaillierte Bewertung von RV, TLC und TGV
    befund_text_bodyspleth += "\n**Detaillierte Bewertung:**\n"
    rv_bewertung = "leicht erhöht" if rv < 140 else "mittel" if rv <= 170 else "schwer"
    befund_text_bodyspleth += f"- Das Residualvolumen (RV) ist {rv_bewertung}, basierend auf einem Wert von {rv}% vom Soll.\n"
    tlc_bewertung = "leicht" if tlc < 130 else "mittel" if tlc <= 150 else "schwer"
    befund_text_bodyspleth += f"- Die Totale Lungenkapazität (TLC) wird als {tlc_bewertung} eingestuft, basierend auf einem Wert von {tlc}% vom Soll.\n"
    tgv_bewertung = "leicht" if tgv < 140 else "mittel" if tgv <= 170 else "schwer"
    befund_text_bodyspleth += f"- Das Thorakale Gasvolumen (TGV) wird als {tgv_bewertung} bewertet, basierend auf einem Wert von {tgv}% vom Soll.\n"

    
    # Berechnung des RV/TLC-Quotienten und Graduierung des Emphysems
    rv_tlc_quotient = rv / tlc
    emphysem_grad = "kein Emphysem"
    if rv_tlc_quotient >= 0.6:
        emphysem_grad = "Schweres Emphysem (> 60%)"
    elif rv_tlc_quotient >= 0.5:
        emphysem_grad = "Mittelschweres Emphysem (50% bis 60%)"
    elif rv_tlc_quotient >= 0.4:
        emphysem_grad = "Leichtes Emphysem (< 50%)"

    befund_text_bodyspleth += f"Der RV/TLC Quotient beträgt {rv_tlc_quotient*100:.2f}%, was auf ein {emphysem_grad} hindeutet.\n"

    # Abschließende Bewertung und Empfehlungen
    befund_text_bodyspleth += "\nBasierend auf den vorliegenden Messwerten empfehlen wir eine detaillierte klinische Bewertung sowie ggf. eine Broncholyse, um zwischen reversiblen und irreversiblen Lungenveränderungen zu differenzieren."

    st.markdown(befund_text_bodyspleth)



    
def Bodyplethysmographie_Fluss_Druck_Kurve():
    st.header("Bodyplethysmographie - Fluss-Druck-Kurve")
    
    st.write('Zur Bestimmung des Widerstandes wird der Munddruck gemessen. Dieser wird dann graphisch in der Fluss-Druck-Kurve (= Atemschleife) dargestellt. Es werden Fluss und Munddruck gegen das Verschiebevolumen aufgetragen, wodurch zwei Schleifen entstehen.')

    # Erster Informationstext in einem ausklappbaren Bereich
    with st.expander("Basisinformationen:"):
        st.write("""
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

def main():
    st.sidebar.title("Analysebereiche - Lungenfunktion")
    analyse_bereich = st.sidebar.radio(
        "",
        ("Spirometrie qualitativ", "Spirometrie quantitativ", "Bodyplethysmographie - Residualvolumen", 
         "Bodyplethysmographie - Fluss-Druck-Kurve", "Funktionstests - Broncholyse", "Funktionstests - Provokation", 
         "Gasaustausch - Transferfaktor", "Gasaustausch - Blutgasanalyse","P0-Atemkraftmessung"),
        key="analysebereich_radio"
    )

    if analyse_bereich == "Spirometrie qualitativ":
        spirometrie_qualitativ()
    elif analyse_bereich == "Spirometrie quantitativ":
        tiffeneau_index_berechnung()
    elif analyse_bereich == "Bodyplethysmographie - Residualvolumen":
        Bodyplethysmographie_Residualvolumen()
    elif analyse_bereich == "Bodyplethysmographie - Fluss-Druck-Kurve":
        Bodyplethysmographie_Fluss_Druck_Kurve()

if __name__ == "__main__":
    main()
    
def main():
    st.sidebar.title("Analysebereiche - Spiroergometrie")
    analyse_bereich = st.sidebar.radio(
        "",
        ("noch in Arbeit","xxx"),
        key="analysebereich_Spiroergometrie"
    )

    if analyse_bereich == "Spirometrie qualitativ":
        spirometrie_qualitativ()
    elif analyse_bereich == "Spirometrie quantitativ":
        tiffeneau_index_berechnung()
    elif analyse_bereich == "Bodyplethysmographie - Residualvolumen":
        Bodyplethysmographie_Residualvolumen()
    elif analyse_bereich == "Bodyplethysmographie - Fluss-Druck-Kurve":
        Bodyplethysmographie_Fluss_Druck_Kurve()

if __name__ == "__main__":
    main()
    
def main():
    st.sidebar.title("Analysebereiche - Rechtsherzkatheter")
    analyse_bereich = st.sidebar.radio(
        "",
        ("noch in Arbeit", "xxx"),
        key="analysebereich_Rechtsherzkatheter"
    )

    if analyse_bereich == "Spirometrie qualitativ":
        spirometrie_qualitativ()
    elif analyse_bereich == "Spirometrie quantitativ":
        tiffeneau_index_berechnung()
    elif analyse_bereich == "Bodyplethysmographie - Residualvolumen":
        Bodyplethysmographie_Residualvolumen()
    elif analyse_bereich == "Bodyplethysmographie - Fluss-Druck-Kurve":
        Bodyplethysmographie_Fluss_Druck_Kurve()

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





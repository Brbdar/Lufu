#!/usr/bin/env python
# coding: utf-8

# In[21]:


import streamlit as st

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
        
    # Zweiter Informationstext in einem ausklappbaren Bereich
    with st.expander("Fehlermöglichkeiten bei Beurteilung"):
        st.write("""
        - Lungenfibrose: sReff normal, vermindertes FRCpleth führt zu numerisch hohem Reff, suggeriert fälschlich Obstruktion.
        - Adipöse Patienten: Atemmittellage nahe RV, vorzeitiger Verschluss kleiner Atemwege bei Exspiration, erhöhter Reff, „dreieckige“ Form der Atemschleife. Anhebung zur TLC normalisiert Widerstand.
        - Lungenemphysem: sReff stark erhöht, hohes FRCpleth lässt Reff niedrig oder normal erscheinen, täuscht Normalität vor.
        """)


    st.write("""
    Die Bodyplethysmographie ermöglicht es uns, präzise das Residualvolumen (RV), die totale Lungenkapazität (TLC) und das thorakale Gasvolumen (TGV) zu messen. Diese Messungen sind entscheidend, um das Vorhandensein und das Ausmaß von Zuständen wie Emphysem und Air Trapping zu beurteilen.
    """)

    # Benutzereingaben für Verdachtsmomente
    fibrose_verdacht = st.checkbox("Verdacht auf Lungenfibrose?")
    adipositas_verdacht = st.checkbox("Verdacht auf Adipositas?")
    emphysem_verdacht = st.checkbox("Verdacht auf Lungenemphysem?")

    # Interpretation des Atemwegswiderstands
    def interpretiere_reff(fibrose_verdacht, adipositas_verdacht, emphysem_verdacht):
        interpretationen = []
        if fibrose_verdacht:
            interpretationen.append("Achtung: Normaler sReff bei Lungenfibrose könnte eine Obstruktion vortäuschen.")
        if adipositas_verdacht:
            interpretationen.append("Achtung: Erhöhter Reff bei Adipositas könnte einen vorzeitigen Verschluss kleiner Atemwege anzeigen.")
        if emphysem_verdacht:
            interpretationen.append("Achtung: Ein normaler oder niedriger Reff bei Lungenemphysem täuscht eine nicht vorhandene Normalität vor.")
        if not interpretationen:
            interpretationen.append("Keine spezifischen Risiken identifiziert.")
        return " ".join(interpretationen)

    # Funktion zur Bewertung des Atemwegswiderstands und möglicher Hindernisse
    def bewerte_awr_und_hindernisse(Reff_post_broncholyse):
        if Reff_post_broncholyse < 170:
            return "Normal", "Kein Hinweis auf signifikantes Strömungshindernis."
        elif 170 <= Reff_post_broncholyse <= 350:
            return "Erhöht", "Möglicherweise intrathorakales Strömungshindernis."
        else:
            return "Deutlich erhöht", "Möglicherweise extrathorakales Strömungshindernis."

    # Funktion zur Bewertung des Schweregrads basierend auf Prozentwerten
    def grad_bewertung(wert, niedrig, mittel):
        if wert < niedrig:
            return "leicht erhöht"
        elif niedrig <= wert <= mittel:
            return "mittel"
        else:
            return "schwer"

    # Berechnung der prozentualen Veränderung
    def berechne_prozentuale_veraenderung(vorher, nachher):
        if vorher == 0:
            return 0  # Verhindert Division durch Null
        return ((nachher - vorher) / vorher) * 100

    # Eingabefelder für die Messwerte
    FRCpleth = st.number_input("Funktionelle Residualkapazität in Prozent vom Sollwert (FRCpleth):", value=100.0, min_value=0.0, format="%.1f")
    Reff_vor_broncholyse = st.number_input("Atemwegswiderstand (Reff in Pa/s):", value=0.0, format="%.2f")
    tlc_absolut = st.number_input("Totale Lungenkapazität (TLC in Liter):", value=6.0, min_value=0.0, format="%.1f")
    rv_absolut = st.number_input("Residualvolumen (RV in Liter):", value=1.5, min_value=0.0, format="%.1f")
    rv = st.number_input("Residualvolumen (RV) in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f")
    tlc = st.number_input("Totale Lungenkapazität (TLC) in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f")
    tgv = st.number_input("Thorakales Gasvolumen (TGV) in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f")
    FEV1_pre = st.number_input("FEV1 vor Broncholyse (optional, in Pa/s):", value=100.0, min_value=0.0, format="%.1f")
    FEV1_post = st.number_input("FEV1 nach Broncholyse (optional, in Pa/s):", value=100.0, min_value=0.0, format="%.1f")
    Reff_post_broncholyse = st.number_input("Atemwegswiderstand nach Broncholyse (optional, in Pa/s):", value=0.0, format="%.2f")

    # Berechnungen und Zusammenstellung des Befundberichts
    Reff_interpretation = interpretiere_reff(fibrose_verdacht, adipositas_verdacht, emphysem_verdacht)
    Reff_bewertung, hindernis_typ = bewerte_awr_und_hindernisse(Reff_post_broncholyse)
    rv_bewertung = grad_bewertung(rv, 140, 170)
    tlc_bewertung = grad_bewertung(tlc, 130, 150)
    tgv_bewertung = grad_bewertung(tgv, 140, 170)
    rv_tlc_quotient = rv_absolut / tlc_absolut

    emphysem_grad = "kein Emphysem"
    if rv_tlc_quotient >= 0.6:
        emphysem_grad = "Schweres Emphysem (> 60%)"
    elif rv_tlc_quotient >= 0.5:
        emphysem_grad = "Mittelschweres Emphysem (50% bis 60%)"
    elif rv_tlc_quotient >= 0.4:
        emphysem_grad = "Leichtes Emphysem (< 50%)"

    pseudorestriktive_stoerung = rv > 120 and tlc >= 80
    Reff_veraenderung_prozent = berechne_prozentuale_veraenderung(Reff_vor_broncholyse, Reff_post_broncholyse)
    FEV1_veraenderung_prozent = berechne_prozentuale_veraenderung(FEV1_pre, FEV1_post)
    FEV1_post_prozent = (FEV1_post / FEV1_pre) * 100

    # Zusammenstellung des Befundberichts
    befund_text = f"### Vorsicht bei der Interpretation des Atemwegswiderstands:\n{Reff_interpretation}\n\n### Befundbericht:\n"
    if pseudorestriktive_stoerung:
        befund_text += "**Pseudorestriktive Störung:** Bei Überblähung und normaler TLC, aber reduzierter ventilierbarer Volumina, handelt es sich nicht um eine echte Restriktion, sondern um eine pseudorestriktive Störung durch Überblähung.\n"
    befund_text += f"\n- Das Residualvolumen (RV) ist {rv_bewertung}, basierend auf einem Wert von {rv}% vom Soll.\n"
    befund_text += f"- Die Totale Lungenkapazität (TLC) wird als {tlc_bewertung} eingestuft, basierend auf einem Wert von {tlc}% vom Soll.\n"
    befund_text += f"- Das Thorakale Gasvolumen (TGV) wird als {tgv_bewertung} bewertet, basierend auf einem Wert von {tgv}% vom Soll.\n"

    if emphysem_grad != "kein Emphysem":
        befund_text += f"\n**Emphysem Grad:** {emphysem_grad}\n"
    if Reff_veraenderung_prozent != 0:
        befund_text += f"\n**Veränderung des Atemwegswiderstands nach Broncholyse:** {Reff_veraenderung_prozent:.2f}%\n"
    if FEV1_veraenderung_prozent != 0:
        befund_text += f"\n**Veränderung des FEV1 nach Broncholyse:** {FEV1_veraenderung_prozent:.2f}%\n"

    # Anzeige des Befundberichts
    st.markdown(befund_text)
    
    # Ergänzende pathophysiologische Analyse
    def pathophysiologische_analyse(rv, tlc, tgv, FEV1_pre, FEV1_post, Reff_vor_broncholyse, Reff_post_broncholyse):
        ergebnisse = []

        # Analyse der Lungenüberblähung
        if tgv > 120:
            ergebnisse.append("Eine Erhöhung des thorakalen Gasvolumens (TGV) über 120% des Sollwerts deutet auf eine Lungenüberblähung hin. Dies kann auf eine obstruktive Lungenerkrankung wie das Emphysem zurückzuführen sein, bei der eine Zerstörung der Alveolarwände zu einer permanenten Erweiterung der Luftwege führt.")

        # Erkennung restriktiver Muster
        if tlc < 80:
            ergebnisse.append("Eine reduzierte totale Lungenkapazität (TLC) unter 80% des Sollwerts kann auf eine restriktive Ventilationsstörung hinweisen. Dies ist charakteristisch für Erkrankungen, die die Ausdehnung der Lunge beschränken, wie Lungenfibrose, bei der das Lungengewebe vernarbt und steif wird.")

        # Beurteilung der Reversibilität von Atemwegsobstruktionen
        if Reff_post_broncholyse < Reff_vor_broncholyse and FEV1_post > FEV1_pre:
            prozentuale_veraenderung_FEV1 = ((FEV1_post - FEV1_pre) / FEV1_pre) * 100
            ergebnisse.append(f"Ein Rückgang des Atemwegswiderstands (Reff) nach Broncholyse zusammen mit einer Verbesserung des FEV1 um {prozentuale_veraenderung_FEV1:.2f}% deutet auf eine teilweise reversible Atemwegsobstruktion hin. Dies ist ein Indiz für das Vorliegen einer obstruktiven Lungenerkrankung, bei der bronchodilatatorische Medikamente die Atemwegsobstruktion verringern können.")

        # Überprüfung auf Emphysem und Air Trapping
        if rv / tlc > 0.4:
            ergebnisse.append("Ein erhöhtes Verhältnis von Residualvolumen (RV) zu totaler Lungenkapazität (TLC) weist auf Air Trapping und möglicherweise auf ein Emphysem hin. Beide Zustände sind charakteristisch für chronisch obstruktive Lungenerkrankungen (COPD), bei denen es zu einer Beeinträchtigung des Luftstroms kommt.")

        # Fazit
        if not ergebnisse:
            return "Die pathophysiologische Analyse ergab keine spezifischen Auffälligkeiten basierend auf den eingegebenen Messwerten."
        return "Pathophysiologische Analyseergebnisse:\n" + "\n".join(ergebnisse)

    # Beispielaufruf der Funktion
    patho_ergebnisse = pathophysiologische_analyse(rv, tlc, tgv, FEV1_pre, FEV1_post, Reff_vor_broncholyse, Reff_post_broncholyse)
    st.markdown(patho_ergebnisse)


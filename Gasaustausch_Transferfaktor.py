#!/usr/bin/env python
# coding: utf-8

# In[25]:


import streamlit as st

def Gasaustausch_Transferfaktor():
   
    
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


    def Gasaustausch_Transferfaktor():
         st.header("Gasaustausch - Transferfaktor")
        

    tlco_sb = st.number_input("TLCO_SB in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f", key="tlco_sb")
    tlco_va = st.number_input("Transferkoeffizient (TLCO/VA) in Prozent vom Sollwert:", value=100.0, min_value=0.0, format="%.1f", key="tlco_va")
    tiffeneau = st.checkbox("Pathologischer Tiffeneau-Index?", key="tiffeneau")
    vc_reduziert = st.checkbox("Reduzierte Vitalkapazität (VC)?", key="vc_reduziert")
    tlc_reduziert = st.checkbox("Reduzierte Totale Lungenkapazität (TLC)?", key="tlc_reduziert")

    def diffusionskapazitaet_analyse(tlco_sb, tlco_va, tiffeneau, vc_reduziert, tlc_reduziert):
        LLN = 60
        befund = ""
        zusammenfassung = "**Zusammenfassung:** "

        if tlco_sb < 80:
            befund += f"Mit einem TLCO_SB-Wert von {tlco_sb}% liegt eine signifikante Einschränkung der Diffusionskapazität vor, "
            if tlco_sb < 40:
                befund += "was auf eine schwere Beeinträchtigung des Gasaustausches hinweist. "
                zusammenfassung += "**Schwere Diffusionsstörung.** "
                befund += "Solch niedrige Werte sind oft mit fortgeschrittenen Lungenerkrankungen wie einer schweren Fibrose oder einer ausgedehnten Emphysemerkrankung verbunden. "
            elif tlco_sb < 60:
                befund += "die eine mittelschwere Störung des Gasaustausches anzeigt. "
                zusammenfassung += "**Mittelschwere Diffusionsstörung.** "
                befund += "Diese Werte können bei verschiedenen Lungenerkrankungen auftreten, die eine teilweise Einschränkung des Gasaustausches verursachen, wie z.B. mäßige Fibrose oder frühe Stadien eines Emphysems. "
            else:
                befund += "und deutet auf eine leichte Beeinträchtigung hin. "
                zusammenfassung += "**Leichte Diffusionsstörung.** "
                befund += "Leichte Abweichungen können auf frühe oder milde Formen von Lungenerkrankungen hinweisen oder temporäre Zustände reflektieren, die eine genauere Überwachung erfordern. "
        else:
            befund += "Die TLCO_SB-Werte liegen im normalen Bereich, was auf eine normale Diffusionskapazität schließen lässt. "
            zusammenfassung += "**Normale Diffusionskapazität.** "

        if tlco_va < 80:
            befund += "Ein verminderter Transferkoeffizient (TLCO/VA) gibt Hinweise auf spezifische Diffusionsprobleme. "
            if tlco_va < tlco_sb:
                befund += "Dies könnte auf eine Verteilungsstörung innerhalb der Lunge hinweisen, die bei Verteilungs- oder Ventilations-Perfusions-Mismatch auftreten kann. "
                zusammenfassung += "**Verteilungsstörung festgestellt.** "
            elif tlco_va > tlco_sb:
                befund += "Dies deutet auf eine primär durch die Membran bedingte Diffusionsstörung hin, "
                zusammenfassung += "**Membranbedingte Diffusionsstörung.** "
                befund += "was typischerweise bei Erkrankungen auftritt, die die alveolokapilläre Membran direkt betreffen, wie interstitielle Lungenerkrankungen oder Fibrose. "
        else:
            befund += "Der Transferkoeffizient (TLCO/VA) liegt im normalen Bereich und weist auf eine effektive Gasaustauschkapazität hin. "

        befund += "\n**Beurteilung basierend auf TLCO, Tiffeneau-Index, VC und TLC:**\n"
        if not tiffeneau and not vc_reduziert and tlco_sb >= LLN:
            befund += "Ein normaler Befund ohne Hinweise auf pulmonale Gefäßerkrankungen. "
        elif not tiffeneau and vc_reduziert and tlco_sb < LLN:
            befund += "Mögliche Restriktion weist auf eine interstitielle Lungenerkrankung oder Fibrose hin. Eine genauere Diagnostik, wie z.B. eine hochauflösende CT (HRCT) der Lunge, könnte zur weiteren Abklärung beitragen. "
        elif tiffeneau and tlco_sb >= LLN:
            befund += "Eine obstruktive Ventilationsstörung ohne Diffusionsdefizit könnte auf Zustände wie Asthma oder chronische Bronchitis hinweisen. "
        elif tiffeneau and tlco_sb < LLN:
            befund += "Eine Kombination aus obstruktiver Störung und reduzierter TLCO deutet möglicherweise auf ein Emphysem hin, bei dem sowohl die Atemwege als auch der Gasaustausch beeinträchtigt sind. "

        return befund, zusammenfassung

    if st.button('Diffusionskapazität analysieren'):
        befund, zusammenfassung = diffusionskapazitaet_analyse(tlco_sb, tlco_va, tiffeneau, vc_reduziert, tlc_reduziert)
        st.markdown(befund)
        st.markdown(zusammenfassung)



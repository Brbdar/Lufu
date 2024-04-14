#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


st.set_page_config(
    page_title="Pneumo-App",
    layout="wide",
    initial_sidebar_state="expanded")


# Copyright text in small font
st.caption("© Bruno Brito da Rocha 2024")


# In[ ]:


from spirometrie_qualitativ import spirometrie_qualitativ


# In[ ]:


from tiffeneau_index_berechnung import tiffeneau_index_berechnung1


# In[ ]:


from Bodyplethysmographie_Residualvolumen import Bodyplethysmographie_Residualvolumen


# In[ ]:


from Bodyplethysmographie_Fluss_Druck_Kurve import Bodyplethysmographie_Fluss_Druck_Kurve


# In[ ]:


from Funktionstests_Broncholyse import Funktionstests_Broncholyse


# In[ ]:


from Funktionstests_Provokation import Funktionstests_Provokation


# In[ ]:


from P0_Atemkraftmessung import P0_Atemkraftmessung


# In[ ]:


from Gasaustausch_Transferfaktor import Gasaustausch_Transferfaktor


# In[ ]:


from Gasaustausch_Blutgasanalyse import Gasaustausch_Blutgasanalyse


# In[ ]:


from Compliancemessung import Compliancemessung


# In[ ]:


from LTOT import LTOT


# In[ ]:


from EKG import EKG


# In[ ]:


from Klinik import Klinik


# In[ ]:


from HFpEF_Score import HFpEF_Score


# In[ ]:


from COPD_Score import COPD_Score


# In[ ]:


from Blutkultur import Blutkultur


# In[ ]:


from chadsvascore import chadsvascore


# In[ ]:


from erguss1 import erguss1


# In[ ]:


from rhkbefund import rhkbefund


# In[ ]:


from rfi import rfi


# In[ ]:


from ane1 import ane1 


# In[ ]:


from ruleout import ruleout


# In[ ]:


from raai import raai


# In[ ]:


from embo import embo


# In[ ]:


# Multiselect Box für die Auswahl der Seiten
selected_pages_lufu = st.multiselect("Wählen Sie eine oder mehrere Seiten aus dem Bereich **Lungenfunktion** aus:",
                                ["Spirometrie qualitativ", "Spirometrie quantitativ", "Bodyplethysmographie - Residualvolumen",
                                "Bodyplethysmographie - Fluss-Druck-Kurve", "Funktionstests - Broncholyse", "Funktionstests - Provokation",
                                "Gasaustausch - Transferfaktor", "Gasaustausch - Blutgasanalyse", "P0-Atemkraftmessung",
                                "Compliancemessung", "LTOT - Algorithmus"], key="lufu")

# Logik zur Anzeige der ausgewählten Seiten
if 'Spirometrie Qualitativ' in selected_pages_lufu:
    spirometrie_qualitativ()
if 'Spirometrie quantitativ' in selected_pages_lufu:
    tiffeneau_index_berechnung1()
if "Bodyplethysmographie - Residualvolumen" in selected_pages_lufu:
    Bodyplethysmographie_Residualvolumen()
if "Bodyplethysmographie - Fluss-Druck-Kurve" in selected_pages_lufu:
    Bodyplethysmographie_Fluss_Druck_Kurve()
if "Funktionstests - Broncholyse" in selected_pages_lufu:
    Funktionstests_Broncholyse()
if "Funktionstests - Provokation" in selected_pages_lufu:
    Funktionstests_Provokation()
if "Gasaustausch - Transferfaktor" in selected_pages_lufu:
    Gasaustausch_Transferfaktor()
if "Gasaustausch - Blutgasanalyse" in selected_pages_lufu:
    Gasaustausch_Blutgasanalyse()
if "P0-Atemkraftmessung" in selected_pages_lufu:
    P0_Atemkraftmessung()
if "Compliancemessung" in selected_pages_lufu:
    Compliancemessung()
if "LTOT - Algorithmus" in selected_pages_lufu:
    LTOT()

selected_pages_spiro = st.multiselect("Wählen Sie eine oder mehrere Seiten aus dem Bereich **Spiroergometrie** aus:",
                                ["XXX", "XXX"], key="Spiroergo")

selected_pages_ph = st.multiselect("Wählen Sie eine oder mehrere Seiten aus dem Bereich **PH Diagnostik** aus:",
                                ["EKG", "Klinik", "Thorax-Röntgen", "Lungenfunktion und arterielle Gase","der RHK Befund"], key="pulmonalehypertonie")

if "EKG" in selected_pages_ph:
    EKG()
if "Klinik" in selected_pages_ph:
    Klinik()
if "Thorax Röntgen" in selected_pages_ph:
    Thorax_roentgen()
if "Lungenfunktion und Blutgase" in selected_pages_ph:
    Lufu_BGA()   
if "der RHK Befund" in selected_pages_ph:
    rhkbefund()

selected_pages_copd = st.multiselect("Wählen Sie eine oder mehrere Seiten aus dem Bereich **COPD** aus:",
                                ["COPD Score"], key="COPD")

if "COPD Score" in selected_pages_copd:
    COPD_Score()

selected_pages_ane = st.multiselect("Wählen Sie eine oder mehrere Seiten aus dem Bereich **Anämie** aus:",
                                ["Mikrozytäre Anämie"], key="Anämie")

if "Mikrozytäre Anämie" in selected_pages_ane:
    ane1()

selected_pages_scores = st.multiselect("Wählen Sie eine oder mehrere Seiten aus dem Bereich **Scores & Algorithmen** aus:",
                                ["HFpEF Score", "Blutkultur","Blutungs vs. Thrombose","Pleuraerguss","Renal Failure Index","Rule out ACS","RV Diastole","Verdacht auf Lungenembolie"], key="Scores")

if "HFpEF Score" in selected_pages_scores:
    HFpEF_Score()
if "RV Diastole" in selected_pages_scores:
    raai()
if "Blutkultur" in selected_pages_scores:
    Blutkultur()
if "Blutungs vs. Thrombose" in selected_pages_scores:
    chadsvascore()
if "Pleuraerguss" in selected_pages_scores:
    erguss1()
if "Renal Failure Index" in selected_pages_scores:
    rfi()
if "Rule out ACS" in selected_pages_scores:
    ruleout()
if "Verdacht auf Lungenembolie" in selected_pages_scores:
    embo()


with st.expander("Rechtlicher Hinweis"):

    st.write("""
        **Offizieller rechtlicher Hinweis**

        Diese Anwendung beinhaltet klinische Werkzeuge und Inhalte, die für die Nutzung durch medizinisches Fachpersonal vorgesehen sind. Diese Werkzeuge stellen keine professionelle Beratung dar; Ärzte und anderes medizinisches Fachpersonal, die diese Werkzeuge nutzen, sollten ihr eigenes klinisches Urteil in Bezug auf die von ihnen bereitgestellten Informationen ausüben. Nicht-medizinische Nutzer, die diese Werkzeuge verwenden, tun dies auf eigenes Risiko. Personen mit jeglichen medizinischen Bedingungen wird ausdrücklich geraten, professionellen medizinischen Rat einzuholen, bevor sie irgendeine Art von Gesundheitsbehandlung beginnen. Bei medizinischen Anliegen, einschließlich Entscheidungen über Medikamente und andere Behandlungen, sollten nicht-medizinische Nutzer immer ihren Arzt oder einen anderen qualifizierten Gesundheitsdienstleister konsultieren.

        Die Inhaltsentwickler haben sorgfältig versucht, die Inhalte gemäß den Standards der professionellen Praxis zu gestalten, die zum Zeitpunkt der Entwicklung herrschten. Dennoch ändern sich Standards und Praktiken in der Medizin, da neue Daten verfügbar werden, und der einzelne medizinische Fachmann sollte eine Vielzahl von Quellen konsultieren.

        Die Inhalte dieser Anwendung, wie Texte, Grafiken und Bilder, dienen nur zu Informationszwecken. Es wird keine spezifische Empfehlung oder Befürwortung für bestimmte Tests, Ärzte, Produkte, Verfahren, Meinungen oder andere auf der Plattform erwähnte Informationen ausgesprochen.

        Obwohl die Informationen aus Quellen stammen, die als zuverlässig erachtet werden, wird weder die Genauigkeit der Informationen auf dieser Plattform noch von unseren Inhaltsanbietern garantiert.

        Wir erteilen keine medizinischen Ratschläge, noch bieten wir medizinische oder diagnostische Dienstleistungen an. Medizinische Informationen ändern sich schnell. Weder wir noch unsere Inhaltsanbieter garantieren, dass die Inhalte alle möglichen Anwendungen, Anweisungen, Vorsichtsmaßnahmen, Wechselwirkungen mit Medikamenten oder Nebenwirkungen, die mit therapeutischen Behandlungen verbunden sein können, abdecken.

        Die Nutzung der Informationen und Inhalte, die Sie durch diese Plattform erhalten, erfolgt ausschließlich auf Ihr eigenes Risiko. Weder wir noch unsere Inhaltsanbieter übernehmen irgendeine Haftung oder Verantwortung für Schäden oder Verletzungen (einschließlich Tod) an Ihnen, anderen Personen oder Eigentum, die aus der Nutzung von Produkten, Informationen, Ideen oder Anweisungen resultieren, die in den bereitgestellten Inhalten oder Diensten an Sie vermittelt werden.
        """)

# Fügen Sie weitere Bedingungen für jede Auswahlmöglichkeit hinzu



# In[ ]:


def setup_sidebar():
    # Titel und Auswahl für den Bereich Lungenfunktion
    st.sidebar.title("🌬️ Analysebereiche - Lungenfunktion")
    analyse_bereich_lungenfunktion = st.sidebar.multiselect(
        "Wählen Sie die gewünschten Lungenfunktionstests:",
        [
            "Spirometrie qualitativ", "Spirometrie quantitativ", "Bodyplethysmographie - Residualvolumen",
            "Bodyplethysmographie - Fluss-Druck-Kurve", "Funktionstests - Broncholyse", "Funktionstests - Provokation",
            "Gasaustausch - Transferfaktor", "Gasaustausch - Blutgasanalyse", "P0-Atemkraftmessung",
            "Compliancemessung", "LTOT - Algorithmus"
        ],
        key="analysebereich_lungenfunktion"
    )
    process_selection(analyse_bereich_lungenfunktion)

    # Bereich Spiroergometrie
    st.sidebar.title("🚴🏼‍♂️ Spiroergometrie")
    analyse_bereich_spiroergometrie = st.sidebar.multiselect(
        "Wählen Sie relevante Tests für Spiroergometrie:",
        ["Belastungstest", "VO2max Analyse"],  # Aktualisierte Platzhalterwerte
        key="analysebereich_spiroergometrie"
    )
    process_selection(analyse_bereich_spiroergometrie)

    # Bereich pulmonale Hypertonie
    st.sidebar.title("🫀 Detect Algorithmus - pulmonale Hypertonie")
    analyse_bereich_rechtsherzkatheter = st.sidebar.multiselect(
        "Wählen Sie Tests für die Diagnose von pulmonaler Hypertonie:",
        [
            "EKG", "Klinik", "Thorax-Röntgen", "Lungenfunktion und arterielle Gase", "der RHK Befund"
        ],
        key="analysebereich_rechtsherzkatheter"
    )
    process_selection(analyse_bereich_rechtsherzkatheter)

    # Bereich COPD
    st.sidebar.title("COPD")
    analyse_bereich_COPD = st.sidebar.multiselect(
        "Wählen Sie Tests für COPD:",
        ["COPD Score"],
        key="analysebereich_COPD"
    )
    process_selection(analyse_bereich_COPD)

    # Bereich Anämie
    st.sidebar.title("Anämie")
    analyse_bereich_Anämie = st.sidebar.multiselect(
        "Wählen Sie Tests für Anämie:",
        ["Mikrozytäre Anämie"],
        key="analysebereich_Anämie"
    )
    process_selection(analyse_bereich_Anämie)

    # Bereich Scores und Algorithmen
    st.sidebar.title("Scores und Algorithmen")
    analyse_bereich_scores = st.sidebar.multiselect(
        "Wählen Sie relevante Scores und Algorithmen:",
        ["HFpEF Score", "Blutkultur", "Blutungs vs. Thrombose", "Pleuraerguss", "Renal Failure Index", "Rule out ACS", "RV Diastole", "Verdacht auf Lungenembolie"],
        key="analysebereich_scores"
    )
    process_selection(analyse_bereich_scores)

    # Trennlinie und Information über die Version
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Version:** 2")
    st.sidebar.markdown("**Datum:** 2024-04-13")
    st.sidebar.markdown("---")

def process_selection(selection):
    # Fügen Sie hier die Logik zum Aufrufen von Funktionen basierend auf der Auswahl hinzu
    if "Spirometrie qualitativ" in selection:
        spirometrie_qualitativ()
    if "Spirometrie quantitativ" in selection:
        tiffeneau_index_berechnung1()
    if "Bodyplethysmographie - Residualvolumen" in selection:
        Bodyplethysmographie_Residualvolumen()
    if "Bodyplethysmographie - Fluss-Druck-Kurve" in selection:
        Bodyplethysmographie_Fluss_Druck_Kurve()
    if "Funktionstests - Broncholyse" in selection:
        Funktionstests_Broncholyse()
    if "Funktionstests - Provokation" in selection:
        Funktionstests_Provokation()
    if "Gasaustausch - Transferfaktor" in selection:
        Gasaustausch_Transferfaktor()
    if "Gasaustausch - Blutgasanalyse" in selection:
        Gasaustausch_Blutgasanalyse()
    if "P0-Atemkraftmessung" in selection:
        P0_Atemkraftmessung()
    if "Compliancemessung" in selection:
        Compliancemessung()
    if "LTOT - Algorithmus" in selection:
        LTOT()
    if "EKG" in selection:
        EKG()
    if "Klinik" in selection:
        Klinik()
    if "Thorax Röntgen" in selection:
        Thorax_roentgen()
    if "Lungenfunktion und Blutgase" in selection:
        Lufu_BGA()
    if "HFpEF Score" in selection:
        HFpEF_Score()
    if "Blutkultur" in selection:
        Blutkultur()
    if "COPD Score" in selection:
        COPD_Score()
    if "Blutungs vs. Thrombose" in selection:
        chadsvascore()
    if "Pleuraerguss" in selection:
        erguss1()
    if "der RHK Befund" in selection:
        rhkbefund()
    if "Renal Failure Index " in selection:
        rfi()
    if "Mikrozytäre Anämie" in selection:
        ane1()
    if "Rule out ACS" in selection:
        ruleout()
    if "RV Diastole" in selection:
        raai()
    if "Verdacht auf Lungenembolie" in selection:
        embo()

# Aufruf der Setup-Funktion, um die Sidebar zu initialisieren
setup_sidebar()


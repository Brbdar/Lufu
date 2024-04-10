#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Hauptteil der App
st.title("Pneumo-App")

# Copyright-Text in kleiner Schrift
st.markdown("© Bruno Brito da Rocha 2024", unsafe_allow_html=True)


# In[14]:


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


# In[186]:


from Gasaustausch_Transferfaktor import Gasaustausch_Transferfaktor


# In[97]:


from Gasaustausch_Blutgasanalyse import Gasaustausch_Blutgasanalyse


# In[271]:


from Compliancemessung import Compliancemessung


# In[125]:


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


# Multiselect Box für die Auswahl der Seiten
selected_pages = st.multiselect("Wählen Sie eine oder mehrere Seiten aus dem Bereich Lungenfunktion aus:",
                                ["Spirometrie qualitativ", "Spirometrie quantitativ", "Bodyplethysmographie - Residualvolumen",
                                "Bodyplethysmographie - Fluss-Druck-Kurve", "Funktionstests - Broncholyse", "Funktionstests - Provokation",
                                "Gasaustausch - Transferfaktor", "Gasaustausch - Blutgasanalyse", "P0-Atemkraftmessung",
                                "Compliancemessung", "LTOT - Algorithmus"], key="Lufubox")

# Logik zur Anzeige der ausgewählten Seiten
if 'Spirometrie Qualitativ' in selected_pages:
    spirometrie_qualitativ()
if 'Spirometrie quantitativ' in selected_pages:
    tiffeneau_index_berechnung1()
if "Bodyplethysmographie - Residualvolumen" in selected_pages:
    Bodyplethysmographie_Residualvolumen()
if "Bodyplethysmographie - Fluss-Druck-Kurve" in selected_pages:
    Bodyplethysmographie_Fluss_Druck_Kurve()
if "Funktionstests - Broncholyse" in selected_pages:
    Funktionstests_Broncholyse()
if "Funktionstests - Provokation" in selected_pages:
    Funktionstests_Provokation()
if "Gasaustausch - Transferfaktor" in selected_pages:
    Gasaustausch_Transferfaktor()
if "Gasaustausch - Blutgasanalyse" in selected_pages:
    Gasaustausch_Blutgasanalyse()
if "P0-Atemkraftmessung" in selected_pages:
    P0_Atemkraftmessung()
if "Compliancemessung" in selected_pages:
    Compliancemessung()
if "LTOT - Algorithmus" in selected_pages:
    LTOT()
    
selected_pages = st.multiselect("Wählen Sie eine oder mehrere Seiten aus dem Bereich Spiroergometrie aus:",
                                ["XXX", "XXX"], key="Spiroergo")

selected_pages = st.multiselect("Wählen Sie eine oder mehrere Seiten aus dem Bereich PH Diagnostik aus:",
                                ["EKG", "Klinik", "Thorax-Röntgen", "Lungenfunktion und arterielle Gase","der RHK Befund"], key="pulmonalehypertonie")

if "EKG" in selected_pages:
    EKG()
if "Klinik" in selected_pages:
    Klinik()
if "Thorax Röntgen" in selected_pages:
    Thorax_roentgen()
if "Lungenfunktion und Blutgase" in selected_pages:
    Lufu_BGA()   
if "der RHK Befund" in selected_pages:
    rhkbefund()
    
selected_pages = st.multiselect("Wählen Sie eine oder mehrere Seiten aus dem Bereich COPD aus:",
                                ["COPD Score"], key="COPD")

if "COPD Score" in selected_pages:
    COPD_Score()
    
selected_pages = st.multiselect("Wählen Sie eine oder mehrere Seiten aus dem Bereich Scores & Algorithmen aus:",
                                ["HFpEF Score", "Blutkultur","CHA₂DS₂-VASc Score","Pleuraerguss","Renal Failure Index"], key="Scores")

if "HFpEF Score" in selected_pages:
    HFpEF_Score()
if "Blutkultur" in selected_pages:
    Blutkultur()
if "CHA₂DS₂-VASc Score" in selected_pages:
    chadsvascore()
if "Pleuraerguss" in selected_pages:
    erguss1()
if "Renal Failure Index" in selected_pages:
    rfi()
    
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


import streamlit as st

def setup_sidebar():
    st.sidebar.title("🌬️ Analysebereiche - Lungenfunktion")
    analyse_bereich_lungenfunktion = st.sidebar.multiselect(
        label="",
        options=[
            "Spirometrie qualitativ", "Spirometrie quantitativ", "Bodyplethysmographie - Residualvolumen",
            "Bodyplethysmographie - Fluss-Druck-Kurve", "Funktionstests - Broncholyse", "Funktionstests - Provokation",
            "Gasaustausch - Transferfaktor", "Gasaustausch - Blutgasanalyse", "P0-Atemkraftmessung",
            "Compliancemessung", "LTOT - Algorithmus"
        ],
        key="analysebereich_radio"
    )
    process_selection(analyse_bereich_lungenfunktion)
    
    st.sidebar.title("🚴🏼‍♂️ Spiroergometrie")
    analyse_bereich_spiroergometrie = st.sidebar.multiselect(
        label="",
        options=["XXX", "XXX"
        ],
        key="analysebereich_radio3"
    )
    
    process_selection(analyse_bereich_spiroergometrie)

    st.sidebar.title("🫀 Detect Algorithmus - pulmonale Hypertonie")
    analyse_bereich_rechtsherzkatheter = st.sidebar.multiselect(
        label="",
        options=[
            "EKG", "Klinik", "Thorax-Röntgen", "Lungenfunktion und arterielle Gase","der RHK Befund"
        ],
        key="analysebereich_radio2"
    )
    
    process_selection(analyse_bereich_rechtsherzkatheter)
    
    st.sidebar.title("COPD")
    analyse_bereich_COPD = st.sidebar.multiselect(
        label="",
        options=["COPD Score"
        ],
        key="analysebereich_radio4"
    )
    
    process_selection(analyse_bereich_COPD)
    
    st.sidebar.title("Scores und Algorithmen")
    analyse_bereich_scores = st.sidebar.multiselect(
        label="",
        options=["HFpEF Score", "Blutkultur","CHA₂DS₂-VASc Score","Pleuraerguss", "Renal Failure Index "
        ],
        key="analysebereich_radio5"
    )
    process_selection(analyse_bereich_scores)

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
    if "CHA₂DS₂-VASc Score" in selection:
        chadsvascore()
    if "Pleuraerguss" in selection:
        erguss1()
    if "der RHK Befund" in selection:
        rhkbefund()
    if "Renal Failure Index " in selection:
        rfi()

        
    
def main():
    setup_sidebar()


if __name__ == "__main__":
    main()

        
   # Versionsnummer und Datum in der Sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Version:** 1.9")
    st.sidebar.markdown("**Datum:** 2024-04-10")
    st.sidebar.markdown("---")


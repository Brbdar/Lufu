#!/usr/bin/env python
# coding: utf-8

# import streamlit as st
# 
# # This example assumes the classes and tags do not change. Always verify with the latest Streamlit documentation.
# def set_page_styles():
#     """Apply custom styles to enhance the app's aesthetics via Streamlit's native methods."""
#     st.markdown("""
#         <style>
#             /* Base layout styles */
#             body {
#                 background-color: #f4f4f8;
#                 color: #333;
#                 font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
#             }
#             @media (prefers-color-scheme: dark) {
#                 body {
#                     background-color: #333;
#                     color: #f4f4f8;
#                 }
#                 header {
#                     background-color: #333;
#                 }
#                 .css-1d391kg {
#                     background-color: #222;
#                 }
#                 button {
#                     background-color: #555;
#                     color: white;
#                 }
#                 .stSlider .stThumb {
#                     background-color: #777;
#                 }
#             }
#             header {
#                 background-color: #6c5b7b;
#                 color: #ffffff;
#             }
#             .css-1d391kg {
#                 background-color: #355c7d;
#                 color: #ffffff;
#             }
#             button {
#                 border: none;
#                 border-radius: 5px;
#                 background-color: #c06c84;
#                 color: white;
#                 padding: 10px 20px;
#                 text-align: center;
#                 text-decoration: none;
#                 display: inline-block;
#                 font-size: 16px;
#                 margin: 4px 2px;
#                 transition-duration: 0.4s;
#                 cursor: pointer;
#             }
#             button:hover {
#                 background-color: #f67280;
#                 color: white;
#             }
#             .stSlider .stThumb {
#                 background-color: #6c5b7b;
#             }
#         </style>
#     """, unsafe_allow_html=True)
# # The rest of your functions and main setup remains unchanged
# 
# 
# def configure_page():
#     """Configure the page settings with a refined look."""
#     st.set_page_config(
#         page_title="Pneumo-App",
#         page_icon="🌬️",
#         layout="centered",
#         initial_sidebar_state="auto"
#     )
#     set_page_styles()
# 
# def display_footer():
#     """Display stylish footer information."""
#     footer_text = "<div style='color: #333; font-size: 12px; padding: 10px;'>© Bruno Brito da Rocha 2024 - Version 2.1 / 15.04.24</div>"
#     st.markdown(footer_text, unsafe_allow_html=True)
# 
# def main():
#     """Main function to enhance the Streamlit app design."""
#     configure_page()
#     # Example of additional content
#     st.title("Pneumo-App")
# 
#     display_footer()
# 
# if __name__ == "__main__":
#     main()

# In[88]:


import streamlit as st

def configure_page():
    """
    Configure the page settings with a refined look.
    Set up the page to be responsive to different device sizes and orientations.
    """
    st.set_page_config(
        page_title="Pneumo-App",  # Set the title of the webpage, visible in the browser tab
        page_icon="🌬️",  # Set a fun, related emoji as the page icon
        layout="centered",  # Use the 'wide' layout for better use of screen space on large and small screens
        initial_sidebar_state="auto"  # Automatically adjust the visibility of the sidebar based on the screen size
    )

def display_footer():
    """
    Display footer information using Streamlit components.
    The footer is kept simple and uses markdown for straightforward styling and readability.
    """
    st.markdown("---")  # Draw a horizontal line for separation
    # Provide copyright and version information in a compact and readable format
    st.caption("© Bruno Brito da Rocha 2024 - Version 2.3 / 18.04.24: Anamnesetool")

# Functions to initialize the page configuration and display the footer
configure_page()
display_footer()


# In[41]:


from spirometrie_qualitativ import spirometrie_qualitativ


# In[42]:


from tiffeneau_index_berechnung import tiffeneau_index_berechnung1


# In[43]:


from Bodyplethysmographie_Residualvolumen import Bodyplethysmographie_Residualvolumen


# In[44]:


from Bodyplethysmographie_Fluss_Druck_Kurve import Bodyplethysmographie_Fluss_Druck_Kurve


# In[45]:


from Funktionstests_Broncholyse import Funktionstests_Broncholyse


# In[46]:


from Funktionstests_Provokation import Funktionstests_Provokation


# In[47]:


from P0_Atemkraftmessung import P0_Atemkraftmessung


# In[48]:


from Gasaustausch_Transferfaktor import Gasaustausch_Transferfaktor


# In[49]:


from Gasaustausch_Blutgasanalyse import Gasaustausch_Blutgasanalyse


# In[50]:


from Compliancemessung import Compliancemessung


# In[51]:


from LTOT import LTOT


# In[52]:


from EKG import EKG


# In[53]:


from Klinik import Klinik


# In[54]:


from HFpEF_Score import HFpEF_Score


# In[55]:


from COPD_Score import COPD_Score


# In[56]:


from Blutkultur import Blutkultur


# In[57]:


from chadsvascore import chadsvascore


# In[58]:


from erguss1 import erguss1


# In[59]:


from rhkbefund import rhkbefund


# In[60]:


from rfi import rfi


# In[61]:


from ane1 import ane1 


# In[62]:


from ruleout import ruleout


# In[63]:


from raai import raai


# In[64]:


from embo import embo


# In[65]:


from Inhalator import Inhalator


# In[66]:


from bc import bc


# In[67]:


from AECOPD import AECOPD


# In[68]:


from tvt import tvt


# In[69]:


from anamnese import anamnese


# In[70]:


from tacr import tacr 


# In[87]:


# Button für die Pneumo-Anamnese
if st.button('Pneumo-Anamnese'):
    st.subheader('Pneumo-Anamnese')
    anamnese()  # Funktion zum Starten der Pneumo-Anamnese

selected_pages_allgemeines = st.multiselect(
    "Wählen Sie eine oder mehrere Seiten aus dem Bereich **Allgemeines** aus:",
    ["Pneumoanamnese"], key="anamnese")

# Logik zur Anzeige der ausgewählten Seiten im Bereich Allgemeines
if 'Pneumoanamnese' in selected_pages_allgemeines:
    anamnese()

# Multiselect Box für die Auswahl der Seiten im Bereich Lungenfunktion
selected_pages_lufu = st.multiselect(
    "Wählen Sie eine oder mehrere Seiten aus dem Bereich **Lungenfunktion** aus:",
    ["Spirometrie qualitativ", "Spirometrie quantitativ", "Bodyplethysmographie - Residualvolumen",
     "Bodyplethysmographie - Fluss-Druck-Kurve", "Funktionstests - Broncholyse", "Funktionstests - Provokation",
     "Gasaustausch - Transferfaktor", "Gasaustausch - Blutgasanalyse", "P0-Atemkraftmessung",
     "Compliancemessung", "LTOT - Algorithmus"], key="lufu")

# Logik zur Anzeige der ausgewählten Seiten im Bereich Lungenfunktion
funktions_dict = {
    "Spirometrie qualitativ": spirometrie_qualitativ,
    "Spirometrie quantitativ": tiffeneau_index_berechnung1,
    "Bodyplethysmographie - Residualvolumen": Bodyplethysmographie_Residualvolumen,
    "Bodyplethysmographie - Fluss-Druck-Kurve": Bodyplethysmographie_Fluss_Druck_Kurve,
    "Funktionstests - Broncholyse": Funktionstests_Broncholyse,
    "Funktionstests - Provokation": Funktionstests_Provokation,
    "Gasaustausch - Transferfaktor": Gasaustausch_Transferfaktor,
    "Gasaustausch - Blutgasanalyse": Gasaustausch_Blutgasanalyse,
    "P0-Atemkraftmessung": P0_Atemkraftmessung,
    "Compliancemessung": Compliancemessung,
    "LTOT - Algorithmus": LTOT
}

for seite, funktion in funktions_dict.items():
    if seite in selected_pages_lufu:
        funktion()

# Multiselect Box für die Auswahl der Seiten im Bereich Spiroergometrie
selected_pages_spiro = st.multiselect(
    "Wählen Sie eine oder mehrere Seiten aus dem Bereich **Spiroergometrie** aus:",
    ["Spiroergometrische Analyse", "Leistungsdiagnostik"], key="spiroergo")

# Logik zur Anzeige der ausgewählten Seiten im Bereich Spiroergometrie
if "Spiroergometrische Analyse" in selected_pages_spiro:
    spiroergometrische_analyse()
if "Leistungsdiagnostik" in selected_pages_spiro:
    leistungsdiagnostik()

# Multiselect Box für die Auswahl der Seiten im Bereich PH Diagnostik
selected_pages_ph = st.multiselect(
    "Wählen Sie eine oder mehrere Seiten aus dem Bereich **PH Diagnostik** aus:",
    ["EKG", "Klinik", "Thorax-Röntgen", "Lungenfunktion und arterielle Gase", "RHK Befund"], key="pulmonalehypertonie")

# Logik zur Anzeige der ausgewählten Seiten im Bereich PH Diagnostik
if "EKG" in selected_pages_ph:
    EKG()
if "Klinik" in selected_pages_ph:
    Klinik()
if "Thorax-Röntgen" in selected_pages_ph:
    thorax_roentgen()
if "Lungenfunktion und arterielle Gase" in selected_pages_ph:
    lufu_bga()
if "RHK Befund" in selected_pages_ph:
    rhk_befund()

# Multiselect Box für die Auswahl der Seiten im Bereich COPD
selected_pages_copd = st.multiselect(
    "Wählen Sie eine oder mehrere Seiten aus dem Bereich **COPD** aus:",
    ["COPD Score", "Inhalatorenauswahl", "Risikostratifizierung der AECOPD"], key="COPD")

# Logik zur Anzeige der ausgewählten Seiten im Bereich COPD
if "COPD Score" in selected_pages_copd:
    COPD_Score()
if "Inhalatorenauswahl" in selected_pages_copd:
    Inhalator()
if "Risikostratifizierung der AECOPD" in selected_pages_copd:
    AECOPD()

# Multiselect Box für die Auswahl der Seiten im Bereich Bronchialkarzinom
selected_pages_onko = st.multiselect(
    "Wählen Sie eine oder mehrere Seiten aus dem Bereich **Bronchialkarzinom** aus:",
    ["Malignitäts-Risiko-Score (Mayo Clinic Modell)"], key="BC")

# Logik zur Anzeige der ausgewählten Seiten im Bereich Bronchialkarzinom
if "Malignitäts-Risiko-Score (Mayo Clinic Modell)" in selected_pages_onko:
    bc()

# Multiselect Box für die Auswahl der Seiten im Bereich Anämie
selected_pages_ane = st.multiselect(
    "Wählen Sie eine oder mehrere Seiten aus dem Bereich **Anämie** aus:",
    ["Mikrozytäre Anämie"], key="Anämie")

# Logik zur Anzeige der ausgewählten Seiten im Bereich Anämie
if "Mikrozytäre Anämie" in selected_pages_ane:
    ane1()

# Multiselect Box für die Auswahl der Seiten im Bereich Nephrologie
selected_pages_nephro = st.multiselect(
    "Wählen Sie eine oder mehrere Seiten aus dem Bereich **Nephrologie** aus:",
    ["Tacrolimus und Mykophenolat", "Renal Failure Index"], key="Nephro")

# Logik zur Anzeige der ausgewählten Seiten im Bereich Nephrologie
if "Tacrolimus und Mykophenolat" in selected_pages_nephro:
    tacr()
if "Renal Failure Index" in selected_pages_nephro:
    rfi()

# Multiselect Box für die Auswahl der Seiten im Bereich Scores & Algorithmen
selected_pages_scores = st.multiselect(
    "Wählen Sie eine oder mehrere Seiten aus dem Bereich **Scores & Algorithmen** aus:",
    ["HFpEF Score", "Blutkultur", "Blutungs vs. Thrombose", "Pleuraerguss", "Rule out ACS", "RV Diastole",
     "Verdacht auf Lungenembolie", "TVT Stratifizierung"], key="Scores")

# Logik zur Anzeige der ausgewählten Seiten im Bereich Scores & Algorithmen
scores_funktionen = {
    "HFpEF Score": HFpEF_Score,
    "RV Diastole": raai,
    "Blutkultur": Blutkultur,
    "Blutungs vs. Thrombose": chadsvascore,
    "Pleuraerguss": erguss1,
    "Rule out ACS": ruleout,
    "Verdacht auf Lungenembolie": embo,
    "TVT Stratifizierung": tvt
}

for score, funktion in scores_funktionen.items():
    if score in selected_pages_scores:
        funktion()

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



# def setup_sidebar():
#     # Titel und Auswahl für den Bereich Lungenfunktion
#     st.sidebar.title("Analysebereiche - Lungenfunktion")
#     analyse_bereich_lungenfunktion = st.sidebar.multiselect(
#         "Wählen Sie die gewünschten Lungenfunktionstests:",
#         [
#             "Spirometrie qualitativ", "Spirometrie quantitativ", "Bodyplethysmographie - Residualvolumen",
#             "Bodyplethysmographie - Fluss-Druck-Kurve", "Funktionstests - Broncholyse", "Funktionstests - Provokation",
#             "Gasaustausch - Transferfaktor", "Gasaustausch - Blutgasanalyse", "P0-Atemkraftmessung",
#             "Compliancemessung", "LTOT - Algorithmus"
#         ],
#         key="analysebereich_lungenfunktion"
#     )
#     process_selection(analyse_bereich_lungenfunktion)
# 
#     # Bereich Spiroergometrie
#     st.sidebar.title("Spiroergometrie")
#     analyse_bereich_spiroergometrie = st.sidebar.multiselect(
#         "Wählen Sie relevante Tests für Spiroergometrie:",
#         ["Belastungstest", "VO2max Analyse"],  # Aktualisierte Platzhalterwerte
#         key="analysebereich_spiroergometrie"
#     )
#     process_selection(analyse_bereich_spiroergometrie)
# 
#     # Bereich pulmonale Hypertonie
#     st.sidebar.title("Detect Algorithmus - pulmonale Hypertonie")
#     analyse_bereich_rechtsherzkatheter = st.sidebar.multiselect(
#         "Wählen Sie Tests für die Diagnose von pulmonaler Hypertonie:",
#         [
#             "EKG", "Klinik", "Thorax-Röntgen", "Lungenfunktion und arterielle Gase", "der RHK Befund"
#         ],
#         key="analysebereich_rechtsherzkatheter"
#     )
#     process_selection(analyse_bereich_rechtsherzkatheter)
# 
#     # Bereich COPD
#     st.sidebar.title("COPD")
#     analyse_bereich_COPD = st.sidebar.multiselect(
#         "Wählen Sie Tests für COPD:",
#         ["COPD Score","Inhalatorenauswahl","Risikostratifizierung der AECOPD"],
#         key="analysebereich_COPD"
#     )
#     process_selection(analyse_bereich_COPD)
# 
#     # Bereich Bronchialkarzinom
#     st.sidebar.title("Bronchialkarzinom")
#     analyse_bereich_bc = st.sidebar.multiselect(
#         "Wählen Sie entsprechend für das Thema BC aus:",
#         ["Malignitäts-Risiko-Score (Mayo Clinic Modell)"],
#         key="analysebereich_bc"
#     )
#     process_selection(analyse_bereich_bc)
#     
#     # Bereich Anämie
#     st.sidebar.title("Anämie")
#     analyse_bereich_Anämie = st.sidebar.multiselect(
#         "Wählen Sie Tests für Anämie:",
#         ["Mikrozytäre Anämie"],
#         key="analysebereich_Anämie"
#     )
#     process_selection(analyse_bereich_Anämie)
# 
#     # Bereich Scores und Algorithmen
#     st.sidebar.title("Scores und Algorithmen")
#     analyse_bereich_scores = st.sidebar.multiselect(
#         "Wählen Sie relevante Scores und Algorithmen:",
#         ["HFpEF Score", "Blutkultur", "Blutungs vs. Thrombose", "Pleuraerguss", "Renal Failure Index", "Rule out ACS", "RV Diastole", "Verdacht auf Lungenembolie"],
#         key="analysebereich_scores"
#     )
#     process_selection(analyse_bereich_scores)
# 
#     # Trennlinie und Information über die Version
#     st.sidebar.markdown("---")
#     st.sidebar.markdown("**Version:** 2.1")
#     st.sidebar.markdown("**Datum:** 2024-04-13")
#     st.sidebar.markdown("---")
# 
# def process_selection(selection):
#     # Fügen Sie hier die Logik zum Aufrufen von Funktionen basierend auf der Auswahl hinzu
#     if "Spirometrie qualitativ" in selection:
#         spirometrie_qualitativ()
#     if "Spirometrie quantitativ" in selection:
#         tiffeneau_index_berechnung1()
#     if "Bodyplethysmographie - Residualvolumen" in selection:
#         Bodyplethysmographie_Residualvolumen()
#     if "Bodyplethysmographie - Fluss-Druck-Kurve" in selection:
#         Bodyplethysmographie_Fluss_Druck_Kurve()
#     if "Funktionstests - Broncholyse" in selection:
#         Funktionstests_Broncholyse()
#     if "Funktionstests - Provokation" in selection:
#         Funktionstests_Provokation()
#     if "Gasaustausch - Transferfaktor" in selection:
#         Gasaustausch_Transferfaktor()
#     if "Gasaustausch - Blutgasanalyse" in selection:
#         Gasaustausch_Blutgasanalyse()
#     if "P0-Atemkraftmessung" in selection:
#         P0_Atemkraftmessung()
#     if "Compliancemessung" in selection:
#         Compliancemessung()
#     if "LTOT - Algorithmus" in selection:
#         LTOT()
#     if "EKG" in selection:
#         EKG()
#     if "Klinik" in selection:
#         Klinik()
#     if "Thorax Röntgen" in selection:
#         Thorax_roentgen()
#     if "Lungenfunktion und Blutgase" in selection:
#         Lufu_BGA()
#     if "HFpEF Score" in selection:
#         HFpEF_Score()
#     if "Blutkultur" in selection:
#         Blutkultur()
#     if "COPD Score" in selection:
#         COPD_Score()
#     if "Blutungs vs. Thrombose" in selection:
#         chadsvascore()
#     if "Pleuraerguss" in selection:
#         erguss1()
#     if "der RHK Befund" in selection:
#         rhkbefund()
#     if "Renal Failure Index " in selection:
#         rfi()
#     if "Mikrozytäre Anämie" in selection:
#         ane1()
#     if "Rule out ACS" in selection:
#         ruleout()
#     if "RV Diastole" in selection:
#         raai()
#     if "Verdacht auf Lungenembolie" in selection:
#         embo()
#     if "Inhalatorenauswahl" in selection:
#         Inhalator()
#     if "Malignitäts-Risiko-Score (Mayo Clinic Modell)" in selection:
#         bc()
#     if "Risikostratifizierung der AECOPD" in selection:
#         AECOPD()
#     if "TVT Stratifizierung" in selection:
#         tvt()
#     
# 
# # Aufruf der Setup-Funktion, um die Sidebar zu initialisieren
# setup_sidebar()
# 

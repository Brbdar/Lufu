#!/usr/bin/env python
# coding: utf-8

# In[278]:


import streamlit as st

# Hauptteil der App
st.title("Analysebereich Lungenfunktion")


# In[14]:


from spirometrie_qualitativ import spirometrie_qualitativ


# In[287]:


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


# In[291]:


def main():
    # Benutzerdefiniertes CSS anwenden
    custom_css = """
    <style>
        @media (max-width: 768px) {
            /* Anpassungen für die Sidebar auf kleineren Bildschirmen */
            .css-1d391kg {
                font-size: 14px; /* Kleinere Schriftgröße für den Titel */
            }
            .stRadio > div {
                background-color: #f0f2f6;
                border-radius: 20px;
                padding: 8px; /* Größeres Padding für bessere Klickbarkeit */
                font-size: 16px; /* Größere Schrift für bessere Lesbarkeit */
            }
        }

        /* Standardanpassungen */
        .css-1d391kg { /* Ändert die Farbe des Titels */
            color: #333;
        }
        .stRadio > div { /* Anpassung der Radiobuttons */
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
         "Gasaustausch - Transferfaktor", "Gasaustausch - Blutgasanalyse","P0-Atemkraftmessung","Compliancemessung","LTOT - Algorithmus"),
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
    elif analyse_bereich == "LTOT - Algorithmus":
        LTOT()

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


#!/usr/bin/env python
# coding: utf-8

# In[322]:


import streamlit as st

# Hauptteil der App
st.title("Pneumoapp")


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


# In[ ]:


from EKG import EKG


# In[321]:


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

    st.sidebar.title("🫀 Rechtsherzkatheter in Arbeit")
    analyse_bereich_rechtsherzkatheter = st.sidebar.multiselect(
        label="",
        options=[
            "EKG", "Neue Option"
        ],
        key="analysebereich_radio2"
    )
    process_selection(analyse_bereich_rechtsherzkatheter)
    
    st.sidebar.title("🚴🏼‍♂️ Spiroergometrie in Arbeit")
    analyse_bereich_spiroergometrie = st.sidebar.multiselect(
        label="",
        options=["XXX", "XXX"
        ],
        key="analysebereich_radio3"
    )
    process_selection(analyse_bereich_spiroergometrie)

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
        
    # Fügen Sie weitere Bedingungen für jede Auswahlmöglichkeit hinzu

def main():
    setup_sidebar()

if __name__ == "__main__":
    main()

        
   # Versionsnummer und Datum in der Sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Version:** 1.7")
    st.sidebar.markdown("**Datum:** 2024-04-07")
    st.sidebar.markdown("---")


# In[ ]:





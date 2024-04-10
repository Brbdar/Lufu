#!/usr/bin/env python
# coding: utf-8

# In[16]:


import streamlit as st

def rfi():
    """
    Berechnet den Renal Failure Index (RFI) und gibt einen Befund basierend auf dem Ergebnis aus.
    """

    st.title("Berechnung des Renal Failure Index (RFI)")
    
    def calculate_fe_na(urine_na, plasma_na, urine_cr, plasma_cr):
        """Berechnet die fraktionelle Exkretion von Natrium (FE-Na)."""
        return 100 * ((urine_na / plasma_na) / (urine_cr / plasma_cr))
        
    with st.expander("Über den RFI"):
        st.write("""
        Der Renal Failure Index (RFI) ist ein diagnostisches Werkzeug, das bestimmt, ob das akute Nierenversagen (ARF) durch prärenale oder renale Ursachen bedingt ist, und gleichzeitig zur Überwachung der Kreatininwerte verwendet werden kann.
        
        - **Urin-Natrium (mEq/L)**: Gemessen in mEq/L, liegt der Normbereich zwischen 25 und 150 mEq/L.
        - **Serum-Kreatinin (mg/dL)**: Kreatinin ist ein Abbauprodukt im Stoffwechsel von Muskeln und gewissen Geweben, gefiltert durch das Glomerulus. Der Normbereich beträgt 0.6 bis 1.3 mg/dL.
        - **Urin-Kreatinin (mg/dL)**: Berücksichtigt die Kreatininwerte, die den Filtrationsprozess umgehen und durch den Urin ausgeschieden werden. Der Normbereich für Urin-Kreatinin liegt zwischen 40 und 120 mg/dL.
        """)

    with st.expander("RFI Interpretation"):
        st.write("""
        Die Formel zur Berechnung des RFI lautet: `RFI = Urin-Natrium / (Urin-Kreatinin / Serum-Kreatinin)`
        
        - Ein **RFI > 1** deutet auf renale Ursachen hin, die von einem tastbaren Blasenvolumen, hydronephrotischen Nieren, einer vergrößerten Prostata oder Nierensteinen begleitet sein können.
        - Ein **RFI ≤ 1** weist auf prärenale Ursachen hin, die von Volumenmangel, bestehender kongestiver Herzinsuffizienz, schwerer Lebererkrankung oder Ödemen begleitet sein können.
        """)
    
    with st.expander("Zum Kontext von ARF und ATN"):
        st.write("""
        Akutes Nierenversagen (ARF) und Akute Tubulusnekrose (ATN) sind zwei Zustände, die in diesem Kontext relevant sind. ARF ist durch eine schnelle Verschlechterung der Nierenfunktion gekennzeichnet und kann durch verschiedene Faktoren, einschließlich ATN, verursacht werden. ATN, die häufigste Ursache für AKI (Akute Nierenverletzung), ist durch Schäden an den Tubuluszellen gekennzeichnet, die durch niedrigen Blutdruck und/oder den Einsatz von nephrotoxischen Medikamenten verursacht werden können.
        """)

    # Formular für die Eingabe der Werte
    with st.form(key='rfi_form'):
        plasma_na = st.number_input("Natrium im Plasma (mEq/L)", min_value=100.0, max_value=150.0, value=140.0, format="%.2f")
        serum_cr = st.number_input("Serum Kreatinin (mg/dL)", min_value=0.1, max_value=10.0, value=1.0, format="%.2f")
        urine_na = st.number_input("Natrium im Urin (mEq/L)", min_value=0.0, max_value=200.0, value=40.0, format="%.2f")
        urine_cr = st.number_input("Kreatinin im Urin (mg/dL)", min_value=10.0, max_value=300.0, value=100.0, format="%.2f")
        submit_button = st.form_submit_button(label='Berechnen')

    if submit_button:
        rfi_value = urine_na / (urine_cr / serum_cr)
        fe_na = calculate_fe_na(urine_na, plasma_na, urine_cr, serum_cr)
        
        # RFI Interpretation
        st.write(f"Renal Failure Index (RFI): {rfi_value:.2f}")
        if rfi_value > 1:
            st.write("Befund: Der RFI-Wert weist auf eine renale Ursache hin. Eine weitere Diagnostik wird empfohlen.")
        else:
            st.write("Befund: Der RFI-Wert weist auf prärenale Ursachen hin. Eine Anpassung der Flüssigkeitszufuhr und weiterführende Untersuchungen könnten notwendig sein.")

        # FE-Na Interpretation
        st.write(f"Fraktionelle Natriumexkretion (FE-Na): {fe_na:.2f}%")
        if fe_na < 1:
            st.write("Befund: FE-Na < 1% weist auf prärenale Azotämie oder akute Glomerulonephritis hin.")
        elif fe_na > 1:
            st.write("Befund: FE-Na > 1% weist auf ATN oder eine postrenale Azotämie hin.")
            
    st.markdown("""
        **Referenzartikel:**  
        T R Miller, R J Anderson, S L Linas, W L Henrich, A S Berns, P A Gabow, R W Schrier.  
        _Urinary diagnostic indices in acute renal failure: a prospective study_.  
        PMID: 666184 DOI: 10.7326/0003-4819-89-1-47  
        [Zugriff auf PubMed](https://www.ncbi.nlm.nih.gov/pubmed/666184)
        """, unsafe_allow_html=True)
    
   


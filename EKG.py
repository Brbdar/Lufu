#!/usr/bin/env python
# coding: utf-8

# In[12]:


import streamlit as st


def EKG():
    # Titel der Seite
    st.title('Früherkennung von Pulmonaler Hypertonie (PH) durch EKG-Analyse')

    # Einführungstext
    st.write("""
    Bestimmte Veränderungen im Elektrokardiogramm (EKG) können auf das Vorhandensein einer PH hinweisen.
    Diese interaktive Seite führt Sie durch eine Reihe von Fragen zu EKG-Veränderungen und gibt am Ende eine Einschätzung.
    Bitte beachten Sie, dass diese Anwendung eine professionelle medizinische Diagnose nicht ersetzen kann.
    """)
    
    st.write("""
    Typische elektrokardiografische Veränderungen bei PH umfassen:
    - P-pulmonale
    - Rechtsachsenabweichung oder die Lagetypen SIQIII beziehungsweise SISIISIII
    - Rechtsventrikuläre Hypertrophie
    - Große R-Zacken in V1 und V2 und tiefe S-Zacken in V5 und V6
    - Rechtsschenkelblock
    - qR-Konfiguration in V1 sowie ST-Senkungen und negative T-Wellen
    
    Es ist wichtig zu beachten, dass ein normales EKG eine PH nicht sicher ausschließt, insbesondere bei milder PH. EKG-Parameter für rechtsventrikuläre Hypertrophie haben zwar eine hohe Spezifität, aber nur eine geringe Sensitivität.
    """)

    # Option zur Anzeige weiterführender Informationen
    if st.expander("Mehr über diagnostische Grenzen und statistische Daten"):
        st.write("""
        Die Rechtsachsenabweichung, eine qR-Konfiguration in V1 und eine niedrige S-Amplitude in V1 weisen hohe positiv prädiktive Werte bei Erwachsenen mit PH-Verdacht auf. Allerdings sind die positiv und negativ prädiktiven Werte für EKG-Kriterien der rechtsventrikulären Hypertrophie für eine sichere Diagnose oder Ausschluss unzureichend.
        Sind EKG und (NT-pro-)BNP unauffällig, ist eine PH unwahrscheinlich.
        """)

    # Eingabefelder für die Benutzerinteraktion
    st.header('Bitte beantworten Sie die folgenden Fragen basierend auf dem EKG-Bericht:')

    q1 = st.radio('Liegt eine Belastung, Hypertrophie oder Dilatation des rechten Herzens vor?', ('Ja', 'Nein', 'Unbekannt'))
    q2 = st.radio('Sind EKG-Veränderungen vorhanden?', ('Ja', 'Nein', 'Unbekannt'))
    q3 = st.radio('Sind Biomarker wie BNP bzw. NT-proBNP normwertig?', ('Ja', 'Nein', 'Unbekannt'))

    st.header('Spezifische EKG-Veränderungen')
    q4 = st.checkbox('P pulmonale (P > 0,25 mV in Ableitung II)')
    q5 = st.checkbox('Rechts- oder Sagittalachsenabweichung (QRS-Achse > 90° oder unbestimmbar)')
    q6 = st.checkbox('RV-Hypertrophie (R/S > 1, mit R > 0,5 mV in V1; R in V1 + S in Ableitung V5 > 1 mV)')
    q7 = st.checkbox('Rechtsschenkelblock – komplett oder inkomplett (qR- oder rSR-Muster in V1)')
    q8 = st.checkbox('RV-Belastung (ST-Senkung/T-Welleninversion in den rechts präkordialen [V1–4] und inferioren [II, III, aVF] Ableitungen)')
    q9 = st.checkbox('Verlängertes QTc-Intervall (unspezifisch)')

    # Auswertungslogik
    if st.button('Ergebnis auswerten'):
        positive_signs = sum([q4, q5, q6, q7, q8, q9])
        if q1 == 'Ja' and q2 == 'Ja' and q3 == 'Nein' and positive_signs >= 3:
            st.success('Es besteht eine erhöhte Wahrscheinlichkeit für PH. Bitte suchen Sie einen Spezialisten auf.')
        elif q1 == 'Nein' and q2 == 'Nein' and q3 == 'Ja' and positive_signs < 3:
            st.info('PH ist eher unwahrscheinlich. Halten Sie dennoch Rücksprache mit Ihrem Arzt.')
        else:
            st.warning('Die Informationen sind nicht eindeutig. Bitte führen Sie weitere Untersuchungen durch.')

    with st.expander("Erläuterung der EKG-Veränderungen"):
        st.write("""
        - **P pulmonale**: Ein Indikator für eine atriale Überlastung.
        - **Rechts- oder Sagittalachsenabweichung**: Kann auf eine Belastung des rechten Ventrikels hinweisen.
        - **RV-Hypertrophie**: Verdickung der Wände des rechten Ventrikels.
        - **Rechtsschenkelblock**: Ein Muster, das eine Verzögerung der rechtsventrikulären Erregung anzeigt.
        - **RV-Belastung**: Zeichen der Belastung des rechten Ventrikels.
        - **Verlängertes QTc-Intervall**: Kann auf eine Repolarisationsstörung hinweisen.
        """)
        
    # Link zur Studie
    st.markdown(
        "Für weiterführende Informationen zu diesem Thema, "
        "besuchen Sie bitte die folgende Seite: "
        "[Zur Studie](https://www.thrombosisresearch.com/action/showPdf?pii=S0049-3848%2811%2900116-2)."
    )



        
        # Hauptfunktion aufrufen
if __name__ == "__main__":
    EKG()



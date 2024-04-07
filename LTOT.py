#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st

def LTOT():
    st.header("LTOT - Algorithmus")
    
    st.write("Die LTOT-Leitlinie wurde am 23.07.2020 nach einem 1,5-jährigen Prozess mit neun wissenschaftlichen Gesellschaften und der LOT e.V. veröffentlicht. Der Artikel fasst die Hauptpunkte zusammen, insbesondere die Bedeutung für die Patientenversorgung bei Lungenerkrankungen.")
    link = "https://www.sauerstoffliga.de/wp-content/uploads/2021/11/O²_Report_Langzeit-Sauerstoff-Leitlinie-2020-Teil1-und-Teil2.pdf"
    st.markdown("Die überarbeitete LTOT-Leitlinie wurde am 23.07.2020 veröffentlicht. Hier ist der [Link zur Leitlinie]({}).".format(link))
    
    with st.expander("Indikationen:"):
        st.write("""
        - Indikationen zur LTOT haben sich im Vergleich zu 2008 prinzipiell nicht geändert.
        - Einleitung einer LTOT erfordert eine chronische Hypoxämie über mindestens drei Wochen mit einem pO2 ≤ 55 mmHg, zweimalig nachgewiesen mittels Blutgasanalyse.
        - Bei einem pO2 ≤ 60 mmHg, erhöhtem Hämatokrit und/oder Belastung des Lungenkreislaufs durch Hypoxämie mit Folge einer Rechtsherzbelastung ist ebenfalls eine LTOT-Verordnung angezeigt.
        - Eine LTOT-Verordnung bei höheren pO2-Werten als in der Leitlinie genannt hat keinen Einfluss auf das Überleben.
        """)

    with st.expander("Womit die Indikationsstellung?"):
        st.write("""
        - Eine alleinige Messung der Sauerstoffsättigung durch Pulsoxymeter ist nicht ausreichend zur Indikationsstellung für LTOT, da nicht sicher zwischen Patienten, die keine Sauerstofftherapie benötigen, und solchen, die sie benötigen, unterschieden werden kann.
        - Eine Sauerstoffsättigung ≤92 % sollte Anlass für weitere Diagnostik mit Blutgasanalyse geben, nach einer Ruhezeit von mindestens 10 Minuten durchgeführt.
        - Hyperventilation (erniedrigter pCO2) erfordert eine entsprechende Korrektur des Sauerstoffwerts, da Hyperventilation ein Kompensationsmechanismus des Körpers bei Sauerstoffmangel darstellt.
        - Bei Erhöhung des pCO2 muss die Indikation zur Einleitung einer Nicht-Invasiven Beatmung (NIV) überprüft werden. 
        - Bei Indikation zur LTOT sollte der Effekt der Therapie unter der gewählten Flussrate überprüft werden, mit dem Ziel, den pO2 auf mindestens 60 mmHg oder um mindestens 10 mmHg zu steigern.
        - Bei einigen Patienten kann die LTOT zu einer Abnahme des Atemantriebs mit einem Anstieg des pCO2 führen. Es ist wichtig, einen kritischen Anstieg zu vermeiden, der zu einer Entgleisung des Säure-Basen-Haushalts führt. Gegebenenfalls sind nächtliche Messungen des CO2-Werts über Hautelektroden erforderlich.
        """)

    with st.expander("Dauer der LTOT"):
        st.write("""
        - Studiendaten empfehlen eine tägliche Durchführung der LTOT von ≥15 Stunden.
        - Aktuelle Beobachtungsstudien zeigen, dass eine längere Verwendungsdauer keine zusätzlichen Vorteile bezüglich der Endpunkte erneute Krankenhausaufnahme und Sterblichkeit bringt.
        - Einige mobile Patienten benötigen zusätzlich mobile Sauerstoffversorgungsgeräte, um die empfohlene Gesamtdauer von ≥15 Stunden pro Tag zu erreichen.
        """)
        
    with st.expander("LTOT und Krankheitsbilder"):
        st.write("""
        - **COPD**  
        - Bei COPD wurde gezeigt, dass eine entsprechende Verordnung von LTOT die Krankheitsfolgen und die Sterblichkeit senken kann.
        - Im LOTT (Long Term Oxygen Trial) wurde vor einigen Jahren gezeigt, dass diese Effekte bei Patienten mit nur mäßiger Hypoxämie (Sauerstoffsättigung zwischen 80–92 %) nicht nachgewiesen werden konnten.
        - Auch bei alleiniger Belastungshypoxämie ist ein lebensverlängernder Effekt der LTOT nicht nachgewiesen.
        - **Interstitielle Erkrankungen**
        -  Analog zur COPD kann bei Patienten mit interstitiellen Lungenerkrankungen eine LTOT unterhalb der gleichen Grenzwerte für pO2 und Sauerstoffsättigung empfohlen werden.
        - Eine rein nächtliche Sauerstofftherapie wird nicht empfohlen.
        - Eine aktuelle Studie hat gezeigt, dass die Sauerstoffgabe bei Belastungshypoxämie einen positiven Effekt auf Atemnot und Belastbarkeit haben kann.
        - **Zystische Fibrose**
        - Wie bei COPD
        - **Neuromuskuläre Erkrankungen**
        - Bei Patienten mit neuromuskulären Erkrankungen wird die Bedeutung der Atempumpenschwäche hervorgehoben, die häufig bei diesen Erkrankungen auftritt.
        - Primär sollte die Indikation zur Nicht-Invasiven Beatmung (NIV) überprüft werden, gegebenenfalls in Kombination mit einem intensiven Sekretmanagement, bevor unkritisch Sauerstoff verschrieben wird.
        - **Chronische Herzinsuffizienz**
        - Bei gesunder Lunge ist die Hypoxämie weniger auf eine verminderte Sauerstoffaufnahme in der Lunge zurückzuführen, sondern eher auf einen vermehrten Sauerstoffverbrauch in den peripheren Organen bei fehlender Lungenstauung.
        - Es gibt keine Langzeitdaten zur Langzeit-Sauerstofftherapie (LTOT) bei chronischer Herzinsuffizienz; meist ist die Hypoxämie nur mäßig ausgeprägt, so dass keine Indikation zur LTOT im chronischen Verlauf besteht.
        - In akuten Phasen der Herzschwäche oder palliativ zur Behandlung von Atemnot in den Endstadien der Erkrankung kann Sauerstoff eingesetzt werden.
        - **Pulmonale Hypertonoe**
        - Eine LTOT wird bei einem pO2 <60 mmHg empfohlen.
        """)
        
        
    
    st.title("Algorithmus zur LTOT")


    # Schritt 1: Start des Algorithmus
    pa02_in_ruhe = st.number_input(
        'PAO₂ in Ruhe (mmHg)', 
        min_value=0.0, 
        format="%.2f", 
        help="Geben Sie den Sauerstoffpartialdruck in Ruhe ein."
    )
    cor_pulmonale_oder_polyglobulie = st.checkbox(
        'Cor pulmonale oder Polyglobulie oder Hypoxämie im Schlaf'
    )

    if pa02_in_ruhe < 55 or (55 <= pa02_in_ruhe <= 65 and cor_pulmonale_oder_polyglobulie):
        # Schritt 2: Überprüfung der Grundkrankheit
        st.subheader("Therapie-Überprüfung")
        therapie_optimiert = st.radio(
            "Ist die Grundkrankheit adäquat therapiert?",
            ('Ja', 'Nein')
        )

        if therapie_optimiert == 'Nein':
            st.warning("Therapie optimieren und Tabakentwöhnung vornehmen.")
        else:
            # Schritt 3: Überprüfung der Hypoxämie in Ruhe
            st.subheader("Hypoxämie-Überprüfung")
            hypoxaemie_in_ruhe = st.radio(
                "Liegt eine Hypoxämie in Ruhe vor?",
                ('Ja', 'Nein')
            )

            if hypoxaemie_in_ruhe == 'Ja':
                # Schritt 4: Überprüfung von PAO₂ ≥60 mmHg oder Anstieg um ≥10 mmHg
                st.subheader("PAO₂-Überprüfung")
                pa02_60_mmhg_oder_anstieg_um_10 = st.checkbox(
                    'PAO₂ ≥60 mmHg oder Anstieg um ≥10 mmHg'
                )

                if pa02_60_mmhg_oder_anstieg_um_10:
                    # Schritt 5: Überprüfung, ob der Patient mobil ist
                    st.subheader("Mobilitäts-Überprüfung")
                    patient_mobil = st.radio(
                        "Ist der Patient mobil?",
                        ('Ja', 'Nein')
                    )

                    if patient_mobil == 'Ja':
                        st.success("Langzeit-Sauerstofftherapie mit mobilem Sauerstoffgerät.")
                    else:
                        st.success("Langzeit-Sauerstofftherapie mit stationärem Sauerstoffgerät.")
                else:
                    st.success("O₂-Applikation in Ruhe.")

            else:
                # Schritt 6: Überprüfung der Hypoxämie nur bei Belastung
                st.subheader("Hypoxämie bei Belastung")
                hypoxaemie_nur_belastung = st.radio(
                    "Liegt eine Hypoxämie nur bei Belastung vor?",
                    ('Ja', 'Nein')
                )

                if hypoxaemie_nur_belastung == 'Ja':
                    st.success("O₂-Applikation unter Belastung.")
                else:
                    # Schritt 7: Sättigung überprüfen
                    st.subheader("Sättigungs-Überprüfung")
                    saettigung_90 = st.radio(
                        "Ist die Sättigung >90% und Belastbarkeit verbessert?",
                        ('Ja', 'Nein')
                    )

                    if saettigung_90 == 'Ja':
                        st.success("Langzeit-Sauerstofftherapie mit mobilem Sauerstoffgerät.")
                    else:
                        st.error("Keine Langzeit-Sauerstofftherapie. Schlafstudie empfohlen.")
    else:
        st.error("Keine Langzeit-Sauerstofftherapie. Weitere Untersuchungen empfohlen.")
        
    if st.button('LTOT Algorithmus anzeigen'):
        st.image("LTOT.jpg", caption="LTOT-Indikationsalgorithmus")



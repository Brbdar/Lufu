#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
        
        
    st.subheader("LTOT-Indikationsprüfung")
    with st.form("ltot_form"):
        po2 = st.number_input("Geben Sie den Sauerstoffpartialdruck (pO2) in mmHg ein:", min_value=0.0, format="%.2f")
        pulm_hyp = st.checkbox("Vorhandensein von pulmonaler Hypertonie")
        polyglobulie = st.checkbox("Vorhandensein von Polyglobulie (Hämatokrit ≥ 55%)")
        submit_button = st.form_submit_button("Prüfung starten")
    
    if submit_button:
        # Logik für die LTOT-Indikationsstellung
        if po2 < 55 or (po2 < 60 and (pulm_hyp or polyglobulie)):
            st.success("Schwere chronische Hypoxämie erkannt. Indikation zur LTOT gegeben.")
        elif 55 <= po2 < 60 and not (pulm_hyp or polyglobulie):
            st.info("Mäßige chronische Hypoxämie erkannt. Keine Indikation zur LTOT.")
        else:
            st.warning("Keine klare Indikation für LTOT. Weitere Untersuchungen empfohlen.")
        
    with st.expander("Wichtiger Hinweis zur BGA-Messung"):
        st.write("""
        In der Regel wird der Sauerstoffpartialdruck (PO2) mittels der BGA aus dem hyperämisierten Ohrläppchen (PcO2) bestimmt. Dieser ist im Mittel etwa 6 mmHg niedriger als der Sauerstoffpartialdruck aus der arteriellen Blutgasanalyse (PaO2). Bei Grenzbefunden sollte daher eine arterielle BGA durchgeführt werden. Innerhalb der stabilen Phase sollten 3 kapilläre BGA innerhalb eines 4-wöchigen Zeitraums durchgeführt werden, während die britische Leitlinie 2 arterielle BGA mit mindestens 3-wöchigem Abstand empfiehlt.
        """)
        
    # Postakute Sauerstofftherapie (PoaOT) Abfrage
    st.subheader("Postakute Sauerstofftherapie (PoaOT)")
    with st.expander("Information zur PoaOT"):
        st.write("""
        Nach einer akuten Exazerbation einer COPD oder einer Pneumonie kann bei Sättigungswerten unter 93% und Dyspnoe vor der Entlassung aus dem Krankenhaus eine PoaOT verordnet werden. Die Indikation wird durch 2 Verlaufskontrollen in einem stabilen Zeitraum von 6–12 Wochen nach Entlassung überprüft.
        """)
    
    poaot_sattigung = st.number_input("Sättigungswert eingeben (< 93% für PoaOT):", min_value=0.0, max_value=100.0, step=0.1, format="%.2f")
    dyspnoe = st.radio("Dyspnoe vor Entlassung vorhanden?", ("Ja", "Nein"))
    
    if st.button('PoaOT-Indikation prüfen'):
        if poaot_sattigung < 93 and dyspnoe == "Ja":
            st.success("Eine PoaOT-Verordnung kann in Betracht gezogen werden. Zwei Verlaufskontrollen im Zeitraum von 6–12 Wochen nach Entlassung sind empfohlen.")
        else:
            st.error("Basierend auf den eingegebenen Daten ist keine PoaOT-Verordnung erforderlich oder weitere Bewertungen sind notwendig.")

    
    # Bilder als Platzhalter für interaktive Auswahl
    with st.columns(1)[0]:  # Direkter Zugriff auf das erste Element der Liste
        if st.button('LTOT Algorithmus'):
            st.session_state.selected_curve = 'LTOT'   
    
    if 'selected_curve' in st.session_state:
        if st.session_state.selected_curve == 'LTOT':
            st.image("LTOT.jpg")


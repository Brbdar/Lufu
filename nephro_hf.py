#!/usr/bin/env python
# coding: utf-8

# In[82]:


import streamlit as st

def nephro_hf():

    st.markdown("""
        # Diuretic Therapy for Patients With Heart Failure: JACC State-of-the-Art Review
        
        **Autoren:** G. Michael Felker MD, MHS a b, David H. Ellison MD c d e, Wilfried Mullens MD, PhD f g, Zachary L. Cox PharmD h i, Jeffrey M. Testani MD, MTR j
        
        **Veröffentlicht in:** [Journal of the American College of Cardiology](https://www.sciencedirect.com/science/article/pii/S0735109720301947?ref=pdf_download&fr=RR-2&rr=877c96951f653641)
        
        Dieser umfassende Review-Artikel diskutiert aktuelle Erkenntnisse und Praktiken im Bereich der Diuretikatherapie für Patienten mit Herzinsuffizienz. Die Autoren, führende Experten auf ihrem Gebiet, bieten eine gründliche Analyse der Mechanismen, Wirkungen und klinischen Outcomes von Diuretika bei der Behandlung dieser komplexen Erkrankung.""")
        
    with st.expander("Einsatz von Schleifendiuretika bei Krankenhausaufenthalt wegen HF"):
        st.write("""
        - **Hauptbehandlung:** Parenterale Schleifendiuretika sind die Hauptstütze der Behandlung von Patienten, die wegen HF hospitalisiert sind.
        - **Evidenzbasis:** Trotz ihrer weitverbreiteten Anwendung in der klinischen Praxis ist die Evidenzbasis für die angemessene Verwendung von Schleifendiuretika im Vergleich zu vielen anderen Bereichen der HF-Behandlung gering.
        - **Leitlinien:** Aktuelle Leitlinien geben Diuretika eine Klasse-I-Empfehlung in einer Vielzahl von klinischen Situationen, basieren jedoch auf keiner höheren Evidenz als Level B oder C.
        - **Allgemeine Fragen:** Zu den allgemeinen Fragen bei der Behandlung hospitalisierter HF-Patienten mit Zeichen von Kongestion gehören:
          - Wahl der Anfangsdosis des Schleifendiuretikums
          - Entscheidung zwischen intermittierenden Bolusgaben oder kontinuierlichen Infusionen
          - Anpassungen der Therapie bei unzureichender diuretischer Reaktion (z. B. Diuretikaresistenz)
                """)

    with st.expander("Die DOSE-Studie: Optimierung der Schleifendiuretikatherapie bei Herzinsuffizienz"):
        st.write("""
            ### Studienziel
            Die DOSE-Studie wurde entworfen, um zwei wichtige Fragen bezüglich der intravenösen Schleifendiuretikatherapie bei hospitalisierten Patienten mit Herzinsuffizienz zu beantworten:
            1. Ob eine höhere Dosierung von Furosemid einer niedrigeren vorzuziehen ist.
            2. Ob eine kontinuierliche Infusion von Furosemid intermittierenden IV-Bolusgaben überlegen ist.
            
            ### Studiendesign
            - **Teilnehmer:** 308 Patienten mit HF und Anzeichen von Kongestion.
            - **Randomisierung:** Patienten wurden in einem 2x2 faktoriellen Design entweder zu IV-Bolusgaben alle 12 Stunden oder zu einer kontinuierlichen Infusion randomisiert, und zu niedrigen Dosen (entsprechend der täglichen oralen Heimdosis des Patienten) oder zu hohen Dosen (2,5-fache der täglichen oralen Heimdosis).
            
            ### Ergebnisse
            - **Symptombewertung:** Unterschiede in der globalen Bewertung der Symptome durch die Patienten erreichten keine statistische Signifikanz.
            - **Sekundäre Endpunkte:** Die Gruppe mit der hohen Dosis hatte günstigere Ergebnisse in Bezug auf Linderung der Dyspnoe, Gewichtsveränderung und Nettoflüssigkeitsverlust.
            - **Nierenfunktion:** Eine Verschlechterung der Nierenfunktion trat häufiger in der Hochdosisgruppe auf. Ein anfänglicher Anstieg des Plasmakreatinins war jedoch mit besseren langfristigen klinischen Ergebnissen verbunden.
            
            ### Pharmakodynamische Überlegungen
            Kontinuierliche Infusionen halten die Furosemidkonzentration konstant über dem diuretischen Schwellenwert und vermeiden hohe Spitzenwerte, die zu Toxizität führen können.
            
            ### Klinische Implikationen
            Obwohl kleinere Studien potenzielle klinische Vorteile einer kontinuierlichen Infusion suggerieren, zeigte die DOSE-Studie keine signifikanten Unterschiede in den klinischen Endpunkten zwischen den Vergleichsgruppen. Die Frage, ob eine kontinuierliche Infusion von Schleifendiuretika in anderen klinischen Situationen effektiver oder sicherer sein kann, bleibt offen.
            
            ### Schlussfolgerungen
            Die DOSE-Studie bietet wichtige Erkenntnisse für die Behandlung von ADHF, insbesondere hinsichtlich aggressiverer Ansätze bei der Dosierung von Schleifendiuretika.
                    """)


    with st.expander("Definition und Mechanismen der Diuretikaresistenz"):
        st.write("""
            ### Definition von Diuretikaresistenz
            - **Qualitative Definition:** Diuretikaresistenz beschreibt eine unzureichende Natriurese oder Diurese trotz eines adäquaten Diuretikaregimes.
            - **Quantitative Definition:** Die Umstellung von einer qualitativen zu einer nützlichen quantitativen Definition bleibt schwierig, da ein "adäquates Diuretikaregime" subjektiv und vom klinischen Kontext abhängig ist.
            
            ### Diuretische Effizienz
            - **Beschreibung:** Ein Versuch, die Diuretikantwort im Kontext der verabreichten Dosis zu integrieren, ausgedrückt als Flüssigkeitsausstoß, Gewichtsveränderung oder Natriumausscheidung, angepasst an die Menge des verabreichten Diuretikums.
            - **Problematik:** Niedrige diuretische Effizienz korreliert mit schlechteren Ausgängen, insbesondere bei Patienten mit hoher Dosierung von Schleifendiuretika.
            
            ### Herausforderungen bei der Messung
            - **Klinische Praxis:** Standardmetriken zur Quantifizierung von Diurese und Natriurese sind unzureichend und korrelieren schlecht mit Gewichtsverlust und Nettoharnausstoß.
            - **Neue Ansätze:** Jüngste Studien haben sich auf die Messung der Natriumkonzentrationen in Spot-Urinproben nach Diuretikagabe konzentriert.
            
            ### Mechanismen der Diuretikaresistenz
            - **Diuretikabremsung:** Eine natürliche Reaktion der Niere, die verhindert, dass die anfängliche normale Reaktion von Schleifendiuretika gefährlich wird.
            - **Einteilung:** Kann grob als prärenale und intrarenale Diuretikaresistenz dichotomisiert werden, wobei die letztere weiter nach den anatomischen Nephronsegmenten unterteilt wird, in denen der Resistenzmechanismus auftritt.
            
            ### Klinische Implikationen
            - **Studienlage:** Es gibt wenige Studien über Diuretikaresistenz bei Herzinsuffizienzpatienten, die auf aktueller evidenzbasierter Medizin basieren.
                    """)

    with st.expander("Pre-renale Diuretikaresistenz: Ein einfacher Überblick"):
        st.write("""
            ### Was ist pre-renale Diuretikaresistenz?
            Pre-renale Diuretikaresistenz entsteht durch Herz-Kreislauf-Probleme, die die Nierenfunktion beeinflussen, jedoch spielen bei Herzinsuffizienz (HF) oft die Mechanismen innerhalb der Nieren eine größere Rolle.
            
            ### Wichtige Einsichten
            - **Herzleistung und Diuretikaresistenz:** Veränderungen in der Herzleistung sind meist nicht die Hauptursache für Diuretikaresistenz bei HF.
            - **Medikamenteneffekte:** Die Behandlung mit bestimmten Herzmedikamenten (z.B. Vasodilatatoren) verbessert nicht immer die Wirkung von Diuretika.
            
            ### Einfluss von Natriumaufnahme
            - **Salzkonsum:** Hoher Salzkonsum kann die Wirkung von Diuretika neutralisieren, was bedeutet, dass keine zusätzliche Flüssigkeit ausgeschieden wird.
            - **Behandlungsstrategien:** In einigen Fällen kann eine Kombination aus starken Diuretika und salzarmen Diäten oder die Verabreichung von Salzlösungen helfen, bessere Ergebnisse zu erzielen.
            
            ### Fazit
            Bei der Mehrheit der Patienten wird Diuretikaresistenz nicht durch Probleme mit dem Blutdruck oder der Herzleistung verursacht. Die Anpassung der Medikation ohne klare hämodynamische Ziele führt oft nicht zur Verbesserung.
                    """)


    with st.expander("Intrarenale Diuretikaresistenz bei Herzinsuffizienz"):
        st.write("""
        ### Was ist intrarenale Diuretikaresistenz?
        Intrarenale Diuretikaresistenz tritt auf, wenn trotz adäquater Diuretikadosierung die erwartete Diurese ausbleibt. Dies wird häufig durch Nierenfunktionsstörungen bei Herzinsuffizienz (HF) verursacht.
        
        ### Rolle der Nierenfunktion
        - **Nierenfunktion und Diurese:** Obwohl Nierenfunktionsstörungen oft als Hauptursache für Diuretikaresistenz gelten, zeigt die Forschung, dass die geschätzte glomeruläre Filtrationsrate (eGFR) nicht gut mit der diuretischen Reaktion bei HF korreliert.
        - **Natriumausscheidung:** Patienten mit HF und niedriger eGFR neigen dazu, mehr Natrium pro Nephron auszuscheiden, was eine Kompensation für die geringere Anzahl an Nephronen darstellt.
        
        ### Metabolische Faktoren
        - **Hypochlorämische metabolische Alkalose:** Die Induktion einer solchen Alkalose, oft durch Natriumbikarbonat verursacht, kann die diuretische Antwort erheblich reduzieren. Dies könnte auf eine Verringerung der luminalen Chloridkonzentration oder direkte Effekte des reduzierten intrazellulären Chlorids auf die Natriumregulation zurückzuführen sein.
        
        ### Forschung und Behandlung
        - **Forschungszustand:** Es wird weiterhin erforscht, welche Nephronsegmente am meisten zur tubulären Resistenz in HF beitragen und welche Mechanismen dafür verantwortlich sind.
        - **Behandlungsimpulse:** Die meisten Daten deuten darauf hin, dass Mechanismen jenseits der Henle-Schleife, insbesondere im distalen Tubulus, wesentlich zur Diuretikaresistenz bei adäquater Dosierung von Schleifendiuretika beitragen.
        
        ### Fazit
        Obwohl traditionell die Nierenfunktionsstörung als Haupttreiber der Diuretikaresistenz angesehen wird, weisen aktuelle Studien auf komplexe Wechselwirkungen und Kompensationsmechanismen hin, die für die Entwicklung effektiverer Behandlungsstrategien entscheidend sein können.
                """)

    with st.expander("Detaillierte Strategien zur Überwindung der Diuretikaresistenz"):
        st.write("""
        ### Optimierung der Schleifendiuretikadosierung
        - **Startdosis und Anpassung:** Beginnen mit einer empirischen Dosis, die auf früheren Reaktionen basiert. Wenn der Spot-Urinnatriumgehalt <50 mmol/l oder die Urinausscheidung <150 ml/h nach 2 Stunden beträgt, sollte die Dosis im Allgemeinen verdoppelt werden, bis eine maximale Dosis erreicht ist (häufig bis zu 200-300 mg Furosemid-Äquivalent).
        - **Überwachung und Titration:** Wiederholte Messung von Urinnatrium oder -volumen nach Dosisanpassung. Sobald eine adäquate natriuretische/diuretische Reaktion erreicht ist, kann die Dosis alle 6 bis 12 Stunden wiederholt werden.
        
        ### Kombinationstherapie
        - **Thiazide bei unzureichender Diurese:** Einsatz von Thiazid oder thiazidähnlichen Diuretika, wenn trotz maximaler Dosierung von Schleifendiuretika keine ausreichende Entwässerung erreicht wird. Metolazon ist häufig die erste Wahl.
        - **Schrittweise Titration:** Ein Algorithmus, der die schrittweise Erhöhung der Schleifendiuretikadosis mit der Hinzunahme von Thiaziddiuretika kombiniert, wird oft empfohlen, insbesondere wenn Ultrafiltration nicht den gewünschten Erfolg bringt.
        
        ### Adjunktive Therapien
        - **Spironolacton und seine Metaboliten:** Die Verwendung von Spironolacton kann bei einigen Patienten effektiv sein, jedoch sind längere Zeiträume als 96 Stunden nötig, um die Wirkungen von Canrenon, einem aktiven Metaboliten, zu beurteilen.
        - **Weitere Ergänzungsmittel:**
          - **Dopamin und Nesiritid:** Niedrig dosiertes Dopamin und Nesiritid zeigten in Studien keine klinischen Vorteile, könnten aber in bestimmten Subgruppen nützlich sein.
          - **Vasopressin-Antagonisten:** Tolvaptan und andere Vasopressin-Antagonisten können bei bestimmten Patienten die Diurese fördern.
          - **SGLT-2-Inhibitoren:** Diese zeigen diuretische Effekte und haben in klinischen Studien positive Ergebnisse erbracht. Ihr Einfluss speziell auf Diuretikaresistenz wird weiterhin erforscht.
        
        ### Fazit
        Ein integrierter und personalisierter Ansatz, der die spezifischen Ursachen der Diuretikaresistenz eines Patienten berücksichtigt, ist für eine effektive Behandlung entscheidend. Regelmäßige Überprüfungen und Anpassungen der Therapie sind notwendig, um optimale Ergebnisse zu erzielen.
                """)

    with st.expander("Tipps zur Diuretikatherapie für Kliniker"):
        st.write("""
        ### Anfangsdosierung von Schleifendiuretika bei hospitalisierten Patienten mit HF und Kongestion:
        - **Für Patienten mit langfristiger Schleifendiuretika-Therapie:** 2,5x ihre ambulante Dosis in mg (z.B. bei ambulanter Einnahme von 40 mg Furosemid zweimal täglich, anfängliche IV-Dosierung von 100 mg Furosemid zweimal täglich).
        - **Für Patienten ohne langfristige Schleifendiuretika-Therapie:** Eine empirische Anfangsdosis von 40–80 mg IV Furosemid oder ein Äquivalent zweimal täglich wird empfohlen.
        - **Häufigkeit der Verabreichung:** Aufgrund von post-dosierter Na⁺-Retention sollten IV-Schleifendiuretika mindestens zweimal täglich verabreicht werden.
        
        ### Anpassung der Diuretikadosierung:
        - **Folgedosen:** Sollten basierend auf der klinischen Reaktion auf die Anfangsdosen gesteuert werden. Eine ausreichende Dosis sollte innerhalb von 2 Stunden zu einem messbaren Anstieg der Urinproduktion führen.
        - **Unzureichende Reaktion:** Wenn die Anfangsdosis keine adäquate Reaktion zeigt, sollte die Dosierung erhöht werden, ohne auf die nächste geplante Dosis zu warten. Dosiserhöhungen sind in der Regel substanziell (z.B. Verdopplung).
        - **Urin-Na⁺-Monitoring:** Kann ebenfalls eine effektive Strategie sein, um die Diuretikadosierung zu steuern, obwohl dies in großen Studien noch nicht getestet wurde.
        
        ### Umgang mit zunehmendem Serumkreatinin während der diuretischen Therapie:
        - **Klinischer Kontext ist entscheidend:** Anstiege des Serumkreatinins (bis zu einem Anstieg von 0,5 mg/dl) sind während der diuretischen Behandlung üblich und erfordern nicht immer ein Stoppen oder Verringern der Schleifendiuretikadosierung, besonders wenn die Kongestion anhält.
        - **Klinische Studiendaten:** Solche Veränderungen sind üblicherweise vorübergehend und mit ähnlichen oder sogar besseren Langzeitergebnissen bei effektiver Entwässerung verbunden.
        
        ### Umgang mit Diuretikaresistenz:
        - **Identifikation der Resistenzmechanismen:** Kann individuelle Strategien zur Verbesserung der Diuretikareaktion erleichtern.
        - **Kombinationsnephronblockade:** Das Hinzufügen eines thiazidähnlichen Diuretikums (oft Metolazon) zu Schleifendiuretika kann zu einer robusten Diurese führen, birgt jedoch ein erhebliches Risiko für Elektrolytstörungen.
        - **Dosierung für Kombinationsnephronblockade:** Der Zeitpunkt für die Initiierung ist ungewiss.
        
        ### Anpassung der chronischen Schleifendiuretikadosierung während der Optimierung der GDMT:
        - **Ziel der Langzeitdosierung:** Verwendung der niedrigsten Dosis, die eine effektive Aufrechterhaltung des Volumenstatus ermöglicht.
        - **Optimierung der GDMT:** Kann eine Reduzierung der Schleifendiuretikadosierung ermöglichen, insbesondere zur Minderung des Risikos von Hypotonie oder Volumenerschöpfung (z.B. nach Beginn der Sacubitril-Valsartan-Therapie).
                """)


    
    st.subheader("Strategie basierend auf Urinausstoß zur Behandlung der Diuretikaresistenz")

    # Beginn mit Informationen zur anfänglichen Dosis
    initial_dose = st.number_input('Geben Sie die anfängliche Dosis des Schleifendiuretikums in mg ein (z.B. 80 mg für Schleifendiuretikum-naive Patienten):', min_value=0, value=80, step=10, key='diue_1')
    urine_output = st.number_input('Geben Sie den Urinausstoß in ml/h nach 2-6 Stunden ein:', min_value=0, value=0, step=1, key='urine')

    if st.button('Urinausstoß auswerten'):
        if urine_output > 150:
            st.success(f"Behalten Sie die aktuelle Dosis von {initial_dose} mg alle 6-12 Stunden bei, mit wiederholter Bewertung des Urinausstoßes nach jeder Dosis.")
            st.info("Diese Dosis hat zu einem adäquaten Urinausstoß geführt. Weiter so, um das Tagesziel zu erreichen.")
        elif urine_output <= 150:
            new_dose = min(300, initial_dose * 2)
            st.warning(f"Erhöhen Sie die IV-Schleifendiuretikumdosis auf {new_dose} mg. Wiederholen Sie dies bis zu einer maximalen Dosis von 300 mg Furosemidäquivalent.")
            if new_dose >= 300:
                st.error("Maximale Dosis erreicht. Erwägen Sie die Hinzunahme eines Thiaziddiuretikums.")
                add_thiazide = st.checkbox("Thiaziddiuretikum hinzufügen?")
                if add_thiazide:
                    st.success("Thiaziddiuretikum hinzugefügt. Überwachen Sie weiterhin den Urinausstoß und die klinische Reaktion.")
                add_second_line = st.checkbox("Zweite Linie des Diuretikums hinzufügen (z.B. Acetazolamid, Amilorid oder aldosteronantagonistische Diuretika)?")
                if add_second_line:
                    st.success("Zweite Diuretikalinie hinzugefügt. Überwachen Sie weiterhin den Urinausstoß und die klinische Reaktion.")
        else:
            st.error("Urinausstoß außerhalb des erwarteten Bereichs. Bitte überprüfen Sie den Wert und geben Sie ihn erneut ein.")
    
    st.write("### Anweisungen:")
    st.write("""
    - Beginnen Sie mit einer empirischen IV-Schleifendiuretikumdosis, entweder 2,5x die häusliche orale Dosis in geteilten Dosen oder 80 mg, wenn der Patient Schleifendiuretikum-naiv ist.
    - Messen Sie den Urinausstoß (UOP) nach 2-6 Stunden.
    - Wenn der UOP größer als 150 ml/h ist, wiederholen Sie die aktuelle Dosis alle 6-12 Stunden mit einer erneuten Bewertung des UOP nach jeder Dosis, um die täglichen UOP-Ziele zu erreichen.
    - Wenn der UOP kleiner oder gleich 150 ml/h ist, verabreichen Sie das IV-Schleifendiuretikum in doppelter vorheriger Dosis.
    - Wiederholen Sie dies bis zu einer IV-Schleifendiuretikumdosis von 300 mg Furosemidäquivalenten.
    - Wenn die Ziele mit einer Dosis von 300 mg nicht erreicht werden, erwägen Sie eine Kombinationsdiuretikablockade mit einem Schleifendiuretikum:
        - Erste Linie: Fügen Sie ein Thiaziddiuretikum hinzu.
        - Zweite Linie: Fügen Sie ein zusätzliches Diuretikum hinzu, das Acetazolamid, Amilorid oder aldosteronantagonistische Diuretikadosen enthalten kann.
    """)
    
    st.subheader("Strategie basierend auf Urin-Natrium zur Behandlung der Diuretikaresistenz")

    # Start mit der anfänglichen Dosisinformation
    initial_dose_2 = st.number_input('Geben Sie die anfängliche Dosis des Schleifendiuretikums in mg ein (z.B. 80 mg für Schleifendiuretikum-naive Patienten):', min_value=0, value=80, step=10, key='diu')
    sodium_level = st.number_input('Geben Sie den Urin-Natriumspiegel in mmol/l nach 1-2 Stunden ein:', min_value=0, value=0, step=1, key='sodium')
    
    if st.button('Urin-Natriumspiegel auswerten'):
        if sodium_level >= 50 and sodium_level <= 70:
            st.success(f"Behalten Sie die aktuelle Dosis von {initial_dose} mg alle 6-12 Stunden bei, mit wiederholter Bewertung des Urin-Natriums nach jeder Dosis.")
            st.info("Diese Dosis liegt im optimalen Bereich zur Erreichung einer effektiven Natriurese.")
        elif sodium_level < 50:
            new_dose = min(300, initial_dose * 2)
            st.warning(f"Erhöhen Sie die IV-Schleifendiuretikumdosis auf {new_dose} mg. Wiederholen Sie dies bis zu einer maximalen Dosis von 300 mg Furosemidäquivalent.")
            if new_dose >= 300:
                st.error("Maximale Dosis erreicht. Erwägen Sie die Hinzunahme eines Thiaziddiuretikums.")
                add_thiazide = st.checkbox("Thiaziddiuretikum hinzufügen?")
                if add_thiazide:
                    st.success("Thiaziddiuretikum hinzugefügt. Überwachen Sie weiterhin den Urin-Natriumspiegel und die klinische Reaktion.")
                add_second_line = st.checkbox("Zweite Linie des Diuretikums hinzufügen (z.B. Acetazolamid, Amilorid oder aldosteronantagonistische Diuretika)?")
                if add_second_line:
                    st.success("Zweite Diuretikalinie hinzugefügt. Überwachen Sie weiterhin den Urin-Natriumspiegel und die klinische Reaktion.")
        else:
            st.error("Urin-Natriumspiegel außerhalb des erwarteten Bereichs. Bitte überprüfen Sie den Wert und geben Sie ihn erneut ein.")
    
    st.write("### Anweisungen:")
    st.write("""
        - Beginnen Sie mit einer empirischen IV-Schleifendiuretikumdosis, entweder 2,5x die häusliche orale Dosis in geteilten Dosen oder 80 mg, wenn der Patient Schleifendiuretikum-naiv ist.
        - Nehmen Sie eine Urin-Natriumprobe nach 1-2 Stunden.
        - Wenn das Urin-Natrium ([UNa]) zwischen 50-70 mmol/l liegt, wiederholen Sie die aktuelle Dosis alle 6-12 Stunden mit einer erneuten Bewertung des Urin-Natriums nach jeder Dosis.
        - Wenn [UNa] weniger als 50-70 mmol/l beträgt, verabreichen Sie das IV-Schleifendiuretikum in doppelter vorheriger Dosis.
        - Wiederholen Sie dies bis zu einer IV-Schleifendiuretikumdosis von 300 mg Furosemidäquivalenten.
        - Wenn die Ziele mit einer Dosis von 300 mg nicht erreicht werden, erwägen Sie eine Kombinationsdiuretikablockade mit einem Schleifendiuretikum:
            - Erste Linie: Fügen Sie ein Thiaziddiuretikum hinzu.
            - Zweite Linie: Fügen Sie ein zusätzliches Diuretikum hinzu, das Acetazolamid, Amilorid oder aldosteronantagonistische Diuretikadosen enthalten kann.
        """)
    
    st.subheader('Stufenweises Vorgehen bei Diuretikaresistenz1 (nach Ellison und Felker 2017)')

    # Benutzereingaben
    furosemide_dose = st.number_input(
        'Geben Sie die vorherige tägliche orale Furosemid-Dosis in mg ein:',
        min_value=0, value=40, step=10, key='furo_dose'
    )

    # Basisrate für 40 mg Furosemid
    base_dose = 40
    base_rate = 5  # 5 mg/h für 40 mg Furosemid

    # Berechnung der Infusionsrate basierend auf der Eingabedosis
    if furosemide_dose > 0:  # Um Division durch Null zu vermeiden
        infusion_rate = (furosemide_dose / base_dose) * base_rate
        st.write(f"Empfohlene Infusionsrate für {furosemide_dose} mg Furosemid: {infusion_rate:.2f} mg/h")
    else:
        st.error("Die Dosis muss größer als 0 mg sein!")

    # Zusätzliche Informationen zur Dosierungsumrechnung
    bumetanide_dose = furosemide_dose / 40  # 1 mg Bumetanid entspricht 40 mg Furosemid
    torasemide_dose = (furosemide_dose * 20) / 40  # 20 mg Torasemid entspricht 40 mg Furosemid

    st.write(f"Äquivalente Dosis von Bumetanid: {bumetanide_dose:.2f} mg")
    st.write(f"Äquivalente Dosis von Torasemid: {torasemide_dose:.2f} mg")

    st.markdown("""
    Dieser Artikel diskutiert die Nutzung und die Strategien der diuretischen Therapie bei Patienten mit Herzinsuffizienz. Es werden verschiedene Aspekte der Diuretikaverwendung, ihre Effekte, sowie die optimalen Anwendungsweisen und mögliche Herausforderungen in der Behandlung erörtert.
    
    Vollständigen Artikel lesen: [Diuretische Therapie bei Herzinsuffizienz - Rosenfluh Publikationen](https://www.rosenfluh.ch/media/arsmedici-dossier/2018/05/Diuretische-Therapie-bei-Herzinsuffizienz.pdf)
        """)
    
    st.subheader('Perfusorrechner')

    # Eingaben für den Rechner
    tagesdosis = st.number_input('Geben Sie die Tagesdosis in mg ein (TD):', min_value=0.0, format='%f', key='tagesdosis')
    gesamtdosis = st.number_input('Geben Sie die Gesamtdosis in mg ein (GD), die in der Perfusor-Spritze vorhanden ist:', min_value=0.0, format='%f', key='gesamtdosis')
    gesamtvolumen = st.number_input('Geben Sie das Gesamtvolumen in ml ein (GV), das in der Spritze vorhanden ist:', min_value=0.0, format='%f', key='gesamtvolumen')
    stunden = st.number_input('Geben Sie die Anzahl der Stunden ein (ST), über die das Medikament verabreicht wird:', min_value=0.0, format='%f', key='stunden')

    # Berechnung der Laufrate
    if st.button('Berechne Laufrate in ml/h'):
        if gesamtdosis > 0 and stunden > 0:  # Überprüfung, ob Division durch Null verhindert wird
            laufrate = (tagesdosis * gesamtvolumen) / (gesamtdosis * stunden)
            st.write(f'Die Laufrate beträgt: {laufrate:.2f} ml/h')
        else:
            st.error('Die Gesamtdosis und die Stunden müssen größer als 0 sein!')

    st.write("### Eingabebeispiel")
    st.info("""
    - **Tagesdosis (TD):** 20 mg
    - **Gesamtdosis (GD):** 20 mg
    - **Gesamtvolumen (GV):** 50 ml
    - **Stunden (ST):** 24 h
    """)

    st.write("### Formel zur Berechnung der Laufrate")
    st.latex(r'''
    Laufrate = \frac{Tagesdosis \, (mg) \times Gesamtvolumen \, (ml)}{Gesamtdosis \, (mg) \times Stunden \, (h)}
    ''')
    
    

    with st.expander("Zusammenfassung zum Einsatz von Schleifendiuretika bei chronischer Herzinsuffizienz"):
        st.write("""
        - **Erhaltungsdosis erforderlich:** Die meisten Patienten mit chronischer HF benötigen eine Erhaltungsdosis eines oralen Schleifendiuretikums, um Euvolämie und klinische Stabilität zu gewährleisten.
        - **Auswahl des Diuretikums:** Die ideale Wahl des Schleifendiuretikums für Patienten mit chronischer HF ist ungewiss. Torasemid und Bumetanid haben eine bessere und vorhersehbare Bioverfügbarkeit als Furosemid, was einen theoretischen Vorteil darstellt.
        - **Dosierungshäufigkeit:** Schleifendiuretika sind in der Regel effektiver, wenn sie zweimal täglich dosiert werden, um Perioden zu minimieren, in denen die Konzentration im Tubulus unter ein therapeutisches Niveau fällt, was zu postdiuretischer Natriumretention führen kann.
        - **Vorteile von Torasemid:** Es gibt Daten, die darauf hindeuten, dass Torasemid im Vergleich zu Furosemid andere günstige Effekte hat, insbesondere in Bezug auf die Milderung von kardialer Fibrose, einem wichtigen Mechanismus der HF-Progression.
        - **TRANSFORM-HF-Studie:** Eine laufende große, pragmatische Outcomes-Studie vergleicht die Auswirkungen von Torasemid gegenüber Furosemid auf die Gesamtmortalität bei einer breiten Population von HF-Patienten.
        
        ### Absetzen von Diuretika
        - **Prognose bei Absetzen:** Beobachtungsdaten deuten darauf hin, dass HF-Patienten, die chronisch ohne Schleifendiuretikum verwaltet werden können, im Allgemeinen eine gute Prognose haben.
        - **Klinische Daten zum Absetzen:** Eine kürzlich präsentierte randomisierte klinische Studie zeigte, dass bei Patienten mit geringem Risiko (tägliche orale Dosis von Furosemid ≤ 80 mg, keine kürzlichen HF-Krankenhausaufenthalte und optimierte HF-Therapie) das Absetzen von Schleifendiuretika nicht mit einer Verschlechterung der Symptome oder einem Bedarf an erneuter Diuretikatherapie verbunden war.
                """)

# Zielhinweis
    st.write("### Behandlungsziel")
    st.info("Das Behandlungsziel besteht in einer täglichen Harnmenge von 3–5 Litern, bis eine klinische Euvolämie erreicht ist. Zu Beginn kann eine intravenöse Applikation der 2,5-fachen vorherigen täglichen oralen Furosemiddosis oder eine Infusion, wie oben beschrieben, vorgenommen werden. Die Harnausscheidung kann täglich durch den Übergang zu einer höheren Stufe erhöht werden, wenn die ausgeschiedene Menge weniger als 3 Liter beträgt.")


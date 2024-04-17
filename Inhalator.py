#!/usr/bin/env python
# coding: utf-8

# In[34]:


import streamlit as st

def Inhalator():
    class Patient:
        def __init__(self, spontane_atmung, gute_koordination, inspirationsfluss):
            self.spontane_atmung = spontane_atmung
            self.gute_koordination = gute_koordination
            self.inspirationsfluss = inspirationsfluss

    class Inhalator:
        empfehlungen = {
            'überdruck': {
                'beschreibung': "Überdruckinhalator mit Spacer oder Vernebler",
                'hinweise': "Geeignet für intubierte oder beatmete Patienten."
            },
            'koordination_niedrig_fluss_hoch': {
                'beschreibung': "Dosieraerosol mit Spacer oder atemzugsgesteuert, Vernebler",
                'hinweise': "Für Patienten mit unzureichender Koordination, aber gutem Inspirationsfluss."
            },
            'koordination_niedrig_fluss_niedrig': {
                'beschreibung': "Dosieraerosol mit Spacer, ggf. mit Maske, oder Sprühvernebler",
                'hinweise': "Für Patienten mit unzureichender Koordination und geringem Inspirationsfluss, z.B. Kinder."
            },
            'koordination_hoch_fluss_hoch': {
                'beschreibung': "Dosieraerosol oder Trockenpulverinhalator",
                'hinweise': "Für Patienten mit guter Koordination und ausreichendem Inspirationsfluss."
            },
            'koordination_hoch_fluss_niedrig': {
                'beschreibung': "Dosieraerosol oder Sprühvernebler",
                'hinweise': "Für Patienten mit guter Koordination, aber geringem Inspirationsfluss, z.B. bei schwerer Obstruktion."
            }
        }

        @staticmethod
        def empfehlung_für_inhalationssystem(patient):
            if patient.spontane_atmung == "Nein":
                return Inhalator.empfehlungen['überdruck']
            if patient.gute_koordination == "Nein":
                if patient.inspirationsfluss > 30:
                    return Inhalator.empfehlungen['koordination_niedrig_fluss_hoch']
                return Inhalator.empfehlungen['koordination_niedrig_fluss_niedrig']
            if patient.inspirationsfluss > 30:
                return Inhalator.empfehlungen['koordination_hoch_fluss_hoch']
            return Inhalator.empfehlungen['koordination_hoch_fluss_niedrig']

    # Starten der Streamlit-Anwendung mit Benutzereingaben
    st.header("Der richtige Inhalator?")
    # Streamlit Widgets zur Eingabe von Patientendaten
    spontane_atmung = st.radio("Hat der Patient eine spontane Atmung?", ("Ja", "Nein"))
    gute_koordination = st.radio("Hat der Patient eine gute Koordination?", ("Ja", "Nein"))
    inspirationsfluss = st.number_input("Bitte geben Sie den Inspirationsfluss des Patienten ein:", min_value=0, max_value=100, step=1, value=30)

    # Erstellen des Patientenobjekts mit den eingegebenen Daten
    patient = Patient(spontane_atmung, gute_koordination, inspirationsfluss)

    if st.button("Empfehlung anzeigen"):
        # Abrufen der Empfehlung basierend auf den eingegebenen Informationen
        empfehlung = Inhalator.empfehlung_für_inhalationssystem(patient)
        st.success(f"Empfohlenes Inhalationssystem: {empfehlung['beschreibung']}")
        st.success(f"Hinweise: {empfehlung['hinweise']}")
            
        
    with st.expander("Informationen über Pulverinhalatoren"):
        st.write("""
        **Allgemeine Informationen:**
        - Es gibt Pulverinhalatoren mit gerätebedingt mittlerem bis hohem Strömungswiderstand.
        - Bei allen Pulverinhalatoren ist ein gerätespezifischer minimaler Inspirationsfluss notwendig, um die optimale Freisetzung des Wirkstoffs zu erzielen.
        - **Wichtig:** Der Patient muss einen geeigneten Inspirationsdruck aufbringen können!

        **Pulverinhalatoren mit mittlerem Widerstand:**
        - Erfordern geringere inspiratorische Kraft im Vergleich zu Geräten mit hohem Widerstand.
        - Inhalation sollte als langsame Einatmung erfolgen.

        **Pulverinhalatoren mit hohem Widerstand:**
        - Benötigen größere inspiratorische Kraft als solche mit mittlerem Widerstand.
        - Höhere Turbulenzen im Inhalator erleichtern die Trennung des Wirkstoffs von der Trägersubstanz (Desagglomeration).
        - Inhalation: Kräftige und schnelle Einatmung.
        - Abhängig von den Lungenfunktionswerten.
        - Messung des Peak-Inspiratory-Flow (PIF) vor Verordnung erleichtert die Auswahl des passenden Systems. Beachten Sie, dass PIF-Messgeräte im klinischen Alltag nicht weit verbreitet sind und PIF ggfs. ohne Gerätewiderstand gemessen wird, was das Ergebnis beeinflussen kann.

        **Besondere Überlegungen bei FEV1 < 50% des Sollwertes:**
        - Überprüfen Sie, ob der Patient den zum Entleeren und zur Freisetzung des Wirkstoffs nötigen inspiratorischen Fluss erzeugen kann.
        - Maximaler Inspirationsdruck und inspiratorische Flüsse können z.B. vermindert sein bei:
            - Lungenüberblähung (schwere COPD, u.a.)
            - Schwäche der Atemmuskeln (neuro-muskuläre Erkrankungen)
            - Thoraxdeformität (Skoliose, u.a.)
        """)

    with st.expander("Zusammenfassung über Dosieraerosole und Sprühvernebler"):
        st.write("""
            - **Geringer Strömungswiderstand:** Besonders geeignet für Patienten, die nur einen geringen maximalen inspiratorischen Druck (PImax) erzeugen können.
            - **Inhalation aus einem Dosieraerosol:** Sollte langsam und kontinuierlich erfolgen.
            - **Inhalation aus einem Sprühvernebler:** Sehr langsam und kontinuierlich durchführen.
            - **Elektrische Vernebler:**
                - Das normale Atemzugvolumen wird ein- und ausgeatmet.
                - Inhalation sollte möglichst langsam und ausreichend tief erfolgen.
            """)

    # Laden und Anzeigen des Bildes
    image_path = "atemarbeit.jpg"
    st.image(image_path, caption="Atemarbeit")

    # Anzeigen des Links
    st.markdown("[Richtig inhalieren - Informationen und Auswahl des richtigen Inhalationssystems (PDF)](https://www.atemwegsliga.de/richtig-inhalieren.html?file=files/eigene-dateien/informationsmaterial/Praesentationen/Auswahl-Inhalationssystem.pdf&cid=2361)")

    # Laden und Anzeigen des Bildes
    image_path = "Inhalator.jpg"
    st.image(image_path, caption="Inhalator")

    # Anzeigen des Links
    st.markdown("[Link zur COPD Inhaler Device Chart Poster](https://lungfoundation.com.au/resources/copd-inhaler-device-chart-poster/)")




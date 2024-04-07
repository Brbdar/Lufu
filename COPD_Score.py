#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st

def COPD_Score():
    st.header("COPD Score")
    
    st.write("""
        ### Bewertung der Evidenz

        Der COPD-Bewertungstest wurde ursprünglich in einer Kohorte von 1.503 Patienten entwickelt, die 6 Länder repräsentieren (Jones 2009). Es wurde gezeigt, dass er ein zuverlässiges Maß für die Gesamtschwere der COPD aus der Perspektive des Patienten bietet, unabhängig von der Sprache.

        Hinsichtlich der Validität wurde auch gezeigt, dass er sowohl mit der Mortalität (Husebø 2016 fand ein Hazard-Ratio von 1,24 (1,05-1,37, p<0,01) für jede 8-Punkte-Erhöhung) als auch mit den Ergebnissen in der pulmonalen Rehabilitation korreliert (Dodd 2011). Es besteht auch eine hohe Korrelation mit dem St. George’s Respiratory Questionnaire (r = 0,84 über sieben europäische Länder (Jones 2011) und r = 0,80 in den USA (Jones 2009)).

        Derzeit wird Forschung betrieben, um Bereiche der CAT-Score-Schwere zu definieren und ein besseres Verständnis für die minimal klinisch relevante Änderung eines CAT-Scores von einem Besuch zum nächsten zu erlangen.
        """)
    
    with st.expander("Überblick und Messqualitäten"):
        st.write("""
        Diese Studie hat einen kurzen, einfachen, von Patienten ausgefüllten Fragebogen für COPD mit sehr guten Messqualitäten erstellt. Trotz der geringen Anzahl von Komponenten deckt er eine breite Palette von Auswirkungen der COPD auf die Gesundheit der Patienten ab. Die Qualität der Anpassung an ein Rasch eindimensionales Modell deutet darauf hin, dass es echte Intervallskalierungseigenschaften besitzt. Basierend auf Daten aus sechs Ländern zeigen Tests der internen Konsistenz, dass es ein zuverlässiges Maß für die Gesamtschwere der COPD aus der Perspektive des Patienten bietet, unabhängig von der Sprache.
    """)

    with st.expander("Entwicklungsprozess und Item-Reduktion"):
        st.write("""
        Der Prozess der Item-Reduktion folgte einer strengen Methodik, die klassische Testtheorie und IRT kombinierte, zusammen mit sorgfältiger Überwachung des Inhalts. Items mit schlechten Messqualitäten wurden entfernt, während eine breite Abdeckung der verschiedenen Auswirkungen der COPD erhalten blieb. Bei der Entscheidung, ob ein Item während der Fragebogenentwicklung einbezogen oder ausgeschlossen werden sollte, war es notwendig, seine Schwächen und Stärken gegenüber seinem Gesamtbeitrag abzuwägen. Ein Item wurde nicht aufgrund eines einzelnen Kriteriums ausgeschlossen, sondern wegen seiner Gesamtleistung im Vergleich zu den anderen. Entwickler- und klinisches Urteil waren in diesem Prozess erforderlich.
        """)

    with st.expander("Endgültiger Inhalt und Format"):
        st.write("""
        Der endgültige Inhalt umfasst Husten, Schleim, Brustenge, Atemnot beim Aufsteigen von Hügeln/Treppen, Aktivitätsbeschränkung zu Hause, Vertrauen, das Haus zu verlassen, Schlaf und Energie. Das Prinzip, dass das Instrument zuverlässige Messqualitäten haben sollte, mit allen Items, die strenge statistische Anforderungen erfüllen, wurde erreicht. Der endgültige CAT besteht aus acht Items, die jeweils als semantische sechspunktige Differenzialskala formatiert sind, was das Werkzeug leicht zu administrieren und für Patienten leicht auszufüllen macht. Die Items wurden ausgewählt, um eine breite Palette von Krankheitsschweregraden abzudecken.
        """)

    with st.expander("Limitationen und Validierung"):
        st.write("""
        Eine Einschränkung dieser Studie ist, dass die Zuverlässigkeits- und Validierungsbefunde nur auf Daten aus den USA basieren. Es ist jedoch klar, dass der CAT sehr ähnliche diskriminative Eigenschaften wie der wesentlich komplexere SGRQ-C aufweist, was zeigt, dass er in der Lage sein wird, die Auswirkungen der COPD auf die Gesundheit einzelner Patienten zu messen. Die Validierung eines Instruments ist ein kontinuierlicher Prozess, und internationale Studien werden durchgeführt, um seine psychometrischen Eigenschaften weiter zu testen. Der CAT wird Klinikern und Patienten ein einfaches und zuverlässiges Maß für den allgemeinen gesundheitlichen Status im Zusammenhang mit COPD zur Beurteilung und langfristigen Nachverfolgung einzelner Patienten bieten.
        """)

    # Titel der Webanwendung
    st.title("CAT-Score Rechner für Lungenerkrankungen")

    # Symptome und deren Beschreibungen
    symptome = {
        "Husten": "0 ('Ich huste nie') bis 5 ('Ich huste ständig')",
        "Schleim": "0 ('Ich habe überhaupt keinen Schleim in der Brust') bis 5 ('Meine Brust ist vollständig mit Schleim gefüllt')",
        "Brustenge": "0 ('Meine Brust fühlt sich überhaupt nicht eng an') bis 5 ('Meine Brust fühlt sich sehr eng an')",
        "Atemnot": "0 ('Beim Gehen auf einen Hügel oder eine Treppe bekomme ich keine Luftnot') bis 5 ('Beim Gehen auf einen Hügel oder eine Treppe bin ich sehr kurzatmig')",
        "Aktivitäten": "0 ('Ich bin bei keiner Aktivität zu Hause eingeschränkt') bis 5 ('Ich bin bei Aktivitäten zu Hause sehr eingeschränkt')",
        "Vertrauen": "0 ('Ich bin zuversichtlich, mein Haus trotz meiner Lungenerkrankung zu verlassen') bis 5 ('Ich habe kein Vertrauen, mein Haus wegen meiner Lungenerkrankung zu verlassen')",
        "Schlaf": "0 ('Ich schlafe fest') bis 5 ('Ich schlafe wegen meiner Lungenerkrankung nicht fest')",
        "Energie": "0 ('Ich habe viel Energie') bis 5 ('Ich habe überhaupt keine Energie')"
    }

    # Slider für jedes Symptom
    scores = {symptom: st.slider(f"{symptom} ({beschreibung})", min_value=0, max_value=5, value=0) for symptom, beschreibung in symptome.items()}

    # Berechnung der Gesamtpunktzahl
    total_score = sum(scores.values())

    # Interpretation des CAT-Scores
    if total_score <= 10:
        health_impact = "Niedrig"
        recommendation = "Raucherentwöhnung, präventive Pflege und Reduzierung der Expositionsrisikofaktoren; LAMA und Notfallinhalatoren in Betracht ziehen"
    elif total_score <= 20:
        health_impact = "Mittel"
        recommendation = "Raucherentwöhnung, präventive Pflege, Reduzierung der Expositionsrisikofaktoren, und LAMA und Notfallinhalatoren; ICS und/oder LABA, Überweisungen zur Lungensanierung, und mögliche Bewertung der Lungentransplantation in Betracht ziehen"
    elif total_score <= 30:
        health_impact = "Hoch"
        recommendation = "Raucherentwöhnung, präventive Pflege, Reduzierung der Expositionsrisikofaktoren, ICS/LABA/LAMA-Therapie, Überweisungen zur Lungensanierung, mögliche Bewertung der Lungentransplantation und O₂-Supplementierung"
    else:
        health_impact = "Sehr hoch"
        recommendation = "Spezifische Empfehlungen basierend auf individueller Bewertung"

    # Anzeige des Ergebnisses
    st.write(f"### CAT-Score: {total_score}")
    st.write(f"### Gesundheitliche Auswirkung: {health_impact}")
    st.write(f"### Empfehlung: {recommendation}")
    
    st.markdown("""
    Development and first validation of the COPD Assessment Test

    P. W. Jones, G. Harding, P. Berry, I. Wiklund, W-H. Chen, N. Kline Leidy  
    *European Respiratory Journal* 2009 34: 648-654; DOI: [10.1183/09031936.00102509](https://erj.ersjournals.com/content/34/3/648.long)
    """)



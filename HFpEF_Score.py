#!/usr/bin/env python
# coding: utf-8

# In[10]:


import streamlit as st

def HFpEF_Score():
    st.header("HFpEF Score")
    
    with st.expander("Verständnis von HFpEF"):
        st.write("""
        HFpEF, Herzinsuffizienz mit erhaltener Ejektionsfraktion, macht die Hälfte aller Krankenhausaufenthalte aufgrund von Herzinsuffizienz aus. Bei hospitalisierten Patienten sind Symptome wie offensichtliche Überlastung leicht durch körperliche Untersuchung, Thoraxröntgen und natriuretische Peptid-Tests erkennbar. Im Gegensatz dazu fehlen bei ambulanten Patienten mit Belastungsdyspnoe oft klare Anzeichen einer Überlastung in Ruhe, was die Diagnose erschwert.
        """)

    with st.expander("Die Rolle des H2FPEF Scores"):
        st.write("""
        Der H2FPEF Score wurde entwickelt und validiert, um die Wahrscheinlichkeit von HFpEF zu bewerten, indem er klinische und echokardiographische Variablen nutzt. Dieser Score hilft, HFpEF bei Patienten mit niedrigen Werten auszuschließen, bei höheren Werten die Diagnose mit hoher Zuversicht zu stellen und bei Zwischenwerten auf den Bedarf weiterer Tests hinzuweisen.
        """)

    with st.expander("Auswahl und Bedeutung des Endmodells"):
        st.write("""
        Das Endmodell kombiniert Variablen, die aufgrund ihrer zentralen Rolle in der Pathogenese von HFpEF ausgewählt wurden, wie Adipositas und Vorhofflimmern. Diese Auswahl erfolgte durch multiple logistische Regressionsanalyse und agnostische CART, unter Berücksichtigung der Diskriminierungsfähigkeit und Einfachheit der Berechnung.
        """)

    with st.expander("Assoziation von Komorbiditäten mit HFpEF"):
        st.write("""
        HFpEF wird als systemische Störung angesehen, die größtenteils durch Komorbiditäten wie Adipositas und Vorhofflimmern angetrieben wird. Die Analyse zeigte, dass diese Bedingungen unabhängig die Wahrscheinlichkeit erhöhen, dass HFpEF vorliegt, während die Präsenz von Diabetes mellitus über Adipositas hinaus keinen zusätzlichen diagnostischen Wert bietet.
        """)

    st.title('HFpEF Score Berechnung')

# Eingabe der Benutzerdaten
    age = st.number_input('Alter in Jahren', value=30, min_value=18, max_value=120)
    bmi = st.number_input('BMI', value=25.0, min_value=10.0, max_value=50.0)
    e_e_prime_ratio = st.number_input("E/e' Verhältnis", value=10.0, min_value=1.0, max_value=30.0)
    pasp = st.number_input("Pulmonalarterieller systolischer Druck in mmHg", value=25, min_value=10, max_value=100)
    af = st.selectbox('Vorhofflimmern', options=['Nein', 'Ja'])
    af_bin = 1 if af == 'Ja' else 0  # Für die Berechnung des Scores

    # Funktion zur Berechnung des HFpEF-Scores basierend auf kontinuierlichen Variablen
    def calculate_hfpef_score(age, bmi, e_e_prime_ratio, pasp, af):
        y = -9.1917 + 0.0451 * age + 0.1307 * bmi + 0.0859 * e_e_prime_ratio + 0.0520 * pasp + 1.6997 * af
        z = pow(2.7183, y)  # e^y
        probability = (z / (1 + z)) * 100  # Umwandlung in Prozent
        return probability

    def calculate_hfpef_points(af, bmi, pasp, e_e_prime_ratio, age):
        points = 0
        debug_info = []  # Liste zum Speichern von Debug-Informationen
    
        if af == 1:
            points += 3
            debug_info.append("Vorhofflimmern: +3")
        if bmi > 30:
            points += 2
            debug_info.append("BMI > 30: +2")
        if pasp > 35:
            points += 1
            debug_info.append("PASP > 35: +1")
        if e_e_prime_ratio > 9:
            points += 1
            debug_info.append("E/e′ > 9: +1")
        if age > 60:
            points += 1
            debug_info.append("Alter > 60: +1")
    
        return points

    def interpret_hfpef_points(points):
        if points <= 1:
            return "HFpEF kann relativ sicher ausgeschlossen werden."
        elif 2 <= points <= 5:
            return "Weitere Diagnostik ist nötig."
        elif points >= 6:
            return "HFpEF kann relativ sicher diagnostiziert werden."

    if st.button('HFpEF Score berechnen'):
        points = calculate_hfpef_points(af_bin, bmi, pasp, e_e_prime_ratio, age)
        score = calculate_hfpef_score(age, bmi, e_e_prime_ratio, pasp, af_bin)
        interpretation = interpret_hfpef_points(points)

        st.write(f"Erreichte Punktzahl basierend auf diskreten Kriterien: {points}")
        st.write(f"Interpretation der Punktzahl: {interpretation}")
        st.write(f"Basierend auf den kontinuierlichen Variablen beträgt der HFpEF-Score: {score:.2f}%")
    
    with st.expander("Über die Forschung"):
        st.markdown("""
        Der H2FPEF Score basiert auf der Forschung von Yogesh N.V. Reddy, Rickey E. Carter, Masaru Obokata, Margaret M. Redfield und Barry A. Borlaug, die in ihrem Artikel *A Simple, Evidence-Based Approach to Help Guide Diagnosis of Heart Failure With Preserved Ejection Fraction* einen evidenzbasierten Ansatz zur Unterstützung der Diagnose von Herzinsuffizienz mit erhaltener Ejektionsfraktion (HFpEF) vorschlagen.

        Diese Studie liefert wichtige Einsichten in die Diagnose von HFpEF, indem sie einen neuen Score einführt, der klinische und echokardiografische Variablen verwendet, die in der klinischen Praxis weit verbreitet sind. Ziel ist es, Ärzten ein Werkzeug an die Hand zu geben, mit dem sie HFpEF effektiver diagnostizieren können, insbesondere in Fällen, in denen die Diagnose aufgrund fehlender offensichtlicher Symptome schwierig ist.

        Weitere Details zur Studie und zum H2FPEF Score finden Sie im vollständigen Artikel, veröffentlicht in *Circulation*, unter dem folgenden Link:
        [Circulation. 2018;138:861–870](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.118.034646)
        """, unsafe_allow_html=True)


# In[ ]:





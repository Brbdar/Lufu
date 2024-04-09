#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st

def erguss1():
    # Titel der App
    st.title('Diagnose-Tool für Pleuraergüsse')

    # Unterüberschrift
    st.header("Pleuraerguss")

    # Informationen zu den Light-Kriterien
    st.write('Informationen zu den Light-Kriterien')
    
    with st.expander("Die Entwicklung der Light-Kriterien"):
        st.write("""
        Als ich 1968 bis 1969 Internist am Johns Hopkins Hospital in Baltimore, Maryland, war, hatte ein großer Prozentsatz meiner Patienten einen Pleuraerguss. Der Oberarzt, Dr. Richard Winterbauer, machte seine Runden um Mitternacht und fragte mich immer, was die Thorazentese ergeben hatte. Zu dieser Zeit maßen wir routinemäßig die Zellzahl und Differenzierung, Glukose und Protein und führten Abstriche und Kulturen auf der Pleuraflüssigkeit durch. Ich fragte Dr. Winterbauer nach der Bedeutung ...
        """)

    with st.expander("Warum die Light-Kriterien immer noch nützlich sind"):
        st.write("""
        Die erste Referenz, die den Namen der Light-Kriterien verwendet, die mir bekannt ist, wurde 1989 veröffentlicht. Seit der ursprünglichen Veröffentlichung im Jahr 1972 gab es viele Studien, die andere Messungen mit den Light-Kriterien für die Trennung von Transsudaten und Exsudaten verglichen haben, aber im Allgemeinen haben sich die Light-Kriterien als besser erwiesen als alles andere. Ich bin erstaunt, dass die Light-Kriterien nach 40 Jahren immer noch verwendet werden.
        """)

    with st.expander("Transsudative Ergüsse, die durch die Light-Kriterien fehlklassifiziert wurden"):
        st.write("""
        Wenn die Light-Kriterien verwendet werden, wie werden diese transsudativen Pleuraergüsse identifiziert, die fälschlicherweise klassifiziert wurden? Wenn klinisch der Verdacht besteht, dass ein Patient einen transsudativen Erguss hat, aber exsudative Kriterien nur knapp erfüllt sind (Proteinverhältnis zwischen 0,5 und 0,65, LDH-Verhältnis zwischen 0,6 und 1,0, pleurale Flüssigkeits-LDH zwischen zwei Dritteln und der oberen Normalgrenze für Serum), sollte versucht werden zu bestimmen, ob der Patient wirklich einen transsudativen Erguss hat. Die 2 Hauptmaßnahmen, die ...
        """)

    # Zusammenfassung der Light-Kriterien
    st.markdown("""
    **Zusammenfassung:**

    Die Light-Kriterien dienen als guter Ausgangspunkt bei der Trennung von Transsudaten von Exsudaten. Die Light-Kriterien klassifizieren etwa 25% der Transsudate fälschlicherweise als Exsudate, und die meisten dieser Patienten nehmen Diuretika. Wenn angenommen wird, dass ein Patient wahrscheinlich eine Krankheit hat, die einen transsudativen Pleuraerguss verursacht, aber die Light-Kriterien deuten nur knapp auf ein Exsudat hin, sollte der Serum-Pleuraflüssigkeits-Protein-Gradient untersucht werden. Wenn dieser größer als 3,1 gm/dL ist, hat der Patient wahrscheinlich ein ...
    """)

    # Input fields for required values
    st.write('Bitte geben Sie die folgenden Werte ein:')
    serum_protein = st.number_input('Serumprotein (g/dL)', format="%.2f")
    pleural_fluid_protein = st.number_input('Pleurale Flüssigkeitsprotein (g/dL)', format="%.2f")
    serum_ldh = st.number_input('Serum LDH (U/L)', format="%.2f")
    pleural_fluid_ldh = st.number_input('Pleurale Flüssigkeits-LDH (U/L)', format="%.2f")
    serum_ldh_upper_limit = st.number_input('Obergrenze des normalen Serum-LDH (U/L)', format="%.2f")

    # Initialize criteria as False
    criteria_1 = criteria_2 = criteria_3 = False

    # Check and calculate each criterion
    if serum_protein > 0:
        criteria_1 = pleural_fluid_protein / serum_protein > 0.5
    if serum_ldh > 0:
        criteria_2 = pleural_fluid_ldh / serum_ldh > 0.6
    if serum_ldh_upper_limit > 0:
        criteria_3 = pleural_fluid_ldh > 2/3 * serum_ldh_upper_limit

    # Display result based on criteria
    if st.button('Diagnose'):
        if criteria_1 or criteria_2 or criteria_3:
            st.success('Basierend auf Lights Kriterien handelt es sich um einen exsudativen Erguss.')
            st.info('Bitte beachten Sie, dass Lights Kriterien eine hohe Sensitivität (98%) für exsudative Ergüsse aufweisen, die Spezifität jedoch nur 83% beträgt.')
        else:
            st.error('Basierend auf Lights Kriterien handelt es sich nicht um einen exsudativen Erguss.')
            st.info('Falls erforderlich, konsultieren Sie weitere diagnostische Verfahren.')
    
    # Wichtige Informationen und Referenzen
    st.markdown('''
    **Wichtige Informationen:**
    - *Sensitivität und Spezifität der Lights Kriterien:* Lights Kriterien haben eine Sensitivität von 98% und eine Spezifität von 83% für die Identifizierung exsudativer Ergüsse.
    - *Evidenzbewertung:* Die original prospektive Studie umfasste 150 verschiedene Patienten, deren Pleuraflüssigkeitsanalysen ausgewertet wurden. Mehr als 70% der Exsudate wurden mit den Lights Kriterien korrekt identifiziert, jedoch wurden 10% der Exsudate fälschlicherweise als Transudate klassifiziert.
    ''')

    st.markdown("""
    # Zellen in Pleuraflüssigkeit
    ## Ihr Wert in der Differentialdiagnose
    **Richard W. Light, MD; Yener S. Erozan, MD; Wilmot C. Ball Jr., MD**

    Author Affiliations: *Arch Intern Med.* 1973;132(6):854-860. doi:[10.1001/archinte.1973.03650120060011](https://doi.org/10.1001/archinte.1973.03650120060011)

    Volltext des Artikels verfügbar unter: [JAMA Network](https://jamanetwork.com/journals/jamainternalmedicine/article-abstract/582207)
    """)




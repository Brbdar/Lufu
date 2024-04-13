#!/usr/bin/env python
# coding: utf-8

# In[16]:


import streamlit as st
import numpy as np
import streamlit as st
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def raai():
    import math


    st.title('Echocardiographic evaluation of right ventricular diastolic function in pulmonary hypertension')

    
    with st.expander("Infos"):
        st.write("""
        
        Die Diastole:
        - **Diastolische Funktion:** Während der Diastole entspannt sich das Herz und erlaubt den Einstrom von Blut in die Ventrikel. Die Effizienz dieser Phase ist entscheidend für die gesamte Herzfunktion.
        Gewebedopplemessungen:
        - ** Tissue Doppler Imaging (TDI) ist eine Ultraschalltechnik, die es ermöglicht, die Geschwindigkeiten von Herzmuskelbewegungen zu messen. Diese Methode ist besonders nützlich für die Bewertung der diastolischen Funktion des Herzens, d.h. wie gut sich die Herzkammern mit Blut füllen.
        - **TDI-Messungen:** TDI misst die Geschwindigkeit der Myokardfasern während der Systole und Diastole. Diese Geschwindigkeiten sind Indikatoren für die Myokardfunktion und können Aufschluss über die Herzmuskelfunktion geben.
        
        Klinische Bedeutung:
        - **Systolische und frühdiastolische Geschwindigkeiten:** Diese sind durch TDI im linken Ventrikel messbar und korrelieren mit dem Grad der Fibrose und der Dichte der Beta-adrenergen Rezeptoren bei Patienten mit regionaler Dysfunktion des linken Ventrikels.
        - **E/e' und E/A-Verhältnisse:** Diese häufig verwendeten Parameter zur Bewertung der LV-Diastolik sind durch die TDI-Methode leicht zu ermitteln. Für die rechte Kammer (RV) sind diese Parameter jedoch noch nicht vollständig validiert.
        
        Rechter Vorhof bei rechtsventrikulärer Dysfunktion:
        - **Steifigkeit des rechten Ventrikels:** Bei Zuständen wie pulmonaler Hypertonie führt eine erhöhte Steifigkeit des rechten Ventrikels zu einem erschwerten Bluteinstrom während der Diastole. Dies hat direkte Auswirkungen auf den rechten Vorhof.
        - **Rückstau:** Die erhöhte Steifigkeit des Ventrikels kann dazu führen, dass es während der Vorhofkontraktion (Atriumkontraktion) zu einem Rückstau in den großen Venen wie der Vena cava kommt. Dieser Zustand wird oft als "Vena Cava Backflow" bezeichnet und deutet auf eine beeinträchtigte Füllung des rechten Ventrikels hin. """)
    
    # Benutzereingaben über Streamlit's interaktive Widgets
    hoehe_cm = st.number_input("Geben Sie die Körpergröße in cm ein:", min_value=0.0, format="%.2f")
    gewicht_kg = st.number_input("Geben Sie das Gewicht in kg ein:", min_value=0.0, format="%.2f")
    s_prime = st.number_input("Geben Sie den S'-Wert ein:", min_value=0.0, format="%.2f")
    ra_esa = st.number_input("Geben Sie den RA_ESA-Wert ein:", min_value=0.0, format="%.2f")

    def berechne_bsa(hoehe_cm, gewicht_kg):
        return math.sqrt((hoehe_cm * gewicht_kg) / 3600)

    def berechne_raai(ra_esa, bsa):
        st.write(f"RA_ESA: {ra_esa}, BSA: {bsa}")  # Debugging-Ausgabe
        if bsa == 0:
            st.error("BSA darf nicht Null sein. Bitte überprüfen Sie die Eingaben für Höhe und Gewicht.")
            return 0
        else:
            return ra_esa / bsa

    def medizinischer_befund(raai):
        st.write("Medizinischer Befund zum S'/RAAi-Quotienten:")
        if raai >= 0.81:
            st.success("Ein RAAi von ≥ 0.81 m²/(s·cm) deutet auf das Fehlen einer relevanten RV diastolischen Dysfunktion hin. Der Wert zeigt eine gute RV diastolische Funktion und ist prognostisch günstig.")
        else:
            st.error("Ein RAAi von < 0.81 m²/(s·cm) ist ein Hinweis auf mögliche RV diastolische Dysfunktion. Es wird empfohlen, eine detaillierte diagnostische Untersuchung zu erwägen, um weitere klinische Maßnahmen zu planen.")

    # BSA berechnen
    bsa = berechne_bsa(hoehe_cm, gewicht_kg)

    # RAAi berechnen
    raai = berechne_raai(ra_esa, bsa)

    st.write(f"Berechneter RAAi: {raai:.2f}")

    # Medizinischer Befund basierend auf dem berechneten Wert ausgeben
    medizinischer_befund(raai)

    st.markdown("""
    About..

    **Authors:** Athiththan Yogeswaran, Zvonimir A. Rako, Selin Yildiz, Hossein Ardeschir Ghofrani, Werner Seeger, Bruno Brito da Rocha, Henning Gall, Nils C. Kremer, Philipp Douschan, Silvia Papa, Carmine Dario Vizza, Domenico Filomena, Ryan J. Tedford, Robert Naeije, Manuel J. Richter, Roberto Badagliacca, Khodr Tello

    [Read the full article here](https://openres.ersjournals.com/content/erjor/early/2023/06/29/23120541.00226-2023.full.pdf)
    """)
    
    
    st.title('Quantify right ventricular stiffness - EED Calculator invasive')

    st.markdown("<p style='text-align: center; font-size: small;'>WebApp by Bruno Brito da Rocha <br> <a href='https://twitter.com/BrunoRaphaelDd' target='_blank'>BrunoRaphaelDd</a> <br> <a href='https://twitter.com/GiessenPh' target='_blank'>Team Giessen UKGM PH Tello et al.</a></p>", unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    data = []
    info_texts = []
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Unterschiedliche Farben für bis zu drei EEDs

    def func(x, a, b):
        return a * (np.exp(x * b) - 1)

    def process_eed(i, color):
        manual_input = st.checkbox(f'Enter values manually for EED {i+1}?', key=f'manual_input{i}')

        if manual_input:
            bdp = st.number_input(f'BDP {i+1} (mmHg)', value=4.32, key=f'bdp{i}')
            edp = st.number_input(f'EDP {i+1} (mmHg)', value=11.29, key=f'edp{i}')
            esv = st.number_input(f'ESV {i+1} (mmHg)', value=87.0, key=f'esv{i}')
            edv = st.number_input(f'EDV {i+1} (mmHg)', value=157.0, key=f'edv{i}')
        else:
            bdp = st.slider(f'BDP {i+1} (mmHg)', 0.0, 20.0, 4.32, 0.01, key=f'bdp_slider{i}')
            edp = st.slider(f'EDP {i+1} (mmHg)', 0.0, 40.0, 11.29, 0.01, key=f'edp_slider{i}')
            esv = st.slider(f'ESV {i+1} (mmHg)', 0.0, 200.0, 87.0, 0.01, key=f'esv_slider{i}')
            edv = st.slider(f'EDV {i+1} (mmHg)', 0.0, 300.0, 157.0, 0.01, key=f'edv_slider{i}')

        bdpn = 1
        edpn = edp + bdpn - bdp

        x = np.array([0, esv, edv])
        y = np.array([0, bdpn, edpn])

        params, _ = curve_fit(func, x, y, p0=[1, 0])
        alpha, beta = params

        eed = round(alpha * beta * np.exp(edv * beta), 2)

        data.append((x, y, alpha, beta, eed, color))
        info_texts.append(f"EED {i+1}: BDP={bdp}, EDP={edp}, ESV={esv}, EDV={edv}, α={alpha:.3f}, β={beta:.3f}, EED={eed}")

        st.markdown(f"<h2 style='text-align: center;'>EED invasive {i+1} = {eed}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center;'>α {i+1} = {alpha:.3f}, β {i+1} = {beta:.3f}</p>", unsafe_allow_html=True)

    # Basis EED-Berechnung
    process_eed(0, colors[0])

    # Optionale zusätzliche EED-Berechnungen
    for i in range(1, 3):
        if st.checkbox(f'Would you like to calculate EED {i+1}?', key=f'eed{i+1}'):
            st.markdown(f"### EED {i+1}")
            process_eed(i, colors[i])

    # Plot-Iteration, Koordinaten markieren und Legendenbeschriftung
    for i, (x, y, alpha, beta, eed, color) in enumerate(data):
        x_values = np.linspace(0, max(x) + 20, 120)
        y_values = func(x_values, alpha, beta)
        ax.plot(x_values, y_values, linewidth=3, color=color, label=f'EED invasive {i+1}: {eed}')
        ax.scatter(x[1:], y[1:], color=color)  # Koordinaten markieren

    y_offset = 0.1  # Erhöhter Abstand für die Textpositionierung
    for i, text in enumerate(info_texts):
        plt.figtext(0.5, -0.01 - (i * y_offset), text, wrap=True, horizontalalignment='center', fontsize=14)

    ax.set_xlabel('Volume (ml)')
    ax.set_ylabel('Pressure (mmHg)')
    ax.legend()
    st.pyplot(fig)

    if st.button('Save Plot as PDF'):
        pdf_path = 'EED_Calculations.pdf'
        with PdfPages(pdf_path) as pdf:
            pdf.savefig(fig, bbox_inches="tight")
        st.success(f'Plot saved as {pdf_path}')

    # Disclaimer
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <p style='text-align: center; font-size: small;'>
    Disclaimer: This application is based on the method of: "Rain S, Handoko ML, Trip P, Gan CT, Westerhof N, Stienen GJ, Paulus WJ, Ottenheijm CA, Marcus JT, Dorfmüller P, Guignabert C, Humbert M, Macdonald P, Dos Remedios C, Postmus PE, Saripalli C, Hidalgo CG, Granzier HL, Vonk-Noordegraaf A, van der Velden J, de Man FS. Right ventricular diastolic impairment in patients with pulmonary arterial hypertension. Circulation. 2013 Oct 29;128(18):2016-25, 1-10. doi: 10.1161/CIRCULATIONAHA.113.001873. Epub 2013 Sep 20. PMID: 24056688."<br>Use of this app is at your own risk and is intended for scientific purposes only.
    </p>
    """, unsafe_allow_html=True)  


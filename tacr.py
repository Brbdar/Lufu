#!/usr/bin/env python
# coding: utf-8

# In[28]:


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from scipy.interpolate import interp1d

def tacr():


    # Definition der Funktion für das pharmakokinetische Profil
    def pharmacokinetic_profile(times, concentrations):
        # Interpolation der Konzentrationen
        interpolation = interp1d(times, concentrations, kind='linear', fill_value="extrapolate")
        # Berechnung der Konzentrationen für die erweiterten Zeitpunkte
        extended_concentrations = interpolation(extended_times)
        # Berechnung des pharmakokinetischen Profils unter Verwendung der interpolierten Konzentrationen
        absorption = 20 / (1 + np.exp(-0.1 * (extended_times - 60)))
        elimination = extended_concentrations * np.exp(-0.05 * (extended_times - 60))
        profile = absorption * elimination
        return profile

    # Streamlit App
    st.title('Tacrolimus-Konzentration und Pharmakokinetik')

    # Benutzerdefinierte Eingaben für die Konzentrationen
    C0 = st.number_input("Konzentration bei 0 Minuten (ng/mL)", value=0.0)
    C40 = st.number_input("Konzentration bei 40 Minuten (ng/mL)", value=0.0)
    C120 = st.number_input("Konzentration nach 2 Stunden (120 Minuten) (ng/mL)", value=0.0)

    # Zeitpunkte und Konzentrationen für das Plotting
    times = np.array([0, 40, 120])
    concentrations = np.array([C0, C40, C120])

    # Zeitpunkte für die Modellierung bis zu 4 Stunden (240 Minuten)
    extended_times = np.arange(0, 240)  # Von 0 bis 240 Minuten

    # Berechnen des pharmakokinetischen Profils
    profile = pharmacokinetic_profile(times, concentrations)

    # Berechnen der MPA-AUC
    auc = simps(profile, extended_times)

    # Formel zur Berechnung der MPA-AUC
    mpa_auc_formula = "-1.86 + 6.7 * C0 + 1.19 * C40 + 4.8 * C120"

    # Plotten des Modells
    plt.figure(figsize=(8, 6))
    plt.plot(extended_times, profile, label='Pharmakokinetisches Profil', color='blue', linewidth=2)
    plt.fill_between(extended_times, 0, profile, color='blue', alpha=0.3, label=f'MPA-AUC = {auc:.2f}')
    plt.scatter(times, concentrations, color='red', label='Gemessene Konzentrationen')
    plt.xlabel('Zeit (Minuten)', fontsize=12)
    plt.ylabel('Konzentration (ng/mL)', fontsize=12)
    plt.title('Pharmakokinetischer Verlauf der Tacrolimus-Konzentration (bis 4 Stunden)', fontsize=14)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend(loc='upper right', fontsize=10)
    plt.ylim(bottom=0)  # Sicherstellen, dass die y-Achse nicht unter Null geht

    
    # Anzeige der durchschnittlichen Konzentration oben rechts im Plot
    average_concentration = np.mean(concentrations)
    plt.text(0.98, 0.98, f'Durchschnittskonzentration: {average_concentration:.2f} ng/mL',
         horizontalalignment='right', verticalalignment='down', transform=plt.gca().transAxes, fontsize=10, color='green')

    
    st.pyplot(plt)
    # Ergebnisse anzeigen
    st.write(f'MPA-AUC (Mykophenolsäure-Area under the Curve): {auc:.2f}')
    st.write(f'Formel zur Berechnung der MPA-AUC: {mpa_auc_formula}')


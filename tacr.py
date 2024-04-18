#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from scipy.interpolate import interp1d

def tacr():
    # Definition der Funktion für das pharmakokinetische Profil
    def pharmacokinetic_profile(times, concentrations):
        # Interpolation der Konzentrationen
        interpolation = interp1d(times, concentrations, kind='quadratic', fill_value="extrapolate")
        # Berechnung der Konzentrationen für die erweiterten Zeitpunkte
        extended_concentrations = interpolation(extended_times)
        # Berechnung des pharmakokinetischen Profils unter Verwendung der interpolierten Konzentrationen
        absorption = 20 / (1 + np.exp(-0.1 * (extended_times - 60)))
        elimination = extended_concentrations * np.exp(-0.05 * (extended_times - 60))
        profile = absorption * elimination
        return profile

    # Zeitpunkte für die Modellierung bis zu 4 Stunden (240 Minuten)
    extended_times = np.arange(0, 200)  # Von 0 bis 240 Minuten

    # Streamlit-Anwendung
    st.title('Pharmakokinetischer Verlauf der Tacrolimus-Konzentration (bis 4 Stunden)')

    # Benutzerdefinierte Werte für die Konzentrationen
    C0 = st.number_input("Konzentration bei 0 Minuten (ng/mL)", min_value=0.0)
    C40 = st.number_input("Konzentration bei 40 Minuten (ng/mL)", min_value=0.0)
    C120 = st.number_input("Konzentration nach 2 Stunden (120 Minuten) (ng/mL)", min_value=0.0)

    # Zeitpunkte und Konzentrationen für das Plotting
    times = np.array([0, 40, 120])
    concentrations = np.array([C0, C40, C120])

    # Berechnen des pharmakokinetischen Profils
    profile = pharmacokinetic_profile(times, concentrations)

    # Berechnen der Durchschnittskonzentration
    average_concentration = np.mean(profile)

    # Berechnen der Fläche unter der Kurve (AUC)
    auc = simps(profile, extended_times)

    # Plotten des Modells
    fig, ax = plt.subplots()
    ax.plot(extended_times, profile, label='Pharmakokinetisches Profil', color='blue', linewidth=2)
    ax.fill_between(extended_times, 0, profile, color='blue', alpha=0.3, label=f'Area under the Curve (AUC) = {auc:.2f}')
    ax.set_xlabel('Zeit (Minuten)', fontsize=12)
    ax.set_ylabel('Konzentration (ng/mL)', fontsize=12)
    ax.set_title('Pharmakokinetischer Verlauf der Tacrolimus-Konzentration (bis 4 Stunden)', fontsize=14)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Anzeigen der Durchschnittskonzentration
    ax.text(0.5, 0.9, f'Durchschnittskonzentration: {average_concentration:.2f} ng/mL', transform=ax.transAxes, fontsize=10, ha='left')

    ax.legend(loc='upper right', fontsize=10)

    # Anzeigen des Plots in Streamlit
    st.pyplot(fig)

    st.write(f'Durchschnittskonzentration: {average_concentration:.2f} ng/mL')


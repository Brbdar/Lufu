#!/usr/bin/env python
# coding: utf-8

# In[31]:


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from scipy.interpolate import interp1d

def tacr():
    def pharmacokinetic_profile(times, concentrations):
        interpolation = interp1d(times, concentrations, kind='linear', fill_value="extrapolate")
        extended_times = np.arange(0, 240)  # Zeitrahmen von 0 bis 240 Minuten
        extended_concentrations = interpolation(extended_times)
        absorption = 20 / (1 + np.exp(-0.1 * (extended_times - 60)))
        elimination = extended_concentrations * np.exp(-0.05 * (extended_times - 60))
        return absorption * elimination

    st.title('Tacrolimus-Konzentration und Pharmakokinetik')

    C0 = st.number_input("Konzentration bei 0 Minuten (ng/mL)", value=0.0)
    C40 = st.number_input("Konzentration bei 40 Minuten (ng/mL)", value=0.0)
    C120 = st.number_input("Konzentration nach 2 Stunden (120 Minuten) (ng/mL)", value=0.0)

    times = np.array([0, 40, 120])
    concentrations = np.array([C0, C40, C120])

    profile = pharmacokinetic_profile(times, concentrations)

    auc = simps(profile, np.arange(0, 240))

    # Berechnung der MPA-AUC nach der angegebenen Formel
    mpa_auc = -1.86 + 6.7 * C0 + 1.19 * C40 + 4.8 * C120

    plt.figure(figsize=(10, 8))
    plt.plot(np.arange(0, 240), profile, color='blue', linewidth=2)
    plt.fill_between(np.arange(0, 240), 0, profile, color='blue', alpha=0.3)
    plt.scatter(times, concentrations, color='red', s=100)  # Größere Punkte für Messdaten
    plt.xlabel('Zeit (Minuten)', fontsize=14)
    plt.ylabel('Konzentration (ng/mL)', fontsize=14)
    plt.title('Pharmakokinetischer Verlauf der Tacrolimus-Konzentration', fontsize=16)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.ylim(bottom=0)
    
    # Keine Legende anzeigen
    # plt.legend(loc='upper right', fontsize=12)

    average_concentration = np.mean(concentrations)
    plt.text(0.98, 0.98, f'Durchschnitt: {average_concentration:.2f} ng/mL',
             horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes, fontsize=12, color='green')
    
    st.pyplot(plt)
    
    st.write(f'MPA-AUC: {mpa_auc:.2f}')
    st.write(f'Berechnete MPA-AUC: {auc:.2f}')
    st.write(f'Formel zur Berechnung der MPA-AUC: -1.86 + 6.7 * C0 + 1.19 * C40 + 4.8 * C120')

# Aktivieren Sie diese Funktion in Ihrer Streamlit-App


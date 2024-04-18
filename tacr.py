#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import streamlit as st

from scipy.interpolate import interp1d
from scipy.integrate import simps

def tacr():
    def create_pharmacokinetic_profile(times, concentrations):
        """Generate pharmacokinetic profile."""
        interpolation = interp1d(times, concentrations, kind='linear', fill_value="extrapolate")
        extended_times = np.arange(0, 240)  # Time frame from 0 to 240 minutes
        extended_concentrations = interpolation(extended_times)
        # Simplified absorption and elimination modeling
        absorption = 20 / (1 + np.exp(-0.1 * (extended_times - 60)))
        elimination = extended_concentrations * np.exp(-0.05 * (extended_times - 60))
        return extended_times, absorption * elimination

    def calculate_auc(profile):
        """Calculate area under the curve (AUC) for the given profile."""
        return simps(profile, np.arange(0, 240))

    def setup_streamlit_ui():
        st.title('Mycophenolate Concentration and Pharmacokinetics')

        C0 = st.number_input("Concentration at 0 minutes (ng/mL)", value=0.0)
        C40 = st.number_input("Concentration at 40 minutes (ng/mL)", value=0.0)
        C120 = st.number_input("Concentration after 2 hours (120 minutes) (ng/mL)", value=0.0)

        times = np.array([0, 40, 120])
        concentrations = np.array([C0, C40, C120])

        extended_times, profile = create_pharmacokinetic_profile(times, concentrations)

        auc = calculate_auc(profile)
        # Assuming similar linear combination for AUC estimation for Mycophenolate
        mpa_auc = -1.86 + 6.7 * C0 + 1.19 * C40 + 4.8 * C120

        plot_pharmacokinetic_curve(extended_times, profile, times, concentrations)

        st.write(f'MPA-AUC: {mpa_auc:.2f}')
        st.write(f'Calculated AUC: {auc:.2f}')
        st.write(f'Formula for AUC calculation: -1.86 + 6.7 * C0 + 1.19 * C40 + 4.8 * C120')

    def plot_pharmacokinetic_curve(extended_times, profile, times, concentrations):
        """Generate and display a matplotlib plot, highlighting absorption and elimination."""
        plt.figure(figsize=(10, 8))
        plt.plot(extended_times, profile, color='blue', linewidth=2)
        plt.fill_between(extended_times, 0, profile, color='blue', alpha=0.3)
        plt.scatter(times, concentrations, color='red', s=100)  # Larger dots for measured data
        cmax_index = np.argmax(profile)
        plt.scatter(extended_times[cmax_index], profile[cmax_index], color='green', s=150)  # Cmax point
        plt.text(extended_times[cmax_index], profile[cmax_index], f' Cmax: {profile[cmax_index]:.2f} ng/mL at {extended_times[cmax_index]} min', fontsize=12, verticalalignment='bottom')
        plt.xlabel('Time (minutes)', fontsize=14)
        plt.ylabel('Concentration (ng/mL)', fontsize=14)
        plt.title('Pharmacokinetic Profile of Mycophenolate', fontsize=16)
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.ylim(bottom=0)
        st.pyplot(plt)


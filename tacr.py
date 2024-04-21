#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from scipy.interpolate import interp1d
from scipy.integrate import simps

def tacr():
    def create_pharmacokinetic_profile(times, concentrations, last_time):
        """Generate pharmacokinetic profile with appropriate time frame based on the last sample."""
        interpolation = interp1d(times, concentrations, kind='linear', fill_value="extrapolate")
        extended_times = np.arange(0, last_time + 1)  # Time frame from 0 to last sample time
        extended_concentrations = interpolation(extended_times)
        absorption = 20 / (1 + np.exp(-0.1 * (extended_times - 60)))  # Generic absorption, adjust if needed
        elimination = extended_concentrations * np.exp(-0.05 * (extended_times - 60))  # Generic elimination, adjust if needed
        return extended_times, absorption * elimination

    def calculate_auc(profile, last_time):
        """Calculate area under the curve (AUC) for the given profile up to last time."""
        return simps(profile, np.arange(0, last_time + 1))

    def plot_pharmacokinetic_curve(extended_times, profile, times, concentrations, therapeutic_range, toxic_range, title):
        """Generate and display a matplotlib plot, highlighting different pharmacokinetic phases and therapeutic ranges."""
        plt.figure(figsize=(10, 8))
        plt.plot(extended_times, profile, color='grey', linewidth=3)
        plt.fill_between(extended_times, 0, profile, 
                         where=(profile >= therapeutic_range[0]) & (profile <= therapeutic_range[1]),
                         color='blue', alpha=0.1, label='Therapeutic Range')
        plt.fill_between(extended_times, 0, profile, 
                         where=(profile >= toxic_range),
                         color='red', alpha=0.3, label='Toxic Range')
        plt.fill_between(extended_times, 0, profile, 
                         where=(profile <= therapeutic_range[0]),
                         color='yellow', alpha=0.1, label='Sub-Therapeutic Range')
        plt.scatter(times, concentrations, color='black', s=100, zorder=5)
        cmax_index = np.argmax(profile)
        plt.scatter(extended_times[cmax_index], profile[cmax_index], color='purple', s=150, zorder=5)
        plt.text(extended_times[cmax_index], profile[cmax_index], f'Cmax: {profile[cmax_index]:.2f} ng/mL at {extended_times[cmax_index]} min', fontsize=12, verticalalignment='bottom')
        plt.xlabel('Time (minutes)', fontsize=14)
        plt.ylabel('Concentration (ng/mL)', fontsize=14)
        plt.title(title, fontsize=16)
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.ylim(bottom=0)
        plt.legend()
        st.pyplot(plt)
    
    def setup_streamlit_ui():
        st.title('Pharmacokinetic Analysis for Tacrolimus and Cyclosporine A')
        
        drug_type = st.radio("Select the drug type:", ('Tacrolimus (MPA-AUC)', 'Cyclosporine A (CSA-AUC)'))
        
        if drug_type == 'Tacrolimus (MPA-AUC)':
            formula_description = "1.86 + (6.7 * C0) + (1.19 * C40) + (4.8 * C120)"
            coefficients = (1.86, 6.7, 1.19, 4.8)
            times = [0, 40, 120]
            profile_title = 'Pharmacokinetic Profile for Tacrolimus'
        else:
            formula_description = "11.8 + (3.71 * C0) + (1.33 * C75) + (3.9 * C240)"
            coefficients = (11.8, 3.71, 1.33, 3.9)
            times = [0, 75, 240]
            profile_title = 'Pharmacokinetic Profile for Cyclosporine A'

        concentrations = [st.number_input(f"Concentration at {time} minutes (ng/mL)", value=0.0) for time in times]
        
        extended_times, profile = create_pharmacokinetic_profile(np.array(times), np.array(concentrations), times[-1])
        
        auc = calculate_auc(profile, times[-1])
        mpa_auc = sum(coef * conc for coef, conc in zip(coefficients, concentrations))
        
        therapeutic_range = [10, 30]  # ng/mL
        toxic_range = 30  # ng/mL
        
        plot_pharmacokinetic_curve(extended_times, profile, np.array(times), np.array(concentrations), therapeutic_range, toxic_range, profile_title)
        
        st.write(f'{drug_type} AUC: {mpa_auc:.2f}')
        st.write(f'Calculated AUC: {auc:.2f}')
        st.write(f'Formula for AUC calculation: {formula_description}')

    setup_streamlit_ui()

if __name__ == "__main__":
    tacr()


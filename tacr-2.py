#!/usr/bin/env python
# coding: utf-8

# In[60]:


import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

from scipy.interpolate import interp1d

def create_pharmacokinetic_profile(times, concentrations, last_time=300):
    """Generate pharmacokinetic profile with appropriate time frame up to 300 minutes."""
    interpolation = interp1d(times, concentrations, kind='linear', fill_value="extrapolate")
    extended_times = np.arange(0, last_time + 1)
    extended_concentrations = interpolation(extended_times)
    return extended_times, extended_concentrations

def calculate_auc(coefficients, concentrations):
    """Calculate AUC using the provided coefficients and concentrations."""
    return sum(coef * conc for coef, conc in zip(coefficients, concentrations))

def plot_pharmacokinetic_curve(times, concentrations, title, therapeutic_range, toxic_range):
    """Generate and display a matplotlib plot for the pharmacokinetic profile."""
    plt.figure(figsize=(10, 8))
    plt.plot(times, concentrations, color='grey', linewidth=3)
    plt.scatter(times[:len(concentrations)], concentrations, color='black', s=100, zorder=5)

    # Highlight different pharmacokinetic phases
    plt.fill_between(times, 0, concentrations, 
                     where=(concentrations >= therapeutic_range[0]) & (concentrations <= therapeutic_range[1]),
                     color='blue', alpha=0.1, label='Therapeutic Range')
    plt.fill_between(times, 0, concentrations, 
                     where=concentrations >= toxic_range,
                     color='red', alpha=0.3, label='Toxic Range')
    plt.fill_between(times, 0, concentrations, 
                     where=concentrations <= therapeutic_range[0],
                     color='yellow', alpha=0.1, label='Sub-Therapeutic Range')

    plt.xlabel('Time (minutes)', fontsize=14)
    plt.ylabel('Concentration (ng/mL)', fontsize=14)
    plt.title(title, fontsize=16)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.ylim(bottom=0)
    plt.legend()
    st.pyplot(plt)

def setup_streamlit_ui():
    st.title('Pharmacokinetic Analysis Tool')
    drug_type = st.radio("Select the drug type:", ('Tacrolimus (MPA-AUC)', 'Cyclosporine A (CSA-AUC)'))

    if drug_type == 'Tacrolimus (MPA-AUC)':
        times = [0, 40, 120]
        coefficients = [1.86, 6.7, 1.19, 4.8]
        profile_title = 'Pharmacokinetic Profile for Tacrolimus'
        formula_description = "1.86 + (6.7 * C0) + (1.19 * C40) + (4.8 * C120)"
    else:
        times = [0, 75, 240]
        coefficients = [11.8, 3.71, 1.33, 3.9]
        profile_title = 'Pharmacokinetic Profile for Cyclosporine A'
        formula_description = "11.8 + (3.71 * C0) + (1.33 * C75) + (3.9 * C240)"

    concentrations = [st.number_input(f"Concentration at {time} minutes (ng/mL)", key=time) for time in times]
    extended_times, profile = create_pharmacokinetic_profile(np.array(times), np.array(concentrations))

    auc = calculate_auc(coefficients, concentrations)

    therapeutic_range = [10, 30]  # ng/mL
    toxic_range = 30  # ng/mL

    plot_pharmacokinetic_curve(extended_times, profile, profile_title, therapeutic_range, toxic_range)

    st.write(f'{drug_type} AUC: {auc:.2f}')
    st.write(f'Formula for AUC calculation: {formula_description}')

if __name__ == "__main__":
    setup_streamlit_ui()


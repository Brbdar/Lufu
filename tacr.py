#!/usr/bin/env python
# coding: utf-8

# In[120]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import streamlit as st
from scipy.interpolate import interp1d
from scipy.integrate import simps
from scipy.interpolate import UnivariateSpline

def tacr():

    
    def create_pharmacokinetic_profile(times, concentrations, last_time):
        try:
            if len(times) > 3:  # Ensuring there are more than three data points for cubic spline
                spline = UnivariateSpline(times, concentrations, s=0, k=3)
            elif len(times) > 2:  # Fallback to quadratic spline
                spline = UnivariateSpline(times, concentrations, s=0, k=2)
            else:  # Fallback to linear spline
                spline = UnivariateSpline(times, concentrations, s=0, k=1)
            extended_times = np.arange(0, last_time + 1)
            extended_concentrations = spline(extended_times)
        except Exception as e:
            st.error(f"Error in spline interpolation: {e}")
            return np.array([]), np.array([])

        extended_concentrations = np.maximum(0,extended_concentrations)
        
        return extended_times, extended_concentrations

    def calculate_auc(profile, last_time):
        """Calculate area under the curve (AUC) for the given profile up to last time."""
        return simps(profile, np.arange(0, last_time + 1))
    
    def plot_pharmacokinetic_curve(times, concentrations, title, therapeutic_range, toxic_range, average_concentration=None):
        """Generate and display a matplotlib plot for the pharmacokinetic profile."""
        plt.figure(figsize=(10, 8))
        plt.plot(times, concentrations, 'grey', linewidth=2, label='PK Curve')
        plt.scatter(times[:len(concentrations)], concentrations, color='black', s=50, zorder=5)
    
        # Plotting average concentration if provided
        if average_concentration is not None:
            plt.plot(times, average_concentration, 'b--', linewidth=2, label='Average Concentration')
    
        plt.fill_between(times, 0, concentrations,
                         where=(concentrations >= therapeutic_range[0]) & (concentrations <= therapeutic_range[1]),
                         color='blue', alpha=0.1, label='Therapeutic Range')
        plt.fill_between(times, 0, concentrations,
                         where=concentrations > toxic_range,
                         color='red', alpha=0.3, label='Toxic Range')
        plt.fill_between(times, 0, concentrations,
                         where=concentrations < therapeutic_range[0],
                         color='yellow', alpha=0.1, label='Sub-Therapeutic Range')
    
        plt.xlabel('Time (minutes)')
        plt.ylabel('Concentration (ng/mL)')
        plt.title(title)
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)

    def setup_streamlit_ui():
        st.title('Analyse-Tool')
        drug_type = st.radio("Select the drug type:", ('Tacrolimus (MPA-AUC) = 1.86 + (6.7 * C0) + (1.19 * C40) + (4.8 * C120)', 'Cyclosporine A (MPA-AUC) = 11.8 + (3.71 * C0) + (1.33 * C75) + (3.9 * C240'))
        last_time = st.number_input("Enter the duration for the pharmacokinetic profile (in minutes):", value=300, step=10)
    
        if drug_type == 'Tacrolimus (MPA-AUC) = 1.86 + (6.7 * C0) + (1.19 * C40) + (4.8 * C120)':
            times = [0, 40, 120]
            coefficients = [1.86, 6.7, 1.19, 4.8]  # Tacrolimus coefficients
            profile_title = 'Pharmakokinetisches Profil bei Tacrolimus Therapie'
            formula_description = "Tacr MPA-AUC = 1.86 + (6.7 * C0) + (1.19 * C40) + (4.8 * C120)"
            therapeutic_range = (5, 30)
            toxic_range = 30
            st.info:("MPA-AUC = 1.86 + (6.7 * C0) + (1.19 * C40) + (4.8 * C120")
        
        else:
            times = [0, 75, 240]
            coefficients = [11.8, 3.71, 1.33, 3.9]  # Cyclosporine A coefficients
            profile_title = 'Pharmakokinetisches Profil bei CsA Therapie'
            formula_description = "AUC = 11.8 + (3.71 * C0) + (1.33 * C75) + (3.9 * C240)"
            therapeutic_range = (15, 30)
            toxic_range = 30
            st.info:("CsA MPA-AUC = 11.8 + (3.71 * C0) + (1.33 * C75) + (3.9 * C240")
    
        concentrations = [st.number_input(f"Concentration at {time} minutes (ng/mL)", key=f"{drug_type}_{time}") for time in times]
        extended_times, extended_concentrations = create_pharmacokinetic_profile(times, concentrations, last_time)
    
        # Calculate average concentration
        average_concentration = np.mean(extended_concentrations) * np.ones_like(extended_concentrations)
    
        if len(extended_times) > 0 and len(extended_concentrations) > 0:
            plot_pharmacokinetic_curve(extended_times, extended_concentrations, profile_title, therapeutic_range, toxic_range)
            auc = calculate_auc(extended_concentrations, last_time)
            st.write(f'{profile_title}')
            st.write(f'AUC: {auc:.2f}')

    setup_streamlit_ui()

    if __name__ == "__main__":
        tacr()


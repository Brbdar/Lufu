#!/usr/bin/env python
# coding: utf-8

# In[13]:


import streamlit as st
from fpdf import FPDF

def anamnese():

    def create_pdf(report):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        pdf.multi_cell(0, 10, report)
        filename = 'Pneumologischer_Anamnesebericht.pdf'
        pdf.output(filename)
        return filename

    def calculate_pack_years(cigarettes, years_smoked):
        return (cigarettes / 20) * years_smoked

    st.title('Pneumologische Anamnese Tool (XX - in ARBEIT - XX)')

    # Geburtsdatum und Geschlecht
    geburtstag = st.date_input("Geburtsdatum")
    geschlecht = st.radio("Geschlecht", options=["Weiblich", "Männlich", "Divers"])
    alter = (datetime.now().date() - geburtstag).days // 365
    
    # Checkliste vor Beginn der Anamnese
    st.subheader('Checkliste vor der Anamnese')
    checklist_items = ['Blutentnahmen', 'Braunüle gelegt', 'Medikation abgeglichen', 'EKG geschrieben']
    checklist = st.multiselect('Bitte bestätigen Sie die durchgeführten Maßnahmen:', checklist_items)
    anamnese_report = "Zu Beginn der Aufnahme wurden folgende Maßnahmen durchgeführt: " + ', '.join(checklist) + ".\n\n"

    # 1. Aufnahmegrund
    st.subheader('Aufnahmegrund')
    reason_for_admission = st.radio('Aufnahmegrund:', ['Elektiv', 'Notfall'])
    details = st.text_area('Details zum Aufnahmegrund', key='admission_detail')
    anamnese_report += f"Der Aufnahmegrund wurde als {reason_for_admission} angegeben. Details dazu: {details}.\n\n"

    # 2. Symptome
    st.subheader('Symptome')
    symptoms_list = ['Husten', 'Dyspnoe', 'Brustschmerzen', 'Atemnot', 'Fieber', 'Gewichtsverlust', 'Nächtliches Schwitzen', 'Keine']
    symptoms = st.multiselect('Bitte Symptome auswählen:', symptoms_list)

    # B-Symptomatik prüfen
    b_symptoms = set(['Fieber', 'Gewichtsverlust', 'Nächtliches Schwitzen'])
    if b_symptoms.intersection(set(symptoms)):
        anamnese_report += "Es liegt eine B-Symptomatik vor mit den Symptomen: " + ', '.join(b_symptoms.intersection(set(symptoms))) + ". "

    # Gewichtsverlust Details
    if 'Gewichtsverlust' in symptoms:
        weight_loss_duration = st.text_input('Seit wann haben Sie Gewichtsverlust? (Monate)', key='weight_loss_duration')
        weight_loss_amount = st.text_input('Wie viel Gewicht haben Sie verloren?', key='weight_loss_amount')
        anamnese_report += f"Gewichtsverlust seit {weight_loss_duration} mit einem Verlust von {weight_loss_amount}. "

    anamnese_report += "Die berichteten Symptome umfassen: " + ', '.join(symptoms) + ".\n\n"

    # 4. Rauchgewohnheiten
    st.subheader('Rauchgewohnheiten')
    smoking_status = st.radio('Rauchstatus:', ['Ja', 'Nein'])
    if smoking_status == 'Ja':
        cigarettes_per_day = st.number_input('Anzahl der täglich gerauchten Zigaretten:', min_value=1, max_value=100, step=1)
        years_smoked = st.number_input('Rauchdauer in Jahren:', min_value=1, max_value=100, step=1)
        pack_years = calculate_pack_years(cigarettes_per_day, years_smoked)
        anamnese_report += f"Rauchstatus: täglicher Konsum von {cigarettes_per_day} Zigaretten über {years_smoked} Jahre, was {pack_years:.1f} Packungsjahre entspricht. "
    else:
        anamnese_report += "Keine Rauchanamnese. "

    # 5. Heimsauerstoff
    st.header('Heimsauerstoff')
    home_oxygen = st.radio('Wird Heimsauerstoff verwendet?', ['Ja', 'Nein'], key='home_oxygen')
    if home_oxygen == 'Ja':
        oxygen_since = st.text_input('Seit wann wird Heimsauerstoff verwendet?', key='oxygen_since')
        oxygen_amount = st.number_input('Wie viel Liter pro Minute?', min_value=0.1, max_value=10.0, step=0.1, key='oxygen_amount')
        anamnese_report += f"Heimsauerstoff wird seit {oxygen_since} verwendet, mit einer Flussrate von {oxygen_amount} Litern pro Minute. "

    # 6. Antikoagulation
    st.header('Antikoagulation')
    anticoagulation = st.radio('Wird eine Antikoagulation durchgeführt?', ['Ja', 'Nein'], key='anticoagulation')
    if anticoagulation == 'Ja':
        anticoagulant_type = st.text_input('Welches Antikoagulans wird verwendet?', key='anticoagulant_type')
        anamnese_report += f"Antikoagulation mit {anticoagulant_type}. "

    # 7. Plättchenhemmung
    st.header('Plättchenhemmung')
    platelet_inhibition = st.radio('Wird eine Plättchenhemmung durchgeführt?', ['Ja', 'Nein'], key='platelet_inhibition')
    if platelet_inhibition == 'Ja':
        platelet_inhibitor_type = st.text_input('Welches Plättchenhemmer wird verwendet?', key='platelet_inhibitor_type')
        platelet_inhibition_reason = st.text_input('Aus welchem Grund wird die Plättchenhemmung durchgeführt?', key='platelet_inhibition_reason')
        anamnese_report += f"Plättchenhemmung mit {platelet_inhibitor_type} aufgrund von {platelet_inhibition_reason}. "

    allergien = st.checkbox("Haben Sie Allergien?")
    if allergien:
        welche_allergien = st.text_input("Welche Allergien haben Sie?", max_chars=50)
        seit_wann_allergien = st.text_input("Seit wann bestehen diese Allergien?", max_chars=50)
        
    heimtransport = st.checkbox("Benötigen Sie einen Heimtransport nach stationärem Aufenthalt?")
    dnr_dni = st.checkbox("Ist ein DNR/DNI gewünscht?")
    patientenverfuegung = st.checkbox("Liegt eine Patientenverfügung vor?")


    # Schwangerschaftsfrage bei relevanten Nutzern
    if alter < 50 and geschlecht == "Weiblich":
        schwanger = st.checkbox("Sind Sie schwanger?")
    
    # PDF Erstellung und Download
    if st.button('Bericht als PDF speichern'):
        pdf_file = create_pdf(anamnese_report)
        with open(pdf_file, "rb") as file:
            st.download_button(
                label="Download PDF",
                data=file,
                file_name="Pneumologischer_Anamnesebericht.pdf",
                mime="application/octet-stream"
            )

    # Anzeige des vorläufigen Anamneseberichts
    st.subheader('Vorläufiger Anamnesebericht')
    st.text_area("", anamnese_report, height=600)


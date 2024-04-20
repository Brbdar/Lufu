#!/usr/bin/env python
# coding: utf-8

# In[50]:


import streamlit as st
from fpdf import FPDF
from datetime import datetime
from dateutil.relativedelta import relativedelta
from COPD_Score import COPD_Score
import matplotlib.pyplot as plt

def calculate_age(born):
    today = datetime.now().date()
    return relativedelta(today, born).years

def calculate_pack_years(cigarettes, years_smoked):
    return (cigarettes / 20) * years_smoked

def create_pdf(report, report_extra):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, 'Pneumologischer Anamnesebericht', align='C')
    pdf.ln(20)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, report + report_extra)
    filename = 'Pneumologischer_Anamnesebericht.pdf'
    pdf.output(filename)
    return filename

def anamnese():
    st.title('Pneumologische Aufnahme')
    anamnese_report = "Pneumologische Anamnese Bericht:\n\n"
    anamnese_report_extra = ""

    tab_labels = ["ID & Aufnahmegrund", "Medizinische Vorgeschichte", "Sozialanamnese", "Konsum", 
                  "Dauertherapie", "Symptome", "Körperliche Untersuchung", "Checkliste", "Anamnesebericht"]
    tabs = st.tabs(tab_labels)
     
    with tabs[0]:
        st.header("Identifikation")
        st.text_input("Pat ID",key='ID')
        geburtstag = st.date_input("Geburtsdatum")
        geschlecht = st.radio("Geschlecht", options=["Weiblich", "Männlich"])
        alter = calculate_age(geburtstag)

        st.subheader('Aufnahmegrund')
        reason_for_admission = st.radio('Aufnahmegrund:', ['Elektiv', 'Notfall'])
        if reason_for_admission == 'Elektiv':
            elective_reason = st.radio('Grund für die elektive Aufnahme:', ['Fibrose Verlaufskontrolle', 'BiPAP Verlaufskontrolle', 'PH Verlaufskontrolle'])
            details = st.text_area('Details zur elektiven Aufnahme', key='elective_detail')
            anamnese_report += f"Der Patient stellt sich elektiv zur {elective_reason} auf unserer Station vor. Details zur Aufnahme: {details}.\n\n"
        elif reason_for_admission == 'Notfall':
            emergency_reason = st.radio('Grund für die notfallmäßige Aufnahme:', ['notfallmäßig über ZNA mit Infektion', 'notfallmäßig über ZNA mit AECOPD', 'notfallmäßig über ZNA mit unklarer Ursache'])
            details = st.text_area('Details zur notfallmäßigen Aufnahme', key='emergency_detail')
            anamnese_report += f"Der Patient wurde stationär mit {emergency_reason} über die Notaufnahme auf unserer Station aufgenommen. Details zur Aufnahme: {details}.\n\n"
            if emergency_reason == 'notfallmäßig über ZNA mit AECOPD':
                if 'show_copd' not in st.session_state:
                    st.session_state.show_copd = False
                if st.button("COPD Scores anzeigen"):
                    st.session_state.show_copd = True
                if st.button("COPD Scores verbergen"):
                    st.session_state.show_copd = False
                if st.session_state.show_copd:
                    COPD_Score()
    
    with tabs[5]:
        st.subheader('Symptome')
        symptoms_list = ['Husten', 'Dyspnoe', 'Brustschmerzen', 'Atemnot', 'Fieber', 'Gewichtsverlust', 'Nächtliches Schwitzen', 'Auswurf', 'Keine']
        symptoms = st.multiselect('Bitte Symptome auswählen:', symptoms_list)
        b_symptoms = set(['Fieber', 'Gewichtsverlust', 'Nächtliches Schwitzen'])
    
        sputum_color = 'Kein Auswurf'
        if b_symptoms.intersection(symptoms):
            anamnese_report += "Es liegt eine B-Symptomatik vor mit den Symptomen: " + ', '.join(b_symptoms.intersection(symptoms)) + ". "
        if 'Gewichtsverlust' in symptoms:
            weight_loss_duration = st.text_input('Seit wann haben Sie Gewichtsverlust? (Monate)', key='weight_loss_duration')
            weight_loss_amount = st.text_input('Wie viel Gewicht haben Sie verloren?', key='weight_loss_amount')
            anamnese_report += f"Gewichtsverlust seit {weight_loss_duration} Monaten mit einem Verlust von {weight_loss_amount} kg. "
        if 'Husten' in symptoms or 'Auswurf' in symptoms:
            sputum_color = st.selectbox('Welche Farbe hat der Auswurf?', ['Kein Auswurf', 'Klar', 'Gelblich', 'Grünlich', 'Blutig'], key='sputum_color')
            if sputum_color != 'Kein Auswurf':
                anamnese_report += f"Auswurf vorhanden, Farbe: {sputum_color}. "
        if sputum_color in ['Gelblich', 'Grünlich']:
            st.warning('Bitte Sputumprobe ins Labor für mikrobiologische Untersuchung schicken.')
        if 'Fieber' in symptoms:
            fever_duration = st.text_input('Seit wann haben Sie Fieber? (Tage)', key='fever_duration')
            anamnese_report += f"Fieber seit {fever_duration} Tagen. "
        if 'Fieber' in symptoms or 'Auswurf' in symptoms:
            with st.expander("Blutkultur Informationen anzeigen/verbergen"):
                st.write("Blutkultur-Anweisungen und weitere Informationen hier einfügen.")
        anamnese_report += "Die berichteten Symptome umfassen: " + ', '.join(symptoms) + ".\n\n"
    
        st.subheader('Dyspnoe')
        dyspnoea_rest = st.radio('Besteht Dyspnoe in Ruhe?', ['Ja', 'Nein'])
        dyspnoea_exertion = st.radio('Besteht Dyspnoe bei Belastung?', ['Ja', 'Nein'])
        walk_distance = st.text_input('Wie lange kann der Patient auf ebener Strecke gehen?', key='walk')
        stairs_climbed = st.text_input('Wie viele Stockwerke können gegangen werden?', key='stock')
        speak_dyspnoea = st.radio('Besteht Sprechdyspnoe?', ['Ja', 'Nein'])
        bendopnea = st.radio('Besteht Bendopnoe?', ['Ja', 'Nein'])
        if bendopnea == 'Ja':
            st.info('Wenn Bendopnoe besteht, dann überprüfen, ob der Patient an pulmonaler Hypertonie leidet.')
            anamnese_report += "Der Patient gibt an, unter Bendopnoe zu leiden."
        nyha_class = 'NYHA Class I'
        if dyspnoea_rest == 'Nein' and dyspnoea_exertion == 'Nein':
            nyha_class = 'NYHA Class I'
        elif dyspnoea_rest == 'Ja' and dyspnoea_exertion == 'Nein':
            nyha_class = 'NYHA Class II'
        elif dyspnoea_rest == 'Ja' and dyspnoea_exertion == 'Ja':
            nyha_class = 'NYHA Class III'
        elif dyspnoea_rest == 'Nein' and dyspnoea_exertion == 'Ja':
            nyha_class = 'NYHA Class IV'
        anamnese_report += f"Der Patient berichtet von {'keiner' if dyspnoea_rest == 'Nein' else 'einer'} Dyspnoe in Ruhe und {'keiner' if dyspnoea_exertion == 'Nein' else 'einer'} Dyspnoe bei Belastung. "
        if dyspnoea_exertion == 'Ja':
            anamnese_report += f"Er/Sie kann auf ebener Strecke etwa {walk_distance} gehen und bis zu {stairs_climbed} Stockwerke steigen. "
        anamnese_report += f"Sprechdyspnoe wurde {'nicht ' if speak_dyspnoea == 'Nein' else ''}berichtet. "
        anamnese_report += f"Die NYHA Klassifizierung lautet {nyha_class}."
    
        st.subheader('Pektanginöse Beschwerden')
        angina_symptoms = st.radio('Bestehen pektanginöse Beschwerden?', ['Ja', 'Nein'])
        if angina_symptoms == 'Ja':
            angina_duration = st.text_input('Seit wann bestehen die Beschwerden?', key='besch')
            angina_location = st.text_input('Wo genau treten die Beschwerden auf?', key='angina')
            anamnese_report += f"Der Patient berichtet über pektanginöse Beschwerden, die seit {angina_duration} bestehen. Die Beschwerden treten hauptsächlich in der Region {angina_location} auf.\n"
        elif angina_symptoms == 'Nein':
            anamnese_report += "Pektanginöse Beschwerden wurden verneint.\n"
    
        st.subheader('Schwindel und Synkopen')
        anamnese_report += "Bezüglich Schwindel und Synkopen"
        dizziness = st.radio('Besteht Schwindel?', ['Ja', 'Nein'])
        if dizziness == 'Ja':
            dizziness_frequency = st.text_input('Wie häufig tritt der Schwindel auf?', key='schwind')
            dizziness_quality = st.text_input('Beschreiben Sie die Qualität des Schwindels (z.B. drehend, schwankend etc.).', key='schwindart')
            recommended_actions = st.checkbox('Soll ein Langzeit-EKG und eine HNO-Untersuchung empfohlen werden?')
            dizziness_details = f"Schwindel ist vorhanden und tritt mit einer Frequenz von {dizziness_frequency} auf. Der Schwindel wird als {dizziness_quality} beschrieben."
            anamnese_report += dizziness_details
            if recommended_actions:
                anamnese_report += " Empfohlene Maßnahmen: Durchführung eines Langzeit-EKGs und Vorstellung beim HNO."
        if 'Schwindel und Synkopen' not in anamnese_report:
            anamnese_report += "Schwindel und Synkopen"
        if 'dizziness' not in locals():
            dizziness = st.radio('Besteht Schwindel?', ['Ja', 'Nein'])
            if dizziness == 'Ja':
                dizziness_frequency = st.text_input('Wie häufig tritt der Schwindel auf?', key='schwindartr')
                dizziness_quality = st.text_input('Beschreiben Sie die Qualität des Schwindels (z.B. drehend, schwankend etc.).', key='schwdbf')
                dizziness_details = f"Schwindel ist vorhanden und tritt mit einer Frequenz von {dizziness_frequency} auf. Der Schwindel wird als {dizziness_quality} beschrieben."
                anamnese_report += dizziness_details
                st.info('Bitte Langzeit-EKG durchführen. Ggf. HNO anmelden.')
        syncope = st.radio('Sind Synkopen bekannt?', ['Ja', 'Nein'])
        if syncope == 'Ja':
            syncope_frequency = st.text_input('Wann und wie oft treten die Synkopen auf?', key='scnk')
            syncope_details = f"Synkopen sind bekannt und treten auf mit einer Häufigkeit von: {syncope_frequency}."
            anamnese_report += syncope_details
            st.info('Bitte Differentialdiagnosen wie Myokarditis, Aortenklappenstenose, Vorhofflimmern in Betracht ziehen.')
        elif syncope == 'Nein' and dizziness == 'Nein':
            anamnese_report += "Es bestehen keine Berichte über Schwindel oder Synkopen. "
    
        st.subheader('Bauchbeschwerden')
        abdominal_symptoms = st.radio('Bestehen Bauchschmerzen, Übelkeit, Erbrechen oder Durchfall?', ['Ja', 'Nein'])
        abdominal_details = ""
        if abdominal_symptoms == 'Ja':
            abdominal_onset = st.text_input('Seit wann bestehen die Beschwerden?', key='abdo')
            abdominal_details = f"Beginn der Beschwerden: {abdominal_onset}. "
        anamnese_report += f"Bauchschmerzen, Übelkeit, Erbrechen oder Durchfall: {abdominal_symptoms}. {abdominal_details}"
    
        st.subheader('Miktions- oder Defäkationsbeschwerden')
        urination_defecation_symptoms = st.radio('Bestehen Miktions- oder Defäkationsbeschwerden?', ['Ja', 'Nein'])
        defecation_details = ""
        if urination_defecation_symptoms == 'Ja':
            onset_frequency = st.text_input('Seit wann bestehen die Beschwerden und wie oft treten sie auf?', key='freq')
            defecation_type = ""
            if 'Defäkationsbeschwerden' in onset_frequency:
                defecation_type = st.text_input('Welche Art von Defäkationsbeschwerden bestehen?', key='defaqn')
                st.info('Bitte weitere Informationen erfassen, falls erforderlich.')
            defecation_details = f"Beginn und Häufigkeit der Beschwerden: {onset_frequency}. Art der Defäkationsbeschwerden: {defecation_type} "
        anamnese_report += f"\nMiktions- oder Defäkationsbeschwerden: {urination_defecation_symptoms}. {defecation_details}"
    
    with tabs[5]:
        st.header('Heimsauerstoff')
        home_oxygen = st.radio('Wird Heimsauerstoff verwendet?', ['Ja', 'Nein'], index=1, key='home_oxygen')
        if home_oxygen == 'Ja':
            oxygen_since = st.text_input('Seit wann wird Heimsauerstoff verwendet?', key='oxygen_since')
            oxygen_amount = st.number_input('Wie viel Liter pro Minute?', min_value=0.1, max_value=10.0, step=0.1, key='oxygen_amount')
            anamnese_report += f"Heimsauerstoff wird seit {oxygen_since} verwendet, mit einer Flussrate von {oxygen_amount:.1f} Litern pro Minute. "
        else:
            anamnese_report += "Es wird kein Heimsauerstoff verwendet. "
    
        st.header('Antikoagulation')
        anticoagulation = st.radio('Wird eine Antikoagulation durchgeführt?', ['Ja', 'Nein'], index=1, key='anticoagulation')
        if anticoagulation == 'Ja':
            anticoagulant_type = st.text_input('Welches Antikoagulans wird verwendet?', key='anticoagulant_type')
            anamnese_report += f"Antikoagulation mit {anticoagulant_type}. "
        else:
            anamnese_report += "Es wird keine Antikoagulation durchgeführt. "
    
        st.header('Plättchenhemmung')
        platelet_inhibition = st.radio('Wird eine Plättchenhemmung durchgeführt?', ['Ja', 'Nein'], index=1, key='platelet_inhibition')
        if platelet_inhibition == 'Ja':
            platelet_inhibitor_type = st.text_input('Welches Plättchenhemmer wird verwendet?', key='platelet_inhibitor_type')
            platelet_inhibition_reason = st.text_input('Aus welchem Grund wird die Plättchenhemmung durchgeführt?', key='platelet_inhibition_reason')
            anamnese_report += f"Plättchenhemmung mit {platelet_inhibitor_type} aufgrund von {platelet_inhibition_reason}. "
        else:
            anamnese_report += "Es wird keine Plättchenhemmung durchgeführt. "

    with tabs[4]:
        st.subheader('Rauchgewohnheiten')
        smoking_options = ['Keine', 'Zigaretten', 'Shisha', 'Vaping', 'Mehrere Optionen']
        smoking_status = st.radio('Rauchstatus:', options=smoking_options, index=0)
        if smoking_status == 'Zigaretten':
            cigarettes_per_day = st.number_input('Anzahl der täglich gerauchten Zigaretten:', min_value=1, max_value=100, step=1)
            years_smoked = st.number_input('Rauchdauer in Jahren:', min_value=1, max_value=100, step=1)
            pack_years = calculate_pack_years(cigarettes_per_day, years_smoked)
            anamnese_report += f"Rauchstatus: täglicher Konsum von {cigarettes_per_day} Zigaretten über {years_smoked} Jahre, was {pack_years:.1f} Packungsjahre entspricht. "
        elif smoking_status in ['Shisha', 'Vaping', 'Mehrere Optionen']:
            if smoking_status == 'Shisha':
                sessions_per_week = st.number_input('Anzahl der Shisha-Sitzungen pro Woche:', min_value=1, max_value=21, step=1)
                years_smoked_shisha = st.number_input('Wie lange rauchen Sie bereits Shisha? (in Jahren):', min_value=1, max_value=100, step=1)
                anamnese_report += f"Shisha-Konsum: {sessions_per_week} Sitzungen pro Woche über {years_smoked_shisha} Jahre. "
            elif smoking_status == 'Vaping':
                sessions_per_day = st.number_input('Wie oft verwenden Sie E-Zigaretten pro Tag?', min_value=1, max_value=50, step=1)
                years_vaping = st.number_input('Wie lange dampfen Sie bereits? (in Jahren):', min_value=1, max_value=100, step=1)
                anamnese_report += f"Vaping: {sessions_per_day} Mal pro Tag über {years_vaping} Jahre. "
            if smoking_status == 'Mehrere Optionen':
                st.write("Bitte geben Sie Details zu Ihren Rauchgewohnheiten an:")
                details_cigarettes = st.text_area("Details zu Zigarettenkonsum", placeholder="Anzahl pro Tag, seit wie vielen Jahren?")
                details_shisha = st.text_area("Details zu Shisha-Konsum", placeholder="Sitzungen pro Woche, seit wie vielen Jahren?")
                details_vaping = st.text_area("Details zu Vaping", placeholder="Anzahl der Nutzung pro Tag, seit wie vielen Jahren?")
                multi_smoking_details = f"Zigaretten: {details_cigarettes}, Shisha: {details_shisha}, Vaping: {details_vaping}"
                anamnese_report += f"Verschiedene Rauchgewohnheiten: {multi_smoking_details}"
        else:
            anamnese_report += "Keine Rauchanamnese vorhanden."
    
        st.subheader('Konsum von Alkohol und Drogen')
        alcohol_use = st.checkbox("Konsumieren Sie Alkohol?")
        alcohol_details = ""
        if alcohol_use:
            alcohol_duration = st.text_input("Seit wann konsumieren Sie Alkohol?", key='alcohol_duration')
            alcohol_details = f"Alkoholkonsum: Ja, seit {alcohol_duration}. "
        else:
            alcohol_details = "Alkoholkonsum: Nein. "
        drug_use = st.checkbox("Konsumieren Sie Drogen?")
        drug_details = ""
        if drug_use:
            drug_duration = st.text_input("Seit wann konsumieren Sie Drogen?", key='drug_duration')
            drug_details = f"Drogenkonsum: Ja, seit {drug_duration}. "
        else:
            drug_details = "Drogenkonsum: Nein. "
        anamnese_report += alcohol_details + drug_details

    with tabs[1]:
        st.subheader('Vorerkrankungen & Familienanamnese')
        existing_conditions = st.radio('Liegen Informationen zu Vorerkrankungen vor?', ['Liegt in vorherigen Arztberichten vor', 'Neue Angabe erforderlich'])
        anamnese_report += "Vorerkrankungen:\n"
    
        if existing_conditions == 'Neue Angabe erforderlich':
            conditions_detail = st.text_area('Bitte geben Sie die Vorerkrankungen an', key='conditions_detail')
            anamnese_report += f"Der Patient hat folgende neue Vorerkrankungen angegeben: {conditions_detail}.\n"
        else:
            anamnese_report += "Es liegen bereits dokumentierte Vorerkrankungen aus früheren Berichten vor.\n"
    
        anamnese_report += "\nSpezifische Gesundheitsinformationen:\n"
        
        malignancy = st.radio('Liegt ein Malignom vor?', ['Ja', 'Nein'], key='malignancy_radio')
        if malignancy == 'Ja':
            malignancy_type = st.text_input('Welches Malignom?', key='malignancy_type')
            anamnese_report += f"Bei dem Patienten wurde ein Malignom diagnostiziert, Typ: {malignancy_type}.\n"
        else:
            anamnese_report += "Es wurde kein Malignom diagnostiziert.\n"
    
        thrombosis_embolism = st.radio('Gab es in der Vergangenheit Thrombosen oder Embolien?', ['Ja', 'Nein'], key='thrombosis_embolism_radio')
        if thrombosis_embolism == 'Ja':
            thrombosis_embolism_detail = st.text_input('Details zu Thrombosen oder Embolien:', key='thrombosis_embolism_detail')
            anamnese_report += f"Der Patient berichtete über vergangene Thrombosen oder Embolien. Details: {thrombosis_embolism_detail}.\n"
        else:
            anamnese_report += "Es wurden keine Thrombosen oder Embolien in der Vergangenheit berichtet.\n"
    
        family_cancer = st.radio('Gibt es Krebsfälle in der Familie?', ['Ja', 'Nein'], key='family_cancer_radio')
        if family_cancer == 'Ja':
            family_cancer_detail = st.text_input('Wer in der Familie und wann?', key='family_cancer_detail')
            anamnese_report += f"In der Familie des Patienten wurden Krebsfälle berichtet. Betroffen sind: {family_cancer_detail}.\n"
        else:
            anamnese_report += "In der Familie des Patienten wurden keine Krebsfälle berichtet.\n"
    
        additional_info = st.text_area('Weitere Informationen zu Vorerkrankungen und Familienanamnese:', key='additional_info')
        if additional_info:
            anamnese_report += f"Weitere relevante Informationen: {additional_info}\n"
    
        
    with tabs[2]:
        st.subheader('Sozialanamnese')
        living_situation = st.radio("Leben Sie alleine?", ['Ja', 'Nein'], key='living_situation')
        mobility = st.radio("Wie ist Ihre Mobilität?", ['Unabhängig', 'Eingeschränkt', 'Stark eingeschränkt'], key='mobility')
        
        living_details = "lebt alleine" if living_situation == 'Ja' else "lebt nicht alleine"
        mobility_status = f"Mobilität ist {'unabhängig' if mobility == 'Unabhängig' else 'eingeschränkt' if mobility == 'Eingeschränkt' else 'stark eingeschränkt'}."
    
        if living_situation == 'Nein':
            family_status = st.radio("Leben Sie mit Ihrer Familie?", ['Ja', 'Nein'], key='family_status')
            care_info = ""
            if family_status == 'Nein':
                care_service = st.checkbox("Wird ein Pflegedienst in Anspruch genommen?", key='care_service')
                care_degree = st.selectbox("Falls ja, welcher Pflegegrad liegt vor?", ['', 'Pflegegrad 1', 'Pflegegrad 2', 'Pflegegrad 3', 'Pflegegrad 4', 'Pflegegrad 5'], index=0, key='care_degree')
                if care_service:
                    care_info = f"Pflegedienst: Ja, Pflegegrad: {care_degree}."
                else:
                    care_info = "kein Pflegedienst."
                family_living = "lebt ohne Familie"
            else:
                family_living = "lebt mit Familie"
            living_and_care = f"{family_living}, {care_info}"
        else:
            living_and_care = "lebt alleine"
    
        additional_notes = st.text_area("Zusätzliche Notizen:", key='additional_notes')
        anamnese_report += f"Patient {living_details}, {mobility_status} {living_and_care} Zusätzliche Notizen: {additional_notes}\n"
    
        # Berufsanamnese hinzufügen
        st.subheader('Berufsanamnese')
        occupation = st.text_input("Aktueller oder letzter Beruf:", key='occupation')
        exposure_to_substances = st.checkbox("Bestand Kontakt zu schädlichen Substanzen?", key='exposure')
        if exposure_to_substances:
            substances = st.text_area("Welche schädlichen Substanzen?", key='substances')
            anamnese_report += f"Beruf: {occupation}. Kontakt zu schädlichen Substanzen: Ja, insbesondere {substances}.\n"
        else:
            anamnese_report += f"Beruf: {occupation}. Kein Kontakt zu schädlichen Substanzen.\n"
    
    with tabs[6]:
        st.subheader('Spezifische Gesundheitsfragen und Körperliche Untersuchung (KU)')
    
        # Abfrage von Ödemen
        edemas = st.radio("Gibt es Ödeme?", ['Ja', 'Nein'])
        edema_info = f"Ödeme: Ja, Standort: {st.text_input('Wo befinden sich die Ödeme?')}" if edemas == 'Ja' else "Ödeme: Nein."
    
        # Abfrage von Wunden
        wounds = st.radio("Gibt es Wunden?", ['Ja', 'Nein'])
        wound_info = f"Wunden: Ja, Standort: {st.text_input('Wo befinden sich die Wunden?')}" if wounds == 'Ja' else "Wunden: Nein."
    
        # Abfrage von anderen Infektionsherden
        infection_sites = st.radio("Gibt es andere Infektionsherde?", ['Ja', 'Nein'])
        infection_info = f"Andere Infektionsherde: Ja, Details: {st.text_input('Beschreibung der Infektionsherde:')}" if infection_sites == 'Ja' else "Keine anderen Infektionsherde."
    
        # Blasendauerkatheter
        urinary_catheter = st.radio("Hat der Patient einen Blasendauerkatheter (BDK)?", ['Ja', 'Nein'])
        catheter_info = f"Blasendauerkatheter (BDK): {urinary_catheter}."
    
        # Abfrage von Gewicht und Körpergröße
        baseline_weight = st.number_input("Gewicht des Patienten (in kg):", min_value=0.0, format="%.2f")
        height = st.number_input("Körpergröße des Patienten (in cm):", min_value=0.0, format="%.2f")
    
        # Berechnung des BMI und der BSA
        if height > 0 and baseline_weight > 0:
            bmi = baseline_weight / ((height / 100) ** 2)
            bsa = 0.007184 * (height ** 0.725) * (baseline_weight ** 0.425)  # Mosteller Formula
    
            # Graduierung des BMI in Adipositasgrade
            if bmi < 18.5:
                bmi_classification = "Untergewicht"
            elif 18.5 <= bmi < 25:
                bmi_classification = "Normalgewicht"
            elif 25 <= bmi < 30:
                bmi_classification = "Übergewicht"
            elif 30 <= bmi < 35:
                bmi_classification = "Adipositas Grad I"
            elif 35 <= bmi < 40:
                bmi_classification = "Adipositas Grad II"
            else:
                bmi_classification = "Adipositas Grad III"
    
            weight_info = f"BMI: {bmi:.2f} ({bmi_classification}), Körperoberfläche (BSA): {bsa:.2f} m²."
        else:
            weight_info = "BMI und Körperoberfläche können nicht berechnet werden, da Gewicht oder Größe nicht spezifiziert."
    
        # Zusammenfassung des Berichts
        final_report = f"""
        ### Spezifische Gesundheitsfragen und Körperliche Untersuchung
    
        {edema_info}
        {wound_info}
        {infection_info}
        {catheter_info}
        Gewicht des Patienten: {baseline_weight} kg, Körpergröße: {height} cm.
        {weight_info}
        """
    
        additional_notes = st.text_area("Zusätzliche Notizen:", key='additional_notes_1')
        if additional_notes:
            final_report += f"\nZusätzliche Notizen: {additional_notes}"
    
        # Ausgabe des kohärenten und lesbaren Textes
        anamnese_report += final_report

        st.subheader('Notizen zur körperlichen Untersuchung')
        physical_examination_notes = st.text_area("Freier Textblock für die körperliche Untersuchung und Sonstige Auffälligkeiten", height=150)
        anamnese_report += f"Notizen zur körperlichen Untersuchung: {physical_examination_notes}\n\n"
    
        st.subheader('Allergien')
        allergies = st.checkbox("Haben Sie Allergien?")
        allergy_details = ""
    
        if allergies:
            st.write("Bitte geben Sie Details zu Ihren Allergien an:")
            welche_allergien = st.multiselect("Welche Allergien haben Sie?", ["Pollen", "Staub", "Nahrungsmittel", "Haustiere", "Medikamente", "Andere"], key='allergy_types')
            seit_wann_allergien = st.text_input("Seit wann bestehen diese Allergien?", max_chars=50, key='allergy_since')
            
            # Zusätzliche spezifische Fragen zu Pollen- und saisonalen Allergien
            seasonal_allergy = st.checkbox("Leiden Sie unter saisonalen Allergien?", key='seasonal_allergy')
            asthma_relevant = st.checkbox("Sind diese Allergien für Asthma relevant?", key='asthma_relevance')
            
            asthma_details = ", relevant für Asthma." if asthma_relevant else ", nicht direkt relevant für Asthma."
            seasonal_details = " Patient leidet auch unter saisonalen Allergien." if seasonal_allergy else ""
            
            allergy_summary = f"Patient hat folgende Allergien: {', '.join(welche_allergien)}, bestehen seit {seit_wann_allergien}.{asthma_details}{seasonal_details}\n"
            anamnese_report += allergy_summary
        else:
            anamnese_report += "Patient hat keine Allergien.\n"
    
        # Weitere Details oder Anmerkungen zu Allergien
        additional_allergy_notes = st.text_area("Weitere Anmerkungen zu Allergien:", key='additional_allergy_notes')
        if additional_allergy_notes:
            anamnese_report += f"Zusätzliche Anmerkungen zu Allergien: {additional_allergy_notes}\n"
    
    with tabs[7]:
        st.subheader('Checkliste vor der Anamnese')
        checklist_items = ['Blutentnahmen', 'Braunüle gelegt', 'Medikation abgeglichen', 'EKG geschrieben']
        checklist_status = {}
        for item in checklist_items:
            checklist_status[item] = st.checkbox(f'{item}', key=item)

        confirmed_actions = [item for item, checked in checklist_status.items() if checked]
        if confirmed_actions:
            anamnese_report_extra += "Zu Beginn der Aufnahme wurden folgende Maßnahmen durchgeführt: " + ', '.join(confirmed_actions) + ".\n\n"
        else:
            anamnese_report_extra += "Zu Beginn der Aufnahme wurden keine Maßnahmen durchgeführt.\n\n"


        st.subheader("Kontaktinformationen")
        patient_phone = st.text_input("Telefonnummer des Patienten", max_chars=15)
        relative_phone = st.text_input("Telefonnummer eines Angehörigen", max_chars=15)
        if patient_phone:
            anamnese_report_extra += f"Telefonnummer des Patienten: {patient_phone}. "
        if relative_phone:
            anamnese_report_extra += f"Telefonnummer eines Angehörigen: {relative_phone}. "
    
        transportation_needs = st.checkbox("Benötigen Sie einen Heimtransport nach stationärem Aufenthalt?")
        dnr_dni_wishes = st.checkbox("Ist ein DNR/DNI gewünscht?")
        living_will_exists = st.checkbox("Liegt eine Patientenverfügung vor?")
        anamnese_report_extra += f"Heimtransport benötigt: {'Ja' if transportation_needs else 'Nein'}. "
        anamnese_report_extra += f"DNR/DNI gewünscht: {'Ja' if dnr_dni_wishes else 'Nein'}. "
        anamnese_report_extra += f"Patientenverfügung vorhanden: {'Ja' if living_will_exists else 'Nein'}. "
    
        if alter < 50 and geschlecht == "Weiblich":
            schwanger = st.checkbox("Besteht eine Schwangerschaft?")
            pregnancy_status = "Schwanger: Ja" if schwanger else "Schwanger: Nein"
            anamnese_report += f" {pregnancy_status}."
    
    with tabs[8]:
        st.subheader('Spezifische Gesundheitsfragen')
        if st.button('Bericht als PDF speichern'):
            pdf_file = create_pdf(anamnese_report, anamnese_report_extra)
            with open(pdf_file, "rb") as file:
                st.download_button(
                    label="Download PDF",
                    data=file,
                    file_name=pdf_file,
                    mime="application/pdf"
                )
        
        st.subheader('Vorläufiger Anamnesebericht')
        st.text_area("", anamnese_report, height=600)
        st.text_area("", anamnese_report_extra, height=300)
    
if __name__ == "__main__":
    anamnese()


# In[ ]:





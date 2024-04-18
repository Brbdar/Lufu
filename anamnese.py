#!/usr/bin/env python
# coding: utf-8

# In[57]:


import streamlit as st
from fpdf import FPDF
from datetime import datetime
from dateutil.relativedelta import relativedelta
from COPD_Score import COPD_Score

def calculate_age(born):
    today = datetime.now().date()
    return relativedelta(today, born).years


def calculate_pack_years(cigarettes, years_smoked):
    return (cigarettes / 20) * years_smoked

def create_pdf(report):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, 'Pneumologischer Anamnesebericht', align='C')
    pdf.ln(20)  # Fügt eine Leerzeile nach dem Titel hinzu
    pdf.multi_cell(0, 10, report)
    filename = 'Pneumologischer_Anamnesebericht.pdf'
    pdf.output(filename)
    return filename

def anamnese():
    st.title('Pneumo Aufnahme')

    # Geburtsdatum und Geschlecht
    geburtstag = st.date_input("Geburtsdatum")
    geschlecht = st.radio("Geschlecht", options=["Weiblich", "Männlich", "Divers"])
    alter = calculate_age(geburtstag)  # Verwende die verbesserte Alterberechnung
    
    # Initialize Anamnese Report
    anamnese_report = "Pneumologische Anamnese Bericht:\n\n"

    
    st.subheader('Checkliste vor der Anamnese')

    # Definiere die Checklisten-Items
    checklist_items = ['Blutentnahmen', 'Braunüle gelegt', 'Medikation abgeglichen', 'EKG geschrieben']
    checklist_status = {}  # Ein Dictionary zum Speichern des Status jedes Items

    # Erstelle für jedes Item eine Checkbox und speichere den Status
    for item in checklist_items:
        checklist_status[item] = st.checkbox(f'{item}', key=item)

    # Sammle alle bestätigten Maßnahmen
    confirmed_actions = [item for item, checked in checklist_status.items() if checked]

    # Update den Anamnesebericht basierend auf den ausgewählten Maßnahmen
    if confirmed_actions:  # Nur wenn mindestens eine Maßnahme bestätigt wurde
        anamnese_report_extra = "Zu Beginn der Aufnahme wurden folgende Maßnahmen durchgeführt: " + ', '.join(confirmed_actions) + ".\n\n"
    else:
        anamnese_report_extra = "Zu Beginn der Aufnahme wurden keine der aufgelisteten Maßnahmen durchgeführt.\n\n"

    st.subheader('Aufnahmegrund')

    # Radio-Button Auswahl für den Aufnahmegrund
    reason_for_admission = st.radio('Aufnahmegrund:', ['Elektiv', 'Notfall'])

    # Erzeugung des Berichtseintrags basierend auf der Auswahl des Aufnahmegrunds
    if reason_for_admission == 'Elektiv':
        elective_reason = st.radio('Grund für die elektive Aufnahme:',
                                   ['Fibrose Verlaufskontrolle', 'BiPAP Verlaufskontrolle', 'PH Verlaufskontrolle'])
        details = st.text_area('Details zur elektiven Aufnahme', key='elective_detail')
        anamnese_report += f"Der Patient stellt sich elektiv zur {elective_reason} auf unserer Station vor. " \
                           f"Details zur Aufnahme: {details}.\n\n"

    elif reason_for_admission == 'Notfall':
        emergency_reason = st.radio('Grund für die notfallmäßige Aufnahme:',
                                    ['notfallmäßig über ZNA mit Infektion', 'notfallmäßig über ZNA mit AECOPD', 'notfallmäßig über ZNA mit unklarer Ursache'])
        details = st.text_area('Details zur notfallmäßigen Aufnahme', key='emergency_detail')
        anamnese_report += f"Der Patient wurde stationär mit {emergency_reason} über die Notaufnahme auf unserer Station aufgenommen. " \
                           f"Details zur Aufnahme: {details}.\n\n"
        # Handling the visibility of COPD scores based on the specific emergency reason
        if emergency_reason == 'notfallmäßig über ZNA mit AECOPD':
            if 'show_copd' not in st.session_state:
                st.session_state.show_copd = False

            if st.button("COPD Scores anzeigen"):
                st.session_state.show_copd = True

            if st.button("COPD Scores verbergen"):
                st.session_state.show_copd = False

            if st.session_state.show_copd:
                COPD_Score()  # Funktion, die COPD Scores anzeigt

    # 2. Vorerkrankungen
    st.subheader('Vorerkrankungen')
    existing_conditions = st.radio('Liegen Informationen zu Vorerkrankungen vor?', 
                                   ['Liegt in vorherigen Arztberichten vor', 'Neue Angabe erforderlich'])

    if existing_conditions == 'Neue Angabe erforderlich':
        conditions_detail = st.text_area('Bitte geben Sie die Vorerkrankungen an', key='conditions_detail')
        anamnese_report += f"Vorerkrankungen: {conditions_detail}\n\n"
    else:
        anamnese_report += "Vorerkrankungen liegen in vorherigen Arztberichten vor.\n\n"

    ############SYMPTOME
    st.subheader('Symptome')
    symptoms_list = ['Husten', 'Dyspnoe', 'Brustschmerzen', 'Atemnot', 'Fieber', 'Gewichtsverlust', 'Nächtliches Schwitzen', 'Auswurf', 'Keine']
    symptoms = st.multiselect('Bitte Symptome auswählen:', symptoms_list)
    b_symptoms = set(['Fieber', 'Gewichtsverlust', 'Nächtliches Schwitzen'])

    sputum_color = 'Kein Auswurf'  # Standardwert setzen

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

    # Fragen zur Dyspnoe
    dyspnoea_rest = st.radio('Besteht Dyspnoe in Ruhe?', ['Ja', 'Nein'])
    dyspnoea_exertion = st.radio('Besteht Dyspnoe bei Belastung?', ['Ja', 'Nein'])
    walk_distance = st.text_input('Wie lange kann der Patient auf ebener Strecke gehen?', key='walk')
    stairs_climbed = st.text_input('Wie viele Stockwerke können gegangen werden?', key='stock')
    speak_dyspnoea = st.radio('Besteht Sprechdyspnoe?', ['Ja', 'Nein'])
    bendopnea = st.radio('Besteht Bendopnoe?', ['Ja', 'Nein'])

    # Information bei Bendopnoe
    if bendopnea == 'Ja':
        st.info('Wenn Bendopnoe besteht, dann überprüfen, ob der Patient an pulmonaler Hypertonie leidet.')
        anamnese_report += "Der Patient gibt an, unter Bendopnoe zu leiden, was eine Überprüfung auf pulmonale Hypertonie nahelegt. "

    # NYHA-Klassifizierung
    nyha_class = 'NYHA Class I'  # Standard als Class I setzen
    if dyspnoea_rest == 'Nein' and dyspnoea_exertion == 'Nein':
        nyha_class = 'NYHA Class I'
    elif dyspnoea_rest == 'Ja' and dyspnoea_exertion == 'Nein':
        nyha_class = 'NYHA Class II'
    elif dyspnoea_rest == 'Ja' and dyspnoea_exertion == 'Ja':
        nyha_class = 'NYHA Class III'
    elif dyspnoea_rest == 'Nein' and dyspnoea_exertion == 'Ja':
        nyha_class = 'NYHA Class IV'

    # Zusammenfassung der Dyspnoe-Informationen in den Anamnesebericht einfügen
    anamnese_report += f"Der Patient berichtet von {'keiner' if dyspnoea_rest == 'Nein' else 'einer'} Dyspnoe in Ruhe und {'keiner' if dyspnoea_exertion == 'Nein' else 'einer'} Dyspnoe bei Belastung. "
    if dyspnoea_exertion == 'Ja':
        anamnese_report += f"Er/Sie kann auf ebener Strecke etwa {walk_distance} gehen und bis zu {stairs_climbed} Stockwerke steigen. "
    anamnese_report += f"Sprechdyspnoe wurde {'nicht ' if speak_dyspnoea == 'Nein' else ''}berichtet. "
    anamnese_report += f"Die NYHA Klassifizierung lautet {nyha_class}."
    
    
    st.subheader('Pektanginöse Beschwerden')

    # Erfassung von Angaben zu pektanginösen Beschwerden
    angina_symptoms = st.radio('Bestehen pektanginöse Beschwerden?', ['Ja', 'Nein'])

    if angina_symptoms == 'Ja':
    # Zusätzliche Details erfragen, wenn Beschwerden bestehen
        angina_duration = st.text_input('Seit wann bestehen die Beschwerden?', key='besch')
        angina_location = st.text_input('Wo genau treten die Beschwerden auf?', key='angina')

    # Anhängen der Informationen an den Anamnesebericht
        anamnese_report += (f"Der Patient berichtet über pektanginöse Beschwerden, die seit {angina_duration} bestehen. "
                        f"Die Beschwerden treten hauptsächlich in der Region {angina_location} auf.\n")
    elif angina_symptoms == 'Nein':
        # Information über das Fehlen von Beschwerden in den Bericht aufnehmen
        anamnese_report += "Pektanginöse Beschwerden wurden verneint.\n"

    # Abfrage zu Schwindel und Synkopen
    st.subheader('Schwindel und Synkopen')

    # Begin the report section for Dizziness and Syncope
    anamnese_report += "Bezüglich Schwindel und Synkopen"

    # Dizziness Inquiry
    dizziness = st.radio('Besteht Schwindel?', ['Ja', 'Nein'])
    if dizziness == 'Ja':
        dizziness_frequency = st.text_input('Wie häufig tritt der Schwindel auf?', key='schwind')
        dizziness_quality = st.text_input('Beschreiben Sie die Qualität des Schwindels (z.B. drehend, schwankend etc.).', key='schwindart')
        recommended_actions = st.checkbox('Soll ein Langzeit-EKG und eine HNO-Untersuchung empfohlen werden?')

        # Collecting dizziness details
        dizziness_details = (f"Schwindel ist vorhanden und tritt mit einer Frequenz von {dizziness_frequency} auf. "
                             f"Der Schwindel wird als {dizziness_quality} beschrieben.")
        anamnese_report += dizziness_details

        # Adding recommendations based on user input
        if recommended_actions:
            anamnese_report += " Empfohlene Maßnahmen: Durchführung eines Langzeit-EKGs und Vorstellung beim HNO."

    # Begin the report section for Dizziness and Syncope, if not already started
    if '### Schwindel und Synkopen' not in anamnese_report:
        anamnese_report += "Schwindel und Synkopen"

    # Dizziness Inquiry - Ensure it only runs if not already asked
    if 'dizziness' not in locals():
        dizziness = st.radio('Besteht Schwindel?', ['Ja', 'Nein'])
        if dizziness == 'Ja':
            dizziness_frequency = st.text_input('Wie häufig tritt der Schwindel auf?', key='schwindartr')
            dizziness_quality = st.text_input('Beschreiben Sie die Qualität des Schwindels (z.B. drehend, schwankend etc.).', key='schwdbf')
            dizziness_details = (f"Schwindel ist vorhanden und tritt mit einer Frequenz von {dizziness_frequency} auf. "
                                 f"Der Schwindel wird als {dizziness_quality} beschrieben.")
            anamnese_report += dizziness_details
            st.info('Bitte Langzeit-EKG durchführen. Ggf. HNO anmelden.')

    # Syncope Inquiry
    syncope = st.radio('Sind Synkopen bekannt?', ['Ja', 'Nein'])
    if syncope == 'Ja':
        syncope_frequency = st.text_input('Wann und wie oft treten die Synkopen auf?', key='scnk')
        syncope_details = (f"Synkopen sind bekannt und treten auf mit einer Häufigkeit von: {syncope_frequency}.")
        anamnese_report += syncope_details
        st.info('Bitte Differentialdiagnosen wie Myokarditis, Aortenklappenstenose, Vorhofflimmern in Betracht ziehen.')
    elif syncope == 'Nein' and dizziness == 'Nein':
        # Only add this if no conditions are reported
        anamnese_report += "Es bestehen keine Berichte über Schwindel oder Synkopen. "
    
     ###################### Inquiry about Abdominal Issues
    st.subheader('Bauchbeschwerden')
    abdominal_symptoms = st.radio('Bestehen Bauchschmerzen, Übelkeit, Erbrechen oder Durchfall?', ['Ja', 'Nein'])
    abdominal_details = ""  # Initialize to ensure it's defined

    if abdominal_symptoms == 'Ja':
        abdominal_onset = st.text_input('Seit wann bestehen die Beschwerden?', key='abdo')
        abdominal_details = f"Beginn der Beschwerden: {abdominal_onset}. "

    # Update the Anamnese report with conditional details
    anamnese_report += f"Bauchschmerzen, Übelkeit, Erbrechen oder Durchfall: {abdominal_symptoms}. {abdominal_details}"

    ######
    # Inquiry about Urination or Defecation Issues
    st.subheader('Miktions- oder Defäkationsbeschwerden')
    urination_defecation_symptoms = st.radio('Bestehen Miktions- oder Defäkationsbeschwerden?', ['Ja', 'Nein'])
    defecation_details = ""  # Initialize to ensure it's defined

    if urination_defecation_symptoms == 'Ja':
        onset_frequency = st.text_input('Seit wann bestehen die Beschwerden und wie oft treten sie auf?', key='freq')
        defecation_type = ""  # Initialize to ensure it's defined even if not set

        # Conditional input based on specific defecation complaints
        if 'Defäkationsbeschwerden' in onset_frequency:  # Checking if the keyword is part of the user input
            defecation_type = st.text_input('Welche Art von Defäkationsbeschwerden bestehen?', key='defaqn')
            st.info('Bitte weitere Informationen erfassen, falls erforderlich.')

        # Compile details about urination or defecation issues
        defecation_details = (f"Beginn und Häufigkeit der Beschwerden: {onset_frequency}. "
                              f"Art der Defäkationsbeschwerden: {defecation_type} ")

    # Update the Anamnese report with compiled details
    anamnese_report += f"\nMiktions- oder Defäkationsbeschwerden: {urination_defecation_symptoms}. {defecation_details}"
    
    st.header('Heimsauerstoff')
    home_oxygen = st.radio('Wird Heimsauerstoff verwendet?', ['Ja', 'Nein'], index=1, key='home_oxygen')

    if home_oxygen == 'Ja':
        oxygen_since = st.text_input('Seit wann wird Heimsauerstoff verwendet?', key='oxygen_since')
        oxygen_amount = st.number_input('Wie viel Liter pro Minute?', min_value=0.1, max_value=10.0, step=0.1, key='oxygen_amount')

        # Update the Anamnese report with formatted oxygen usage details
        anamnese_report += (f"Heimsauerstoff wird seit {oxygen_since} verwendet, "
                            f"mit einer Flussrate von {oxygen_amount:.1f} Litern pro Minute. ")
    else:
        # Ensure the report notes the absence of home oxygen use if applicable
        anamnese_report += "Es wird kein Heimsauerstoff verwendet. "

    ##################### Anticoagulation
    st.header('Antikoagulation')
    anticoagulation = st.radio('Wird eine Antikoagulation durchgeführt?', ['Ja', 'Nein'], index=1, key='anticoagulation')

    # Collecting information on anticoagulation
    if anticoagulation == 'Ja':
        anticoagulant_type = st.text_input('Welches Antikoagulans wird verwendet?', key='anticoagulant_type')
        anamnese_report += f"Antikoagulation mit {anticoagulant_type}. "
    else:
        # Document if no anticoagulation is being used
        anamnese_report += "Es wird keine Antikoagulation durchgeführt. "

    ##################### Platelet Inhibition
    st.header('Plättchenhemmung')
    platelet_inhibition = st.radio('Wird eine Plättchenhemmung durchgeführt?', ['Ja', 'Nein'], index=1, key='platelet_inhibition')

    # Collecting information on platelet inhibition
    if platelet_inhibition == 'Ja':
        platelet_inhibitor_type = st.text_input('Welches Plättchenhemmer wird verwendet?', key='platelet_inhibitor_type')
        platelet_inhibition_reason = st.text_input('Aus welchem Grund wird die Plättchenhemmung durchgeführt?', key='platelet_inhibition_reason')
        anamnese_report += (f"Plättchenhemmung mit {platelet_inhibitor_type} aufgrund von {platelet_inhibition_reason}. ")
    else:
        # Document if no platelet inhibition is being used
        anamnese_report += "Es wird keine Plättchenhemmung durchgeführt. "

    ###################### Allergies
    st.subheader('Allergien')
    allergies = st.checkbox("Haben Sie Allergien?")
    allergy_details = ""

    if allergies:
        welche_allergien = st.text_input("Welche Allergien haben Sie?", max_chars=50)
        seit_wann_allergien = st.text_input("Seit wann bestehen diese Allergien?", max_chars=50)
        allergy_details = f"Allergien: {welche_allergien}, bestehen seit {seit_wann_allergien}. "
    else:
        allergy_details = "Keine Allergien vorhanden. "

    anamnese_report += allergy_details

   # 4. Rauchgewohnheiten
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
            # Detailed text area for each type of smoking, if multiple types are used
            details_cigarettes = st.text_area("Details zu Zigarettenkonsum", placeholder="Anzahl pro Tag, seit wie vielen Jahren?")
            details_shisha = st.text_area("Details zu Shisha-Konsum", placeholder="Sitzungen pro Woche, seit wie vielen Jahren?")
            details_vaping = st.text_area("Details zu Vaping", placeholder="Anzahl der Nutzung pro Tag, seit wie vielen Jahren?")
            multi_smoking_details = f"Zigaretten: {details_cigarettes}, Shisha: {details_shisha}, Vaping: {details_vaping}"
            anamnese_report += f"Verschiedene Rauchgewohnheiten: {multi_smoking_details}"
    else:
        anamnese_report += "Keine Rauchanamnese vorhanden."
    
    ###################### Alcohol and Drug Use
    st.subheader('Konsum von Alkohol und Drogen')
    # Alcohol consumption inquiry
    alcohol_use = st.checkbox("Konsumieren Sie Alkohol?")
    alcohol_details = ""

    if alcohol_use:
        alcohol_duration = st.text_input("Seit wann konsumieren Sie Alkohol?", key='alcohol_duration')
        alcohol_details = f"Alkoholkonsum: Ja, seit {alcohol_duration}. "
    else:
        alcohol_details = "Alkoholkonsum: Nein. "

    # Drug use inquiry
    drug_use = st.checkbox("Konsumieren Sie Drogen?")
    drug_details = ""

    if drug_use:
        drug_duration = st.text_input("Seit wann konsumieren Sie Drogen?", key='drug_duration')
        drug_details = f"Drogenkonsum: Ja, seit {drug_duration}. "
    else:
        drug_details = "Drogenkonsum: Nein. "

    # Append information to the anamnese report
    anamnese_report += alcohol_details + drug_details
    
    ###################### Social History
    st.subheader('Sozialanamnese')

    ###################### Living Situation
    st.subheader('Lebenssituation')

    living_situation = st.radio("Leben Sie alleine?", ['Ja', 'Nein'], key='living_situation')

    # Mobility question is asked regardless of living situation
    mobility = st.radio("Wie ist Ihre Mobilität?", ['Unabhängig', 'Eingeschränkt', 'Stark eingeschränkt'], key='mobility')

    if living_situation == 'Nein':
        family_status = st.radio("Leben Sie mit Ihrer Familie?", ['Ja', 'Nein'], key='family_status')
        if family_status == 'Nein':
            care_service = st.checkbox("Wird ein Pflegedienst in Anspruch genommen?", key='care_service')
            care_degree = st.selectbox("Falls ja, welcher Pflegegrad liegt vor?", ['', 'Pflegegrad 1', 'Pflegegrad 2', 'Pflegegrad 3', 'Pflegegrad 4', 'Pflegegrad 5'], index=0, key='care_degree')

            if care_service:
                anamnese_report += f"Lebt ohne Familie, Mobilität: {mobility}, Pflegedienst: Ja, Pflegegrad: {care_degree}. "
            else:
                anamnese_report += f"Lebt ohne Familie, Mobilität: {mobility}, kein Pflegedienst. "
        else:
            anamnese_report += f"Lebt mit Familie, Mobilität: {mobility}. "
    else:
        anamnese_report += f"Lebt alleine, Mobilität: {mobility}. "

    # Additional notes field
    additional_notes = st.text_area("Zusätzliche Notizen:", key='additional_notes')
    anamnese_report += f"Zusätzliche Notizen: {additional_notes}"

    ###################### Physical Examination Notes
    st.subheader('Notizen zur körperlichen Untersuchung')
    physical_examination_notes = st.text_area("Freier Textblock für die körperliche Untersuchung und Sonstige Auffälligkeiten", height=150)
    anamnese_report += f"Notizen zur körperlichen Untersuchung: {physical_examination_notes}\n\n"

    ###################### Specific Health Inquiries
    st.subheader('Spezifische Gesundheitsfragen')

    # Inquiry about edemas
    edemas = st.radio("Gibt es Ödeme?", ['Ja', 'Nein'])
    if edemas == 'Ja':
        edema_location = st.text_input("Wo befinden sich die Ödeme?")
        anamnese_report += f"Ödeme: Ja, Standort: {edema_location}. "
    else:
        anamnese_report += "Ödeme: Nein. "

    # Inquiry about wounds
    wounds = st.radio("Gibt es Wunden?", ['Ja', 'Nein'])
    if wounds == 'Ja':
        wound_location = st.text_input("Wo befinden sich die Wunden?")
        anamnese_report += f"Wunden: Ja, Standort: {wound_location}. "
    else:
        anamnese_report += "Wunden: Nein. "

    # Inquiry about other infection sites
    infection_sites = st.radio("Gibt es andere Infektionsherde?", ['Ja', 'Nein'])
    if infection_sites == 'Ja':
        infection_site_details = st.text_input("Beschreibung der Infektionsherde:")
        anamnese_report += f"Andere Infektionsherde: Ja, Details: {infection_site_details}. "
    else:
        anamnese_report += "Keine anderen Infektionsherde. "

    # Inquiry about urinary catheter
    urinary_catheter = st.radio("Hat der Patient einen Blasendauerkatheter (BDK)?", ['Ja', 'Nein'])
    anamnese_report_extra += f"Blasendauerkatheter (BDK): {urinary_catheter}. "

    # Inquiry about baseline weight
    baseline_weight = st.number_input("Wie hoch ist das Basisgewicht des Patienten (in kg)?", min_value=0.0, format="%.2f")
    anamnese_report_extra += f"Basisgewicht des Patienten: {baseline_weight} kg."
    
    # Contact information
    st.subheader("Kontaktinformationen")
    patient_phone = st.text_input("Telefonnummer des Patienten", max_chars=15)
    relative_phone = st.text_input("Telefonnummer eines Angehörigen", max_chars=15)

    # Append contact information to the report
    if patient_phone:
        anamnese_report_extra += f"Telefonnummer des Patienten: {patient_phone}. "
    if relative_phone:
        anamnese_report_extra += f"Telefonnummer eines Angehörigen: {relative_phone}. "
    
    ###################### Transportation, DNR/DNI, Living Will
    transportation_needs = st.checkbox("Benötigen Sie einen Heimtransport nach stationärem Aufenthalt?")
    dnr_dni_wishes = st.checkbox("Ist ein DNR/DNI gewünscht?")
    living_will_exists = st.checkbox("Liegt eine Patientenverfügung vor?")

    # Append information to the report
    anamnese_report_extra += f"Heimtransport benötigt: {'Ja' if transportation_needs else 'Nein'}. "
    anamnese_report_extra += f"DNR/DNI gewünscht: {'Ja' if dnr_dni_wishes else 'Nein'}. "
    anamnese_report_extra += f"Patientenverfügung vorhanden: {'Ja' if living_will_exists else 'Nein'}. "

    ###################### Pregnancy Question for Relevant Users
    if alter < 50 and geschlecht == "Weiblich":
        schwanger = st.checkbox("Besteht eine Schwangerschaft?")
        pregnancy_status = "Schwanger: Ja" if schwanger else "Schwanger: Nein"
        anamnese_report += f" {pregnancy_status}."
    
     # PDF Erstellung und Download
    if st.button('Bericht als PDF speichern'):
        anamnese_report = "Hier wird der vollständige Anamnesebericht erstellt."
        pdf_file = create_pdf(anamnese_report)
        with open(pdf_file, "rb") as file:
            st.download_button(
                label="Download PDF",
                data=file,
                file_name=pdf_file,
                mime="application/pdf"
            )

    # Anzeige des vorläufigen Anamneseberichts
    st.subheader('Vorläufiger Anamnesebericht')
    st.text_area("", anamnese_report, height=600)
    st.text_area("", anamnese_report_extra, height=300)


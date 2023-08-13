# auth: Flynn Wang
# date: 12/08/23
# desc: GUI of clinic

from tkinter import *
from tkinter import messagebox

from controller import Clinic

clinic_name = 'XYZ Medical Center'
clinic = Clinic(clinic_name)

# window elements
root = Tk()
root.title(clinic_name)

# Frame 1
frame1 = LabelFrame(root)
label_patients = Label(frame1, text='Patients')
listbox_patients = Listbox(frame1, exportselection=0)
for patient in clinic.patients:
    listbox_patients.insert(patient.id, patient)
label_doctors = Label(frame1, text='Doctors')
listbox_doctors = Listbox(frame1, exportselection=0)
for doctor in clinic.doctors:
    listbox_doctors.insert(doctor.id, doctor)
label_frame_consultations = LabelFrame(frame1, text='Consultation')
label_date = Label(label_frame_consultations, text='Date:')
entry_date = Entry(label_frame_consultations)
label_reason = Label(label_frame_consultations, text='Reason:')
entry_reason = Entry(label_frame_consultations)
label_fee = Label(label_frame_consultations, text='Fee:')
entry_fee = Entry(label_frame_consultations)
label_date.grid(row=0, column=0, padx=10, pady=10)
entry_date.grid(row=0, column=1, padx=10, pady=10)
label_reason.grid(row=1, column=0, padx=10, pady=10)
entry_reason.grid(row=1, column=1, padx=10, pady=10)
label_fee.grid(row=2, column=0, padx=10, pady=10)
entry_fee.grid(row=2, column=1, padx=10, pady=10)

label_patients.grid(row=0, column=0, padx=10, pady=10)
listbox_patients.grid(row=1, column=0, padx=10, pady=10)
label_doctors.grid(row=0, column=1, padx=10, pady=10)
listbox_doctors.grid(row=1, column=1, padx=10, pady=10)
label_frame_consultations.grid(row=0, column=2, rowspan=2, padx=10, pady=10)
frame1.pack(side=TOP, fill="x", padx=10, pady=10)


def get_selected_doctor():
    selected_item = listbox_doctors.curselection()
    if not selected_item:
        messagebox.showerror('Error', 'Please select a doctor!')
        return
    doctor_id = listbox_doctors.get(selected_item)
    selected_doctor = clinic.search_for_doctor(doctor_id)
    return selected_doctor


def get_selected_patient():
    selected_item = listbox_patients.curselection()
    if not selected_item:
        messagebox.showerror('Error', 'Please select a patient!')
        return
    patient_id = listbox_patients.get(selected_item)
    selected_patient = clinic.search_for_patient(patient_id)
    return selected_patient


def assign_doctor():
    selected_doctor = get_selected_doctor()
    selected_patient = get_selected_patient()
    if selected_doctor and selected_patient:
        clinic.assign_doctor2patient(selected_doctor.id, selected_patient.id)
        messagebox.showinfo('Assign Doctor', f'{selected_doctor} is assigned to {selected_patient}')


def add_consultation():
    selected_doctor = get_selected_doctor()
    selected_patient = get_selected_patient()
    if selected_doctor and selected_patient:
        date = entry_date.get()
        reason = entry_reason.get()
        try:
            fee = float(entry_fee.get())
            if date and reason and fee:
                clinic.add_consultation(date, selected_doctor.id, selected_patient.id, reason, fee)
                messagebox.showinfo('Add Consultation', f'Consultation is added to {selected_patient}')
            else:
                messagebox.showerror('Error', 'Please fill in all the fields!')
        except ValueError:
            messagebox.showerror('Error', 'Please enter a valid fee!')


def doctor_information():
    selected_doctor = get_selected_doctor()
    if selected_doctor:
        messagebox.showinfo('Doctor Information', f'{clinic.get_doctor_information(selected_doctor.id)}')


def patient_information():
    selected_patient = get_selected_patient()
    if selected_patient:
        messagebox.showinfo('Patient Information', f'{clinic.get_patient_information(selected_patient.id)}')


def consultation_report():
    messagebox.showinfo('Consultation Report', f'{clinic.get_consultation_report()}')


# Frame 2
frame2 = LabelFrame(root)
button_assign_doctor = Button(frame2, text='Assign Doctor', command=assign_doctor)
button_add_consultation = Button(frame2, text='Add Consultation', command=add_consultation)
button_assign_doctor.pack(side=LEFT, padx=10, pady=10)
button_add_consultation.pack(side=RIGHT, padx=10, pady=10)
frame2.pack(fill="x", padx=10, pady=10)

# Frame 3
frame3 = LabelFrame(root)
frame_left = Frame(frame3)
frame_right = Frame(frame3)
button_doctor_information = Button(frame_left, text='Doctor Information', command=doctor_information)
button_patient_information = Button(frame_left, text='Patient Information', command=patient_information)
button_consultation_report = Button(frame_right, text='Consultation Report', command=consultation_report)

button_doctor_information.pack(side=TOP, padx=10, pady=10)
button_patient_information.pack(side=BOTTOM, padx=10, pady=10)
button_consultation_report.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
frame_left.pack(side=LEFT, padx=10, pady=10)
frame_right.pack(side=RIGHT, padx=10, pady=10)
frame3.pack(side=BOTTOM, fill="x", padx=10, pady=10)

root.mainloop()

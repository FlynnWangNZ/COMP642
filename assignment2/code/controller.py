# auth: Flynn Wang
# date: 12/08/23
# desc:
from model import Doctor, Patient, Consultation


class Clinic:
    def __init__(self, name):
        self.__name = name
        self.__doctors = []
        self.__patients = []
        self.__consultations = []
        self.__read_doctors_from_file()
        self.__read_patients_from_file()

    def __read_doctors_from_file(self):
        with open('Doctor.txt', 'r') as f:
            for line in f:
                info = line.split(',')
                doctor = Doctor(info[0].strip(), info[1].strip(), info[2].strip())
                self.doctors.append(doctor)

    def __read_patients_from_file(self):
        with open('Patient.txt', 'r') as f:
            for line in f:
                info = line.split(',')
                patient = Patient(info[0].strip(), info[1].strip())
                self.patients.append(patient)

    @property
    def name(self):
        return self.__name

    @property
    def doctors(self):
        return self.__doctors

    @property
    def patients(self):
        return self.__patients

    @property
    def consultations(self):
        return self.__consultations

    def assign_doctor2patient(self, doctor_id, patient_id):
        doctor = self.search_for_doctor(doctor_id)
        patient = self.search_for_patient(patient_id)
        doctor.patients.append(patient)
        patient.doctor = doctor

    def add_consultation(self, date, doctor_id, patient_id, reason, fee):
        doctor = self.search_for_doctor(doctor_id)
        patient = self.search_for_patient(patient_id)
        consultation = Consultation(date, doctor, patient, reason, fee)
        self.__consultations.append(consultation)

    def search_for_doctor(self, kw):
        for doctor in self.doctors:
            if str(kw) in doctor.__str__():
                return doctor
        return None

    def get_doctor_information(self, doctor_id):
        doctor = self.search_for_doctor(doctor_id)
        doctor_information = doctor.__str__() + '\n\nPatient List:\n'
        for patient in doctor.patients:
            doctor_information += patient.__str__() + '\n'

        doctor_information += '\nConsultations:\n'
        for consultation in doctor.consultations:
            doctor_information += consultation.__str__() + '\n'

        return doctor_information

    def search_for_patient(self, kw):
        for patient in self.patients:
            if str(kw) in patient.__str__():
                return patient
        return None

    def get_patient_information(self, patient_id):
        patient = self.search_for_patient(patient_id)
        patient_information = patient.__str__() + '\n- Doctor:' + patient.doctor.__str__()
        patient_information += '\n\nConsultations:\n'
        for consultation in patient.consultations:
            patient_information += consultation.__str__() + '\n'
        patient_information += '\nTotal Fees Due: $' + str(patient.get_total_fee())
        return patient_information

    def __get_total_fee(self):
        total_fee = 0
        for consultation in self.consultations:
            total_fee += consultation.fee
        return total_fee

    def get_consultation_report(self):
        report = 'Consultation Report for ' + self.name + '\n\n'
        for consultation in self.consultations:
            report += consultation.__str__() + '\n'
        report += '\nTotal Fees: $' + str(self.__get_total_fee())
        return report

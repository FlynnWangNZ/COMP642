# auth: Flynn Wang
# date: 12/08/23
# desc:


class Doctor:
    doctor_id = 1000

    def __init__(self, firstname, lastname, specialisation):
        self.__id = Doctor.doctor_id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__specialisation = specialisation
        self.__patients = []
        self.__consultations = []
        Doctor.doctor_id += 1

    @property
    def id(self):
        return self.__id

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def specialisation(self):
        return self.__specialisation

    @property
    def patients(self):
        return self.__patients

    @patients.setter
    def patients(self, patient):
        self.__patients.append(patient)

    @property
    def consultations(self):
        return self.__consultations

    def add_consultation(self, consultation):
        self.__consultations.append(consultation)

    def __str__(self):
        return f"{self.id} {self.firstname} {self.lastname}"


class Patient:
    patient_id = 100

    def __init__(self, firstname, lastname):
        self.__id = Patient.patient_id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__doctor = None
        self.__consultations = []
        Patient.patient_id += 1

    @property
    def id(self):
        return self.__id

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def doctor(self):
        return self.__doctor

    @doctor.setter
    def doctor(self, doctor):
        self.__doctor = doctor

    @property
    def consultations(self):
        return self.__consultations

    def add_consultation(self, consultation):
        self.consultations.append(consultation)

    def display_consultations(self):
        for consultation in self.consultations:
            print(consultation)

    def get_total_fee(self):
        total_fee = 0
        for consultation in self.consultations:
            total_fee += consultation.fee
        return total_fee

    def __str__(self):
        return f"{self.id} {self.firstname} {self.lastname}"


class Consultation:

    def __init__(self, date, doctor, patient, reason, fee):
        self.__date = date
        self.__doctor = doctor
        self.doctor.add_consultation(self)
        self.__patient = patient
        self.patient.add_consultation(self)
        self.__reason = reason
        self.__fee = fee

    @property
    def date(self):
        return self.__date

    @property
    def doctor(self):
        return self.__doctor

    @property
    def patient(self):
        return self.__patient

    @property
    def reason(self):
        return self.__reason

    @property
    def fee(self):
        return self.__fee

    def __str__(self):
        return f"{self.date} {self.reason} {self.patient} {self.fee}"

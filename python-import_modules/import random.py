class Patient:
    def __init__(self, id, name, age, gender, admission_date, condition):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.condition = condition


    def get_details(self):
        return f"{self.name} with id {self.id} is {self.gender} and {self.age} years old. the date of admission date is {self.admission_date} and the condition {self.condition}"


patient_detail = Patient(89, "Telda", 26, "M", "may", "Good")
print(patient_detail.get_details())
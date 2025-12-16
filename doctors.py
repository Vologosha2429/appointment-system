class DoctorsModule:
    def __init__(self):
        self.doctors = [
            {"id": 1, "name": "Dr. Smith", "specialty": "Cardiology"},
            {"id": 2, "name": "Dr. Johnson", "specialty": "Dermatology"}
        ]

    def get_doctors(self):
        return self.doctors

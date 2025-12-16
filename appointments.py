class AppointmentsModule:
    def __init__(self):
        self.appointments = []

    def create_appointment(self, user_id, doctor_id, time):
        appointment = {
            "user_id": user_id,
            "doctor_id": doctor_id,
            "time": time
        }
        self.appointments.append(appointment)
        return {"status": "ok", "appointment": appointment}

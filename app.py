from flask import Flask, request, jsonify
from users import UsersModule
from doctors import DoctorsModule
from appointments import AppointmentsModule

app = Flask(__name__)

users = UsersModule()
doctors = DoctorsModule()
appointments = AppointmentsModule()

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    return jsonify(users.register_user(data["name"], data["email"]))

@app.route("/doctors", methods=["GET"])
def get_doctors():
    return jsonify(doctors.get_doctors())

@app.route("/appointments", methods=["POST"])
def create_appointment():
    data = request.json
    return jsonify(
        appointments.create_appointment(
            data["user_id"],
            data["doctor_id"],
            data["time"]
        )
    )

if __name__ == "__main__":
    app.run(debug=True)

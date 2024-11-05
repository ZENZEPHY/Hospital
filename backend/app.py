from flask import Flask, jsonify,  request
from flask_cors import CORS

from database import MySqlDB

db = MySqlDB()

app = Flask(__name__) 

CORS(app,supports_credentials=True)  # corss policy violation

@app.route('/loginUser',methods=['POST'])
def login_user():
    username = request.json["username"]
    password = request.json["password"]

    if not username or not password:
        return jsonify({"message": "Some mandatory fields need to be filled"}),400

    check = db.fetchone("SELECT id FROM users WHERE username=%s and password=%s",username,password)

    if not check:
        return jsonify({"message": "Email or password is incorrect"}),400
    
    return jsonify({"message": "login success"}),200


@app.route('/registerUser',methods=['POST'])
def register_user():
    
    username = request.json["username"]
    date = request.json["date"]
    password = request.json["password"]
    repassword = request.json["confirmPassword"]
    email = request.json["email"]
    phoneNumber = request.json["phoneNumber"]

    # check = db.fetchone("SELECT * FROM login WHERE email=%s",email)
    # if check:
    #     return jsonify({"message": "This Email is already registered!"}),400

    if password!=repassword:
        return jsonify({"message": "Passwords does not match!"}),400
    
    db.execute("INSERT INTO users(username,date,password,email,phone) VALUES(%s,%s,%s,%s,%s)",username,date,password,email,phoneNumber)
    return jsonify({"message": "Account Registered successfully."}),200

@app.route('/loginDoctor', methods=['POST'])
def login_doctor():
    username = request.json["username"]
    password = request.json["password"]

    if not username or not password:
        return jsonify({"message": "Some mandatory fields need to be filled"}), 400

    check = db.fetchone("SELECT id FROM doctors WHERE username=%s and password=%s", username, password)

    if not check:
        return jsonify({"message": "Email or password is incorrect"}), 400

    return jsonify({"message": "login success"}), 200


@app.route('/registerDoctor', methods=['POST'])
def register_doctor():
    username = request.json["username"]
    date = request.json["date"]
    password = request.json["password"]
    repassword = request.json["confirmPassword"]
    email = request.json["email"]
    phoneNumber = request.json["phoneNumber"]


    if password != repassword:
        return jsonify({"message": "Passwords do not match!"}), 400

    db.execute("INSERT INTO doctors(username, date, password, email, phoneNumber) VALUES(%s, %s, %s, %s, %s)",
               username, date, password, email, phoneNumber)
    return jsonify({"message": "Account Registered successfully."}), 200



@app.route('/scheduleAppointment', methods=['POST'])
def schedule_appointment():
    patient_name = request.json["patientName"]
    doctor_name = request.json["doctorName"]
    date = request.json["date"]
    time = request.json["time"]

    # You can add any validation or checks here if needed

    # Insert the appointment into the database
    db.execute("INSERT INTO appointments(patient_name, doctor_name, date, time) VALUES(%s, %s, %s, %s)", 
               patient_name, doctor_name, date, time)
    
    return jsonify({"message": "Appointment scheduled successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
    
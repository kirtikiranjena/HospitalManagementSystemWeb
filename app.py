from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample data
doctors = [
    {'id': 1, 'name': 'Dr. Arjun Mehta', 'department': 'Cardiology'},
    {'id': 2, 'name': 'Dr. Naina Sinha', 'department': 'Neurology'},
    {'id': 3, 'name': 'Dr. Rohit Sharma', 'department': 'Orthopedics'},
    {'id': 4, 'name': 'Dr. Meera Kapoor', 'department': 'Dermatology'},
    {'id': 5, 'name': 'Dr. Rakesh Das', 'department': 'Pediatrics'},
    {'id': 6, 'name': 'Dr. Anita Rao', 'department': 'Oncology'},
    {'id': 7, 'name': 'Dr. Dev Mishra', 'department': 'Radiology'},
    {'id': 8, 'name': 'Dr. Sneha Roy', 'department': 'Psychiatry'},
    {'id': 9, 'name': 'Dr. Vishal Nayak', 'department': 'ENT'},
    {'id': 10, 'name': 'Dr. Priya Patil', 'department': 'General Medicine'}
]

patients = []
bills = []

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Add patient
@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        address = request.form['address']
        department = request.form['department']

        doctor = next((doc for doc in doctors if doc['department'] == department), None)
        patient_id = len(patients) + 1
        assigned_doctor = doctor['name'] if doctor else 'Not Assigned'

        patients.append({
            'id': patient_id,
            'name': name,
            'age': age,
            'address': address,
            'doctor': assigned_doctor
        })

        return render_template('add_patient.html', success=True, patient_id=patient_id)
    return render_template('add_patient.html')

# View patient
@app.route('/view_patient', methods=['GET', 'POST'])
def view_patient():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        patient = next((p for p in patients if p['id'] == int(patient_id)), None)
        return render_template('view_patient.html', patient=patient)
    return render_template('view_patient.html')

# View doctors
@app.route('/view_doctors')
def view_doctors():
    return render_template('view_doctors.html', doctors=doctors)

# Generate bill
@app.route('/generate_bill', methods=['GET', 'POST'])
def generate_bill():
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        amount = request.form['amount']
        payment_method = request.form['payment_method']

        bill = {
            'bill_id': len(bills) + 1,
            'patient_id': patient_id,
            'amount': amount,
            'payment_method': payment_method,
            'status': 'Pending'
        }
        bills.append(bill)

        return render_template('generate_bill.html', success=True, bill=bill)
    return render_template('generate_bill.html')

# View bills
@app.route('/view_bills')
def view_bills():
    return render_template('view_bills.html', bills=bills)

# Update payment status
@app.route('/update_payment_status', methods=['GET', 'POST'])
def update_payment_status():
    if request.method == 'POST':
        bill_id = request.form['bill_id']
        new_status = request.form['status']

        bill = next((b for b in bills if b['bill_id'] == int(bill_id)), None)
        if bill:
            bill['status'] = new_status
            return render_template('update_payment_status.html', success=True, bill=bill)

    return render_template('update_payment_status.html')

# Logout route
@app.route('/logout')
def logout():
    return redirect('/')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import joblib
import pickle
app = Flask(__name__)

# Load your machine learning model
model = pickle.load(open(r"/app/app/randomForest_model.pkl", "rb"))
#model = joblib.load(r"/app/model.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    #print(request.form)
    loan_amount = float(request.form['loanAmount'])
    #print(loan_amount)
    term_36 = int(request.form.get('term36', 0) == 'on')  # Checkbox value (1 if checked, 0 if not)
    term_60 = int(request.form.get('term60', 0) == 'on')  # Checkbox value (1 if checked, 0 if not)
    inquiries = int(request.form['inquiries'])
    initial_list_status = 0
    employment_length = int(request.form['employmentLength'])
    annual_income = float(request.form['annualIncome'])
    outstanding_principle = float(request.form['outstandingPrinciple'])
    total_payment = float(request.form['totalPayment'])
    total_recovered_interest = float(request.form['totalRecoveredInterest'])
    total_late_fee_recovered = float(request.form['totalLateFeeRecovered'])
    recoveries = 0
    last_payment_amount = float(request.form['lastPaymentAmount'])
    delinquency_amount = 0
    debt_settlement = 0  # Checkbox value (1 if checked, 0 if not)

    # Status checkboxes (multiple values can be selected)
    status_complete = int(request.form.get('complete', 0) == 'on')
    status_active = int(request.form.get('active', 0) == 'on')
    status_broken = int(request.form.get('broken', 0) == 'on')
    status_cancelled = int(request.form.get('cancelled', 0) == 'on')
    status_denied = int(request.form.get('denied', 0) == 'on')
    status_draft = int(request.form.get('draft', 0) == 'on')

    # House ownership checkboxes
    house_rented = int(request.form.get('rented', 0) == 'on')
    house_mortgage = int(request.form.get('mortgage', 0) == 'on')
    house_own = int(request.form.get('own', 0) == 'on')

    # Verified checkboxes
    verified = int(request.form.get('verified', 0) == 'on')

    # Source Verified
    source_verified = request.form['sourceVerified']

    # Purpose checkboxes
    purpose_car = int(request.form.get('car', 0) == 'on')
    purpose_credit_card = int(request.form.get('creditCard', 0) == 'on')
    purpose_debt_consolidation = int(request.form.get('debtConsolidation', 0) == 'on')
    purpose_home_improvement = int(request.form.get('homeImprovement', 0) == 'on')
    purpose_house = int(request.form.get('house', 0) == 'on')
    purpose_major_purchase = int(request.form.get('majorPurchase', 0) == 'on')
    purpose_medical = int(request.form.get('medical', 0) == 'on')
    purpose_moving = int(request.form.get('moving', 0) == 'on')
    purpose_renewable_energy = int(request.form.get('renewableEnergy', 0) == 'on')
    purpose_small_business = int(request.form.get('smallBusiness', 0) == 'on')
    purpose_vacation = int(request.form.get('vacation', 0) == 'on')
    purpose_wedding = int(request.form.get('wedding', 0) == 'on')

    # Other processing or validation logic as needed
    id = 1
    term = check_term_status(term_36, term_60)
    A, B, C, D = check_status(status_active, status_broken, status_complete, status_denied)
    interest_rate, loan_status, initial_list_status, status, debt_settlement, not_verified = get_loan_details()
    if source_verified == '':
        verified = 0
    
    source_verified = 0
    # Example: Convert the collected data into a format that can be passed to the model
    input_data = [
        loan_amount, term, interest_rate, inquiries, initial_list_status,
        outstanding_principle, total_payment, total_recovered_interest, total_late_fee_recovered,
        recoveries, last_payment_amount, delinquency_amount, debt_settlement, A, B, C, D, house_rented, house_mortgage, house_own, not_verified, source_verified, verified,
        purpose_car, purpose_credit_card, purpose_debt_consolidation, purpose_home_improvement,
        purpose_house, purpose_major_purchase, purpose_medical, purpose_moving,
        purpose_renewable_energy, purpose_small_business, purpose_vacation, purpose_wedding
    ]
    #print(input_data)
    # Make predictions using the model
    prediction = model.predict([input_data])
    print("prediction", prediction)
    # Process the prediction or take further actions based on your application's requirements
    print(prediction)
    if prediction[0] == 1:
        predictions = 0
    else:
        predictions = 1
    return render_template('result.html', prediction=predictions)

def check_status(status_active, status_broken, status_complete, status_denied):
    if status_active == 1:
        A = 1
    else:
        A = 0
    if status_broken == 1:
        B = 1
    else:
        B = 0
    if status_complete == 1:
        C = 1
    else:
        C = 0
    if status_denied == 1:
        D = 1
    else:
        D = 0
    return A, B, C, D

def check_term_status(term_36, term_60):
    term = 0
    if term_36 == 1:
        term = 0
    elif term_60 == 1:
        term = 1
    return term

def get_loan_details():
    interest_rate = 15.050000
    loan_status = 3
    initial_list_status = 1
    status = 0
    debt_settlement = 1
    not_verified = 1
    return interest_rate, loan_status, initial_list_status, status, debt_settlement, not_verified
if __name__ == '__main__':
    app.run(debug=True)

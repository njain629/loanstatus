from flask import Flask, request, jsonify, render_template
import server.util as util

app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")

@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("app.html")


@app.route('/predict_loanapp_status', methods=['POST'])
def predict_loanapp_status():
    Married=int(request.form['rel'])
    ApplicantIncome=float(request.form['app_income'])
    CoapplicantIncome=float(request.form['co_app_income'])
    LoanAmount=float(request.form['loan_amount'])
    Loan_Amount_Term=float(request.form['loan_amount_term'])
    Credit_History=int(request.form['cred'])
    Dependents_0=int(request.form['dep'])
    Property_Area_Rural=int(request.form['prop'])

    response = jsonify({
        'loanStatus': util.get_loanAplication_status(Married,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Dependents_0,Property_Area_Rural)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    app.run()

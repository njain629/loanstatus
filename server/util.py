import pickle
import json
import numpy as np
import os

__model = None

def get_loanAplication_status(Married,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Dependents_0,Property_Area_Rural):

    x = np.zeros(len(__model.feature_names_))
    x[0] = Married
    x[1] = ApplicantIncome
    x[2] = CoapplicantIncome
    x[3] = LoanAmount
    x[4] = Loan_Amount_Term
    x[5] = Credit_History
    x[6] = Dependents_0
    x[7] = Property_Area_Rural

    return "Approved" if __model.predict([x])==1  else "Rejected"

def load_saved_artifacts():
    print("loading saved artifacts...start")

    path = os.path.dirname(__file__) 
    artifacts = os.path.join(path, "artifacts"),

    global __model
    if __model is None:
        with open(artifacts[0]+"/pickle_loanData_model.pickle", 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

load_saved_artifacts()

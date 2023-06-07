
from flask import Flask,jsonify,render_template,request

from project_app.utils import CreditCardLimit
import config

app = Flask(__name__,template_folder='templates')

@app.route("/")
def hello_flask():
    print("Welcome to credit card prediction site")
    return render_template("index.html")

@app.route("/predict_credit_limit",methods=['POST','GET'])
def get_pred():
    if request.method == 'GET':
        print("We are in Get method")

        Age = float(request.args.get("Age"))
        Gender = request.args.get("Gender")
        Income = float(request.args.get("Income"))
        Education = request.args.get("Education")
        Marital_Status = request.args.get("Marital_Status")
        Number_of_Children = float(request.args.get("Number_of_Children"))
        Home_Ownership = request.args.get("Home_Ownership")
        Credit_Score = request.args.get("Credit_Score")
        Loan_amount = float(request.args.get("Loan_amount"))
        EMI = float(request.args.get("EMI"))
        Inhand_Sallary = float(request.args.get("Inhand_Sallary"))

    else :
        print("error")

    credit_prediction = CreditCardLimit(Age,Gender,Income,Education,Marital_Status,Number_of_Children,Home_Ownership,Credit_Score,Loan_amount,EMI,Inhand_Sallary)
    limit = credit_prediction.get_credit_limit()

    if limit == 0:
        return render_template("index.html",prediction="Credit Card is Approved, Predicted Limit is 3 to 4.5 Lakhs")
    elif limit == 1:
        return render_template("index.html",prediction="Credit Card is Approved, Predicted Limit is 1.5 to 3 Lakhs")
    elif limit == 3:
        return render_template("index.html",prediction="Credit Card is Approved, Predicted Limit is 1 to 1.5 Lakhs")
    else:
        return render_template("index.html",prediction="Sorry, Your request for Credit Card is Declined")


if __name__ == "__main__":
     app.run(host=config.HOST,port=config.PORT,debug=False)

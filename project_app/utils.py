import numpy as np
import pandas as pd

import pickle
import json

import config

class CreditCardLimit():
    def __init__(self,Age,Gender,Income,Education,Marital_Status,Number_of_Children,Home_Ownership,Credit_Score,Loan_amount,EMI,Inhand_Sallary):
        self.Age= Age
        self.Gender=Gender
        self.Income=Income
        self.Education=Education
        self.Marital_Status=Marital_Status
        self.Number_of_Children=Number_of_Children
        self.Home_Ownership=Home_Ownership
        self.Credit_Score=Credit_Score
        self.Loan_amount=Loan_amount
        self.EMI=EMI
        self.Inhand_Sallary=Inhand_Sallary

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

        with open(config.SCALER_FILE_PATH,'rb') as f:
            self.scaler = pickle.load(f)

    def get_credit_limit(self) :

        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.Age
        test_array[1] = self.json_data["Gender"][self.Gender]          
        test_array[2] = self.Income            
        test_array[3] = self.json_data["Education"][self.Education] 
        test_array[4] = self.json_data["Marital Status"][self.Marital_Status]        
        test_array[5] = self.Number_of_Children           
        test_array[6] = self.json_data["Home Ownership"][self.Home_Ownership]        
        test_array[7] = self.json_data["Credit Score"][self.Credit_Score]      
        test_array[8] = self.Loan_amount        
        test_array[9] = self.EMI       
        test_array[10] = self.Inhand_Sallary

        print(test_array)
        # limit = round(self.model.predict([test_array])[0],2)

        test_df = pd.DataFrame([test_array],columns=self.json_data['columns'])
        test_df_2 = test_df[['Age','Income','Number of Children','Loan amount','EMI','Inhand Sallary']]
        scaled_df = self.scaler.transform(test_df_2)
        test_df[['Age','Income','Number of Children','Loan amount','EMI','Inhand Sallary']] = scaled_df
        limit = round(self.model.predict(test_df)[0],2)

        return limit
    

if __name__ == "__main__":
    Age=25.00
    Gender='Female'
    Income=50000.00
    Education="Bachelor's Degree"
    Marital_Status= 'Single'
    Number_of_Children=0.00
    Home_Ownership='Rented'
    Credit_Score='High'
    Loan_amount=6000000.00
    EMI=16666.67
    Inhand_Sallary=33333.00

    card_limit = CreditCardLimit(Age,Gender,Income,Education,Marital_Status,Number_of_Children,Home_Ownership,Credit_Score,Loan_amount,EMI,Inhand_Sallary)
    limit = card_limit.get_credit_limit()

    if limit == 0:
        print("Credit Card is Approved, Predicted Limit is 3 to 4.5 Lakhs")
    elif limit == 1:
        print("Credit Card is Approved, Predicted Limit is 1.5 to 3 Lakhs")
    elif limit == 3:
        print("Credit Card is Approved, Predicted Limit is 1 to 1.5 Lakhs")
    else:
        print("Sorry, Your request for Credit Card is Declined")
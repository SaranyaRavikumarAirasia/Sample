import streamlit as st
import pickle
# load the train model
with open('train_model.pkl', 'rb') as pkl:
  train_model = pickle.load(pkl)

def main():
    bg = """<div style='background-color:'#00325B'; padding:13px'>
              <h1 style='color:#654321'>LOAN ELIGIBILITY PREDICTION APP</h1>
       </div>"""
    st.markdown(bg, unsafe_allow_html=True)
    left, right = st.columns((2,2))
    Gender = left.selectbox('Gender', ('Male', 'Female'))
    Married = right.selectbox('Married', ('Yes', 'No'))
    Dependents = left.selectbox('Dependents', ('None', 'One', 'Two', 'Three'))
    Education = right.selectbox('Education', ('Graduate', 'Not Graduate'))
    Self_Employed = left.selectbox('Self-Employed', ('Yes', 'No'))
    ApplicantIncome = right.number_input('Applicant Income($)')
    CoapplicantIncome = left.number_input('Coapplicant Income($)')
    LoanAmount = right.number_input('Loan Amount(in Thousands)')
    Loan_Amount_Term = left.number_input('Loan Tenor (in months)')
    Credit_History = right.number_input('Credit History', 0.0, 1.0)
    Property_Area = left.selectbox('Property Area', ('Semiurban', 'Urban', 'Rural'))
    button = right.button('Predict')


    # if button is clicked
    if button:
        # make prediction
        result = predict(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
                        CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area)
        st.success(f'You are {result} for the loan')



def predict(gender, married, dependent, education, self_employed, applicant_income,
           coApplicantIncome, loanAmount, loan_amount_term, creditHistory, propertyArea):
    # processing user input
    gen = 0 if gender == 'Male' else 1
    mar = 0 if married == 'Yes' else 1
    dep = float(0 if dependent == 'None' else 1 if dependent == 'One' else 2 if dependent == 'Two' else 3)
    edu = 0 if education == 'Graduate' else 1
    sem = 0 if self_employed == 'Yes' else 1
    pro = 0 if propertyArea == 'Semiurban' else 1 if propertyArea == 'Urban' else 2
    Lam = loanAmount / 1000
    cap = coApplicantIncome / 1000
    # making predictions
    prediction = train_model.predict([[gen, mar, dep, edu, sem, applicant_income, cap,
                                      Lam, loan_amount_term, creditHistory, pro]])
    verdict = 'Not Eligible' if prediction == 0 else 'Eligible'
    return verdict
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://insuranceadviceonline.com/wp-content/uploads/2022/04/13.jpg");
             background-attachment: fixed;
             background-size: contain;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

def add_buttoncolor():
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #ed3419;
        color:#ffffff;
    }
    div.stButton > button:hover {
        background-color: #ffffff;
        color:#000000;
        }
    </style>""", unsafe_allow_html=True)

add_buttoncolor()





if __name__ == '__main__':
    main()

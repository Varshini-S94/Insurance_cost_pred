import streamlit as st
import pandas as pd

import datetime
import pickle

insurance_df = pd.read_csv("/Users/Varshini/PycharmProjects/PythonProject/insurance_pred.csv")
st.write(
    """
    # Medical insurance cost prediction

    """
)
st.header( "Information of the beneficiary", divider="rainbow")

encode_dict = {
    "Diabetes":{"Yes":1, "No": 2},
    "BP_problems": {"Yes":1, "No": 2},
    "Transplants": {"Yes":1, "No": 2},
    "Chronic_ds" : {"Yes":1, "No": 2},
    "Allergies" : {"Yes":1, "No": 2},
    "Cancer_hist" : {"Yes":1, "No": 2}
}

def model_pred(Age, BMI, Diabetes,Transplants, BP_problems, Chronic_ds, Surgery_nos):
    # loading the model
    with open("/Users/Varshini/PycharmProjects/Insurance_cost_pred/insurance.pkl", "rb") as file:
            reg_model = pickle.load(file)
            input_features = [[Age, BMI, Diabetes,Transplants, BP_problems, Chronic_ds, Surgery_nos]]
            return reg_model.predict(input_features)

## formatting and adding dropdowns and sliders
col1, col2 = st.columns(2)

Age = col1.slider("Select the age", 15, 70,step=2)
Diabetes = col1.selectbox("Select if the beneficiary has Diabetes or not",
                           ["Yes", "No"])
BP_problems = col1.selectbox("Select if the beneficiary has Blood pressure issues or not",
                           ["Yes", "No"])
Surgery_nos = col1.selectbox("Number of surgeries done", [0,1,2,3])
BMI = col2.slider("BMI(Body Mass Index) value", 15.00 , 50.00, step=1.00)
Transplants = col2.selectbox("Select if the beneficiary has any transplants done or not",
                                   ["Yes", "No"])
Chronic_ds = col2.selectbox("Select if the beneficiary has any chronic disease or not",
                       ["Yes", "No"])


if (st.button("Predict Premium")):
     Diabetes = encode_dict["Diabetes"][Diabetes]
     BP_problems = encode_dict["BP_problems"][BP_problems]
     Transplants = encode_dict["Transplants"][Transplants]
     Chronic_ds = encode_dict["Chronic_ds"][Chronic_ds]

     price = model_pred(Age, BMI, Diabetes,Transplants, BP_problems, Chronic_ds, Surgery_nos)
     if price is not None:
         st.subheader(f"Predicted Premium for the beneficiary is: {round(price[0],2)} rupees")
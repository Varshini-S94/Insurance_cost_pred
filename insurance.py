import streamlit as st
import pandas as pd

import datetime
import pickle

insurance_df = pd.read_csv("insurance_pred.csv")
st.write(
    """
    # Insurance cost prediction

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

def model_pred(Age, BMI, Surgery_nos, Transplants, BP_problems, Chronic_ds):
    # loading the model
    with open("insurance.pkl", "rb") as file:
            reg_model = pickle.load(file)
            input_features = [[Age, BMI, Surgery_nos, Transplants, BP_problems, Chronic_ds]]
            return reg_model.predict(input_features)

## formatting and adding dropdowns and sliders
col1, col2 = st.columns(2)

Age = col1.slider("Select the age", 15, 70,step=2)
Surgery_nos = col1.selectbox("Number of surgeries done", [0,1,2,3])
BP_problems = col1.selectbox("Select if the beneficiary has Blood pressure issues or not",
                           ["Yes", "No"])
BMI = col2.slider("BMI value", 15.00 , 50.00, step=1.00)
Transplants = col2.selectbox("Select if the beneficiary has any transplants done or not",
                                   ["Yes", "No"])
Chronic_ds = col2.selectbox("Select if the beneficiary has any chronic disease or not",
                       ["Yes", "No"])


if (st.button("Predict Premium")):
     BP_problems = encode_dict["BP_problems"][BP_problems]
     Transplants = encode_dict["Transplants"][Transplants]
     Chronic_ds = encode_dict["Chronic_ds"][Chronic_ds]

     price = model_pred(Age, BMI, Surgery_nos, Transplants, BP_problems, Chronic_ds)
     if price is not None:
         st.subheader(f"Predicted Premium for the beneficiary is: {round(price[0],2)} rupees")

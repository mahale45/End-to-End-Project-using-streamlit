import pandas as pd
import streamlit as st
import pickle
import warnings
warnings.filterwarnings('ignore')

with open('model.pkl','rb') as pkl:
    classifier=pickle.load(pkl)
def main():

    st.write('Diabetes Prediction')  
    st.header('Diabetes Prediction')  
    left,right=st.columns((2,2))
    Pregnancies=left.number_input('Enter Pregnancies as whole number',step=1,value=0)
    Glucose=right.number_input('Enter Glucose as Whole number',step=1,value=0)
    BloodPressure=left.number_input('Enter BloodPressure as whole number',step=1,value=0)
    SkinThickness=right.number_input('Enter SkinThickness as Whole number',step=1,value=0)
    Insulin=left.number_input('Enter Insulin as whole number',step=1,value=0)
    BMI=right.number_input('Enter BMI as Decimal number',step=1,value=0)
    DiabetesPedigreeFunction=left.number_input('Enter DiabetesPedigreeFuction as whole number',step=1,value=0)
    Age=right.number_input('Enter Age as Whole number',step=1,value=0)

    Predict_button=st.button('AM I Diabetic???')

    if Predict_button:
        res=classifier.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if res[0]==0:
            st.success ('you are not a diabetic')
        else:
            st.success ('you are a diabetic')   


if __name__=='__main__':
    main()
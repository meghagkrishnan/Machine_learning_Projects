# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import joblib
import pandas as pd

data = pd.read_csv(r'C:\Users\User\Desktop\ANACONDA\insurance.csv')

#def main():
st.write("""
             # My first App
             """)
    
    
p1 = st.slider("Enter Your Age",18,100)
s1=st.selectbox("Sex",("Male","Female"))
if s1=="Male":
    p2=1
else:
    p2=0

p3 =st.number_input("Enter Your BMI Value")
p4 = st.slider("Enter Number of Children",0,4) 
    
s2=st.selectbox("Smoker",("Yes","No"))
if s2=="Yes":
    p5=1
else:
    p5=0
      
p6 = st.slider("Enter Your Region [1-4]",1,4)
  
model = joblib.load(r'C:\Users\User\Desktop\ANACONDA\model_gbr')  
if st.button('Predict'):
    prediction = model.predict([[p1,p2,p3,p4,p5,p6]])
    st.balloons()
    st.success('Insurance Amount is {} '.format(round(prediction[0],2)))  
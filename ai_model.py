# -*- coding: utf-8 -*-
"""ai model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16vf3j_0AA56aQR1ep0af6DVmiqgLonBp
"""

#from google.colab import drive
#drive.mount('/content/drive')

#pip install streamlit

#import libraries
import streamlit as st
import pickle
import pandas as pd
import numpy
from scikitlearn.metrics import classification_report

#Christopher Katondo
#Noralle Matanda
#Fortune Gono

#Import the loaded model in read mode
pickle_in = open('disease_classification.pkl', 'rb')
classifier = pickle.load(pickle_in)

def pred(symptom1,symptom2,symptom3,symptom4):
    '''
    parameters:
		name:  symptom1
		in: query
		type: text
		required: True
        name: symptom2
        in: query
        type: text
        required: True
	responses:
		200:
			description: utput values
    
    '''
    prediction=classifier.predict([[symptom1,symptom2,symptom3,symptom4]])
    print(prediction)
    return prediction

def main():
    #Define title
    st.title('Disease Classification')
    #html_temp =
    symptom1 = st.text_input("symptom1","Type here", key='Type')
    symptom2=st.text_input("symptom2","Type here")
    symptom3=st.text_input("symptom3","Type here")
    symptom4=st.text_input("symptom4","Type here")
    result = " "
    if st.button("Predict"):
        result=pred(symptom1,symptom2,symptom3,symptom4)
    st.success("output is {}".format(result))

if __name__ == '__main__':
    sy = st.multiselect("Symptoms", [['itching'],['itching', 'skin_rash,nodal_skin_eruptions'],['shivering'], ['chills'],['continuous_sneezing', 'ulcers_on_tongue'],['chills','joint_pain'],['skin_rash,nodal_skin_eruptions'],['continuous_sneezing'],['ulcers_on_tongue'], ['ulcers_on_tongue','itching'], 'skin_rash,nodal_skin_eruptions',['shivering','chills'],['joint_pain'],['stomach_pain'],['acidity']])
    
    main()

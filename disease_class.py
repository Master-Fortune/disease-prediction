#Disease Classification APP
"""Developers:
            Noralle Matanda
            Christopher Katondo
            Fortune Gono
            """

#import external libraries
import streamlit as st
import numpy as np
import pandas as pd

st.title('Disease Classification App')
st.text('Type your age below')
n = st.number_input('Age', step=2)
area = st.text_input('Enter the name of the city you are in to locate nearest hospital: ')

def residence():
    if area == 'HARARE' or 'harare' or 'Harare' or 'CHITUNGWIZA' or 'Chitungwiza' or 'chitungwiza':
        st.text(f'Nearest hospitals are Parirenyatwa and Harare Hospital to {area}')
    elif area == 'BULAWAYO' or 'bulawayo' or 'Bulawayo' or 'Gwanda' or 'GWANDA' or 'gwanda':
        st.text(f'Nearest hospitals are Impilo Hospital to {area}')
    elif area == 'MUTARE' or 'Mutare' or 'mutare' or 'Nyanga' or 'NYANGA' or 'nyanga' or 'Chipinge' or 'Chipinge':
        st.text(f'Nearest hospitalS are Mutare Hosptital to {area}')
    else:
        st.text('Could not locate your city')

#x = [ ]
def pred():
    name = ''
    if ch == ([['itching'],['skin rash']]):
        name = 'Fungal infection'
        st.write(name)
    elif ch ==([['itching'],['skin rash'],['nodal skin erupions']]):
        name = 'Fungal infection'
        st.write(name)
    elif ch == ([['itching'],['continuous sneezing'],['shiverng']]):
            name = 'Allergy'
            st.write(name)
    elif ch == ([['itching'],['chills'],['watering from eyes']]):
            name = 'Allergy'
            st.write(name)
    elif ch == ([['itching'],['stomach pain'],['acidity']]):
            name = 'GERD'
            st.write(name)
    elif ch == ([['itching'],['ulcers on tongue'],['yellowish of skin']]):
            name = 'GERD'
            st.write(name)
    elif ch == (['nausea'],['vomiting']):
            aname = 'Chronic Cholestasis'
            st.write(name)
    elif ch == ([['itching'],['stomach pain']]):
            name = 'Drug Reaction'
            st.write(name)        
    return name

    
if __name__ == '__main__':
    #Selectbox
    ch = st.multiselect('Symptoms', [['itching'] , ['skin rash'] , ['nodal skin eruptions'] , ['continuous sneezing'] , ['shivering'] , ['chills'] , ['watering from eyes'], ['stomach pain'], ['acidity'], ['ulcers on tongue'], ['yellowish of skin'], ['nausea'], ['vomiting'], ['cough'], ['loss of apetite']])
    result =''
    result = pred()
    pred()
    if st.button("Predict"):
        result=pred()
    st.success("output is {}".format(result))
    residence()

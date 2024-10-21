#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 23:04:43 2024

@author: ayagad
"""
import pandas as pd
import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open('/Users/ayagad/Hotel_canceling/trained_model.sav','rb'))

st.title('Hotel Booking Cancelation Prediction')
st.info('A Web app About Hotel Booking Cancelation')
# create function for prediction
st.title('Prediction Page')
st.write("### Enter Some Information to Predict the Booking Cancelation!")
number_of_adults=st.selectbox('number of adults',(1,2,3,4))
number_of_weekend_nights=st.text_input('number of weekend nights',1)
number_of_weeknights=st.text_input('number of week nights',1)
room=('Room_Type 1', 'Room_Type 2', 'Room_Type 3', 'Room_Type 4','Room_Type 5','Room_Type 6','Room_Type 7')
roo_ty=st.selectbox('room type',room)
room_type=0.000000
if roo_ty=='Room_Type 1':
    room_type=0.000000
elif roo_ty=='Room_Type 2':
    room_type=0.833333
elif roo_ty=='Room_Type 3':
    room_type=0.333333
elif roo_ty=='Room_Type 4':
    room_type=0.500000
elif roo_ty=='Room_Type 5':
    room_type=0.666667    
elif roo_ty=='Room_Type 6':
    room_type=0.166667 
elif roo_ty=='Room_Type 7':
    room_type=1.000000  



lead_time=st.text_input('lead time',1)
Seg_type=('Online','Offline','Corporate','Complementary','Aviation')
segment_type=st.selectbox('market segment type',Seg_type)
market_segment_type=1.00

if segment_type=='Online':
    market_segment_type=1.00
elif segment_type=='Offline':
    market_segment_type=0.75
elif segment_type=='Corporate':
    market_segment_type=0.50
elif segment_type=='Complementary':
    market_segment_type=0.00    
elif segment_type=='Aviation':
    market_segment_type=0.25                   
repeated=st.selectbox('repeated',(0,1))
average_price=st.text_input('average price',1.0)
special_requests=st.selectbox('special requests',(0,1,2,3,4,5))
        
df=pd.DataFrame({'number of adults':[number_of_adults],'number of weekend nights':[number_of_weekend_nights],'number of week nights':[number_of_weeknights],'room type':[room_type],
                 'lead time':[lead_time],'market segment type':[market_segment_type],'repeated':[repeated],'average price': [average_price],'special requests':special_requests})
submit=st.button('Submit')
if submit:
    result=loaded_model.predict(df)
    if result== 0.0:
        st.write('Booking Was Canceled')
    else:
        st.write('Booking Was Not Canceled')


        
        





import streamlit as st
import datetime

st.header('First Streamlit Demo', divider='rainbow')

d = st.date_input("Select Date" , value = None)
t = st.time_input("Set an alarm for", value=None)
title = st.text_input("Note", value = None, placeholder = "Type your note...")


st.write(d,"Alarm is set for", t," ( Note: ",title ,")")








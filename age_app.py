from datetime import date
import streamlit as st


def get_age():
    st.header('Age Calculator')
    year = st.number_input('Year of Birth', value=1994)
    month = st.number_input('Month of Birth', value=3)
    day = st.number_input('Date of Birth', value=30)
    dob = date(year, month, day)
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) <
          (dob.month, dob.day))
    button = st.button('Check')
    if button:
        st.text(f'You are {age} years old')

import streamlit as st
from math import pow


def loan():
    st.header('Loan Calculator')
    principal = st.number_input('Enter loan amount', value=100000)
    interest = st.number_input('Enter the interest rate (%)', value=7.5)
    years = st.number_input('Enter the loan duration in years', value=30)
    button = st.button('Calculate')
    monthly_payment = calc_loan(principal, interest, years)
    total_amount = monthly_payment * years * 12

    res = f'Amount = ${principal}  \
          \nYears = {years} years \
           \nInterest = {interest}% \
          \nMonthly payment =  ${round(monthly_payment, 2)} \
           \n------------------------------------- \
           \nTotal amount to be paid =  ${round(total_amount, 2)}'

    if button:
        st.text(res)


def calc_loan(principal, int, yr):
    """Calculate and return monthly payment amount"""
    int_rate = int / (100 * 12)
    months = yr * 12
    # monthly payment
    payment = principal * (int_rate / (1 - pow((1+int_rate), (-months))))
    return payment

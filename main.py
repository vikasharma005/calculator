import streamlit as st
from age_app import get_age
from simult import simultaneous
from data import stats
from loan_app import loan
from maths import basic_maths


def main():
    option = st.sidebar.selectbox('What do you want to calculate?', ['Basic Maths', 'loan', 'Age', 'Statistics','Simultaneous Equation'])
    if option == 'Basic Maths':
        basic_maths()
    elif option == 'loan':
        loan()
    elif option == 'Age':
        get_age()
    elif option == 'Statistics':
        stats()
    else:
         simultaneous()





if __name__ == '__main__':
    main()

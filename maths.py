import streamlit as st





def basic_maths():
    st.header('Basic Maths Operation')
    num1 = st.number_input('Enter a number', value=20)
    num2 = st.number_input('Enter another number', value=5)
    operation = st.radio('Select an operation', ['Add', 'Subtract', 'Multiply', 'Divide'])
    button = st.button('Calculate')
    if button:
        calc_maths(operation, num1, num2)

def calc_maths(op, num1, num2):
    result = 0
    if op == 'Add':
        result = num1 + num2
    elif op == 'Subtract':
        result = num1 - num2
    elif op == 'Multiply':
        result = num1 * num2
    elif op == 'Divide':
        result = num1 / num2
    else:
        st.warning('Division by 0 error, please enter a non_zero number.')
        res = 'Undefined'

    st.success(f'Result = {result}')


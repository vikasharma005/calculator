import streamlit as st



def simultaneous():
    st.header('Simultaneous Equation')
    num = st.radio('Number of unknowns', [2, 3])
    if num == 2:
        simul_2_eqn()
    else:
        simul_3_eqn()

def simul_2_eqn():
    left, right = st.columns((2, 2))
    num1 = left.number_input('Enter the first number', value=1)
    num2 = right.number_input('Enter the second number', value=6)
    num3 = left.number_input('Enter the first equal number', value=3)
    num4 = right.number_input('Enter the third number', value=1)
    num5 = left.number_input('Enter the fourth number', value=1)
    num6 = right.number_input('Enter the second equal number', value=-2)
    button = st.button('Solve')
    if button:
        solver(num1, num2, num3, num4, num5, num6)

def solver(num1, num2, num3, num4, num5, num6):
    for x in range(-100, 100):
        for y in range(-50, 50):
            if (num1 * x) + (num2 * y) == num3 and (num4 * x) + (num5 * y) == num6:
                st.text(f'x = {x} \
                        \ny = {y}')


def simul_3_eqn():
    left, right = st.columns((2, 2))
    num1 = left.number_input('first number Eqn(1)', value=1)
    num2 = right.number_input('Second number Eqn(1)', value=-3)
    num3 = left.number_input('Third number Eqn(1)', value=-2)
    num4 = right.number_input('First equal number Eqn(1)', value=6)
    num5 = left.number_input('First number Eqn(2)', value=2)
    num6 = right.number_input('Second number Eqn(2)', value=-4)
    num7 = left.number_input('Third number Eqn(2)', value=-3)
    num8 = right.number_input('Second Equal number Eqn(2)', value=8)
    num9 = left.number_input('First number Eqn(3)', value=-3)
    num10 = right.number_input('Second number Eqn(3)', value=6)
    num11 = left.number_input('Third number Eqn(3)', value=8)
    num12 = right.number_input('Third equal number Eqn(3)', value=-5)
    button = st.button('Solve')
    if button:
        SOLVER(num1, num2, num3, num4, num5, num6, num7, num8,
               num9, num10, num11, num12)

def SOLVER(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12):
    for x in range(-100, 100):
        for y in range(-100, 100):
            for z in range(-100, 100):
                if (n1*x + n2*y + n3*z) == n4 and (n5*x + n6*y + n7*z) == n8 and (n9*x + n10*y + n11*z) == n12:
                    st.text(f'x = {x} \
                            \ny = {y} \
                            \nz = {z}')



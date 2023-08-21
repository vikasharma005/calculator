import streamlit as st
from statistics import mean, median, mode
import altair as alt
import re
from itertools import repeat
import pandas as pd



def stats():
    st.header('Statistics')
    numbs_only = lambda x: [int(i) for i in re.split('[^0-9]', x) if i != '']
    num = st.text_input('Please enter numbers')
    freq = st.text_input('Please enter frequency')
    x = numbs_only(num)
    y = numbs_only(freq)
    if len(x) != len(y):
        st.error('The numbers should be of equal length')
        return None
    list_merged = flatten(x, y)
    op = st.radio('Select an operation', ['mean', 'median', 'mode', 'bar chart', 'line chart', 'area chart'])
    button = st.button('Calculate')
    df = pd.DataFrame({'Number': x, 'Frequency': y})
    if button:
        if op == 'mean':
            result = mean(list_merged)
            st.text(f'Mean = {round(result, 2)}')
        elif op == 'median':
            st.text(f'Median = {median(list_merged)}')
        elif op == 'mode':
            st.text(f'Mode = {mode(list_merged)}')
        elif op == 'bar chart':
            bar = alt.Chart(df).mark_bar().encode(
                 y = 'Frequency',
                 x = 'Number'
            )
            st.altair_chart(bar, use_container_width=True)
        elif op == 'line chart':
            st.line_chart(df)
        else:
            st.area_chart(df)

def flatten(x, freq):
    res = []
    for i in zip(x, freq):
        res.append(list(repeat(i[0], i[1])))
    res = [i for k in res for i in k]
    return res

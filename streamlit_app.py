import streamlit as st
import pandas as pd
st.title('🪴Iris')

st.sidebar.subheader('Input')
url_input = st.sidebar.text_input('URL', '')

#st.subheader('Output')
#st.warning(f'The GitHub URL of your data is: {url_input}', icon="ℹ️")

if url_input:
    st.subheader('Output')
    st.warning(f'The GitHub URL of your data is: {url_input}', icon="ℹ️")
    df = pd.read_csv(url_input)
    st.write(df)

    column_names = df.columns[-1]

    st.write(column_names)
    df2 = df.groupby(column_names).mean()
    st.write(df2)
    st.bar_chart(df2)
else:
    st.subheader('Enter your input')
    st.error('👈 Awaiting your input!')

#https://raw.githubusercontent.com/gooogolf/example-st-xmas/master/iris.csv

import streamlit as st
st.write('# Streamlit calculator')
number1=st.number_input('number1')
number2=st.number_input('number2')
number3=number1+number2
st.write('#Answer is',number3)

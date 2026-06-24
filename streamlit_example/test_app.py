# https://docs.streamlit.io/develop/api-reference

import streamlit as st
import pandas as pd
import datetime
a = 3
b = 2
c = a+b

st.write("# Project")
st.write("This is my beautiful project"*20)


st.write("## Chapter 1")
st.write("This is my beautiful chapter one"*20)

age = int(st.text_input("Enter the age of your dog: "))

st.write(f"your dog in human age: {age*7}")

df = pd.read_csv("data/cleaned_timeseries.csv")

d = df.describe()

st.write(d)
st.write(c)
st.write(df)


st.line_chart(df["unit_sales"])


d = st.date_input("When's your birthday", min_value=datetime.date(2013, 1, 1))
st.write("Your birthday is:", d)

df["date"] = pd.to_datetime(df["date"])


st.write(df[df["date"]>pd.to_datetime(d)])

col1, col2 = st.columns(2)

with col1:
    st.write("This is my beautiful chapter one"*20)

with col2:
    st.write(df)


st.write("## Chapter 2")
st.write("This is my beautiful chapter two"*20)

import streamlit as st
import pandas as pd
from datetime import datetime
import csv

st.title("Data Input Example")
now = datetime.now()
number = st.number_input("Enter a number:", min_value=0, max_value=100, value=50)
if number == 49:
    st.success("You entered 49!")
else:
    st.error("You did not enter 49.")
st.write("**You entered:**", number)
c1, c2 = st.columns(2)
with c1:
    name = st.text_input("Enter your name:")
with c2:
    text = st.text_input(label="Enter some text")
current_time = now.strftime("%H:%M:%S")
if st.button("Write to file"):
    with open("data.csv", "a") as file:
        row_to_write = [name, current_time, text]
        writer = csv.writer(file)
        writer.writerow(row_to_write)
    st.success("Data written to file successfully!")
df = pd.read_csv("data.csv")
with st.expander("View Data"):
    st.write(df)

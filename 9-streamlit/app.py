import streamlit as st
import pandas as pd

st.title("Hello Anish")
st.write("This the the sample text")

df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]},
                   index=['falcon', 'dog', 'spider', 'fish'])

st.write(f"here is the DataFrame")
st.write(df)

name=st.text_input("enter the name")
if name:
    st.write(f"hello,{name}")

age=st.slider("enter your age",0,150,18)
st.write(age,f"age:{age}")

upload_file=st.file_uploader("choose a csv file",type="csv")
if upload_file is not None:
    df = pd.read_csv(upload_file,on_bad_lines='skip')
    st.write(df)




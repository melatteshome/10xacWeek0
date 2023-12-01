import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Dash Board')
st.text('slack channel analysis')

upload_file = st.file_uploader('upload your file')

if upload_file:
    df = pd.read_json(upload_file)
    st.header('Data Header')
    st.write(df.head())

    st.header('Data Statstics')
    st.write(df.describe())

    df = df[:3]
    fig, ax= plt.subplots(1,1)

    #tested using the user.json data from the slack channel data you guys gave us
    ax.bar(df['name'] , df['is_email_confirmed'])
    ax.set_xlabel('Name')
    ax.set_ylabel('emoji')

    st.pyplot(fig)




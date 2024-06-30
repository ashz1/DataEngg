import streamlit as st
import altair as alt


st.set_page_config(page_title="Data Engineering Project", page_icon="❄️", layout="wide")
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
# I used Altair for the dark theme
alt.themes.enable("dark")
    
# I loaded my custom CSS style
with open('homestyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  
# Project Overview
st.title("Data Engineering Project by Aashay")
st.subheader("Project Summary")

with st.container():
    st.markdown("""
    Welcome to my Data Engineering project! This project demonstrates the steps taken to import data from Amazon S3, process it on an EC2 instance, and save the data in a GitHub repository using Streamlit.

    **Project Highlights**:
    - Uploading data to Amazon S3.
    - Setting up and configuring an EC2 instance.
    - Connecting to the EC2 instance via VSCode for seamless development.
    - Creating a Python virtual environment and installing necessary packages.
    - Configuring AWS credentials for secure access.
    - Running and hosting a Streamlit app to visualize the data.

    For a detailed walkthrough of the project steps, please head to the **Steps** section in the sidebar.
    """)

with st.container():
    st.markdown("""
    This project showcases the integration of various AWS services and Python libraries to achieve data engineering tasks. The code for importing and processing the data can be viewed on the separate code page accessible from the sidebar.
    """)

with st.container():
    st.write("Project by Aashay © 2024")

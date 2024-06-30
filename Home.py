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
# Enable Altair dark theme for charts
alt.themes.enable("dark")
    
# Custom CSS
with open('homestyle.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  

st.subheader("Project Summary")

# Introduction
with st.container():
    st.markdown("""
    Welcome to my Data Engineering project! This project demonstrates the steps taken to import data from Amazon S3, process it on an EC2 instance, and visualize it using Streamlit. Below is an overview of the steps involved in this project.
    """)

# Step 1: Upload CSV files to S3
with st.expander("Step 1: Upload CSV files to S3"):
    st.markdown("""
    The first step was to upload two CSV files to an Amazon S3 bucket. 
    
        Amazon S3 (Simple Storage Service) is a scalable object storage service that offers high availability, security, and performance. It is designed to store and retrieve any amount of data from anywhere on the web.

    **Key Features of Amazon S3**:
                
    - **Scalability**: S3 automatically scales to handle large volumes of data and high request rates.
    - **Durability**: S3 is designed for 99.999999999% (11 9's) of durability.
    - **Security**: S3 provides comprehensive security and compliance capabilities that meet even the most stringent regulatory requirements.
    - **Accessibility**: Data stored in S3 can be accessed from anywhere via the internet.
    - **Cost-Effectiveness**: S3 offers a range of storage classes to help you optimize costs.
    """)

# Step 2: Create EC2 Instance
with st.expander("Step 2: Create EC2 Instance"):
    st.markdown("""
    Next, I created an EC2 instance on an Ubuntu machine. This instance serves as the environment where the data processing will take place.
    """)

# Step 3: Clone GitHub Repository
with st.expander("Step 3: Clone GitHub Repository"):
    st.markdown("""
    After setting up the EC2 instance, I cloned the GitHub repository containing the Streamlit app. This repository includes the necessary scripts and configurations for the project.
    """)

# Step 4: Create Python Virtual Environment
with st.expander("Step 4: Create Python Virtual Environment"):
    st.markdown("""
    Within the EC2 instance, I created a Python virtual environment. This ensures that all the dependencies are isolated and managed properly. The commands used were:
    ```
    python3 -m venv myenv
    source myenv/bin/activate
    pip install -r requirements.txt
    ```
    """)

# Step 5: Configure AWS Credentials
with st.expander("Step 5: Configure AWS Credentials"):
    st.markdown("""
    AWS credentials were configured on the EC2 instance to allow access to the S3 bucket. This was done using the AWS CLI:
    ```
    aws configure
    ```
    """)

# Step 6: Run Streamlit App
with st.expander("Step 6: Run Streamlit App"):
    st.markdown("""
    Finally, I ran the Streamlit app, which includes code to import data from the S3 bucket and display it. The data visualization can be viewed on the next page in the sidebar.
    ``` 
    streamlit run /path/to/your/streamlit_app.py
    ```
    """)

# Conclusion
with st.container():
    st.markdown("""
    This project showcases the integration of various AWS services and Python libraries to achieve data engineering tasks. The code for importing and processing the data can be viewed on the separate code page accessible from the sidebar.
    """)

# Footer
with st.container():
    st.write("Project by Aashay © 2024")
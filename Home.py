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
  

st.subheader("**Project Summary**")

# Introduction
with st.container():
    st.markdown("""
    Welcome to my Data Engineering project! This project demonstrates the steps taken to import data from Amazon S3, process it on an EC2 instance, and visualize it using Streamlit. Below is an overview of the steps involved in this project.
    """)

# Step 1: Upload CSV files to S3
with st.expander("**Step 1: Upload CSV files to S3**"):
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
with st.expander("**Step 2: Create EC2 Instance**"):
    st.markdown("""
    Next, I created an EC2 instance on an Ubuntu machine. Amazon Elastic Compute Cloud (EC2) is a web service that provides secure, resizable compute capacity in the cloud. It allows users to run applications on a virtual server in the cloud, providing flexibility and scalability for various workloads.

    EC2 is widely used for applications such as web hosting, data analysis, machine learning, large-scale data processing, and more. 
    It provides virtual machines (VMs) that are resizable and customizable according to the specific needs of an application. Users can choose the operating system, storage, and instance type (compute, memory, storage optimized) that best fits their requirements. By providing on-demand virtual servers, EC2 enables businesses to quickly scale their infrastructure according to their needs without upfront hardware investments.

    **Elastic IP Addresses**:
    In AWS, an Elastic IP address is a static IPv4 address designed for dynamic cloud computing. It is associated with your AWS account and can be allocated to any instance in your account. Unlike a standard IP address, an Elastic IP address allows you to mask the failure of an instance or software by rapidly remapping the address to another instance in your account. This ensures continuity and availability of applications even in case of instance failures.    
    
    **Expose Streamlit Port**:
    I also exposed port 8501, which Streamlit uses, on the EC2 instance. This ensures that the Streamlit app is accessible from the web.""")

with st.expander("**Step 3: Creating virtual environment**"):
    st.markdown("""
Within the EC2 instance, I created a Python virtual environment. This ensures that all the dependencies are isolated and managed properly. The commands used were:
    ```
    sudo apt install python3-pip
    python3 -m venv myenv
    source myenv/bin/activate
    ```            
    """)

with st.expander("**Step 4: Connecting Visual Code Studio to EC2**"):
    st.markdown("""
    After setting up the virtal envoirnment, I cloned the GitHub repository containing the Streamlit app within the Ubuntu environment. This repository includes the necessary scripts and configurations for the project.

    **Connecting VSCode to EC2 via SSH**:
    First, I connected my local VSCode to the EC2 instance using SSH. This allows for seamless development and management of the files on the remote server directly from my local VSCode editor.

    1. **Generate an SSH Key Pair**:
       On your local machine, generate an SSH key pair if you don't already have one:
       ```
       ssh-keygen -t rsa -b 2048
       ```

    2. **Copy the SSH Key to EC2 Instance**:
       Use the following command to copy your SSH key to the EC2 instance:
       ```
       ssh-copy-id -i ~/.ssh/your_key.pem ubuntu@your_ec2_public_ip
       ```

    3. **Configure VSCode**:
       In VSCode, install the Remote - SSH extension. Then, configure the SSH connection by adding the EC2 instance to the SSH configuration file (`~/.ssh/config`):
       ```
       Host my-ec2-instance
           HostName your_ec2_public_ip
           User ubuntu
           IdentityFile ~/.ssh/your_key.pem
       ```

    4. **Connect to EC2 via VSCode**:
       Use the Remote Explorer in VSCode to connect to the EC2 instance by selecting the configured host. """)




with st.expander("**Step 5: Installing Required Packages and Libraries**"):
    st.markdown("""
    **Setting Up the Environment**:
    Before running the Streamlit app, I performed several setup steps on the EC2 instance:

    1. **Update and Install Required Packages**:
       ```
       sudo apt update
       sudo apt-get update
       sudo apt upgrade -y
       sudo apt install git curl unzip tar make sudo vim wget -y
       ```

    2. **Clone the GitHub Repository**:
       ```
       git clone "Your-repository"
       ```

    3. **Install Dependencies**:
       ```
       pip install -r requirements.txt
       ```
    
    """)

# Step 5: Configure AWS Credentials
with st.expander("**Step 6: Configure AWS Credentials**"):
    st.markdown("""
    AWS credentials were configured on the EC2 instance to allow access to the S3 bucket. Proper configuration of AWS credentials is crucial for secure and authenticated access to AWS services such as S3.

    **Steps to Configure AWS Credentials**:
    
    1. **Install AWS CLI**:
       First, ensure that the AWS Command Line Interface (CLI) is installed on your EC2 instance. If not installed, use the following command:
       ```
       sudo apt-get install awscli -y
       ```

    2. **Configure AWS CLI**:
       Run the `aws configure` command to set up your AWS credentials. You will need your AWS Access Key ID, Secret Access Key, region, and output format. The command will prompt you to enter these details:
       ```
       aws configure
       ```

       When you run this command, you will be prompted to enter the following information:
       - **AWS Access Key ID**: Your AWS account’s access key ID.
       - **AWS Secret Access Key**: Your AWS account’s secret access key.
       - **Default region name**: The region you want to use (e.g., `us-east-1`).
       - **Default output format**: The format in which you want the CLI to display the output (e.g., `json`).

    3. **Verify Configuration**:
       After configuring, you can verify that the credentials have been set up correctly by listing your S3 buckets:
       ```
       aws s3 ls
       ```
    """)

# Step 6: Run Streamlit App
with st.expander("**Step 6: Run Streamlit App**"):
    st.markdown("""
    Finally, I ran the Streamlit app, which includes code to import data from the S3 bucket and display it. The code can be viewed [here](https://dataengg.streamlit.app/Data_Import_from_AWS_S3_through_EC2).
    ``` 
    streamlit run Home.py
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
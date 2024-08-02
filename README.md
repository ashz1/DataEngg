<h1>Data Engineering Project Summary</h1>

<p>Welcome to my Data Engineering project! This project demonstrates the steps taken to import data from Amazon S3, process it on an EC2 instance, and save the data in a GitHub repository using Streamlit.</p>

<a href="https://sqlproject.streamlit.app/"><b>Live Demo of Data Engineering Project</b></a>

<h2>Project Highlights</h2>

<b>Uploading Data to Amazon S3</b>
<p>Amazon S3 (Simple Storage Service) is a scalable object storage service designed for high availability, durability, security, and cost-effectiveness. Key features include scalability, durability (11 9’s of durability), security, accessibility, and cost-effectiveness. Two CSV files were uploaded to an S3 bucket for this project.</p>

<b>Creating an EC2 Instance</b>
<p>Amazon Elastic Compute Cloud (EC2) provides secure, resizable compute capacity in the cloud. EC2 is used for various applications, including web hosting, data analysis, and machine learning. An Ubuntu machine was used to create the EC2 instance. An Elastic IP address was associated with the instance for consistent accessibility. Port 8501 was exposed for the Streamlit app.</p>

<b>Setting Up the Environment</b>
<p>A Python virtual environment was created within the EC2 instance to manage dependencies. Necessary packages were installed to ensure smooth operation.</p>
<p>Commands used include:</p>
<pre>
sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt install python3-pip
python3 -m venv myenv
source myenv/bin/activate
</pre>

<b>Connecting Visual Studio Code to EC2</b>
<p>VSCode was connected to the EC2 instance using SSH for seamless development. Steps included generating an SSH key pair, copying the SSH key to the EC2 instance, and configuring VSCode to connect via SSH.</p>

<b>Installing Required Packages and Libraries</b>
<p>The environment was set up by updating and installing necessary packages:</p>
<pre>
sudo apt install git curl unzip tar make sudo vim wget -y
git clone "Your-repository"
pip install -r requirements.txt
</pre>

<b>Configuring AWS Credentials</b>
<p>AWS CLI was installed and configured on the EC2 instance to allow access to the S3 bucket. AWS credentials were set up securely for authenticated access. Verification of the setup was done by listing S3 buckets.</p>

<b>Running the Streamlit App</b>
<p>The Streamlit app was run to import data from the S3 bucket and display it.</p>
<p>Command used:</p>
<pre>streamlit run Home.py</pre>


<h2>Conclusion</h2>
<p>This project showcases the integration of various AWS services and Python libraries to achieve data engineering tasks. It serves as a practical example of how to manage and process data using modern cloud technologies.</p>

<p>If you have any questions or need further assistance, feel free to contact me.</p>

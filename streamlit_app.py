import streamlit as st

st.header("Code to import data from S3 server through an EC2 instance")
st.code("""import boto3
import pandas as pd
from io import StringIO""")
st.code("""# defining read_csv_from_s3
        
    def read_csv_from_s3(bucket_name, file_key):
        s3 = boto3.client('s3')
        csv_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        body = csv_obj['Body']
        csv_string = body.read().decode('utf-8')
        return csv_string""")

st.code("""# I chose to define 2 main() for each csv file
        
    def main():
         st.title('S3 CSV Import Example')
         bucket_name = 'ecomsql'
         file_key = '1.csv'  # or '2.csv' depending on which file you want to read
         csv_string = read_csv_from_s3(bucket_name, file_key)
    
         # Save CSV to a local file
         local_csv_path = '1.csv'
         with open(local_csv_path, 'w') as f:
         f.write(csv_string)
    
         # Read the local CSV file into a DataFrame
         df = pd.read_csv(local_csv_path)
    
         # Display the dataframe
         st.write(df)
        
    if __name__ == "__main__":
         main()

    def main1():
         st.title('S3 CSV Import Example')
          Replace with your bucket name and file key
          bucket_name = 'ecomsql'
          file_key = '2.csv'  # or '2.csv' depending on which file you want to read
          csv_string = read_csv_from_s3(bucket_name, file_key)
          local_csv_path = '2.csv'
          with open(local_csv_path, 'w') as f:
          f.write(csv_string)
          df = pd.read_csv(local_csv_path)
          st.write(df)
         
    if __name__ == "__main__":
         main1()
""")

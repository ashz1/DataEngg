import streamlit as st
import boto3
import pandas as pd
from io import StringIO

def read_csv_from_s3(bucket_name, file_key):
    s3 = boto3.client('s3')
    csv_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    body = csv_obj['Body']
    csv_string = body.read().decode('utf-8')
    return pd.read_csv(StringIO(csv_string))

def main():
    st.title('S3 CSV Import Example')
    
    # Replace with your bucket name and file key
    bucket_name = 'ecomsql'
    file_key = '1.csv'  # or '2.csv' depending on which file you want to read
    
    # Read CSV from S3
    df = read_csv_from_s3(bucket_name, file_key)
    
    # Display the dataframe
    st.write(df)

if __name__ == "__main__":
    main()

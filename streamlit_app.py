import streamlit as st
import altair as alt


st.set_page_config(page_title="Data Engineering Project by Aashay", page_icon="❄️", layout="wide")
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
  
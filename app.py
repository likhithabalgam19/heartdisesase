import streamlit as st
from frontend.home import home_page

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

home_page()
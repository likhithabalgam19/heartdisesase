import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        .main{
            background-color:#F8F9FA;
        }

        h1{
            color:#C62828;
            text-align:center;
        }

        .stButton>button{
            width:100%;
            background:#C62828;
            color:white;
            font-size:18px;
            border-radius:10px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
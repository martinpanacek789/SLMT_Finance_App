import streamlit as st

import pandas as pd


@st.cache_data
def load_revenue_data_db():
    return pd.read_csv("data/revenue_items.csv")


st.title("Hello World")

st.write("Some text here...")

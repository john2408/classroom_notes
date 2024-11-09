import streamlit as st
import pandas as pd
import altair as alt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


st.title("Hello, Streamlit")

# -----------------
# Data
# -----------------

ROOT = "https://raw.githubusercontent.com/kirenz/datasets/master/"
DATA = "loan50.csv"
df = pd.read_csv(ROOT + DATA)

# -----------------
# Steamlit
# -----------------

st.dataframe(df)

# -------------------
# Altair
# --------------------

plot = alt.Chart(df).mark_bar().encode(
    x ='count(homeownership)', 
    y = 'homeownership'
)

st.altair_chart(plot)
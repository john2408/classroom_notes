import streamlit as st
import altair as alt
from data_loan50 import df, df_describe
from altir_charts import plot_bar, plot_scatter, plot_hist, plot_box, plot_it

# ----------- ------
# Steamlit
# -----------------
st.title("Hello, Streamlit")
st.dataframe(df)

st.altair_chart(plot_bar)
st.altair_chart(plot_scatter)
st.altair_chart(plot_hist)

st.dataframe(df_describe)

st.altair_chart(plot_box)
st.altair_chart(plot_it)

# Box plot
# max limit = Q3 + 1.5 IQR for outliers
# min limit = Q1 - 1.5 IQR
# IQR = Q3 - Q1
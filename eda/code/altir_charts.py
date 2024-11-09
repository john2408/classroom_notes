import streamlit as st
from data_loan50 import df
import altair as alt
# -------------------
# Altair
# --------------------

plot_bar = alt.Chart(df).mark_bar().encode(
    x ='count(homeownership)', 
    y = 'homeownership'
).properties(
    width=600,
    height=400,
    title="Home Ownership"
)


plot_scatter = alt.Chart(df).mark_point().encode(
    x ='annual_income', 
    y ='loan_amount'
).properties(
    width=600,
    height=400,
    title="Scatter Plot of Annual Income vs Loan Amount"
)


plot_hist = alt.Chart(df).mark_bar().encode(
    x=alt.X('annual_income', bin=True, title='Annual Income'),  # Binning the annual_income variable
    y=alt.Y('count()', title='Count')
).properties(
    width=600,
    height=400,
    title="Histogram of Annual Income"
)

plot_box = alt.Chart(df).mark_boxplot().encode(
    y=alt.Y('annual_income', title='Annual Income')
).properties(
    width=600,
    height=400,
    title="Box Plot of Annual Income"
)

plot_it= alt.Chart(df).mark_boxplot().encode(
    y=alt.Y('interest_rate', title='Interest Rate'),
    x='grade',
    color='grade'
).properties(
    width=600,
    height=400,
    title="Box Plot of Interest Rate"
)

plot_box = alt.Chart(df).mark_boxplot().encode(
    y=alt.Y('annual_income', title='Annual Income'),
    x='grade'
).properties(
    width=600,
    height=400,
    title="Box Plot of Annual Income"
)
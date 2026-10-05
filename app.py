# PSEUDOCODE FOR EXPENSE TRACKER WEB APP

# 1. Display the title of the web app and a short description.
# 2. Provide a widget for the user to upload a CSV file.
# 3. Check if a file has been uploaded:
    # IF a file is present THEN
        # TODO: Read the CSV file into a Pandas DataFrame
        # TODO: Display the raw data table to the user
        # TODO: Group data by 'Category' and sum the 'Amount' column
        # TODO: Display the totals as a chart or table
    # ELSE
        # TODO: Show an info message asking the user to upload a file

import pandas as pd
import streamlit as st

st.title("Expense Tracker")
st.write("Upload a file:")
uf = st.file_uploader("Choose a CSV file", type="csv")

if uf is not None:
    df = pd.read_csv(uf)
    st.dataframe(df)
    st.write("--------Total Expenses--------")
    st.write(df)
    category = df.groupby('Category')['Amount'].sum()
    st.write("--------Total by Category--------")
    st.write(category)
else:
    st.info("Please upload a CSV file to see the data.")
import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_months_tab():
    response = requests.get(f"{API_URL}/analytics_monthly/")
    if response.status_code != 200:
        st.error("Failed to fetch monthly data")
        return

    data = response.json()
    df = pd.DataFrame(data)
    df_sorted = df.sort_values(by="month_number")

    st.title("Expense Breakdown By Months")
    st.bar_chart(data=df_sorted.set_index("month_name")["total"], use_container_width=True)

    df_sorted = df_sorted[["month_number", "month_name", "total"]]
    df_sorted["total"] = df_sorted["total"].map("{:.2f}".format)
    st.table(df_sorted)
import streamlit as st
import sqlite3
import pandas as pd
import os

# In-memory database (fresh every run)
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Load SQL schema
sql_file = "banking_transaction_project.sql"
if not os.path.exists(sql_file):
    st.error("❌ SQL file missing.")
    st.stop()

try:
    with open(sql_file, "r") as f:
        sql_script = f.read()
    cursor.executescript(sql_script)
    conn.commit()
except Exception as e:
    st.error(f"❌ SQL execution failed: {e}")
    st.stop()

st.title("🏦 Banking Transaction Analyzer")

# Load data
customers = pd.read_sql("SELECT * FROM customers", conn)
accounts = pd.read_sql("SELECT * FROM accounts", conn)
transactions = pd.read_sql("SELECT * FROM transactions", conn)

# Show tables
st.subheader("👥 Customers")
st.dataframe(customers)

st.subheader("💳 Accounts")
st.dataframe(accounts)

st.subheader("💰 Transactions")
st.dataframe(transactions)

# Summary
st.subheader("📊 Summary")
st.metric("Total Bank Balance", f"${accounts['balance'].sum():,.2f}")
st.metric("Total Transactions", len(transactions))
st.metric("Total Credit", f"${transactions[transactions['type']=='credit']['amount'].sum():,.2f}")
st.metric("Total Debit", f"${transactions[transactions['type']=='debit']['amount'].sum():,.2f}")

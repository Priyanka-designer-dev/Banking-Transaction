import streamlit as st
import sqlite3
import pandas as pd
import os

# File path
sql_file = "banking_transaction_project.sql"

# Check if SQL file exists
if not os.path.exists(sql_file):
    st.error(f"❌ Missing required file: {sql_file}")
    st.stop()

# Create SQLite database
conn = sqlite3.connect("banking.db")
cursor = conn.cursor()

# Read and execute SQL script
try:
    with open(sql_file, "r") as f:
        sql_script = f.read()
    cursor.executescript(sql_script)
    conn.commit()
except Exception as e:
    st.error(f"❌ SQL execution failed: {e}")
    st.stop()

# App UI
st.title("🏦 Banking Transaction Analyzer")

# Customers
st.subheader("👥 Customers")
customers = pd.read_sql("SELECT * FROM customers", conn)
st.dataframe(customers)

# Accounts
st.subheader("💳 Accounts")
accounts = pd.read_sql("SELECT * FROM accounts", conn)
st.dataframe(accounts)

# Transactions
st.subheader("💰 Transactions")
transactions = pd.read_sql("SELECT * FROM transactions", conn)
st.dataframe(transactions)

# Summary
st.subheader("📊 Summary")
st.metric("Total Balance", f"${accounts['balance'].sum():,.2f}")
st.metric("Total Transactions", len(transactions))
st.metric("Total Credits", f"${transactions[transactions['type']=='credit']['amount'].sum():,.2f}")
st.metric("Total Debits", f"${transactions[transactions['type']=='debit']['amount'].sum():,.2f}")

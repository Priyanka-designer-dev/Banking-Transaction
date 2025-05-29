import streamlit as st
import sqlite3
import pandas as pd

# Create SQLite DB from SQL file
conn = sqlite3.connect("banking.db")
cursor = conn.cursor()

with open("banking_transaction_project.sql", "r") as f:
    sql_script = f.read()
cursor.executescript(sql_script)
conn.commit()

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

# Simple Summary
st.subheader("📊 Summary")
total_balance = accounts['balance'].sum()
total_transactions = len(transactions)
total_credits = transactions[transactions['type'] == 'credit']['amount'].sum()
total_debits = transactions[transactions['type'] == 'debit']['amount'].sum()

st.metric("Total Bank Balance", f"${total_balance:,.2f}")
st.metric("Total Transactions", total_transactions)
st.metric("Total Credit", f"${total_credits:,.2f}")
st.metric("Total Debit", f"${total_debits:,.2f}")
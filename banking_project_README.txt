
# 🏦 Banking Transaction Analyzer

## 🧩 Project Overview
This SQL-based project simulates a banking environment to analyze customer transactions. It helps identify spending behavior, account types, transaction volumes, and anomalies.

## 📁 Database Structure
- **customers**: Customer details
- **accounts**: Financial account info linked to customers
- **transactions**: Credit and debit events associated with accounts

## 🔍 Use Cases
- Monthly transaction summaries
- Detection of unusually large transactions
- City-wise transaction distribution
- Debit-to-credit ratios by account type

## 🛠️ SQL Concepts Used
- JOINs (1:many)
- Aggregations (SUM, COUNT, AVG)
- GROUP BY with CASE
- Filtering with HAVING and WHERE
- Date truncation for month/year grouping

## 📈 Example Queries
- Total credits and debits by month
- Accounts with top transaction values
- Ratio analysis of credit vs debit across account types
- Customer trends based on balance and activity

## 🚀 How to Run
1. Run the `banking_transaction_project.sql` file to create schema and insert records.
2. Analyze the data using SQL IDEs or BI tools.

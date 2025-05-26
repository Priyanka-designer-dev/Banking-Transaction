# 💳 Banking Transaction Analyzer

A portfolio project that simulates a banking transaction system using PostgreSQL. This project includes customers, accounts, and transactions data, with a dashboard to explore and analyze key metrics.

## 🚀 Features

- Customer and account browsing
- Transaction history filtering
- Summary KPIs and charts
- Powered by PostgreSQL and Streamlit

## 📦 Technologies

- PostgreSQL (Railway)
- Streamlit
- Python (psycopg2, pandas, sqlalchemy)

## 🛠 Setup Instructions

1. **Clone this repo**  
   ```bash
   git clone https://github.com/your-username/banking-analyzer.git
   cd banking-analyzer
   ```

2. **Set up your PostgreSQL database**
   - Create a free PostgreSQL DB on [Railway](https://railway.app)
   - Import the `banking_transaction_project.sql` file into your Railway DB
   - Copy your DB connection string

3. **Create a `.env` file**  
   Copy from the example:
   ```bash
   cp .env.example .env
   ```

4. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Streamlit app**  
   ```bash
   streamlit run app.py
   ```

## 🌐 Live Demo

👉 [Add your deployed Streamlit Cloud or Render link here]

## 📁 Files

- `banking_transaction_project.sql` — SQL schema and sample data
- `app.py` — Streamlit app
- `db.py` — DB connection logic
- `.env.example` — Sample DB URL config

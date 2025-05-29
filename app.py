import streamlit as st
import sqlite3
import pandas as pd
import os

# File path
sql_file = "banking_transaction_project.sql"

# Check if SQL file exists
if not os.
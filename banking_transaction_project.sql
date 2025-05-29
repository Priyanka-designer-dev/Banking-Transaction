
-- SCHEMA AND SAMPLE DATA FOR BANKING TRANSACTION ANALYZER

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    city VARCHAR(50),
    account_open_date DATE
);

INSERT INTO customers VALUES
(1, 'Alice', 30, 'New York', '2019-01-10'),
(2, 'Bob', 45, 'Chicago', '2020-03-15'),
(3, 'Charlie', 28, 'San Francisco', '2021-06-20');

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    customer_id INT,
    account_type VARCHAR(20),
    balance DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO accounts VALUES
(101, 1, 'Savings', 5000.00),
(102, 2, 'Checking', 12000.50),
(103, 3, 'Savings', 3000.75);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    transaction_date DATE,
    amount DECIMAL(10,2),
    type VARCHAR(10),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

INSERT INTO transactions VALUES
(1, 101, '2023-01-10', 1000.00, 'credit'),
(2, 101, '2023-01-12', 200.00, 'debit'),
(3, 102, '2023-02-01', 500.00, 'debit'),
(4, 103, '2023-02-15', 1500.00, 'credit'),
(5, 103, '2023-02-20', 400.00, 'debit');

# Money Exchange System

## Project Introduction
This project is a simple Money Exchange System developed using Python and SQLite3 for **MSE800 Week 3 - Activity 5**. 
The system manages customer details, currencies, exchange rates, and exchange transactions based on Object-Oriented Programming (OOP) principles.

---

## Database Architecture (4 Tables)

1. **`Customer`**: Stores customer identity details (ID, First Name, Last Name, Phone Number). Necessary to link transactions to specific clients.
2. **`Currency`**: Stores supported currency details (ID, Code, Name like NZD, USD, CNY). Prevents string duplication across transaction records.
3. **`ExchangeRate`**: Stores conversion rates between currency pairs (Rate ID, From Currency, To Currency, Exchange Rate). Necessary for independent rate management.
4. **`TransactionHistory`**: Records every executed exchange (Transaction ID, Customer ID, From Currency, To Currency, Amount, Exchange Rate). Necessary for business transaction logging.

---

## Entity-Relationship (ER) Diagram

```mermaid
erDiagram
    CUSTOMER ||--o{ TRANSACTION_HISTORY : places
    CURRENCY ||--o{ EXCHANGE_RATE : "from/to"
    CURRENCY ||--o{ TRANSACTION_HISTORY : "source/target"

    CUSTOMER {
        int Customer_ID PK
        string First_Name
        string Last_Name
        string Phone_Number
    }

    CURRENCY {
        int Currency_ID PK
        string Currency_Code
        string Currency_Name
    }

    EXCHANGE_RATE {
        int Rate_ID PK
        string From_Currency
        string To_Currency
        float Exchange_Rate
    }

    TRANSACTION_HISTORY {
        int Transaction_ID PK
        int Customer_ID FK
        string From_Currency
        string To_Currency
        float Amount
        float Exchange_Rate
    }
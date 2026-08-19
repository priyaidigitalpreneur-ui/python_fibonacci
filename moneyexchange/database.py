import sqlite3

class AppDatabase:
    def __init__(self, db_file="money_exchange.db"):
        self.db_file = db_file

    def get_connection(self):
        return sqlite3.connect(self.db_file)

    def init_db(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        # Enable Foreign Keys
        cursor.execute("PRAGMA foreign_keys = ON;")

        # Table 1: Client Information
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Client (
                client_id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                contact_no TEXT
            )
        ''')

        # Table 2: Currency Info
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Currency (
                currency_id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                title TEXT NOT NULL
            )
        ''')

        # Table 3: Rates
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ExchangeRate (
                rate_id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_curr_id INTEGER,
                target_curr_id INTEGER,
                conversion_rate REAL NOT NULL,
                FOREIGN KEY(source_curr_id) REFERENCES Currency(currency_id),
                FOREIGN KEY(target_curr_id) REFERENCES Currency(currency_id)
            )
        ''')

        # Table 4: Transaction Record
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TransactionRecord (
                tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER,
                source_curr_id INTEGER,
                target_curr_id INTEGER,
                src_amount REAL,
                converted_amount REAL,
                FOREIGN KEY(client_id) REFERENCES Client(client_id),
                FOREIGN KEY(source_curr_id) REFERENCES Currency(currency_id),
                FOREIGN KEY(target_curr_id) REFERENCES Currency(currency_id)
            )
        ''')

        conn.commit()
        conn.close()
        print("Database schema successfully configured!")
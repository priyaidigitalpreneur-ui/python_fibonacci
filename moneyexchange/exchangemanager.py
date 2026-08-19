from database import AppDatabase

class MoneyExchangeService:
    def __init__(self):
        self.db = AppDatabase()
        self.db.init_db()

    def register_client(self, name, phone):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Client (full_name, contact_no) VALUES (?, ?)", (name, phone))
        conn.commit()
        conn.close()
        print(f"Client '{name}' registered successfully.")

    def add_currency(self, code, title):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Currency (code, title) VALUES (?, ?)", (code.upper(), title))
            conn.commit()
            print(f"Currency '{code.upper()}' added.")
        except Exception as e:
            print(f"Error: Currency might already exist. ({e})")
        finally:
            conn.close()

    def set_exchange_rate(self, src_id, tgt_id, rate):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ExchangeRate (source_curr_id, target_curr_id, conversion_rate) VALUES (?, ?, ?)", 
                       (src_id, tgt_id, rate))
        conn.commit()
        conn.close()
        print("Conversion rate updated successfully.")

    def process_transaction(self, client_id, src_id, tgt_id, amount, rate):
        total = round(amount * rate, 2)
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO TransactionRecord 
            (client_id, source_curr_id, target_curr_id, src_amount, converted_amount) 
            VALUES (?, ?, ?, ?, ?)
        ''', (client_id, src_id, tgt_id, amount, total))
        conn.commit()
        conn.close()
        print(f"Transaction Complete! Converted Amount: {total}")

    def view_all_transactions(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT T.tx_id, C.full_name, T.src_amount, T.converted_amount 
            FROM TransactionRecord T
            JOIN Client C ON T.client_id = C.client_id
        ''')
        records = cursor.fetchall()
        conn.close()

        print("\n--- All Recorded Transactions ---")
        if not records:
            print("No transactions found.")
        for r in records:
            print(f"Tx ID: {r[0]} | Client: {r[1]} | Exchanged Amount: {r[2]} | Received: {r[3]}")
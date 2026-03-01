import sqlite3


class Database:
    def __init__(self, db_path="credit_system.db"):
        self.db_path = db_path
        self.conn = None

    def get_connection(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def init_schema(self):
        conn = self.get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                passport_no TEXT NOT NULL UNIQUE
            )
            """
        )

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS credit_applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                status TEXT NOT NULL,
                note TEXT,
                FOREIGN KEY(customer_id) REFERENCES customers(id)
            )
            """
        )

        conn.commit()

    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
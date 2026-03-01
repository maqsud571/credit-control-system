from models.customer import Customer
from database.db import Database


class CustomerRepository:
    def __init__(self, db):
        # db: Database
        self.db = db

    def create(self, name, passport_no):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO customers (name, passport_no) VALUES (?, ?)",
            (name, passport_no),
        )
        conn.commit()
        customer_id = cur.lastrowid
        return Customer(customer_id, name, passport_no)

    def get_by_id(self, customer_id):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, name, passport_no FROM customers WHERE id = ?",
            (customer_id,),
        )
        row = cur.fetchone()
        if row:
            return Customer(row[0], row[1], row[2])
        return None

    def get_all(self):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, passport_no FROM customers")
        rows = cur.fetchall()
        customers = []
        for r in rows:
            customers.append(Customer(r[0], r[1], r[2]))
        return customers
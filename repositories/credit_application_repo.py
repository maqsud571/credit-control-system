from models.credit_application import CreditApplication
from database.db import Database


class CreditApplicationRepository:
    def __init__(self, db):
        # db: Database
        self.db = db

    def create(self, customer_id, amount, note=""):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO credit_applications (customer_id, amount, status, note) VALUES (?, ?, ?, ?)",
            (customer_id, amount, "requested", note),
        )
        conn.commit()
        app_id = cur.lastrowid
        return CreditApplication(app_id, customer_id, amount, "requested", note)

    def update_status(self, application_id, new_status, note=""):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE credit_applications SET status = ?, note = ? WHERE id = ?",
            (new_status, note, application_id),
        )
        conn.commit()

    def get_by_status(self, status):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, customer_id, amount, status, note FROM credit_applications WHERE status = ?",
            (status,),
        )
        rows = cur.fetchall()
        apps = []
        for r in rows:
            apps.append(CreditApplication(r[0], r[1], r[2], r[3], r[4] or ""))
        return apps

    def get_all(self):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, customer_id, amount, status, note FROM credit_applications")
        rows = cur.fetchall()
        apps = []
        for r in rows:
            apps.append(CreditApplication(r[0], r[1], r[2], r[3], r[4] or ""))
        return apps
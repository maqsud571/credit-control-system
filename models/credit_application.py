class CreditApplication:
    def __init__(self, id, customer_id, amount, status, note):
        self.id = id
        self.customer_id = customer_id
        self.amount = amount
        self.status = status
        self.note = note

    def __repr__(self):
        return "CreditApplication(id=%s, customer_id=%s, amount=%s, status=%s)" % (
            self.id,
            self.customer_id,
            self.amount,
            self.status,
        )
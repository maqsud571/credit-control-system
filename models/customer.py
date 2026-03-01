class Customer:
    def __init__(self, id, name, passport_no):
        self.id = id
        self.name = name
        self.passport_no = passport_no

    def __repr__(self):
        return "Customer(id=%s, name=%s, passport_no=%s)" % (self.id, self.name, self.passport_no)
class CreditService:
    def __init__(self, customer_repo, application_repo):
        self.customer_repo = customer_repo
        self.application_repo = application_repo

    def request_credit(self, customer_id, amount, note=""):
        customer = self.customer_repo.get_by_id(customer_id)
        if customer is None:
            raise ValueError("Customer topilmadi")
        return self.application_repo.create(customer_id, amount, note)

    def approve_application(self, application_id, note="Approved"):
        self.application_repo.update_status(application_id, "approved", note)

    def reject_application(self, application_id, note="Rejected"):
        self.application_repo.update_status(application_id, "rejected", note)

    def get_requested_list(self):
        return self.application_repo.get_by_status("requested")

    def get_approved_list(self):
        return self.application_repo.get_by_status("approved")
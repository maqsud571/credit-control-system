from database.db import Database
from repositories.customer_repo import CustomerRepository
from repositories.credit_application_repo import CreditApplicationRepository
from services.credit_service import CreditService
from views.cli import run_cli


def main():
    db = Database("credit_system.db")
    db.init_schema()

    customer_repo = CustomerRepository(db)
    app_repo = CreditApplicationRepository(db)
    service = CreditService(customer_repo, app_repo)

    run_cli(service, customer_repo)

    db.close()


if __name__ == "__main__":
    main()
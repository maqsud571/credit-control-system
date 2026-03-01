from services.credit_service import CreditService
from repositories.customer_repo import CustomerRepository


def print_menu():
    print("\n===== CREDIT SYSTEM =====")
    print("1. Mijoz qo'shish")
    print("2. Kreditga ariza berish")
    print("3. Kredit olmoqchi bo'lganlar ro'yxati (REQUESTED)")
    print("4. Kredit olganlar ro'yxati (APPROVED)")
    print("5. Arizani tasdiqlash")
    print("6. Arizani rad etish")
    print("0. Chiqish")


def run_cli(service, customer_repo):
    while True:
        print_menu()
        choice = input("Tanlang: ")

        if choice == "1":
            name = input("Mijoz ismi: ")
            passport_no = input("Passport raqami: ")
            try:
                customer = customer_repo.create(name, passport_no)
                print("Yangi mijoz qo'shildi:", customer)
            except Exception as e:
                print("Xato:", e)

        elif choice == "2":
            customers = customer_repo.get_all()
            if not customers:
                print("Avval mijoz qo'shing.")
                continue

            print("Mijozlar:")
            for c in customers:
                print("ID=%s, Name=%s" % (c.id, c.name))

            cid = input("Qaysi mijoz ID si uchun ariza beriladi: ")
            amount = input("Kredit summasi: ")
            note = input("Izoh (ixtiyoriy): ")

            try:
                cid_int = int(cid)
                amount_float = float(amount)
                app = service.request_credit(cid_int, amount_float, note)
                print("Ariza yaratildi:", app)
            except Exception as e:
                print("Xato:", e)

        elif choice == "3":
            apps = service.get_requested_list()
            if not apps:
                print("Hozircha requested arizalar yo'q.")
            else:
                print("\nRequested arizalar:")
                for a in apps:
                    cust = customer_repo.get_by_id(a.customer_id)
                    name = cust.name if cust else "?"
                    print("ID=%s, Customer=%s, Amount=%s, Status=%s" % (a.id, name, a.amount, a.status))

        elif choice == "4":
            apps = service.get_approved_list()
            if not apps:
                print("Hozircha approved arizalar yo'q.")
            else:
                print("\nApproved arizalar:")
                for a in apps:
                    cust = customer_repo.get_by_id(a.customer_id)
                    name = cust.name if cust else "?"
                    print("ID=%s, Customer=%s, Amount=%s, Status=%s" % (a.id, name, a.amount, a.status))

        elif choice == "5":
            app_id = input("Qaysi ariza ID sini tasdiqlaysiz: ")
            note = input("Izoh (ixtiyoriy, default=Approved): ")
            if note.strip() == "":
                note = "Approved"
            try:
                app_id_int = int(app_id)
                service.approve_application(app_id_int, note)
                print("Ariza tasdiqlandi.")
            except Exception as e:
                print("Xato:", e)

        elif choice == "6":
            app_id = input("Qaysi ariza ID sini rad etasiz: ")
            note = input("Sabab (Rejected sababi): ")
            if note.strip() == "":
                note = "Rejected"
            try:
                app_id_int = int(app_id)
                service.reject_application(app_id_int, note)
                print("Ariza rad etildi.")
            except Exception as e:
                print("Xato:", e)

        elif choice == "0":
            print("Chiqildi.")
            break

        else:
            print("Noto'g'ri tanlov.")
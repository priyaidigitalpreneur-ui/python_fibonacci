from exchangemanager import MoneyExchangeService

def launch_app():
    service = MoneyExchangeService()

    while True:
        print("\n=================================")
        print("   MONEY EXCHANGE MANAGEMENT     ")
        print("=================================")
        print("1. Register New Client")
        print("2. Add Supported Currency")
        print("3. Define Exchange Rate")
        print("4. Execute Exchange Transaction")
        print("5. View Transaction History")
        print("0. Exit System")
        
        user_choice = input("\nSelect an option (0-5): ").strip()

        if user_choice == "1":
            name = input("Enter Client Full Name: ")
            phone = input("Enter Contact Number: ")
            service.register_client(name, phone)

        elif user_choice == "2":
            code = input("Enter Currency Code (e.g., USD): ")
            title = input("Enter Currency Title (e.g., US Dollar): ")
            service.add_currency(code, title)

        elif user_choice == "3":
            src_id = int(input("Enter Source Currency ID: "))
            tgt_id = int(input("Enter Target Currency ID: "))
            rate = float(input("Enter Conversion Rate: "))
            service.set_exchange_rate(src_id, tgt_id, rate)

        elif user_choice == "4":
            c_id = int(input("Enter Client ID: "))
            s_id = int(input("Enter Source Currency ID: "))
            t_id = int(input("Enter Target Currency ID: "))
            amt = float(input("Enter Amount to Convert: "))
            rate = float(input("Enter Applied Rate: "))
            service.process_transaction(c_id, s_id, t_id, amt, rate)

        elif user_choice == "5":
            service.view_all_transactions()

        elif user_choice == "0":
            print("Shutting down the exchange console. Goodbye!")
            break

        else:
            print("Invalid selection! Please enter a valid menu option.")

if __name__ == "__main__":
    launch_app()
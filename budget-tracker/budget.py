def main():
    balance = 0.0
    transactions = []

    while True:
        print("\nBudget Tracker")
        print("1. Add income")
        print("2. Add expense")
        print("3. Show balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Income amount: "))
            balance += amount
            transactions.append(("income", amount))
            print("Income added.")
        elif choice == "2":
            amount = float(input("Expense amount: "))
            balance -= amount
            transactions.append(("expense", amount))
            print("Expense added.")
        elif choice == "3":
            print(f"Current balance: ${balance:.2f}")
            if transactions:
                for idx, (t_type, amt) in enumerate(transactions, start=1):
                    print(f"{idx}. {t_type.title()}: ${amt:.2f}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

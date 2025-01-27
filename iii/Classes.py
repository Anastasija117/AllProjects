class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction("Deposit", amount))
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction("Withdrawal", amount))
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"\nAccount {self.account_number} - {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}\n")

    def show_transactions(self):
        print(f"\nTransaction History for {self.account_holder}:")
        if not self.transactions:
            print("No transactions yet.")
        for transaction in self.transactions:
            print(f"{transaction.type}: ${transaction.amount:.2f}")
        print()


class Transaction:
    def __init__(self, transaction_type, amount):
        self.type = transaction_type
        self.amount = amount


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            print("Account number already exists.")
            return

        account_holder = input("Enter account holder's name: ")
        initial_balance = float(input("Enter initial deposit amount: "))
        self.accounts[account_number] = BankAccount(account_number, account_holder, initial_balance)
        print(f"Account created successfully for {account_holder}.\n")

    def get_account(self):
        account_number = input("Enter your account number: ")
        return self.accounts.get(account_number, None)

    def run(self):
        while True:
            print("\n===== Bank System Menu =====")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. View Transactions")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.create_account()
            elif choice in ["2", "3", "4", "5"]:
                account = self.get_account()
                if not account:
                    print("Account not found. Try again.")
                    continue

                if choice == "2":
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                elif choice == "3":
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                elif choice == "4":
                    account.display_balance()
                elif choice == "5":
                    account.show_transactions()
            elif choice == "6":
                print("Thank you for using the bank system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the bank system
if __name__ == "__main__":
    bank = Bank()
    bank.run()


class BankAccount:
    def __init__(self,acc_num,acc_holder,balance=0.0):
        self.acc_num = acc_num
        self.acc_holder = acc_holder
        self.balance = balance
        self.transactions = []

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction("Deposit",amount))
            print(f"Deposited ${amount:.2f} to {self.acc_holder}.New balance ${self.balance}")
        else:
            print("Deposit must be greater than 0!")

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction("Withdraw",amount))
            print(f"Withdrawn ${amount:.2f} to {self.acc_holder}.New balance ${self.balance}")
        else:
            print("Invalid withrawal amount or insufficient funds.")

    def display_balance(self):
        print(f"Account number: {self.acc_num}, Holder: {self.acc_holder}, Balance: {self.balance}")

    def show_transactions(self):
        print(f"Transaction history for {self.acc_holder}:")
        if not self.transactions:
            print("No transactions yet!")
        else:
            for tranaction in self.transactions:
                print(f"{tranaction.type}:${tranaction.amount:.2f}")
        print()


class Transaction:
    def __init__(self,trans_type,amount):
        self.type = trans_type
        self.amount = amount


class Bank:
    def __init__(self):
        self.accounts = {}


    def create_account(self):
        acc_num = input("Enter your account number: ")
        if acc_num in self.accounts:
            print("Account already exists!")
            return

        acc_holder = input("Enter account holder's name: ")
        initial_bal = float(input("Enter initial balance: "))

        self.accounts[acc_num] = BankAccount(acc_num,acc_holder,initial_bal)
        print(f"Account created successfully for {acc_holder}.")

    def get_account(self):
        acc = input("Enter your account number: ")
        return self.accounts.get(acc, None)

    def display_accounts(self):
        if not self.accounts:
            print("No accounts found.")
            return

        print("\n--------------------Account list--------------------")
        for acc_num,account in self.accounts.items():
            print(f"Account number: {acc_num}, Holder: {account.acc_holder}")
        print("----------------------------------------------------\n")
    def run(self):

        while True:
            print("-----Bank system menu-----")
            print("     1.Create account")
            print("     2.Display accounts")
            print("     3.Deposit money")
            print("     4.Withdraw money")
            print("     5.Check balance")
            print("    6.View transactions")
            print("          7.Exit")
            print("--------------------------")
            choice = input("Choose an option: ")

            if choice == "1":
                self.create_account()

            elif choice == "2":
                self.display_accounts()

            elif choice in ["3","4","5","6"]:
                account = self.get_account()
                if not account:
                    print("Account not found.Try again.")
                    continue

                if choice == "3":
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)

                elif choice == "4":
                    amount = float(input("Enter withdraw money: "))
                    account.withdraw(amount)

                elif choice == "5":
                    account.display_balance()

                elif choice == "6":
                    account.show_transactions()

            elif choice == "7":
                print("Thank you for using the bank system.Goodbye!")
                break
            else:
                print("Invalid choice.Please try again!")

if __name__ == "__main__":
    bank = Bank()
    bank.run()
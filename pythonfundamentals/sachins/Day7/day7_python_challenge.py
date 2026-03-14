import sys

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Customer(Person):
    def __init__(self, firstname, lastname, accountnumber, balance):
        super().__init__(firstname, lastname)
        self.accountnumber = accountnumber
        self.balance = balance

    def __str__(self):
        print(f"{self.balance}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("You cannot withdraw more than you have")
        else:
            self.balance -= amount

sachin_customer = Customer("Sachin", "Sharma","12345", 0)
do_continue = True

while do_continue:
    msg = '''1. Withdraw
    2. Deposit
    3. Exit'''
    choice = int(input("Select whether you want to deposit or withdraw?"+msg))
    if choice == 1:
        amount = int(input("Enter amount to withdraw: "))
        sachin_customer.withdraw(amount)
        print(f'Balance is {sachin_customer.balance}')
        want_to_continue = input("Do you want to continue (Y/N)?")
        if want_to_continue == "Y" or want_to_continue == 'y':
            continue
        else:
            sys.exit(1)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        sachin_customer.deposit(amount)
        print(f'Balance is {sachin_customer.balance}')
        want_to_continue = input("Do you want to continue (Y/N)?")
        if want_to_continue == "Y" or want_to_continue == 'y':
            continue
        else:
            sys.exit(1)
    elif choice == 3:
        sys.exit(1)

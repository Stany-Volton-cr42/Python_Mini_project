class Atm:
    # Constructor
    def __init__(self):
        self.balance = 0
        self.pin = ''
        self.menu()
    # Now we create the funtionality of the ATM
    def menu(self):
        user_input = input("""
        Hi! How Can I help you?
            Press 1 to create pin
            Press 2 to change pin
            Press 3 to Cheak balance
            Press 4 to withdraw
            Press 5 to exit()
            """)
        if user_input == '1':
            # crate pin
            self.creat_pin()
        elif user_input == '2':
            # change pin
            self.change_pin()
        elif user_input == '3':
            # cheak balance   
            self.cheak_balance()
        elif user_input == '4':
            # withdraw
            self.withdraw()
        else:
            print("your at exit")

    def creat_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin

        user_balance = int(input("Enter your balance: "))
        self.balance = user_balance

        print("Your pin is created succesfully! ")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter your old pin: ")
        if old_pin == self.pin:
            # Let him change the pin
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("Pin changed successfully! ")
            self.menu()
        else:
            print("pin Nhi change kar sakte re baba: ")
            self.menu()

    def cheak_balance(self):
        user_pin2 = input("Enter your pin: ")
        if user_pin2 == self.pin:
            print("Your account Ballance is",self.balance)
            self.menu()
        else:
            print("balance nhi dikha sakta")
            self.menu()

    def withdraw(self):
        user_pin3 = input("Enter your pin: ")
        if user_pin3 == self.pin:
            # allow to withdraw
            amount = int(input("Enter the balance: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdraw Successful, Your avabiable balance is,",self.balance)
            else:
                print("sale chor")
        else:
            print("Chal nikal yha se: ")
        self.menu()

# crating object
obj = Atm()
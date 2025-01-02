'''
we need to check following things in order
1] account balance enquiry
2] cash withdrawal
3]cash deposit
4]pin change
5]transaction history
'''

class ATM:
    def __init__(self):
        # Initialize account balance, transaction history, and PIN
        self.balance = 5000
        self.transaction_history = []
        self.pin = "1234"

    # Function to check account balance
    def account_balance_enquiry(self):
        print(f"Your current balance is: ${self.balance}")

    #  cash withdrawal
    def cash_withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Please enter a valid amount.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.transaction_history.append(f"Withdrawn ${amount}")

    # cash deposit
    def cash_deposit(self, amount):
        if amount <= 0:
            print("Please enter a valid deposit amount.")
        else:
            self.balance += amount
            print(f"${amount} deposited successfully.")
            self.transaction_history.append(f"Deposited ${amount}")

    
    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            if old_pin == new_pin:
                print("New PIN cannot be the same as the old PIN.")
            else:
                self.pin = new_pin
                print("PIN changed successfully.")
                self.transaction_history.append("PIN Changed")
        else:
            print("Incorrect current PIN.")

    
    def show_transaction_history(self):
        if not self.transaction_history:
            print("No transaction history available.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

atm = ATM()

attempts = 3
while attempts > 0:
    pin = input("Please Enter your 4-digit PIN: ")
    if pin == atm.pin:
        print("Permission granted.")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. {attempts} attempt(s) remaining.")
    if attempts == 0:
        print("Account locked due to too many incorrect attempts.")
        exit()  


while True:
    print("\nATM Menu:")
    print("#############################")
    print("1: Account Balance Inquiry")
    print("2: Cash Withdrawal")
    print("3: Cash Deposit")
    print("4: Change PIN")
    print("5: View Transaction History")
    print("6: Exit")
    
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        atm.account_balance_enquiry()
    elif choice == '2':
        try:
            amount = float(input("Enter the amount to withdraw: "))
            atm.cash_withdrawal(amount)
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
    elif choice == '3':
        try:
            amount = float(input("Enter the amount to deposit: "))
            atm.cash_deposit(amount)
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
    elif choice == '4':
        old_pin = input("Enter your current PIN: ")
        new_pin = input("Enter your new PIN: ")
        atm.change_pin(old_pin, new_pin)
    elif choice == '5':
        atm.show_transaction_history()
    elif choice == '6':
        print("Thank you for using the ATM. Have a nice day!")
        break
    else:
        print("Invalid choice, please try again.")





'''
ATM CODE EXPLAINATION
The program functions like an ATM. It allows users to do the following:

1. Check Account Balance: 
2. Withdraw Cash:
3. Deposit Cash:
4. Change PIN:
5. View Transaction History:
#######################################################################################################################
#######################################################################################################################

##How the Code is Organized##


#1. The ATM Class
    This is the main part of the program where all account-related actions are handled.

    Initialization (__init__):
        a]  The account starts with a balance of $5000.
        b]  It keeps track of all transactions (like money added or taken out).
        c]  The default PIN is set to "1234".

#2. What Each Function Does
    Check Account Balance (account_balance_enquiry):

        a]  This function simply shows the current balance in the account.

    Withdraw Money (cash_withdrawal):

        a]  It checks if there is enough money in the account to withdraw.
        b]  It prevents users from withdrawing amounts that are less than or equal to zero.
        c]  If everything is okay, it deducts the amount from the balance and records the withdrawal in the transaction history.

    Deposit Money (cash_deposit):

        a]  This function ensures the deposit amount is greater than zero.
        b]  If valid, it adds the amount to the balance and logs the deposit in the transaction history.

#3.Change PIN (change_pin):

        a]  It checks if the current PIN entered by the user is correct.
        b]  It ensures the new PIN is different from the old one.
        c]  If everything is valid, it updates the PIN and records the change.

    Transaction History (show_transaction_history):

        a]  This function displays a list of past actions (like deposits, withdrawals, or PIN changes).
        b]  If no transactions have been made, it shows a message indicating that.

##How the Program Runs##
    PIN Authentication:

        a]  The user has three chances to enter the correct PIN.
        b]  If they enter it correctly, they can access the ATM menu.
        c]  If all attempts fail, the program exits
ATM Menu:

    After logging in, the user sees options to:

        a]  Check balance
        b]  Withdraw cash
        c]  Deposit cash
        d]  Change PIN
        e]  View transaction history
        f]  Exit the program
    The user selects an option, and the program performs the corresponding action.

    Error Handling:

        a]  If the user inputs something invalid (like letters instead of numbers), the program displays a clear error message.
        b]  If the user chooses an invalid menu option, they are prompted to try again.
Exit:

        The user can exit the program at any time by selecting the exit option.
'''




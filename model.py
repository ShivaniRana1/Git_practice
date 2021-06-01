
from tkinter import *
import datetime

root = Tk()
root.title("shivani phonebook")

class Bank:
    __bank_name = 'Bro Bank Pvt. Ltd.'
    __interest_rate = 10

    def __init__(self, name, age, nationality, address, balance = 0):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.address = address
        self.balance = balance
    
    def add_balance(self, add_balance):
        if add_balance < 0:
            print('Please enter valid amount')
        else:
            self.balance = self.balance + add_balance
            print('Your total balance is {}'.format(self.check_balance()))
  
    
   
   
while True:
    print('***************************************************************')
    print('Today is {}/{}/{}'.format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
    print('Welcome to {}'.format(Bank.get_bank_name()))
    print("Today's date time is {}".format(Bank.current_date()))

    user_choice = input('Enter \n 1 to open account. \n 2 to add balance. \n 3 to withdraw balance. \n 4 to check balance. \n 5 to check interest rate. \n 6 to print holidays  ')
    if user_choice == '1':
        user_name = input('Enter name: ')
        user_age = input('Enter age: ')
        user_address = input('Enter address: ')
        user_nationality = input('Enter nationality: ')

        user = Bank(user_name, user_age, user_nationality, user_address)

        print('Yaaayyyyyyyy!! An account has been created for you.')

    elif user_choice == '2':
        deposit_balance = int(input('Enter deposit amount: '))
        user.add_balance(deposit_balance)

    elif user_choice == '3':
        withdraw_amount = int(input('Enter withdraw amount: '))
        user.withdraw_balance(withdraw_amount)

    elif user_choice == '4':
        print('Your balance is {}.'.format(user.check_balance()))
    
    elif user_choice == '5':
        print("Bank's interest rate is {}".format(Bank.check_interest_rate()))
    
    elif user_choice == '6':
        Bank.print_holiday()
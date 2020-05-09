import random
import json
import os

n = 10
log_in = True
start = True
while start:
    user_input = input('''Please choose an option
1) Login
2) Close App
Please enter a choice: ''')
    if user_input == '1':
        staff_username = input('Username: ')
        staff_password = input('Password: ')
        with open('staff.txt') as file:
            user_details = json.load(file)
            for items in user_details:
                if staff_username == items['Username'] and staff_password == items['Password']:
                    session_store = open('session.txt', 'w')
                    session_store.write(staff_username)
                    session_store.close()

                    while log_in:
                        print(f'Welcome {staff_username}. What would you like to do today?')
                        print("""1) Create new bank account
2) Check Account details
3) Logout""")
                        staff_choice = input('Please make a choice: ')
                        if staff_choice == '1':
                            print('Please provide the following details \n')
                            acct_number = ''.join(["{}".format(random.randint(0, 9)) for num in range(0, n)])
                            overall_data = []
                            acct_name = input('Name: ')
                            balance = input('Opening Number: ')
                            acct_type = input('Account type: ')
                            email = input('Email: ')
                            banking_details = {
                                'Acoount name': acct_name,
                                'Opening Balance': balance,
                                'Account type': acct_type,
                                'Email': email,
                                'Account Number': acct_number
                            }
                            user_data = {staff_username: banking_details}
                            overall_data.append(user_data)
                            with open('customer.txt', 'w') as new_object:
                                json.dump(overall_data, new_object)
                                print(f'The new account number is: {acct_number}')

                        elif staff_choice == '2':
                            choice = input('Please provide account number: ')
                            with open('customer.txt') as files:
                                customer_details = json.load(files)
                                for line in customer_details:
                                    if choice == line[staff_username]['Account Number']:
                                        print(line)

                        elif staff_choice == '3':
                            os.remove('session.txt')
                            break

                        else:
                            print('\n Please enter a choice \n')

                else:
                    print('Invalid username or password')

    else:
        start = False
        print('Thank you for banking with us')

#############################
# PYTHON ATM SYSTEM         #
#                           #
# Author Paulina Karczewska #
#                           #
#                           #
# 8-Mar-2024                #
#############################

#initialise account data

user = {
    'pin': 6666,
    'balance':5000.00
}

withdrawl_op = {
    1: 10,
    2: 20,
    3: 40,
    4: 60,
    5: 80,
    6: 100
}

is_quit = False

def widthdraw_cash():
    while True:
        for i in range(1, 7):
            print(i, ". £", str(withdrawl_op[i]), "\n")
        print("Enter 0, to return to the main menu\n")
        choice = int(input("Enter the amount of money you want to widthdraw: "))
        if choice == 0: return
        amount = withdrawl_op[choice]
        if withdrawl_op[choice] > user['balance']:
            print("You do not have sufficient funds to make this widthdrawal")
        else:
            user['balance'] = user['balance'] - amount
            print({amount},  "Pounds successfully widthdrawn your remaining balance is {user['balance']} Pounds")
            print('')
            return False

def deposit_funds():
      #Explicitly cast deposit input(str) to float for addition to current balance
      new_deposit = int(input("How much do you wish to deposit, in Pounds?"))
      user['balance'] += new_deposit
      print('\n')

def display_balance():
    print("Your current balance is", "{:.2f}".format(user['balance']))
    print('\n')

print('')
print("Welcome to the Python ATM")

pin = int(input('Please enter your four digit pin: '))

if pin == user['pin']:
    while is_quit == False:
        print("What do you want to choose")
        print(" Enter 1 to Display Balance \n Enter 2 To Withdraw Funds \n Enter 3 to Deposit Funds \n 9 to Return Card ")

        query = float(input("Enter the number corresponding to the activity you want to do: "))

        if query == 1:
          display_balance()
        elif query == 2:
           widthdraw_cash()
        elif query == 3:
           deposit_funds()
        elif query == 9:
            print("Please remove your card and thank you for your business") 
            is_quit = True
        else:
            print("Invalid option. Please enter a correct value as shown on the menu")
else:
    print("Entered Wrong Pin")

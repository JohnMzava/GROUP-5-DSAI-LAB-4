x = input('Enter menu code: ')
menu = '*150*00#'


def send_money():
    a = 'Send to a mobile number'
    b = 'Send to the  bank' 
    print (a, b)

def buy_airtime(): 
    a = 'Buy airtime\n'
    b = 'Buy bundles' 
    print (a, b)

def pay_bills():
    a = 'Government Services\n'
    b = 'Pay Tv\n'
    c = 'Financial Services\n'
    d = 'Insurance Services\n'
    e = 'Internet Subscription\n'
    f = 'NGO\n'
    g = 'Others' 
    print (a, b, c, d, e, f, g)

def check_balance():
    balance = 250000 
    print(f"Your account balance is: {balance} TZS")

    choice = input("Do you want to check the balance again? (y/n): ").lower()

    if choice == "y":
        check_balance()  
    elif choice == "n":
        print("Thank you! Goodbye.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        check_balance()   

if x == menu:
    print(  '1. Send Money\n', 
            '2. Buy Airtime\n', 
            '3. Pay Bills\n', 
            '4. Check Balance\n',
            '5. Exit')
    
    y = int(input('Enter number: '))
    if y == 1:
     send_money()
    elif y == 2:
        buy_airtime()
    elif y == 3:
        pay_bills()
    elif y == 4:
        check_balance()
    elif y == 5:
        print('Thank you for using our services')
    else:
        print('Wrong input')
else:
    print('wrong code')




x = input('Enter menu code: ')
menu = '*150*00#'

    
# 1 = 'Send Money' 
# 2 = 'Buy Airtime' 
# 3 = 'Pay Bills' 
# 4 = 'Check Balance'
# 5 = 'Exit'

def send_money():
    a = 'Send to a mobile number'
    b = 'Send to the  bank' 
    print (a, b)

if x == menu:
    print(  '1. Send Money\n', 
            '2. Buy Airtime\n', 
            '3. Pay Bills\n', 
            '4. Check Balance\n',
            '5. Exit')
else:
    print('print wrong code')

y = int(input('Enter number: '))
if y == 1:
    print(send_money)
else:
    print('wrong input')




#def buy_airtime(): 

#def pay_bills(): 

#def check_balance(): 
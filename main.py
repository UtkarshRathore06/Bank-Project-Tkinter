from bankutil import *
from pymysql import *
ans='y'
while ans=='y':
    print('1. Open Account')
    print('2. Deposit Amount')
    print('3. Withdraw Amount')
    print('4. Show Balance')
    print('5. Exit')
    print('Enter Choice 1..5')
    choice=int(input())
    if choice==1:
        acno=int(input('Account No'))
        name=input('Name of Person')
        doo=input('Enter Date yyyy-mm-dd')
        amt=float(input('Enter Amount'))
        openaccount(acno,name,doo,amt)
    elif choice==2:
        acno=int(input('Account No'))
        dod=input('Enter Date yyyy-mm-dd')
        amt=float(input('Enter Amount'))
        deposit(acno,amt,dod)
    elif choice==3:
        acno=int(input('Account No'))
        dod=input('Enter Date yyyy-mm-dd')
        amt=float(input('Enter Amount'))
        withdraw(acno,amt,dod)
    elif choice==4:
        acno=int(input('Account No'))
        balance(acno)
    elif choice==5:
        exit(0)
    print('continue...y/n')
    ans=input()
    
    
    
    
    
    
    
    
    
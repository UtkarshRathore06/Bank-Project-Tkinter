from showbal import *
from deposit import *
from openaccount import *
from pymysql import *
from tkinter import *
from tkinter import messagebox as msg
from withdraw import *
class Bank(Frame):
    def __init__(self,m):
        super().__init__(m)
        self.b1=Button(self,text='open account',bg='light blue',fg='red',font=('algerian',14),command=self.open)
        self.b2=Button(self,text='deposit',bg='light blue',fg='red',font=('algerian',14),command=self.deposit)
        self.b3=Button(self,text='withdraw ammount',bg='light blue',fg='red',font=('algerian',14),command=self.withdraw)
        self.b4=Button(self,text='show balance',bg='light blue',fg='red',font=('algerian',14),command=self.balance)
        self.b5=Button(self,text='exit',bg='light blue',fg='red',font=('algerian',14),command=self.close)
        self.rowconfigure(index=0,pad=20)
        self.rowconfigure(index=1,pad=5)
        self.rowconfigure(index=2,pad=5)
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)
        self.b1.grid(row=1,column=0)
        self.b2.grid(row=1,column=1)
        self.b3.grid(row=2,column=0)
        self.b4.grid(row=2,column=1)
        self.b5.grid(columnspan=2)
        self.pack()
    def close(self):
        exit(0)
    def open(self):
        root=Tk()
        ob=AccountOpen(root)
        root.title('Account Open Form')
        root.geometry('300x300')
        root.mainloop()
    def deposit(self):
        root=Tk()
        ob=AmountDeposit(root)
        root.title('Deposit Form')
        root.geometry('200x200')
        root.mainloop()
    def withdraw(self):
        root=Tk()
        ob=AmountWithdraw(root)
        root.title('Withdraw Form')
        root.geometry('200x200')
        root.mainloop()
    def balance(self):
        root=Tk()
        ob=ShowBalance(root)
        root.title('Balance Form')
        root.geometry('200x200')
        root.mainloop()
root=Tk()
obj=Bank(root)
root.title('Main Form')
root.geometry('480x250')
root.mainloop()        
        
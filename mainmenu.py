from pymysql import *
from tkinter import *
from tkinter import messagebox as msg
from openaccount import *
class Bank(Frame):
    def __init__(self,m):
        super().__init__(m)
        
        self.b1=Button(self,text='Open Account',bg='light blue',
                       fg='red',font=('algerian',14),command=self.acopen)
        self.b2=Button(self,text='Deposit Amount',bg='light blue',
                       fg='red',font=('algerian',14))
        self.b3=Button(self,text='Withdraw Amount',bg='light blue',
                       fg='red',font=('algerian',14))
        self.b4=Button(self,text='Show Balance',bg='light blue',
                       fg='red',font=('algerian',14))
        self.b5=Button(self,text='Exit',bg='light blue',fg='red',
                       font=('algerian',14))
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
    def acopen(self):
        root=Tk()
        ob=AccountOpen(root)
        root.title('Account Opening Form')
        root.geometry('300x300')
        root.mainloop()
root=Tk()
obj=Bank(root)
root.title('Main Form')
root.geometry('480x250')
root.mainloop()
        
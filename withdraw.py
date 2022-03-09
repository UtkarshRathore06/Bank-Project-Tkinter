from tkinter import messagebox as msg
from tkinter import *
from bankutility import *
class AmountWithdraw(Frame):
    def __init__(self,m):
        super().__init__(m)
        
        self.l1=Label(self,text='Account No')
        self.l2=Label(self,text='Amount Withdraw')
        self.t1=Entry(self)
        self.t2=Entry(self)
        self.b1=Button(self,text='Withdraw Amount',command=self.call)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)
        self.l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)
        
        self.l2.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)
        
        
        self.b1.grid(columnspan=2)
        self.pack()
    def call(self):
        acno=(int)(self.t1.get())
        amt=float(self.t2.get())
        ob=utility()
        mes=ob.withdrawaccount(acno,amt)
        msg.showinfo('Information',mes)
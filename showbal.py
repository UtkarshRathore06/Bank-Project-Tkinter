from tkinter import *
from tkinter import messagebox as msg
from bankutility import *
class ShowBalance(Frame):
	def __init__(self,m):
		super().__init__(m)
		
		self.l1=Label(self,text='Account No')
		self.t1=Entry(self)
		self.b1=Button(self,text='Show',command=self.show)
		self.l2=Label(self)
		self.rowconfigure(index=0,pad=15)
		self.rowconfigure(index=1,pad=15)
		self.rowconfigure(index=2,pad=15)
		self.columnconfigure(index=0,pad=15)
		self.columnconfigure(index=1,pad=15)
		self.l1.grid(row=0,column=0)
		self.t1.grid(row=0,column=1)
		self.b1.grid(columnspan=2)
		self.l2.grid(row=2,column=1)
		self.pack()
	def show(self):
		ac=(int)(self.t1.get())
		ob=utility()
		bal=ob.showbalance(ac)
		self.l2.config(text=bal)
		
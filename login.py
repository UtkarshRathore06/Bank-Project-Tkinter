from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
from adminpanel import *
class login(Frame):
    def __init__(self,m):
        super().__init__(m)
        
        self.UI()
    def UI(self):
        self.l1=Label(self,text='User Name')
        self.l2=Label(self,text='Password')
        self.t1=Entry(self)
        self.t2=Entry(self,show='*')
        self.b1=Button(self,text='Login',command=self.check)
        self.rowconfigure(index=0,pad=20)
        self.rowconfigure(index=1,pad=20)
        self.rowconfigure(index=2,pad=20)
        self.columnconfigure(index=0,pad=20)
        self.columnconfigure(index=1,pad=20)
		
        self.l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)
		
        self.l2.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)
	
        self.b1.grid(columnspan=2)
        self.pack()
    def check(self):
        con=connect(db='kamal',user='root',passwd='root',host='localhost')
        cur=con.cursor()
        
        uid=self.t1.get()
        pwd=self.t2.get()
        cur.execute("select * from login where userid='%s' and password='%s'"%(uid,pwd))
        
        rs=cur.fetchall()
        if len(rs)>0:
            self.t1.delete(0,'end')
            self.t2.delete(0,'end')
            root=Tk()
            obj=Adminpanel(root)
            root.title('Admin')
            root.geometry('400x400')
            root.mainloop()
from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
class Registration(Frame):
    def __init__(self,m):
        super().__init__(m)
        
        self.UI()
    def UI(self):
        self.l1=Label(self,text='Employee No')
        self.l2=Label(self,text='Employee Name')
        self.l3=Label(self,text='Designation')
        self.l4=Label(self,text='Salary')
        self.l5=Label(self,text='Depatment No')
        self.l6=Label(self,text='User Name')
        self.l7=Label(self,text='Password')
        self.t1=Entry(self)
        self.t2=Entry(self)
        self.t3=Entry(self)
        self.t4=Entry(self)
        self.t5=Entry(self)
        self.t6=Entry(self)
        self.t7=Entry(self,show='*')
        self.b1=Button(self,text='Save',command=self.save)
        self.rowconfigure(index=0,pad=20)
        self.rowconfigure(index=1,pad=20)
        self.rowconfigure(index=2,pad=20)
        self.rowconfigure(index=3,pad=20)
        self.rowconfigure(index=4,pad=20)
        self.rowconfigure(index=5,pad=20)
        self.rowconfigure(index=6,pad=20)
        
        self.columnconfigure(index=0,pad=20)
        self.columnconfigure(index=1,pad=20)
		
        self.l1.grid(row=0,column=0)
        self.t1.grid(row=0,column=1)
		
        self.l2.grid(row=1,column=0)
        self.t2.grid(row=1,column=1)
	
        self.l3.grid(row=2,column=0)
        self.t3.grid(row=2,column=1)
		
        self.l4.grid(row=3,column=0)
        self.t4.grid(row=3,column=1)
		
        self.l5.grid(row=4,column=0)
        self.t5.grid(row=4,column=1)
		
        self.l6.grid(row=5,column=0)
        self.t6.grid(row=5,column=1)
        
        self.l7.grid(row=6,column=0)
        self.t7.grid(row=6,column=1)
        self.b1.grid(columnspan=2)
        self.pack()
    def save(self):
        con=connect(db='kamal',user='root',passwd='root',host='localhost')
        cur=con.cursor()
        eno=(int)(self.t1.get())
        ena=self.t2.get()
        desig=self.t3.get()
        sal=(float)(self.t4.get())
        dno=(int)(self.t5.get())
        uid=self.t6.get()
        pwd=self.t7.get()
        i=cur.execute("insert into emp values(%d,'%s','%s',%f,%d)"%(eno,ena,desig,sal,dno))
        if i==1:
            j=cur.execute("insert into login values('%s','%s',%d)"%(uid,pwd,eno))
            
        #i=cur.callproc('sadiya',[eno,ena,desig,sal,dno])
        #print(i)
            if j==1:
                con.commit()
                msg.showinfo('','Saved')
                self.t1.delete(0,'end')
                self.t2.delete(0,'end')
                self.t3.delete(0,'end')
                self.t4.delete(0,'end')
                self.t5.delete(0,'end')
                self.t6.delete(0,'end')
                self.t7.delete(0,'end')
                self.t1.focus()
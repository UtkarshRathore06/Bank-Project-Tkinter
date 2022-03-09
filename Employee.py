from tkinter import *
from tkinter import messagebox as msg
from pymysql import *
from Newuser import *
from login import *
class Employee(Frame):
    def __init__(self,m):
        super().__init__(m)
        
        self.UI()
    def UI(self):
        self.b1=Button(self,text='New User',fg='light blue',bg='red',font=('olephant',15),bd=6,command=self.call1)
        self.b2=Button(self,text='Login',fg='light blue',bg='red',font=('olephant',15),bd=6,command=self.log)
        self.b3=Button(self,text='Admin Panel',fg='light blue',bg='red',font=('olephant',15),bd=6)
        
        self.b1.grid(columnspan=2)
        self.b2.grid(columnspan=2)
        self.b3.grid(columnspan=2)
        self.pack()
    def call1(self):
        root=Tk()
        ob=Registration(root)
        root.title('New User')
        root.geometry('350x350')
        root.mainloop()
    def log(self):
        root=Tk()
        ob=login(root)
        root.title('login')
        root.geometry('250x200')
        root.mainloop()
        
root=Tk()
ob=Employee(root)
root.title('Employee Management')
root.geometry('350x350')
root.mainloop()
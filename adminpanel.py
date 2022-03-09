from tkinter import *
from tkinter import messagebox as msg
class Adminpanel(Frame):
    def __init__(self,m):
        super().__init__(m)
        
        self.UI()
    def UI(self):
        self.b1=Button(self,text='Attendence',fg='light blue',bg='red',font=('olephant',15),bd=6)
        self.b2=Button(self,text='Salary',fg='light blue',bg='red',font=('olephant',15),bd=6)
        self.b3=Button(self,text='Leave',fg='light blue',bg='red',font=('olephant',15),bd=6)
        
        self.b1.grid(columnspan=2)
        self.b2.grid(columnspan=2)
        self.b3.grid(columnspan=2)
        self.pack()
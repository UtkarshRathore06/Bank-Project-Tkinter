from pymysql import *
from datetime import *
class utility:
    def openconnection(self):
        self.con=connect(db='bank',user='root',passwd='root',host='localhost')
        return self.con
    def openaccount(self,acno,name,amt):
        dt=datetime.now()
        dd=dt.day
        mm=dt.month
        yy=dt.year
        dod=str(yy)+"-"+str(mm)+"-"+str(dd)
        con=self.openconnection()
        cur=con.cursor()
        i=cur.execute("insert into account values(%d,'%s','%s',%f)"%(acno,name,dod,amt))
        if i==1:
            j=cur.execute("insert into trans value(%d,'%s','%s',%f)"%(acno,'D',dod,amt))
            if j==1:
                con.commit()
                con.close()
        return "Saved"
    def depositaccount(self,acno,amt):
        dt=datetime.now()
        dd=dt.day
        mm=dt.month
        yy=dt.year
        dod=str(yy)+"-"+str(mm)+"-"+str(dd)
        con=self.openconnection()
        cur=con.cursor()
        i=cur.execute("update account set balance=balance+%f where acno=%d"%(amt,acno))
        if i==1:
            j=cur.execute("insert into trans value(%d,'%s','%s',%f)"%(acno,'D',dod,amt))
            if j==1:
                con.commit()
                con.close()
        return "Deposited"
    def withdrawaccount(self,acno,amt):
        dt=datetime.now()
        dd=dt.day
        mm=dt.month
        yy=dt.year
        dod=str(yy)+"-"+str(mm)+"-"+str(dd)
        con=self.openconnection()
        cur=con.cursor()
        i=cur.execute("update account set balance=balance-%f where acno=%d"%(amt,acno))
        if i==1:
            j=cur.execute("insert into trans value(%d,'%s','%s',%f)"%(acno,'W',dod,amt))
            if j==1:
                con.commit()
                con.close()
        return "Withdrawn"
    def showbalance(self,acno):
        con=self.openconnection()
        cur=con.cursor()
        cur.execute("select balance from account where acno=%d"%(acno))
        rs=cur.fetchall()
        bal=rs[0][0]
        return bal 
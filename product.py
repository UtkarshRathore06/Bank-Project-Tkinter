from pymysql import *
def Menu():
    ans='y'
    print('1. Add Product')
    print('2. Search Product')
    print('3. Exit')
    ch=(int)(input('Choice '))
    if ch==1:
        newproduct()
    elif ch==2:
        search()
    elif ch==3:
        exit(0)
def connection():
	con=connect(db='bank',user='root',passwd='root',host='localhost')
	return con
def newproduct():
    con=connection()
    print('Product Id')
    pid=(int)(input())
    print('Prroduct Name')
    pname=input()
    print('Product Price')
    price=(float)(input())
    print('Total Qty')
    qty=(int)(input())
    print('Description')
    desc=input()
    print('Product Color')
    color=input()
    print('Size')
    size=input()
    print('Guarantee')
    g=input()
    cur=con.cursor()
    i=cur.execute("insert into product values(%d,'%s',%f,%d)"
    %(pid,pname,price,qty))
    if i==1:
        j=cur.execute("insert into pdesc values(%d,'%s','%s','%s','%s')"%(pid,desc,color,size,g))
        if j==1:
            print('Record Added in table')
            con.commit()
            con.close()
def search():
    con=connection()
    cur=con.cursor()
    pid=(int)(input('Product Id'))
    cur.execute("select p.pid,p.pname,p.price,d.description,d.color,d.size from product p,pdesc d where p.pid=%d and d.pid=%d"%(pid,pid))
    result=cur.fetchall()
    print('Procduct Name :',result[0][1])
    print('Procduct Price :',result[0][2])
    print('Description :',result[0][3])
    print('Procduct Color :',result[0][4])
    print('Procduct Size :',result[0][5])
    
if __name__=='__main__':
    Menu()
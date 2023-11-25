import sqlite3
from contextlib import closing

def dbConnect():
    conn=sqlite3.connect('products.sqlite')
    if conn:
        print('DBConnect Success')
        return conn
    print('DBConnect Failure')
    return -1

def createTable(conn):
    with closing(conn.cursor()) as c:
        query='''create table if not exists products(prodID int,name text,quantity int,price real)'''
        c.execute(query)

def insertRecords(conn):
    n=int(input('Enter no of products: '))
    with closing(conn.cursor()) as c:
        for i in range(n):
            id1,name,qty,price=input('Enter id,name,quantity and price').split()
            id1=int(id1)
            qty=int(qty)
            price=float(price)
            query='''insert into products values(?,?,?,?)'''
            c.execute(query,(id1,name,qty,price))
    conn.commit()
    
def disp(conn):
    with closing(conn.cursor()) as c:
        query='''select * from products'''
        c.execute(query)
        result=c.fetchall()
        print('The products are:')
        for prod in result:
            print(prod[0],' ',prod[1],' ',prod[2],' ',prod[3])

def delProd(conn):
    pID=int(input('Enter id to delete:'))
    with closing(conn.cursor()) as c:
        query='''delete from products where prodID=?'''
        c.execute(query,(pID,))
        print('After delete:')
        disp(conn)
    conn.commit()

def incPrice(conn):
     with closing(conn.cursor()) as c:
        query='''update products set price = price + price*0.1 where price<50'''
        c.execute(query)
        print('After increase in price:')
        disp(conn)
     conn.commit()

def dispLt(conn):
    with closing(conn.cursor()) as c:
        query='''select * from products where quantity < 40'''
        c.execute(query)
        result=c.fetchall()
        print('The products with quantity <40 are:')
        for prod in result:
            print(prod[0],' ',prod[1],' ',prod[2],' ',prod[3])

def main():
    conn=dbConnect()
    if conn!=-1:
        createTable(conn)
        insertRecords(conn)
        disp(conn)
        delProd(conn)
        incPrice(conn)
        dispLt(conn)
        
if  __name__=='__main_':
    main()
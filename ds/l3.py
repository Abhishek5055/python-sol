import csv
def addData(books):
    n=int(input("Enter no of books:"))
    for i in range(n):
        bno=int(input("Enter book no"))
        title=input("Enter title:")
        author=input("Enter author:")
        price=int(input("Enter price:"))
        books.append([bno,title,author,price])
        
    with open("books.csv",'a',newline='')as file:
        writerobj=csv.writer(file)
        writerobj.writerows(books)
        
def searchbyauthor():
    flag=0
    au=input("Enter auhtor name:")
    with open("books.csv",newline='')as file:
        readerobj=csv.reader(file)
        for line in readerobj:
            if au==line[2]:
                flag=1
                print("Book found with details:",line)

        if flag==0:
            print("Books not found")
            
def searchbyprice():
    flag=0
    try:
      pr=int(input("Enter price:"))
      if pr<=0:
        raise ValueError("price should be greater than zero")
    except ValueError as e:
        print(e)
    with open("books.csv",newline='')as file:
        readerobj=csv.reader(file)
        for line in readerobj:
            if pr>=int(line[3]):
                flag=1
                print("Book found with details:",line)
        if flag==0:
            print("Books not found")
            
def searchbyword():
    flag=0
    word=input("Enter word:")
    with open("books.csv",newline='')as file:
        readerobj=csv.reader(file)
        for line in readerobj:
            if word in line[1]:
                flag=1
                print("Book found with details:",line)
        if flag==0:
            print("Books not found")        
        

def main():
    books=[]
    addData(books)
    print("books are:")
    with open("books.csv",newline='')as file:
        readerobj=csv.reader(file)
        for line in readerobj:
            print(line)
            
    while(1):
        print("1.search by auhtor 2.search by price 3.search by word  4.exit")
        opt=int(input("Enter option:"))
        if opt==1:
            searchbyauthor()
        elif opt==2:
            searchbyprice()
        elif opt==3:
            searchbyword()
        elif opt==4:
            break
        else:
            print("Incorrect choice")
            break
if __name__=="__main()__":
    main()
class Person:
    def __init__(self, fname="", lname="", email=""):
        self.fname = fname
        self.lname = lname
        self.email = email

    def getDescription(self):
        print("Name:", self.fname, self.lname, "\nEmail:", self.email)

class Customer(Person):
    def __init__(self, fname="", lname="", email="", cnum=0):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.cnum = cnum

    def getDescription(self):
        print("\tCustNum:", self.cnum, "\n\tName:", self.fname, self.lname, "\n\tEmail:", self.email)

class Employee(Person):
    def __init__(self, fname="", lname="", email="", pan=0):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.pan = pan

    def getDescription(self):
        print("\tPAN:", self.pan, "\n\tName:", self.fname, self.lname, "\n\tEmail:", self.email)

def main():
    objects = []
    ch = 1
    while (ch!=4):
        print("\n******Menu: 1.Person, 2.Enter Customer 3.Enter Employee   4.Exit******")
        ch = int(input("Enter your choice: "))

        if ch==1:
            fname, lname = input("\tEnter Person Name: ").split()
            email = input("\tEnter Person Email: ")
            objects.append(Person(fname, lname, email,))
            
        elif ch==2:
            fname, lname = input("\tEnter Customer Name: ").split()
            email = input("\tEnter Customer Email: ")
            cnum = int(input("\tEnter Customer Number: "))
            objects.append(Customer(fname, lname, email, cnum))

        elif ch==3:
            fname, lname = input("\tEnter Employee Name: ").split()
            email = input("\tEnter Employee Email: ")
            pan = int(input("\tEnter Employee PAN: "))
            objects.append(Employee(fname, lname, email, pan))
            
            
        elif ch==4:
            for obj in objects:
                if isinstance(obj, Customer):
                    print("--- Customer Details ---")
                    obj.getDescription()

        else:
                    print("--- Employee Details ---")
                    obj.getDescription()

if __name__ == '__main__':
    main()

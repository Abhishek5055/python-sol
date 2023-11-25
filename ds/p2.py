import random
l=[]
n=int(input("Enter no of friends:"))
for i in range(n):
    name=input("Enter the names:")
    l.append(name)
print("Today the bill will be paid by:",random.choice(l))
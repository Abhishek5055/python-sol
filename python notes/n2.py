a=6
b=3
print(a+b)#addition
print(a-b)#subtraction
print(a*b)#Multiplcation
print(a/b)# floating point Division
print(a//b)#Integer division
print(a%b)#Modulo Operation
print(a**b)#Exponential Operation

#\n newline
#\t new tab
#\r return
#\" Quotation mark in a double quoted string
#\' Quotation mark in a single quoted string\
# \\ Backslash
print("Hello World\"Good Morning Friends\"Welcome to the world of coding")

#sep and end arguments
print(1,2,3,4,sep='[]') #sep argument
print(1,2,3,4,end ='!!')

#miles driven poblem
print("The Miles per Gallon program")

milesdriven=int(input("Enter the milesdriven:"))
gallonsused=int(input("Enter the gallons used:"))

mileage=round(milesdriven/gallonsused,2)
print("Mileage is:"+str(mileage))
print("Good")
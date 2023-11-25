from datetime import time,date,datetime
date=input("Enter the day of birth (MM/DD/YYYY):")
birthdate=datetime.strptime(date,"%m/%d/%Y")
print("Date of birth:",birthdate)
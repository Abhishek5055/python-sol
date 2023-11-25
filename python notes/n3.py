# # #Two string methods
# # a="Abhi"
# # b="abhi"
# # print(a.lower()==b.lower())
# # #if clause and elif clauses,and else clause
# # price =int(input("Enter the price:"))
# # if price <=100:
# #     print("discount_percent=2")
# # elif price >100 and price<250:
# #     print("discount_percent=10")
# # elif price>250 and price<1000:
# #     print("discount_percent=20")
# # else:
# #     print("discount_percent=25")

# # #Example 2:
# # #Student grading system
# # score =int(input("Enter the test score:"))
# # if score>=90 and score<=100:
# #    print("grade=A")
# # elif score>=75 and score<90:
# #    print("grade=B")
# # elif score>=60 and score<75:
# #    print("grade=C")
# # elif score>=35 and score<60:
# #   print("grade=D")
# # else:
# #    print("grade=F")
    
# # #Example 3:
# # totalscores=0
# # scores=int(input("Enter test scores:"))
# # if scores>=0 and scores<=100:
# #     totalscores+=scores
# # else:
# #     print("Test score must be between o to 100")
    
    
# #Example for customer type:
# customer_type=input("Enter the typecode(r/w):")
# invoice_total=int(input("Enter the invoice_total:"))
# if customer_type.lower() =="r" and invoice_total<100:
#     print("discount_percent=0")
# elif customer_type.lower() =="r" and(invoice_total>=100 and invoice_total<=250):
#     print("discount_percent=.1")
# elif customer_type.lower() =="r" and(invoice_total>=250):
#     print("discount_percent=.2") 
  
# elif customer_type.lower() =="w" and invoice_total<500:
#     print("discount_percent=.4")
# elif customer_type.lower() =="w" and invoice_total>=500:
#     print("discount_percent=.5")
# else:
#     print("discount_percent=0")
    
# #FOR LOOP WITH RANGE () fUNCTION
# sum=0
# for i in range(1,5):
#     sum+=i
# print(sum)

# #continue in while loop
# print("Enter exit when you're done:")
# while True:
#     data=input("Enter an integer to square:")
#     if data=='exit':
#         break
#     i=int(data)
#     print(i,"Squared is",i*i,'\n')
# print("Good bye")

choice="y"
while choice.lower() =="y":
    monthly_investment=float(input("Enter the monthly investment:"))
    yearly_interest_rate=float(input("Enter the yearly interest rate:"))
    years=int(input("Enter the number of years:"))
    
    #convert yearly to monthly
    monthly_interest_rate=yearly_interest_rate/12/100
    months=years*12

    future_value=0
    for i in range(months):
        future_value +=monthly_investment
        monthly_interest_amount=future_value*monthly_interest_rate
        future_value +=monthly_interest_amount
        
    print("Future Value: "+str(round(future_value,2)))
    print()

    choice = input("Continue(y/n)?:")
print("Bye")
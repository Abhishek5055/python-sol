counter=0
scoretotal=0
testscore=0

while testscore !=999:
    testscore = int(input("Enter the testscore: "))
    if testscore>=0 and testscore<=100:
        scoretotal +=testscore
        counter += 1
averagescore = round(scoretotal/counter)

print("The Totalscore is:",str(scoretotal))
print("The Average is:",str(averagescore))

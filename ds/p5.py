heights=[57,112,120,145,164,152]
sum=0
for height in heights:
    sum+=height
    average=round(sum/len(heights),2)
print(f"The average height is {average}")



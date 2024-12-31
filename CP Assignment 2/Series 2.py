#series
#4+8+12+.....+n

n= int(input("enter the Last number: "))
sum=0
for x in range(4,n+1,4):
    sum +=x
print(sum)

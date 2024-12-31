#series
#2*2+4*4+6*6+.....+n

n= int(input("enter the Last number: "))
sum=1
for x in range(2,n+1,2):
    sum =sum*(x**2)
print(sum)

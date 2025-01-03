#series
#2*2+4*2+8*2+.....+n
n= int(input("enter the Last number: "))
sum=0
term=2

for x in range(1, n + 1):
    if term>n:
        break
    sum+=term**2
    term*=2
print(sum)

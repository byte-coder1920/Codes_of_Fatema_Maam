#joint
a=[2,34,4,1,24,50,60,50]
b=[2,33,2,4,3,"rahim"]
a1=[True,False]

c=a+b
print(c)

a.extend(b)
print(a)

a.extend(b+a1)
print(a)

for x in b:
    a.append(x)
    print(x)
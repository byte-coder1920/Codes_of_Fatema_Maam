#tuple update
a=(1,3,5,7,9,0)
y=list(a)
y.append(100)
a=tuple(y)
print(a)

y=list(a)
y[2]="kiwi"
a=tuple(y)
print(a)

y=list(a)
y.remove(9)
a=tuple(y)
print(a)

del a

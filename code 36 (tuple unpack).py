#tuple unpack
a1=(1,3,5,7,9,)
(a,b,c,d,e)=a1
print(a)
print(b)
print(c)
print(d)
print(e)

(a11,*b11,c11)=a1
print(a11)
print(*b11)
print(c11)
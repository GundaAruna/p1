a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
c=int(input("Enter c value: "))
big=0
low=0
middle=0
sum=a+b+c
if(a>b and a>c):
    big=a
elif(b>a and b>c):
    big=b
else:
    big=c
if(a<b and a<c):
    low=a
elif(b<a and b<c):
    low=b
else:
    low=c
middle=sum-(big+low)
c=big
b=middle
a=low
print(a,b,c)


n=int(input("Enter the number: "))
f1=0
f2=1
if(n==0 or n==1):
    print("not possible to generate series")
else:
    print(f1)
    print(f2)
    while(n!=2):
        f3=f1+f2
        print(f3)
        f1=f2
        f2=f3
        n=n-1

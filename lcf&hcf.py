n1=6
n2=12
l1=[]
l2=[]
l3=[]
for i in range(1,n1+1):
    if(n1%i==0):
        l1.append(i)
for j in range(1,n2+1):
    if(n2%j==0):
        l2.append(j)
for i in l1:
    for j in l2:
        if(i==j):
            l3.append(i)
hcf=max(l3)
l3.remove(1)
lcf=min(l3)
print(hcf)
print(lcf)

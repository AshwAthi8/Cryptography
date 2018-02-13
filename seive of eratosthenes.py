n=int(input())
a=[]
for i in range (2,n+1):
    a.append(i)

for i in range (1,int(n**.5)+1,1):
    if i in a :
        for j in range (2*i,n+1,i):
            if j in a :
                a.remove(j)
                
print(a)


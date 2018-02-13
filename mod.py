print("a to the power b mode p")
a=int(input())
b=int(input())
p=int(input())
ans=1
for i in range (0,b):
    ans=(ans*(a%p) )%p
print(ans)

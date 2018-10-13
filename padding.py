s=input() #the string which has to be padded
x=len(s)
c=x%16
r=16-c	#hex of this number will be used to pad the string.
for i in range (0,r,1):
	s=s+"\\"+hex(r)
print(s) #the padded string.




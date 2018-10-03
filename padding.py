#python 2 code for padding

s=raw_input()
x=len(s)
r=16-x%16
s=s+hex(r)*r
print(s)


num=int(input())
for x in range(2,num):
	if num%x==0:
		break
x=x+1
if num==x:
	print("Prime no.")
else:
	print("Not prime no.")

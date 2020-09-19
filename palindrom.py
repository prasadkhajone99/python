num=int(input("Enter the number...\n"))
x,sum=num,0
while x :
	sum=sum*10+x%10
	x=x//10
if sum==num :
	print("Palindrom")
else :
	print("Not palindrom")

	
	

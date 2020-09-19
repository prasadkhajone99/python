num=int(input())
sum=0
x=num
while num:
	sum=sum*10+num%10
	num=num//10
if sum==x:
	print("Palindrome")
else:
	print("Not Palindrome")


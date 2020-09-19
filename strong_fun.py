def strong(n) :
	m=n
	sum=0
	while m :
		fact=1
		r=m%10
		while r :
			fact=fact*r
			r=r-1
		sum=sum+fact
		m=m//10
	if sum==n :
		return 1
	else :
		return 0
	
num=int(input("Enter the number...\n"))
k=strong(num)
if k==1 :
	print("Strong number...")
else :
	print("Not strong number...")

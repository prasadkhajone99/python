n=int(input("Enter row"))
for x in range(1,n+1):
	print(' '*(n-x),end="")
	print('* ' *(x),end="")
	print()

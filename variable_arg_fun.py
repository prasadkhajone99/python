def add(*arg) :
#	print(arg)
#	return sum(arg)
	
	t=0	
	for sum in arg :
		t=t+sum
	return t


print(add(10,20,30))
print(add(10.5,20.5))
print(add(10,20.5,30))

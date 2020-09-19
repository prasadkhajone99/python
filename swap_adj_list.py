l=str(input("Enter data...\n"))
l=l.split()
m=len(l)
print(m)
for i in range (0,m,2) :
	l[i],l[i+1]=l[i+1],l[i]
print(l)


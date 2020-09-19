def word_count(str) :
	l=str.split()
	counts=len(l)
	return counts

str=str(input("Enter thr string..\n"))
k=word_count(str)
print(k)

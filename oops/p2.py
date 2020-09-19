class student :
	def _init_(self,n,a):
		print("constructor")
		self.name=n
		self.age=a
		

obj=student("Prasad",23)
print(obj.name,obj.age)

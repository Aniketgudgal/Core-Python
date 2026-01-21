class A:
	def m1(self):
		print("Parent a method")
class B(A):
	def m2(self):
		print("Parent b method")
        

obj = B()
obj.m2()
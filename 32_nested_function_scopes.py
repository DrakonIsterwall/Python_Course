x=10

def function1():
	x=1
	print("My x value is:",x)

	def function2insidefunction1():
		x=2
		print("My x value is:",x)

	function2insidefunction1()
function1()


print("Outside function",x)

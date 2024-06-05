x=1
print(x)
def function1():
	global x
	x = 10
	print(x)

	def function2():
		global x
		x = 100
		print(x)
	function2()
function1()
print(x)

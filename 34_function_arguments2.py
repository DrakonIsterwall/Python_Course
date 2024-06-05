def math(a,b=1,c=2,d=3):
	sum = a+b+c+d
	print(sum)
	mult = a*b*c*d
	print(mult)	

math(1)
math(1,5)
math(1,5,10)
math(1,5,10,20)

#all parameters with standard values have to be on the right side, so it can not be (a,b=1,c,d=3) it would have to be (a,c,b=1,d=3)

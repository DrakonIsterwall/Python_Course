print("Type a number")
my_number = int(input()) 
#here we combine the input directly with the int() command so it datatype is changed to an int value
if my_number < 0 :
   print("Your number is negative")
elif my_number == 0 :
   print("Your number is zero")
else:
   print("Your number is positive")


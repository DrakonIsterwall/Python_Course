print("Type in a string")
my_str = input()
if len(my_str) <= 1:
   print("Short")
elif len(my_str) <10:
   print("still short")
elif len(my_str) <25:
   print("not that short anymore")
elif len(my_str) <50:
   print("we getting somewhere here")
elif len(my_str) <100:
   print("long string")
elif len(my_str) >100:
   print("gigantic string, maybe or just a bit longer long string")
else:
   print("you probably did something wrong")


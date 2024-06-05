my_list = ["1Apple0","2Apple1","3Apple2","4Apple3","5Apple4"]

x=0
for x in range(5) :
   if x == 2:
      continue
   if x == 4:
      break
   print("Object" + str(x+1) + ": " + my_list[x])
print("Object 3 should be not shown and Object 5")

print("Give me a value from 1-10 and see if u hit my number")
guessed_number = input()
#guessed_number = int(guessed_number) you have to change the data type here with this command or in the if command
my_number = 9
if int(guessed_number) == my_number :
   print("You found my number")
else:
   print("Try again you did not find my number")

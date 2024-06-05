my_file = open("newfile.txt","w")

# the option "w" creates a file if it not already exists, if it exists it erases the content of the file and add the new content to the beginning of the file

my_file.write("I added this content to a File wohoo!!!")

my_file.close()

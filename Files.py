# In Python, you can read and write from files.
f = open("file_name", "r")
print(f.read())


# You can also create and write files. 
f = open("demofile1.txt", "a") # Append to an existing file
f.write("The file will include more text..")
f.close()

f = open("demofile2.txt", "w") # Creating and writing to a new file
f.write("demofile2 file created, with this content in!")
f.close()



# In the code editor, write Python code to read the flag.txt file. What is the flag in this file?
f = open("flag.txt", "r")
print(f.read())
# The Flage is : THM{F1LE_R3AD}

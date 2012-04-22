from sys import argv

# Import sys (python library of codes) & use the following argument variables
script, filename = argv

# a text file needs to be opened (the 'filename' is the text file provided)
txt=open(filename)

# 'here is your [file provided]'
print "Here's your file %r:" % filename
# text in file is shown
print txt.read()

# user is prompted to enter a file. file_again is the reference to the raw_input which collects what the user typed.
print "Type the filename again:"
file_again=raw_input("> ")
# the user's information (file_again) is now referred to 'txt_again.' This opens the text file.
txt_again=open(file_again)

# This shows the text file's contents
print txt_again.read()

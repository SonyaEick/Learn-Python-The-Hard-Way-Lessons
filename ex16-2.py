from sys import argv

script, filename=argv

txt=open(filename)
target=open(filename, 'w')

print "I will now open %r:" % filename
target.read("test.txt")

print "I want you to add a few more lines now."

line5=raw_input("line 5: ")
line6=raw_input("line 6: ")
line7=raw_input("line 7: ")

print "Printing..."

target.write("%s \n %s \n %s" %(line5, line6, line7))

print "So how are you? "
howareyou=raw_input()

print "Well, %r. So I'll show you what the file looks like now:" %howareyou
target.read("test.txt")

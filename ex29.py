people = 20
cats = 30
dogs = 15

if people < cats:
   print "Too many cats! The world is doomed!"

if people > cats:
   print "Not many cats; The world is saved!"

if people < dogs:
   print "The world is drooled on!"

if people > dogs:
   print "The world is dry!"

dogs += 5

if people >= dogs:
   print "People are greater than or equal to dogs."

if people <= dogs:
   print "People are less than or equal to dogs."

if people == dogs:
   print "People are dogs."

# 1. What do you think the 'if' does to the code under it?
# It works just like it does in English. It states that, "if" something is a true statement, run this code.

# 2. Why does the code need to be indented?
# It is indented so that python knows to run it accordingly with the if statement.

# 3. What happens if it isn't indented?
# All the code runs. All those sentences above will get printed without any regulation. That, or you'll get an error, because python expects some sort if indentation.

# 4. Can you put other boolean expressions from Ex.27 in the if-statement? Try it.
# How's this:
people = 25
dogs = 10

if people != dogs:
   print "People are catty."

# 5. What happens if you change the variables for people, cats, and dogs?
# The statements become wrong and you will end up getting an error. If you mean, what happens when you change the numbers, it will change what prints.


people=30
cars=40
buses=15

if cars>people:
   print "We should take the cars."
elif cars<people:
   print "We should not take the cars."
else:
   print "We can't decide."

if buses>cars:
   print "That's too many buses."
elif buses<cars:
   print "Maybe we could take the buses."
else:
   print "We still can't decide."

if people>buses:
   print "Alright, let's just take the buses."
else:
   print "Fine, let's stay home then."

# 1. What are elif & else doing?
# It's saying, when the if statement is false, run this new statement. 
# Basically, "Else if." When that won't run either, "else" means "otherwise" run this final statement, so that something will run.
# 3. Try more complex boolean expressions like 'cars>people and buses<cars.'

if people>cars and cars>buses:
    print "There will be people left at home."
else:
    print "Everyone is coming with us."

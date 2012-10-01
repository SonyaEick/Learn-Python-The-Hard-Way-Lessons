ten_things="Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff=ten_things.split(' ') # split(ten_things, ' ')
more_stuff=["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # while length of stuff is not equal to 10
   next_one=more_stuff.pop() # next_one: adds new items to the end of the list
   print "Adding: ", next_one
   stuff.append(next_one)
   print "There's %d items now." % len(stuff)

print "There we go: ", stuff #Once the while loop is satisfied, this prints

print "Let's do some things with stuff."

print stuff[1] # prints the item in the 1 spot
print stuff[-1] # removes the last item?
print stuff.pop() # .pop returns the last item in the list
print ' '.join(stuff) #
print '#'.join(stuff[3:5]) # 

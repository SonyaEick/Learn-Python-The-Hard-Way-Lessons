cities={'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY']='New York'
cities['OR']='Portland'

def find_city(themap, state):
   if state in themap:
      return themap[state]
   else:
      return "Not Found."

#Below is an important lesson!

cities['_find'] = find_city

while True:
   print "State? (ENTER to quit)"
   state=raw_input("> ")
   
   if not state: break

   #This line is the most important
   city_found=cities['_find'](cities, state)
   print city_found

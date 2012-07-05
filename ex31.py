print "You enter a dark room with two doors. Do you go through door 1 or 2?"

door = raw_input("> ")

if door == "1":
   print "There's a giant bear here eating a cheese cake. What do you do?"
   print "1. Take the cheese cake."
   print "2. Scream at the bear."
   print "3. Keep walking."

   bear = raw_input("> ")

   if bear == "1":
      print "The bear eats your face off. Good Job!"
   elif bear == "2":
      print "The bear eats your legs off. Good Job!"
   elif bear == "3":
      print "You see a genie lamp on a nightstand. Do you rub the lamp?"
      print "1. Yes"
      print "2. No"
      
      lamp = raw_input("> ")
         
      if lamp == "1":
            print "A Genie come out and offers you three wishes. What do you wish for?"
            print "1. The love of my life."
            print "2. All the money in the world."
            print "3. All the knowledge of the world."
            
            wish = raw_input("> ")
            
            if wish == "1":
               print "The love of your life appears before you... only... it is a mirror. You live happily ever after. The End."
            elif wish == "2":
               print "The room fills entirely with cash, to the point of crushing you with the pressure of every cent and bill in the world. At least you are rich! You expire happily ever after. The End. "
            elif wish == "3":
               print "You are given every ounce of knowledge that exists in the world. You suddenly get horribly depressed and withdrawn. You commit suicide out of knowing too much. The End."
            else:
               print "The genie rejects %s and instead trades places with you. You are forever waiting in a golden lamp for the next fool to summon you. The End." %wish

      elif lamp == "2":
            print "The bear sees you and swipes at your spine, leaving you immobile. Good Job!"
   else:
      print "Well, doing %s is probably better. Bear Runs away." %bear

elif door == "2":
   print "You stare into the endless abyss at Cthulu's retina."
   print "1. Blueberries."
   print "2. Yellow jacket clothespins."
   print "3. Understanding revolvers yelling melodies."

   insanity = raw_input("> ")
   if insanity == "1" or insanity == "2":
      print "Your body survives powered by a mind of jello. Good Job!"
   else:
      print "The insanity rots your eyes into a pool of muck. Good Job!"
else:
   print "You stumble around and fall on a knife and die. Good job!"

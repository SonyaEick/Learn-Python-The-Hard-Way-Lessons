# Define 'cheese_and_crackers' which is (cheese_count + boxes_of_crackers) - This is the format you are asking to print per cheese_and_crackers
# When 'cheese_and_crackers' is typed, the computer will print the following statements.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" %cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
# This is where cheese_count & boxes_of_crackers are given numbers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# Telling the computer each one and then typing the function to run which is 'cheese_and_crackers
print "OR, we can use variables from out script:"
amount_of_cheese=10
amount_of_crackers=50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# Adding the numbers inside the brackets.
print "We can even do math inside too:"
cheese_and_crackers(10+20,5+6)
# Took numbers from the script that said 10:50 and add more to it.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers+1000)

# --------------------

def fishcake(hicap, boxjelly):
	print "There are %d hicap members inside fishcake." %hicap
	print "There are %d boxjelly members inside fishcake." %boxjelly
	print "Altogether they make a sweet team of winners, totaling %d people!(approximately)\n" % (hicap + boxjelly)
# one
print "Hicap members + Boxjelly members today:"
fishcake(11, 5)
# two
print "Hicap members + Boxjelly members today:"
hicap=11
boxjelly=5
fishcake(hicap, boxjelly)
# three
print "Hicap members + Boxjelly members today:"
fishcake(10+1,2+3)
# four
print "Hicap members + Boxjelly members today:"
fishcake(hicap+9, boxjelly+5)
# five
print "Hicap members + Boxjelly members today:"
hicap=5+9
boxjelly=3+2
fishcake(hicap, boxjelly)
# six
print "Hicap members + Boxjelly members today:"
hicap=9/3
boxjelly=6/2
fishcake(hicap, boxjelly)
# seven
print "Hicap members + Boxjelly members today:"
fishcake(100/5, 51/3)
# eight
print "Hicap members + Boxjelly members today:"
fishcake(4*hicap, 4*boxjelly)
# nine
print "Hicap members + Boxjelly members today:"
hicap=11
boxjelly=6
fishcake(boxjelly+hicap, boxjelly/boxjelly)
# ten
print "Hicap members + Boxjelly members today:"
hicap=11
boxjelly=6
fishcake(hicap*hicap, boxjelly*boxjelly)

# %d tells py it needs to use the number 10 in the sentence.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# Same thing, except there are two blanks. Py goes in order of the parenthesis
y = "Those who know %s and those who %s." % (binary, do_not)

# These print the sentences that are now considered 'x' and 'y' for faster use.
# string inside a string 1
print x
# string inside a string 2
print y

# A quicker way to reference the previous sentence again.
# string inside a string 3
print "I said: %r." % x
# string inside a string 4
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# string inside a string 5
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

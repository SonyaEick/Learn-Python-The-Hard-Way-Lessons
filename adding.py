from sys import argv

script, number1, number2 = argv

print "added = ",
print int(number1)+int(number2)

print "subtracted = ",
print int(number1)-int(number2)
#space - (02/23/12: Nope, that was dumb. Seeing as Python ignores these)
print "multiplied = ",
print int(number1)*int(number2)

print "divided = ",
print int(number1)/int(number2)

# 02/23/12: this one doesn't work yet. I'll come back to it.
print "%s < %s = " (number1, number2),
print int(number1)<int(number2)


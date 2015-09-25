# python program to do the same thing (but w/o web interface)
def timesTwo(x):
    return x*2
    
def minusFive(x):
    return x-5
    
def plusThree(x):
    return x+3
    
try:
    x = int(raw_input("Enter a number: "))
except ValueError:
    print "Must be an integer.  You will need to re-enter"
    x = 0
print 'Your number is ', plusThree(minusFive(timesTwo(x)))
 

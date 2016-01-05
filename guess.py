import random
name = raw_input("Howdy, what's your name?\n")
number = random.randint(1, 100)
numguesses = 0
guess = None
print "%s, I'm thinking of a number between 1 and 100." % (name)

while guess != number: 
    try: 
        guess = int(raw_input("What is your guess?\n"))
    except ValueError:
        print "Oops! That was not a number. Please try again. This time, with an integer!"
    numguesses +=1 
    if guess < 1 or guess > 100:
        print "You are dumb and didn't pick a number between 1 and 100."
    elif guess > number:
        print "Your guess is too high!"
    elif guess < number: 
        print "Your guess is too low!"    
    else:
        print "Congratulations, %s you win! You took %d tries!" % (name, numguesses)


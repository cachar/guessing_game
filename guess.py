import random
name = raw_input("Howdy, what's your name?\n")
scores = [100]

def newgame():
    numguesses = 0
    guess = None
    number = random.randint(1, 100)
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
            if numguesses < min(scores): 
                print "You got the best score yet!"
            scores.append(numguesses)
            playagain()
            
def playagain():
    response = raw_input("Do you want to play again? Y/N\n")
    if response == "Y" or response == "y":
        newgame()
    elif response == "N" or response == "n":
        print "Bye!"
    else:
        print "You didn't print a valid answer."
        playagain()


newgame()
import random
while True:
    a=True
    while a:
        get_range=input("Enter a number above 5 ")
        if get_range.isdigit() and int(get_range)>5:
            get_range=int(get_range)
            print("Game on!!")
            a=False
        else:
            print("Invalid entry, Please try again")
    hidden=random.randint(1,get_range-1)
    a=True
    b=0
    c=0
    while a:
        score=10-c
        c+=1
        guess=input('Guess the hidden number that is between '+str(b)+" and "+str(get_range)+" ")
        if c==10:
            print("You are bad at guessing. Your score is: ",score-1)
            a=False
        elif guess.isdigit() and int(guess)<get_range+1:
            guess=int(guess)
            if guess==hidden:
                print("You guessed the right number! your score is: ",score," out of 10!!" )
                a=False
            elif c==3:
                if hidden%2==0:
                    print("A clue: The hidden number is an even number")
                else: print("A clue: The hiddn number is an odd number")
            elif c==5:
                if hidden<int(get_range/2)+1:
                    print("A clue: The hidden number is above 0 and below ", int(get_range/2)+1)
                elif hidden>int(get_range/2)-1:
                    print("A clue: the hidden number is above ", int(get_range/2)-1, " and below ",get_range)
            elif guess!=hidden:
                print("Nop! The hidden number is not ",guess, ". Go for another try.")
        else:
            print("Invalid entry, Please try again")